## Manual Deployment of the Exporter on a VM

#### Create a VM on Azure Portal
* For this walkthrough I created a VM called **target-1**
* Choose size. Here I chose **B1s** (€30.75 per month)
* Save .pem file `target-1_key.pem` in `azure/`

#### Connect to VM using ssh
```
cd System-Telemetry-Agent
chmod 600 azure/target-1_key.pem
ssh -i azure/target-1_key.pem azureuser@52.169.145.243
```
Notes: 
* *target-1_key.pem* is the file containing the SSH key (!!!! DO NOT COMMIT IT !!!)
* *azureuser* is the user with Admin priviledge over the VM
* *20.107.240.171* is the VM public IP address

#### Install Python and requirements
```
# Within azureuser@target-1
sudo apt-get update
sudo apt-get install --no-install-recommends -y python3 python3-dev python3-pip curl build-essential
```

#### Copy files from local to VM
```
# Within azureuser@target-1
sudo mkdir -p /usr/src/app
sudo chown -R azureuser:azureuser /usr/src/app/

# Within System-Telemetry-Agent
scp -i azure/target-1_key.pem -r exporter azureuser@52.169.145.243:/usr/src/app/
scp -i azure/target-1_key.pem requirements.txt azureuser@52.169.145.243:/usr/src/app/
scp -i azure/target-1_key.pem start_exporter.py azureuser@52.169.145.243:/usr/src/app/
scp -i azure/target-1_key.pem azure/scripts/exporter_startup.sh azureuser@52.169.145.243:/usr/src/app/
```

#### Setup Exporter to run on startup
```
# Within azureuser@target-1
sudo nano /etc/rc.local
ctrl+O Enter ctrl+X
sudo chmod +x /etc/rc.local
sudo chmod +x /usr/src/app/exporter_startup.sh
# Check for errors
sudo less /var/log/start_exporter.log
# Modify startup script without re-deploying
sudo nano /usr/src/app/exporter_startup.sh
# Manually startup
sudo /usr/src/app/exporter_startup.sh
```

#### Install Python dependencies from requirements.txt
```
# Within azureuser@target-1
cd /usr/src/app
pip3 install --no-cache-dir -r requirements.txt
```

#### Start exporter
```
# Within azureuser@target-1
cd /usr/src/app
python3 start_exporter.py
http://20.107.240.171:8000/
```