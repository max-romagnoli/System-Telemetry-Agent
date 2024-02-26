from prometheus_client import start_http_server
import time

from .metrics import *
from .collectors.cpu import CPUCollector
from .collectors.network import NetworkCollector

cpu_collector = CPUCollector()
network_collector = NetworkCollector()

def export_metrics(port=8000):
    """
    TODO:
    Starts an http server on port 8000 and enters a loop to collect metrics and export them to Prometheus.
    """
    start_http_server(port)
    print(f"Exporter running on port {port}")
    while True:
        cpu_utilization_gauge.set(cpu_collector.get_utilization())
        network_get_traffic_in_gauge.set(network_collector.get_traffic_in())
        network_get_traffic_out_gauge.set(network_collector.get_traffic_out())
        time.sleep(5)
