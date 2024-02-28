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
        return psutil.cpu_freq()[0]

    def get_temperature(self):
        """
        TODO: @mccooeyc11
        Returns the CPU temperature in degrees Celsius.        
        """
        print("TEMPS:\n")
        print(psutil.sensors_temperatures())
        if not psutil.sensors_temperatures():
            return 20.0
        else:
            return psutil.sensors_temperatures()[0][0][1]

    def __str__(self) -> str:
        """
        @mccooeyc11
        Returns to string representation of all CPU metrics.        
        """
        utilization = self.get_utilization()
        frequency = self.get_frequency()
        temp = self.get_temperature().__str__()
        return "CPU utilization: {utilization}%\n CPU frequency: {frequency}MHz\n CPU temperature: {temp}°C\n"
