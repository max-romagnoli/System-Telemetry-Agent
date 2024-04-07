#### Prometheus
```
# Within azureuser@target-1
sudo apt-get update
wget https://github.com/prometheus/prometheus/releases/download/v2.45.3/prometheus-2.45.3.linux-amd64.tar.gz
tar xvfz prometheus-*.tar.gz
cd prometheus-2.45.3.linux-amd64
sudo mkdir -p /usr/src/app
sudo mkdir -p /var/lib/prometheus
sudo cp ./prometheus /usr/src/app/
sudo cp ./promtool /usr/src/app/
sudo chown prometheus:prometheus /usr/src/app/prometheus
sudo chown prometheus:prometheus /usr/src/app/promtool
sudo chown -R azureuser:azureuser /usr/src/app/
sudo chown -R prometheus:prometheus /var/lib/prometheus/
sudo chmod -R 755 /var/lib/prometheus/
```

#### Copy Prometheus config files to VM
```
scp -i azure/target-1_key.pem prometheus/prometheus.yml azureuser@20.93.119.35:/usr/src/app
scp -i azure/target-1_key.pem -r prometheus/sd azureuser@20.93.119.35:/usr/src/app

sudo vim /etc/systemd/system/prometheus.service
# edit service file
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus
```