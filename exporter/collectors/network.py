import psutil

class NetworkCollector:
    
    
    def __init__(self) -> None:
        """
        Constructor
        """
    

    def get_traffic_in(self):
        """
        @cindyariyo
        Returns the inbound traffic in Mb/s.
        """
        traffic_in = psutil.net_io_counters()
        return self.get_unit(traffic_in.bytes_recv) 

    def get_traffic_out(self):
        """
        @cindyariyo
        Returns the outbound traffic in Mb/s.
        """
        traffic_out = psutil.net_io_counters(nowrap=True)   
        return self.get_unit(traffic_out.bytes_sent) 
    

    def __str__(self) -> str:
        """
        @cindyariyo
        Returns to string representation of all networking metrics.        
        """
        traffic_in = self.get_traffic_in()
        traffic_out = self.get_traffic_out()
        return f"Inbound Traffic: {traffic_in} Mb/s, Outbound Traffic: {traffic_out} Mb/s"


    """
    Helper methods        
    """

    def get_unit(self, bytes):
        bits = bytes * 8
        megabits = bits /1000000
        return megabits