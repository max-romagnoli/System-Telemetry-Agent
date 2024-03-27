import psutil

class NetworkCollector:

    
    def __init__(self) -> None:
        """
        Constructor
        """
        self.prev_traffic_in = 0
        self.prev_traffic_out = 0

    
    def get_traffic_in(self):
        """
        @cindyariyo
        Returns the inbound traffic in Megabits.
        """
        traffic_in = psutil.net_io_counters()
        if not traffic_in:
            return 0.0
        else:
            return self.get_unit(traffic_in.bytes_recv)
    

    def get_traffic_out(self):
        """
        @cindyariyo
        Returns the outbound traffic in Megabits.
        """
        traffic_out = psutil.net_io_counters(nowrap=True)  
        if not traffic_out:
            return 0.0
        else: 
            return self.get_unit(traffic_out.bytes_sent) 
    

    def get_rate_traffic_in(self):
        """
        Returns the inbound traffic in Megabits/s.
        """
        traffic_in_per_sec = 0.0
        curr_traffic = self.get_traffic_in() 
        if curr_traffic !=0 and self.prev_traffic_in != 0:
            traffic_in_per_sec = (curr_traffic - self.prev_traffic_in) / 5
            self.prev_traffic_in = curr_traffic 
            return traffic_in_per_sec
        elif curr_traffic !=0 or self.prev_traffic_in != 0:
            traffic_in_per_sec = max(curr_traffic, self.prev_traffic_in) / 5
            self.prev_traffic_in = curr_traffic
            return traffic_in_per_sec
        else:
            return traffic_in_per_sec
     

    def get_rate_traffic_out(self):
        """
        Returns the outbound traffic in Megabits/s.
        """
        traffic_out_per_sec = 0.0
        curr_traffic = self.get_traffic_out() 
        if curr_traffic !=0 and self.prev_traffic_out != 0:
            traffic_out_per_sec = (curr_traffic - self.prev_traffic_out) / 5
            self.prev_traffic_out = curr_traffic 
            return traffic_out_per_sec
        elif curr_traffic !=0 or self.prev_traffic_out != 0:
            traffic_out_per_sec = max(curr_traffic, self.prev_traffic_out) / 5
            self.prev_traffic_out = curr_traffic
            return traffic_out_per_sec
        else:
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

if __name__ == '__main__':
    print(NetworkCollector().__str__())