import json
import random
import paramiko
import logging
import time
import signal
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

RESOURCE_GROUP = 'NetworkWatcherRG'
VM_SCALE_SET = 'stagent-vms'
SUBSCRIPTION_ID = '3f7efba3-c56c-405e-b6fc-fc955739d7ea'
SSH_USER = 'azureuser'
SSH_KEY_PATH = '../target-1_key.pem'
IPS_FILE_PATH = '../vmss_ips.txt'


normal_workload_script = """
#!/bin/bash
while true; do
    echo "Starting intensive CPU load for 30 seconds."
    for i in {1..4}; do
        head -c 500M </dev/zero | sha1sum > /dev/null &
    done
    sleep 30

    echo "Simulating intensive disk write & CPU load for 60 seconds."
    for i in {1..4}; do
        head -c 500M </dev/zero | sha1sum > /dev/null &
        dd if=/dev/zero of=/tmp/testfile_$i bs=1M count=500 oflag=dsync > /dev/null 2>&1 &
    done
    wait

    for i in {1..4}; do
        rm -f /tmp/testfile_$i
    done

    sleep 60

    echo "Simulating intensive disk write for 30 seconds."
    dd if=/dev/zero of=/tmp/testfile bs=1M count=500 oflag=dsync > /dev/null 2>&1

    rm -f /tmp/testfile

    sleep 30

    echo "Completed one cycle of workload. Starting over..."
done
"""
disk_fill_script = """
#!/bin/bash
mkdir -p /tmp/disk_fill
counter=0
while true; do
  dd if=/dev/urandom of=/tmp/disk_fill/fill_file_$counter bs=1M count=10 oflag=append conv=notrunc
  let counter=counter+1
  sleep 5
done
"""


with open(IPS_FILE_PATH, 'r') as file:
    targets = [line.strip() for line in file.readlines() if line.strip()]


def get_workloads():
    """
    Returns a list of workload commands with the specified distribution.
    """
    workloads = [
        # normal workloads, normal fluctuation of CPU & Disk
        "bash /tmp/normal_workload.sh",
        "bash /tmp/normal_workload.sh",
        # 1 machine running a 5 spike of CPU and IO stress
        "stress-ng --cpu 1 --io 1 --timeout 5s",
        # 1 machine running memory stress
        "stress-ng --vm 2 --vm-bytes 95% --timeout 2000s",
        # 1 machine running CPU stress for 2000s
        "stress-ng --cpu 1 --timeout 2000s",
        # Disk fill workload
        "bash /tmp/disk_fill_script.sh"
    ]
    random.shuffle(workloads)
    return workloads


def simulate_workload(ips, ssh_user, ssh_key_path):
    """
    Distributes specified workloads among VMs with a 2:1:1:1 ratio.
    """

    if len(ips) < 5:
        print("Insufficient number of IPs provided. Exiting.")
        return

    ssh_clients = []
    workloads = get_workloads()

    def signal_handler(sig, frame):
        """
        Kills processes and cleanup on each VM on signal.
        """
        print('Stopping all workloads on the VMs...')
        for ssh in ssh_clients:
            try:
                ssh.exec_command("pkill -f normal_workload.sh")
                ssh.exec_command("pkill -f stress-ng")
                ssh.exec_command("rm -f /tmp/testfile*")
                ssh.exec_command("rm -rf /tmp/disk_fill")
                ssh.exec_command("pkill -f disk_fill_script.sh")
                ssh.close()
            except Exception as e:
                print(f"Failed to stop workloads cleanly: {e}")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    selected_ips = random.sample(ips, 5)

    for i, ip in enumerate(selected_ips):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(ssh_key_path)
        ssh_clients.append(ssh)
        try:
            ssh.connect(hostname=ip, username=ssh_user, pkey=private_key)
            workload_command = workloads[i]
            if "normal_workload.sh" in workload_command:
                ssh.exec_command(f"echo '''{normal_workload_script}''' > /tmp/normal_workload.sh")
                ssh.exec_command("chmod +x /tmp/normal_workload.sh")
            elif "disk_fill_script.sh" in workload_command:
                ssh.exec_command(f"echo '''{disk_fill_script}''' > /tmp/disk_fill_script.sh")
                ssh.exec_command("chmod +x /tmp/disk_fill_script.sh")
            ssh.exec_command(f"nohup {workload_command} > /tmp/workload.log 2>&1 &")
            print(f"Workload simulation ({workload_command}) started on {ip}.")
        except Exception as e:
            print(f"Failed to connect or execute on {ip}: {e}")

    print("Workloads started. Press Ctrl+C to stop.")
    signal.pause()


if __name__ == "__main__":
    simulate_workload(targets, SSH_USER, SSH_KEY_PATH)
