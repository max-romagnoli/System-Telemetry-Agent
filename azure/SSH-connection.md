## Access VM and run exporter on it

#### Prerequisites
* For this walkthrough I created a VM called **target-1** and deployed the exporter onto the VM
* Save .pem file `target-1_key.pem` in `azure/` folder

#### Connect to VM using ssh
```
cd System-Telemetry-Agent
chmod 600 azure/target-1_key.pem
ssh -i azure/target-1_key.pem azureuser@20.107.240.171
```
Notes: 
* *target-1_key.pem* is the file containing the SSH key (!!!! DO NOT COMMIT IT !!!)
* *azureuser* is the user with Admin priviledge over the VM
* *20.107.240.171* is the VM public IP address

#### Start exporter
```
# Within azureuser@target-1
cd /usr/src/app
python3 start_exporter.py
http://20.107.240.171:8000/
```