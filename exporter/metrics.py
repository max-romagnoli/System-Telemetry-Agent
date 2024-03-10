from prometheus_client import Gauge

cpu_utilization_gauge = Gauge("stagent_cpu_utilization_overall_percentage", "System-wide CPU utilization as a percentage")
cpu_frequency_gauge = Gauge("stagent_cpu_frequency_current_mhz", "CPU frequency in MHz")
cpu_temperature_gauge = Gauge("stagent_cpu_coretemp_sensor_1_celsius", "Core temperature from Sensor 1 in Celsius")

network_get_traffic_in_gauge = Gauge("stagent_traffic_in_mbs", "NETWORK inbound traffic in Mb/s")
network_get_traffic_out_gauge = Gauge("stagent_traffic_out_mbs", "NETWORK outbound traffic in Mb/s")

ram_utilization_gauge = Gauge("stagent_ram_utilization_percentage", "Total RAM utilization as a percentage")
ram_memory_gauge = Gauge("stagent_ram_memory_bytes", "Total RAM memory installed in bytes")

disk_utilization_gauge = Gauge("stagent_disk_utilization_percentage", "Used Disk space as a percentage")
disk_total_space_gauge = Gauge("stagent_disk_total_space_bytes", "Disk total storage (used and unused) in bytes")
disk_free_space_gauge = Gauge("stagent_disk_free_space_bytes", "Disk free storage in bytes")
disk_reads_bytes_gauge = Gauge("stagent_disk_reads_bytes", "Disk number of bytes read")
disk_writes_bytes_gauge = Gauge("stagent_disk_writes_bytes", "Disk number of bytes written")
disk_reads_ops_gauge = Gauge("stagent_disk_reads_ops", "Disk number of read operations")
disk_writes_ops_gauge = Gauge("stagent_disk_writes_ops", "Disk number of write operations")