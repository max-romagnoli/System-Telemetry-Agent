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
        @mccooeyc11
        Returns the CPU utilization as a percentage.
        """
        return psutil.cpu_percent()

    def get_frequency(self):
        """
        @mccooeyc11
        Returns the current CPU frequency in MHz.
        """
        return psutil.cpu_freq().current

    def get_temperature(self):
        """
        @mccooeyc11
        Returns the CPU temperature in degrees Celsius.        
        """
        if not psutil.sensors_temperatures():
            return None
        else:
            temps = psutil.sensors_temperatures()['acpitz'] # Temperature sensors may be under a different name - 'acpitz' is what works locally
            if len(temps) > 0:
                return temps[0].current
            else:
                return None

    def __str__(self) -> str:
        """
        @mccooeyc11
        Returns to string representation of all CPU metrics.        
        """
        utilization = self.get_utilization()
        frequency = self.get_frequency()
        temp = self.get_temperature().__str__()
        return f"CPU utilization: {utilization}%\n CPU frequency: {frequency}MHz\n CPU temperature: {temp}°C\n"
