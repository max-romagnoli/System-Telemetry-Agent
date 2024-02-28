from prometheus_client import start_http_server
import time

from .metrics import *
from .collectors.cpu import CPUCollector
from .collectors.ram import RAMCollector


cpu_collector = CPUCollector()
ram_collector = RAMCollector()


def export_metrics(port=8000):

    """
    Starts an http server on port 8000 and enters a loop to collect metrics and export them to Prometheus.
    """

    start_http_server(port)
    print(f"Exporter running on port {port}")

    while True:

        set_gauge(cpu_utilization_gauge, cpu_collector.get_utilization())
        set_gauge(cpu_frequency_gauge, cpu_collector.get_frequency())
        set_gauge(cpu_temperature_gauge, cpu_collector.get_temperature())

        set_gauge(ram_utilization_gauge, ram_collector.get_utilization())
        set_gauge(ram_memory_gauge, ram_collector.get_memory())

        time.sleep(5)


def set_gauge(gauge=Gauge, value=float):

    """
    Sets the gauge to the specified value if the value is not None.
    """
    
    if value is not None:
        gauge.set(value)