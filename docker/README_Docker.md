### Docker set up

* First make sure you have Docker Engine installed. If you haven't, get it from: https://docs.docker.com/engine/install/

* Ensure the Docker Engine is running (if not, open Docker Desktop)

* Open zsh/pwsh/bash in root folder

* Make sure you are in the docker subdirectory: <br>
    `cd docker`

<br>

### Development Workflow


**Start System with N Exporters:**

1. Run the script specifying how many *exporter* replicas you want to generate: <br>
    `./start_replicas.sh <number>`
2. Stop the system and clean up configurations: <br>
    `Press CTRL+C`

<br>

**Start System with One Exporter (No Replicas):**

1. Build a new image as per Dockerfile: <br>
    `docker compose build`

2. Create and run all the containers: <br>
    `docker compose up`
   
<br>

To run only a specific container: `docker compose up service-name` 

---

3. When you are done developing: <br>
    `docker compose down`
