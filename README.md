# System-Telemetry-Agent
A monitoring agent which runs on Linux machines and collects system metrics.


## Setup Prometheus

* Use the correct OS version in the below commands. For example:
    * On Linux/WSL AMD 64: `linux-amd64`
    * On Mac AMD: `darwin-amd64`
    * On Mac ARM: `darwin-arm64`

* Open bash/zsh terminal in root folder:

* `cd prometheus`

* Download tar from GitHub:  
    * **On Linux/WSL**: 
        ```
        wget https://github.com/prometheus/prometheus/releases/download/v2.45.3/prometheus-2.45.3.linux-amd64.tar.gz
        ```
    * **On Mac** (change to *arm64* if on M1): 
        ```
        curl -LO https://github.com/prometheus/prometheus/releases/download/v2.45.3/prometheus-2.45.3.darwin-amd64.tar.gz
        ```

* Unzip folder contents onto current directory keeping current config: <br>
  `tar xvfzk prometheus-2.45.3.<add-your-os>.tar.gz -C . --strip-components=1`

* Delete zipped folder and unnecessary binaries: <br>
  `rm -r prometheus-2.45.3.<add-your-os>.tar.gz console* LICENSE NOTICE`

* Start the Prometheus server on port 9090: <br>
    `./prometheus`

* You can open the Prometheus UI in your browser at: <br>
    `localhost:9090`



## Setup Grafana

* Use the correct OS version in the below commands. For example:
    * On Linux/WSL AMD 64: `linux-amd64`
    * On Mac AMD: `darwin-amd64`
    * On Mac ARM: `darwin-arm64`

* Open bash terminal in root folder:

* `cd grafana`

* Download tar from official website:  
    * **On Linux/WSL**: 
        ```
        wget https://dl.grafana.com/oss/release/grafana-10.3.1.linux-amd64.tar.gz
        ```
    * **On Mac** (change to *arm64* if on M1): 
        ```
        curl -LO https://dl.grafana.com/oss/release/grafana-10.3.1.darwin-amd64.tar.gz
        ```

* Unzip folder contents onto current directory keeping current config: <br>
  `tar xvfzk grafana-10.3.1.<add-your-os>.tar.gz -C . --strip-components=1`

* Delete zipped folder and unnecessary binaries: <br>
  `rm -r grafana-10.3.1.<add-your-os>.tar.gz LICENSE NOTICE.md VERSION`

* Start Grafana server on port 3000: <br>
    `./bin/grafana server`

* You can open the Grafana UI in your browser at: <br>
    `localhost:3000`

* Login using _admin_ for both username and password.

