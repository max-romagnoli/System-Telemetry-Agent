#!/bin/bash

DOCKER_COMPOSE_FILE="docker-compose.yml"
DOCKER_COMPOSE_OVERRIDE_FILE="docker-compose.override.yml"

if ! command -v yq &> /dev/null; then
    echo "yq is not installed. Installing..."
    sudo wget -O /usr/bin/yq https://github.com/mikefarah/yq/releases/download/v4.43.1/yq_linux_amd64
    sudo chmod +x /usr/bin/yq
fi

if ! command -v docker-compose &> /dev/null; then
    echo "docker-compose is not installed. Please install it to proceed."
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

if [ ! -f "$DOCKER_COMPOSE_OVERRIDE_FILE" ]; then
    echo "Docker Compose override file does not exist. Please ensure it's present."
    exit 1
fi


# Pick exporters to shut down

NUM_EXPORTERS=$(yq e '.services | keys | length' "$DOCKER_COMPOSE_OVERRIDE_FILE")

if [ "$NUM_EXPORTERS" -le 2 ]; then
  REMOVE_COUNT=1
else
  REMOVE_COUNT=2
fi

declare -A RAND_NUMS
while [ "${#RAND_NUMS[@]}" -lt "$REMOVE_COUNT" ]; do
    RAND_NUM=$(( RANDOM % NUM_EXPORTERS + 1 ))
    RAND_NUMS[$RAND_NUM]=1
done


# Shut down exporters

for NUM in "${!RAND_NUMS[@]}"
do
    EXPORTER_NAME="exporter-$NUM"
    echo "Stopping and removing $EXPORTER_NAME..."
    docker-compose -f "$DOCKER_COMPOSE_FILE" -f "$DOCKER_COMPOSE_OVERRIDE_FILE" stop "$EXPORTER_NAME"
    docker-compose -f "$DOCKER_COMPOSE_FILE" -f "$DOCKER_COMPOSE_OVERRIDE_FILE" rm -f "$EXPORTER_NAME"
done


cleanup() {
    echo "Restarting all services..."
    docker-compose -f "$DOCKER_COMPOSE_FILE" -f "$DOCKER_COMPOSE_OVERRIDE_FILE" --profile replicas up -d
}

trap cleanup EXIT

echo "Press any key to finalize and restart all services."
read -n 1