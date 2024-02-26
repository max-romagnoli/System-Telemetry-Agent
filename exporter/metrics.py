from prometheus_client import Gauge

cpu_utilization_gauge = Gauge("cpu_utilization", "CPU utilization percentage")
cpu_frequency_gauge = Gauge("cpu_frequency", "CPU frequency in MHz")
cpu_temperature_gauge = Gauge("cpu_temperature", "CPU temperature in Celsius")

network_get_traffic_in_gauge = Gauge("stagent_traffic_in_mbs", "NETWORK inbound traffic in Mb/s")
network_get_traffic_out_gauge = Gauge("stagent_traffic_out_mbs", "NETWORK outbound traffic in Mb/s")

ram_utilization_gauge = Gauge("stagent_ram_utilization_percentage", "Total RAM utilization as a percentage")
ram_memory_gauge = Gauge("stagent_ram_memory_bytes", "Total RAM memory installed in bytes")
