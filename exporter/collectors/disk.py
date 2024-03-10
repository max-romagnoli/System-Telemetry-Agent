import psutil

class DiskCollector:

    def __init__(self) -> None:
        """
        Constructor
        """
        pass

    def get_utilization(self):
        """
        @dalesv
        Returns the Disk space that is spent as a percentage.
        """
        if not psutil.disk_usage("/"):
            return None
        else:
            return psutil.disk_usage("/").percent

    def get_total_space(self):
        """
        @dalesv
        Returns the Disk total storage in bytes.
        """
        if not psutil.disk_usage("/"):
            return None
        else:
            return psutil.disk_usage("/").total
        
    def get_free_space(self):
        """
        @max-romagnoli
        Returns the computers free available storage in bytes.
        """
        if not psutil.disk_usage("/"):
            return None
        else:
            return psutil.disk_usage("/").free

    def get_reads_bytes(self):
        """
        @dalesv
        If Possible
        Returns the reads on the disk in bytes.        
        """
        if not psutil.disk_io_counters():
            return None
        return psutil.disk_io_counters().read_bytes

    def get_writes_bytes(self):
        """
        @dalesv
        If Possible
        Returns the writes on the disk in bytes.        
        """
        if not psutil.disk_io_counters():
            return None
        return psutil.disk_io_counters().write_bytes
    
    def get_reads_ops(self):
        """
        @max-romagnoli
        If Possible
        Returns the number of read operations on the disk.        
        """
        if not psutil.disk_io_counters():
            return None
        return psutil.disk_io_counters().read_count

    def get_writes_ops(self):
        """
        @max-romagnoli
        If Possible
        Returns the number of write operations on the disk.        
        """
        if not psutil.disk_io_counters():
            return None
        return psutil.disk_io_counters().write_count

    def __str__(self) -> str:
        """
        @max-romagnoli
        Returns to string representation of all disk metrics.        
        """
        return (
            """
            Disk utilization: {usage_perc}%
            Total storage: {total} bytes
            Free storage: {free} bytes
            Byte reads: {read_bytes} bytes
            Byte writes: {write_bytes} bytes
            Read ops: {read_ops} ops
            Write ops: {write_ops} ops
            """
            .format(
               usage_perc = self.get_utilization(),
               total = self.get_total_space(),
               free = self.get_free_space(),
               read_bytes = self.get_reads_bytes(),
               write_bytes = self.get_writes_bytes(),
               read_ops = self.get_reads_ops(),
               write_ops = self.get_writes_ops()
            )
        )