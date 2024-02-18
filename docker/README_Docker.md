### Docker set up

* First make sure you have Docker Engine installed. If you haven't, get it from: https://docs.docker.com/engine/install/

* Ensure the Docker Engine is running (if not, open Docker Desktop)

* Open zsh/pwsh/bash in root folder

* Make sure you are in the docker subdirectory: <br>
    `cd docker`

<br>


### FRONTEND Development

**Start System Telemetry Agent locally:**:

1. Build a new image as per Dockerfile: <br>
    `docker compose build`

2. Create and run all the containers: <br>
    `docker compose up`


### BACKEND Development

**Re-run these two commands everytime you make changes and want to test the exporter in Docker**:

1. Build as per docker-compose.yml: <br>
    `docker compose build`

2. Create and run one the exporter container from image: <br>
    `docker compose up exporter`