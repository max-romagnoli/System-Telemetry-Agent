import psutil

class CPUCollector:

    def __init__(self) -> None:
        """
        TODO: @
        Constructor
        """
        pass

    def get_utilization(self):
        """
        TODO: @
        Returns the CPU utilization as a percentage.
        """
        pass

    def get_frequency(self):
        """
        TODO: @
        Returns the current CPU frequency in MHz.
        """
        try:
            with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r') as f:
                frequency = int(f.read()) / 1000 
            return frequency
        except Exception as e:
            print(f"Error reading CPU frequency: {e}")
            return None
        pass

    def get_temperature(self):
        """
        TODO: @
        Returns the CPU temperature in degrees Celsius.        
        """
        pass

    def __str__(self) -> str:
        """
        TODO:
        Returns to string representation of all CPU metrics.        
        """
        pass
