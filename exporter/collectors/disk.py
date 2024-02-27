import psutil

class DiskCollector:

    def __init__(self) -> None:
        """
        TODO: @
        Constructor
        """
        pass

    def get_utilization(self):
        """
        TODO: @
        Returns the Disk space that is spent as a percentage.
        """
        return psutil.disk_usage()

    def get_total_space(self):
        """
        TODO: @
        Returns the computers total available storage.
        """
        return psutil.disk_usage()

    def get_reads(self):
        """
        TODO: @
        If Possible
        Returns the reads on the disk.        
        """
        return psutil.disk_io_counters().read_bytes

    def get_writes(self):
        """
        TODO: @
        If Possible
        Returns the writes on the disk.        
        """
        return psutil.disk_io_counters().write_bytes

    def __str__(self) -> str:
        """
        TODO:
        Returns to string representation of all disk metrics.        
        """
        #inspired by leila's function for the cpu
        utilization = self.get_utilization()
        disk = self.get_total_space()
        return f"Disk Utilization: {utilization}%nAvailable storage: {disk}"
