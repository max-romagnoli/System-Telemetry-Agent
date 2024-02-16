from prometheus_client import Gauge

cpu_utilization_gauge = Gauge("cpu_utilization", "CPU utilization percentage")
cpu_frequency_gauge = Gauge("cpu_frequency", "CPU frequency in MHz")
cpu_temperature_gauge = Gauge("cpu_temperature", "CPU temperature in Celsius")

network_get_traffic_in_gauge = Gauge("network_get_traffic_in", "NETWORK inbound traffic in Mb/s")
network_get_traffic_out_gauge = Gauge("network_get_traffic_in", "NETWORK outbound traffic in Mb/s")