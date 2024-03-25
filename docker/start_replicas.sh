#!/bin/bash
set -xe

NUM_INSTANCES=$1
MAX_INSTANCES=30
PROMETHEUS_SD_FILE='../prometheus/sd/local_replicas.json'

if [ "$(docker-compose ps -q | wc -l)" -gt 0 ]; then
    echo "Detected running services. Performing docker-compose down..."
    docker-compose down
fi

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <number_of_instances>"
    exit 1
fi


if [ "$NUM_INSTANCES" -gt "$MAX_INSTANCES" ]; then
    echo "Error: The number of instances cannot exceed $MAX_INSTANCES."
    exit 1
fi


# write docker-compose.override.yml

echo "version: '3.8'" > docker-compose.override.yml
echo "services:" >> docker-compose.override.yml

for (( i=1; i<=NUM_INSTANCES; i++ ))
do
    PORT=$((8000 + i))
    echo "  exporter-$i:" >> docker-compose.override.yml
    echo "    container_name: exporter-$i" >> docker-compose.override.yml
    echo "    ports:" >> docker-compose.override.yml
    echo "      - \"$PORT:8000\"" >> docker-compose.override.yml
    echo "    extends:" >> docker-compose.override.yml
    echo "      file: docker-compose.yml" >> docker-compose.override.yml
    echo "      service: exporter" >> docker-compose.override.yml
    echo "    profiles:" >> docker-compose.override.yml
    echo "      - replicas" >> docker-compose.override.yml
done

echo "docker-compose.override.yml has been generated."


# write Prometheus SD file

echo "[" > "$PROMETHEUS_SD_FILE"
echo "  {" >> "$PROMETHEUS_SD_FILE"
echo "    \"labels\": {\"job\": \"python_exporter\"}," >> "$PROMETHEUS_SD_FILE"
echo "    \"targets\": [" >> "$PROMETHEUS_SD_FILE"
for (( i=1; i<=NUM_INSTANCES; i++ ))
do
    PORT=$((8000 + i))
    if [ $i -gt 1 ]; then echo "," >> "$PROMETHEUS_SD_FILE"; fi
    echo -n "      \"exporter-$i:8000\"" >> "$PROMETHEUS_SD_FILE"
done
echo -e "\n    ]" >> "$PROMETHEUS_SD_FILE"
echo "  }" >> "$PROMETHEUS_SD_FILE"
echo "]" >> "$PROMETHEUS_SD_FILE"



cleanup() {
    docker-compose --profile replicas down
    echo -e "\nCleaning up docker-compose.override.yml..."
    > docker-compose.override.yml
    echo -e "Cleaning up $PROMETHEUS_SD_FILE...\n"
    > $PROMETHEUS_SD_FILE
    exit 0
}

trap cleanup SIGINT SIGTERM

docker-compose --profile replicas up -d

echo -e "\nDocker Compose started. Press CTRL+C to stop and clean up.\n"

while :; do 
    sleep 1
done
