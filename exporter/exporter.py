from prometheus_client import start_http_server
import time

from .metrics import *
from .collectors.cpu import CPUCollector
from .collectors.network import NetworkCollector
from .collectors.ram import RAMCollector
from .collectors.disk import DiskCollector

cpu_collector = CPUCollector()
ram_collector = RAMCollector()
network_collector = NetworkCollector()
disk_collector = DiskCollector()


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
        utilization_by_logical_core, utilization_by_physical_core = cpu_collector.get_utilization_by_core()
        set_gauge_from_list(cpu_utilization_by_logical_core_gauge, utilization_by_logical_core, label_name="core")    
        set_gauge_from_list(cpu_utilization_by_physical_core_gauge, utilization_by_physical_core, label_name="core")  
             
        set_gauge(ram_utilization_gauge, ram_collector.get_utilization())
        set_gauge(ram_memory_total_gauge, ram_collector.get_memory_total())
        set_gauge(ram_memory_used_gauge,ram_collector.get_memory_used())
        set_gauge(ram_memory_available_gauge,ram_collector.get_memory_available())

        set_gauge(network_get_traffic_in_gauge, network_collector.get_traffic_in())
        set_gauge(network_get_traffic_out_gauge, network_collector.get_traffic_out())
        set_gauge(network_get_traffic_in_rate_gauge, network_collector.get_rate_traffic_in())
        set_gauge(network_get_traffic_out_rate_gauge, network_collector.get_rate_traffic_out())

        set_gauge(disk_utilization_gauge, disk_collector.get_utilization())
        set_gauge(disk_total_space_gauge, disk_collector.get_total_space())
        set_gauge(disk_free_space_gauge, disk_collector.get_free_space())
        set_gauge(disk_reads_bytes_gauge, disk_collector.get_reads_bytes())
        set_gauge(disk_writes_bytes_gauge, disk_collector.get_writes_bytes())
        set_gauge(disk_reads_ops_gauge, disk_collector.get_reads_ops())
        set_gauge(disk_writes_ops_gauge, disk_collector.get_writes_ops())

        time.sleep(5)


def set_gauge(gauge=Gauge, value=float):

    """
    Sets the gauge to the specified value if the value is not None.
    """
    
    if value is not None:
        gauge.set(value)

def set_gauge_from_list(gauge=Gauge, list=list, label_name=str):

    """
    Sets the gauge to the specified list of values if the values are not None.
    """  
    if list is not None:
        for index in range(len(list)):
            value = list[index]
            gauge.labels(**{label_name: str(index)}).set(value)