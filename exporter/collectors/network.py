import psutil
import time

class NetworkCollector:

    
    def __init__(self) -> None:
        """
        Constructor
        """
    
    def get_traffic_in(self):
        """
        @cindyariyo
        Returns the inbound traffic in Megabits.
        """
        traffic = psutil.net_io_counters()
        traffic_in = self.get_unit(traffic.bytes_recv)
        if not traffic_in:
            return None
        else:
            return traffic_in
    

    def get_traffic_out(self):
        """
        @cindyariyo
        Returns the outbound traffic in Megabits.
        """
        traffic = psutil.net_io_counters(nowrap=True)  
        traffic_out = self.get_unit(traffic.bytes_sent) 
        if not traffic_out:
            return None
        else: 
            return traffic_out
    

    def get_rate_traffic_in(self):
        """
        Returns the inbound traffic in Megabits/s.
        """
        prev_traffic = self.get_traffic_in()
        time.sleep(5)
        curr_traffic = self.get_traffic_in()

        if not curr_traffic or not prev_traffic:
            return None
        
        if curr_traffic < prev_traffic:
            return None     # TODO: for now just don't set, in the future need to calculate based on MAX_INTEGER value
        
        traffic_in_per_sec = (curr_traffic - prev_traffic) / 5
        return traffic_in_per_sec
     

    def get_rate_traffic_out(self):
        """
        Returns the outbound traffic in Megabits/s.
        """
        prev_traffic = self.get_traffic_out()
        time.sleep(5)
        curr_traffic = self.get_traffic_out()

        if not curr_traffic or not prev_traffic:
            return None
     
        if curr_traffic < prev_traffic:
            return None     # TODO: for now just don't set, in the future need to calculate based on MAX_INTEGER value

        traffic_out_per_sec = (curr_traffic - prev_traffic) / 5
        return traffic_out_per_sec


    def __str__(self) -> str:
        """
        @cindyariyo
        Returns to string representation of all networking metrics.        
        """
        traffic_in = self.get_rate_traffic_in()
        traffic_out = self.get_rate_traffic_out()
        return f"Inbound Traffic: {traffic_in} Mb/s, Outbound Traffic: {traffic_out} Mb/s"

    """
    Helper functions       
    """  
        
    def get_unit(self, bytes):
        """ 
        @cindyariyo
        Returns bytes sent and received in Megabits.
        """
        bits = bytes * 8
        megabits = bits /1000000
        return megabits