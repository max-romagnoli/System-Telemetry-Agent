import psutil
import time

class NetworkCollector:
    
    
    def __init__(self) -> None:
        """
        Constructor
        """
    
    
    def get_unit(self, bytes):
        """ 
        Returns bytes sent and received in Megabits.
        """
        bits = bytes * 8
        megabits = bits /1000000
        return megabits
    

    def get_traffic_in(self):
        """
        Returns the inbound traffic in Megabits.
        """
        traffic_in = psutil.net_io_counters()
        if not traffic_in:
            return None
        else:
            return self.get_unit(traffic_in.bytes_recv) 
    

    def get_traffic_out(self):
        """
        Returns the outbound traffic in Megabits.
        """
        traffic_out = psutil.net_io_counters(nowrap=True)  
        if not traffic_out:
            return None
        else: 
            return self.get_unit(traffic_out.bytes_sent) 
    

    def get_rate_traffic_in(self):
        """
        Returns the inbound traffic in Megabits/s.
        """
        curr_traffic = self.get_unit(psutil.net_io_counters().bytes_recv)
        time.sleep(5)
        prev_traffic = self.get_traffic_in()
        traffic_in_per_sec = abs(curr_traffic - prev_traffic) / 5
        if not traffic_in_per_sec:
            return None
        else:
            return traffic_in_per_sec
     

    def get_rate_traffic_out(self):
        """
        Returns the outbound traffic in Megabits/s.
        """
        curr_traffic = self.get_unit(psutil.net_io_counters(nowrap=True).bytes_sent)
        time.sleep(5)
        prev_traffic = self.get_traffic_out()
        traffic_out_per_sec = abs(curr_traffic - prev_traffic) / 5
        if not traffic_out_per_sec:
            return None
        else:
            return traffic_out_per_sec


    def __str__(self) -> str:
        """
        Returns to string representation of all networking metrics.        
        """
        traffic_in = self.get_rate_traffic_in()
        traffic_out = self.get_rate_traffic_out()
        return f"Inbound Traffic: {traffic_in} Mb/s, Outbound Traffic: {traffic_out} Mb/s"