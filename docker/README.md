### Docker set up

* First make sure you have Docker Engine installed. If you haven't, get it from: https://docs.docker.com/engine/install/

* Ensure the Docker Engine is running (if not, open Docker Desktop)

* Open zsh/pwsh/bash in root folder

* `cd docker`

* Build a new image as per Dockerfile: <br>
    `docker build -t ubuntu-target-img .`

* Create and run one container from image: <br>
    `docker run -d -p 80:80 -p 9100:9100 --name ubuntu-target1 ubuntu-target-img`