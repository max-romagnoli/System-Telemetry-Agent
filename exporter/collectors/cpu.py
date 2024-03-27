import psutil

class CPUCollector:

    def __init__(self) -> None:
        """
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
        if psutil.cpu_freq():
            return psutil.cpu_freq().current
        else:
            return None

    def get_temperature(self):
        """
        @mccooeyc11
        Returns the CPU temperature in degrees Celsius.        
        """
        print(psutil.sensors_temperatures()) ## Debugging Purposes
        if not psutil.sensors_temperatures():
            return None
        else:
            temps = psutil.sensors_temperatures()['acpitz']
            if temps and len(temps) > 0:
                return temps[0].current
            else:
                return None

    def get_utilization_by_core(self):
        """
        @l3331l4
        Returns a list of CPU utilization percentages for each logical core and physical core.
        """    
        cpu_percent = psutil.cpu_percent(percpu=True)
        logical_processors_per_core = psutil.cpu_count(logical=True) // psutil.cpu_count(logical=False)
        core_utilizations = []  
        for i in range(0, len(cpu_percent), logical_processors_per_core):
            core_utilization = sum(cpu_percent[i:i+logical_processors_per_core]) 
            core_utilizations.append(core_utilization)

        return cpu_percent, core_utilizations

    def __str__(self) -> str:
        """
        @mccooeyc11
        Returns to string representation of all CPU metrics.        
        """
        utilization = self.get_utilization()
        frequency = self.get_frequency()
        temp = self.get_temperature()
        if temp:
            temp = temp.__str__()
            return f"CPU utilization: {utilization}%\n CPU frequency: {frequency}MHz\n CPU temperature: {temp}°C\n"
        else:
            return f"CPU utilization: {utilization}%\n CPU frequency: {frequency}MHz\n CPU temperature: not available\n"
