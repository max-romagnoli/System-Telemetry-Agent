import psutil

class NetworkCollector:

    
    def __init__(self) -> None:
        """
        Constructor
        """
        
    def get_unit(self, bytes):
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        size = bytes
        for unit in units:
            if size < 1024:
                return f"{size:.1f}{unit}"
        size /= 1024

    def get_traffic_in(self):
        """
        Returns the inbound traffic in Mb/s.
        """
        netStat = psutil.net_io_counters()
        return self.get_unit(netStat.bytes_recv) 

    def get_traffic_out(self):
        """
        Returns the outbound traffic in Mb/s.
        """
        netStat = psutil.net_io_counters()     
        return self.get_unit(netStat.bytes_sent) 
    
    def __str__(self) -> str:
        """
        Returns to string representation of all networking metrics.        
        """
        traffic_in = self.get_traffic_in()
        traffic_out = self.get_traffic_out()
        return f"Inbound Traffic: {traffic_in} Mb/s, Outbound Traffic: {traffic_out} Mb/s"

       

