### Docker set up

* First make sure you have Docker Engine installed. If you haven't, get it from: https://docs.docker.com/engine/install/

* Ensure the Docker Engine is running (if not, open Docker Desktop)

* Open zsh/pwsh/bash in root folder

* Make sure you are in the docker subdirectory: <br>
    `cd docker`

<br>

**Re-run these two commands everytime you make changes and want to test the exporter in Docker**:

1. Build a new image as per Dockerfile: <br>
    `docker compose build`

2. Create and run one container from image: <br>
    `docker compose up exporter`