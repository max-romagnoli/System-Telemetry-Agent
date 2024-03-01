### Docker set up

* First make sure you have Docker Engine installed. If you haven't, get it from: https://docs.docker.com/engine/install/

* Ensure the Docker Engine is running (if not, open Docker Desktop)

* Open zsh/pwsh/bash in root folder

* Make sure you are in the docker subdirectory: <br>
    `cd docker`

<br>

### Development Workflow

**Start System Telemetry Agent locally:**

1. Build a new image as per Dockerfile: <br>
    `docker compose build`

2. Create and run all the containers: <br>
    `docker compose up`
   
<br>

To run only a specific container: `docker compose up service-name` 

---

3. When you are done developing: <br>
    `docker compose down`
