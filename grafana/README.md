## Grafana development using Docker

### Run the system

**Start System Telemetry Agent locally:**

1. Build a new image as per Dockerfile: <br>
    `docker compose build`

2. Create and run all the containers: <br>
    `docker compose up`

---

3. When you are done developing: <br>
    `docker compose down`


### Setup Grafana API 
**(1st time only)**

* Run the system as shown above
* Open `localhost:3000`
* Navigate to `Administration/Users and Access/Service Accounts`
* Add a new service account
* Name it `GRAFANA_SYNC_API`
* Change the role to "Admin"
* Click on **Add service account token**
* Name the token `GRAFANA_SYNC_API`
* Copy and paste the secret to your clipboard
* Create a new file called `.env` in the `docker/` folder
* Inside that file write:
  ```
  GRAFANA_SYNC_API=copy_here_your_secret
  COMPOSE_PROJECT_NAME=system-telemetry-agent
  ``` 
* Run the grafana-sync-script container:
    `docker compose up grafana-sync-script`






## [LEGACY] Setup Grafana

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


## [LEGACY] Workflow for Local Development in Grafana

### Setup Grafana API 
**(1st time only)**

* In the browser navigate to `Administration/Users and Access/Service Accounts`
* Add a new service account
* Name it `GRAFANA_SYNC_API`
* Click on **Add service account token**
* Name the token `GRAFANA_SYNC_API`
* Copy and paste the secret to your clipboard.
* **Now open the terminal in VS Code:**
    *  `cd scripts`
    * Write secret into .env file: <br>
      `echo "GRAFANA_SYNC_API=<paste-your-secret-here>" > .env`
    * Write the URI grafana is running on locally (change if needed): <br>
      `echo "GRAFANA_LOCAL_API_URI=http://localhost:3000/api" >> .env`
    * **IMPORTANT:** make sure you never commit the `.env` file!

### Install requirements for script
**(1st time only)**

* **NOTE:** this might change if we run Grafana with Docker.
* In root of the project: <br>
  `pip install -r requirements.txt`

### Workflow

This should be the workflow to follow when developing locally on Grafana:

1. **Start Grafana server: <br>**
   `cd grafana` <br>
   `./bin/grafana server`

2. **Run the export script: <br>**
   `cd ..` <br>
   `cd scripts` <br>
   `python3 export_dashboards.py` <br>
   
3. **Ensure that BOTH Grafana and the script are running without errors <br>**

4. **Open Grafana in browser... <br>**
   `localhost:3000` <br>

5. **... and start developing.**
   Changes made in the browser should appear in the repo.
   
6. **Commit often and add descriptions to your commits.**