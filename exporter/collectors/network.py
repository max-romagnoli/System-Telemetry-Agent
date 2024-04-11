import psutil
import time

class NetworkCollector:

    prev_traffic_out = 0.0
    prev_traffic_in = 0.0
    
    
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
        traffic_in = traffic.bytes_recv
        if traffic_in == None:
            return None
        else:
            return traffic_in
    

    def get_traffic_out(self):
        """
        @cindyariyo
        Returns the outbound traffic in Megabits.
        """
        traffic = psutil.net_io_counters(nowrap=True)  
        traffic_out = traffic.bytes_sent 
        if traffic_out == None:
            return None
        else: 
            return traffic_out
        

    def get_rate_traffic_in(self):
        """
        @ljdzed
        Returns the inbound traffic in Megabits/s.
        """

        curr_traffic = self.get_traffic_in()  

        traffic_in_per_sec = (curr_traffic - self.prev_traffic_in) / 5
       
        if curr_traffic == None or self.prev_traffic_in == None:
            
            return None
        
        if curr_traffic < self.prev_traffic_in:
            return None     # TODO: for now just don't set, in the future need to calculate based on MAX_INTEGER value

        self.prev_traffic_in = curr_traffic        

        return self.get_unit(traffic_in_per_sec)
     

    def get_rate_traffic_out(self):
        """
        @ljdzed
        Returns the outbound traffic in Megabits/s.
        """

        curr_traffic = self.get_traffic_out()

        traffic_out_per_sec = (curr_traffic - self.prev_traffic_out) / 5

        if curr_traffic == None or self.prev_traffic_out == None:
            
            return None
     
        if curr_traffic < self.prev_traffic_out:
            return None     # TODO: for now just don't set, in the future need to calculate based on MAX_INTEGER value

        self.prev_traffic_out = curr_traffic
        return self.get_unit(traffic_out_per_sec)


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
        0.000008
        return megabits