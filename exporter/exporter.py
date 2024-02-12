from prometheus_client import start_http_server, Gauge
import time


def export_metrics(port=8000):

    start_http_server(port)
    print(f"Exporter running on port {port}")

    while True:
        
        # TODO: collect metrics

        time.sleep(5)