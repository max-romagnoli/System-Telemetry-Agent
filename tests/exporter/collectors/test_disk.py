import unittest
from exporter.collectors.disk import DiskCollector


class TestDiskCollector(unittest.TestCase):
    
    
    def test_disk_get_utilization(self):
        """
        @dalesv
        Tests if a percentage as a number is returned
        """
        dc = DiskCollector()
        usage = dc.get_utilization()
        self.assertIsInstance(usage, (int, float)) #
        self.assertTrue(0 <= usage <= 0)

    def test_disk_get_total_space(self):
        """
        @dalesv
        Tests if a number is returned.
        """
        dc = DiskCollector()
        usage = dc.get_total_space()
        self.assertIsInstance(usage, (int, float)) #

    def test_disk_get_reads(self):
        """
        @dalesv
        Tests if a number is returned.
        """
        dc = DiskCollector()
        reads = dc.get_reads()
        self.assertIsInstance(reads, (int, float)) #

    def test_disk_get_writes(self):
        """
        @dalesv
        Tests if a number is returned.
        """
        dc = DiskCollector()
        writes = dc.get_writes()
        self.assertIsInstance(writes, (int, float)) #

    def test_disk__str__(self):
        """
        @dalesv
        Tests if a string is returned.
        """
        dc = DiskCollector()
        string = dc.__str__()
        self.assertIsInstance(string, (str)) #

if __name__ == '__main__':
    unittest.main()
