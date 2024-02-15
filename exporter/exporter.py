from prometheus_client import start_http_server
import time

from .metrics import *
from .collectors.cpu import CPUCollector
from .collectors.ram import RAMCollector


cpu_collector = CPUCollector()
ram_collector = RAMCollector()


def export_metrics(port=8000):

    """
    TODO:
    Starts an http server on port 8000 and enters a loop to collect metrics and export them to Prometheus.
    """

    start_http_server(port)
    print(f"Exporter running on port {port}")

    while True:

        cpu_utilization_gauge.set(cpu_collector.get_utilization())

        time.sleep(5)