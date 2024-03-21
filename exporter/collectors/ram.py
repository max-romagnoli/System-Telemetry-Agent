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
        if psutil.virtual_memory():
            return psutil.virtual_memory().percent
        else:
            return None

    def get_memory_total(self):
        """
        @l3331l4
        Returns the total memory installed.
        """
        if psutil.virtual_memory():
            return psutil.virtual_memory().total
        else:
            return None

    def get_memory_available(self):
        """
        @ljdzed
        Return the total memory available
        """
        if psutil.virtual_memory():
            return psutil.virtual_memory().available
        else:
            return None

    def get_memory_used(self):
        """
        @ljdzed
        Returns the total memory used as the difference of get_memory and get_memory_available
        """
        memory_total = self.get_memory_total()
        memory_available = self.get_memory_available()

        if memory_total and memory_available:
            memory_used = memory_total - memory_available
            return memory_used
        
        else:
            return None
        

    def __str__(self) -> str:
        """
        Returns to string representation of all RAM metrics.        
        """
        utilization = self.get_utilization()
        memoryTotal = self.get_memory_total()
        memoryUsed = self.get_memory_used()
        memoryAvailable = self.get_memory_available()
        return f"RAM Utilization: {utilization}%\nTotal Memory: {memoryTotal} bytes\nUsed Memory: {memoryUsed} bytes\nAvailable Memory: {memoryAvailable} bytes"
