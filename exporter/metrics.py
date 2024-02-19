from prometheus_client import Gauge

cpu_utilization_gauge = Gauge("cpu_utilization", "CPU utilization percentage")
cpu_frequency_gauge = Gauge("cpu_frequency", "CPU frequency in MHz")
cpu_temperature_gauge = Gauge("cpu_temperature", "CPU temperature in Celsius")

ram_utilization_gauge = Gauge("ram_utilization", "RAM utilization percentage")
ram_memory_gauge = Gauge("ram_memory", "Total RAM memory installed")
