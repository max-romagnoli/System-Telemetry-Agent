import psutil

class RAMCollector:

    def __init__(self) -> None:
        """
        @l3331l4
        Constructor
        """
        pass

    def get_utilization(self):
        """
        @l3331l4
        Returns the RAM utilization as a percentage.
        """
        return psutil.virtual_memory().percent

    def get_memory(self):
        """
        @l3331l4
        Returns the total memory installed.
        """
        return psutil.virtual_memory().total

    def get_memory_available(self):
        """
        @ljdzed
        Return the total memory available
        """
        return psutil.virtual_memory().available

    def get_memory_used(self):
        """
        @ljdzed
        Returns the total memory used as the difference of get_memory and get_memory_available
        """
        memoryUsed = self.get_memory() - self.get_memory_available()
        return memoryUsed

    def __str__(self) -> str:
        """
        Returns to string representation of all RAM metrics.        
        """
        utilization = self.get_utilization()
        memoryTotal = self.get_memory()
        memoryUsed = self.get_memory_used()
        memoryAvailable = self.get_memory_available()
        return f"RAM Utilization: {utilization}%\nTotal Memory: {memoryTotal} bytes\nUsed Memory: {memoryUsed} bytes\nAvailable Memory: {memoryAvailable} bytes"
