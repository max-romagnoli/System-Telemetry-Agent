### Setup Email alerts

To allow Alertmanager to send emails, before starting the system with Docker compose:

  * In `docker/.env` add a line for the Gmail App Password:
    ```
    ALERTMANAGER_APP_PWD=<insert app pwd>
    ```