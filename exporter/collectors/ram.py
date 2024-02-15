import psutil

class RAMCollector:

    def __init__(self) -> None:
        """
        @
        Constructor
        """
        pass

    def get_utilization(self):
        """
        @
        Returns the RAM utilization as a percentage.
        """
        return psutil.virtual_memory().percent

    def get_memory(self):
        """
        @
        Returns the total memory installed.
        """
        return psutil.virtual_memory().total

    def __str__(self) -> str:
        """
        Returns to string representation of all RAM metrics.        
        """
        utilization = self.get_utilization()
        memory = self.get_memory()
        return f"RAM Utilization: {utilization}%\nTotal Memory: {memory} bytes"
