#!/bin/bash

error=""

if [ ! -f /usr/src/app/requirements.txt ]; then
    error="${error}Error: requirements.txt not found.\n"
fi

if [ ! -f /usr/src/app/start_exporter.py ]; then
    error="${error}Error: start_exporter.py not found.\n"
fi

if [ ! -d /usr/src/app/exporter/ ]; then
    error="${error}Error: exporter/ directory not found.\n"
fi

if [ ! -z "$error_message" ]; then
    echo -e "One or more errors detected. Please deploy the missing components and restart the VM:\n$error_message"
    exit 1
fi


nohup /usr/bin/python3 /usr/src/app/server.py > /var/log/server.log 2>&1 &
