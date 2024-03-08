# Here are tests about functions from collectors,Add tests if needed.
from exporter.collectors.disk import DiskCollector


def test_disk_get_utilization(self):
    """
    Tests if a percentage as a number is returned.
    """
    usage = DiskCollector.get_utilization()
    assert isinstance(usage, (int, float)) #
    assert (0 <= usage <= 0)

def test_disk_get_total_space():
    """
    Tests if a number is returned.
    """
    usage = DiskCollector.get_total_space()
    assert isinstance(usage, (int, float)) #

def test_disk_get_reads():
    """
    Tests if a number is returned.
    """
    reads = DiskCollector.get_reads()
    assert isinstance(reads, (int, float)) #

def test_disk_get_writes():
    """
    Tests if a number is returned.
    """
    writes = DiskCollector.get_writes()
    assert isinstance(writes, (int, float)) #

def test_disk__str__():
    """
    Tests if a string is returned.
    """
    string = DiskCollector.__str__()
    assert isinstance(string, (str)) #