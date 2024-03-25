## Docker set up

* First make sure you have Docker Engine installed. If you haven't, get it from: https://docs.docker.com/engine/install/

* Ensure the Docker Engine is running (if not, open Docker Desktop)

* Open zsh/pwsh/bash in root folder

* Make sure you are in the docker subdirectory: <br>
    `cd docker`

<br>

## Development Workflow


### **Start System with N Exporters:**

**First time only**: run `chmod +x start_replicas.sh` to make script executable

1. Run the script specifying how many *exporter* replicas you want to generate: <br>
    `./start_replicas.sh <number>`
2. Stop the system and clean up configurations: <br>
    `Press CTRL+C`


### **Start System with One Exporter:**

1. Build a new image as per Dockerfile: <br>
    `docker compose --profile single-exporter build`

2. Create and run all the containers with 1 exporter: <br>
    `docker compose --profile single-exporter up`

   *To run only a specific container:* `docker compose up service-name` 

3. When you are done developing: <br>
    `docker compose --profile single-exporter down`
