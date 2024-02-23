import psutil

class RAMCollector:

    def __init__(self) -> None:
        """
        @Leila
        Constructor
        """
        pass

    def get_utilization(self):
        """
        @Leila
        Returns the RAM utilization as a percentage.
        """
        return psutil.virtual_memory().percent

    def get_memory(self):
        """
        @Leila
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
