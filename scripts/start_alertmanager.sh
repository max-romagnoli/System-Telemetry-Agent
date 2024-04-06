#!/bin/sh

TEMPLATE_FILE="/etc/alertmanager/config/alertmanager.template.yml"
FINAL_CONFIG="/etc/alertmanager/config/alertmanager.yml"

sed "s/\${ALERTMANAGER_APP_PWD}/${ALERTMANAGER_APP_PWD:-defaultvalue}/g" "$TEMPLATE_FILE" > "$FINAL_CONFIG"

exec /bin/alertmanager --config.file=$FINAL_CONFIG --log.level=debug