# System-Telemetry-Agent
A monitoring agent which runs on Linux machines and collects system metrics.


## Setup Prometheus

### Linux/WSL/VMs

* Open bash terminal in root folder:

* `cd prometheus`

* Download tar from GitHub:  
    `wget https://github.com/prometheus/prometheus/releases/download/v2.1.0/prometheus-2.1.0.linux-amd64.tar.gz`

* Unzip folder contents onto current directory keeping current config: <br>
    `tar xvfzk prometheus-2.1.0.linux-amd64.tar.gz -C . --strip-components=1`

* Delete zipped folder and unnecessary binaries: <br>
    `rm -r prometheus-2.1.0.linux-amd64.tar.gz console* LICENSE NOTICE`

* Start the Prometheus server on port 9090: <br>
    `./prometheus`

* You can open the Prometheus UI in your browser at: <br>
    `localhost:9090`


### Windows


### Mac


## Setup Grafana

### Linux/WSL/VMs

* Open bash terminal in root folder:

* `cd grafana`

* Download tar from official website:  
    `wget https://dl.grafana.com/oss/release/grafana-10.3.1.linux-amd64.tar.gz`

* Unzip folder contents onto current directory keeping current config: <br>
    `tar xvfzk grafana-10.3.1.linux-amd64.tar.gz -C . --strip-components=1`

* Delete zipped folder and unnecessary binaries: <br>
    `rm -r grafana-10.3.1.linux-amd64.tar.gz LICENSE NOTICE`

* Start Grafana server on port 3000: <br>
    `./bin/grafana-server`

* You can open the Grafana UI in your browser at: <br>
    `localhost:3000`

* Login using _admin_ for both username and password.


### Windows


### Mac
