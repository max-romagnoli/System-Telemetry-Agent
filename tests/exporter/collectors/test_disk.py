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
        self.assertIsInstance(usage, (int, float))
        self.assertTrue(0 <= usage <= 0)

    def test_disk_get_total_space(self):
        """
        @dalesv
        Tests if a number is returned.
        """
        dc = DiskCollector()
        total = dc.get_total_space()
        self.assertIsInstance(total, (int, float))

    def test_disk_get_free_space(self):
        """
        @max-romagnoli
        Tests if a number is returned.
        """
        dc = DiskCollector()
        free = dc.get_free_space()
        self.assertIsInstance(free, (int, float))

    def test_disk_get_reads_bytes(self):
        """
        @dalesv
        Tests if a number is returned.
        """
        dc = DiskCollector()
        reads = dc.get_reads_bytes()
        self.assertIsInstance(reads, (int, float))

    def test_disk_get_reads_ops_is_integer(self):
        """
        @max-romagnoli
        Tests if an integer is returned.
        """
        dc = DiskCollector()
        read_ops = dc.get_reads_ops()
        self.assertIsInstance(read_ops, int)

    def test_disk_get_writes_bytes(self):
        """
        @dalesv
        Tests if a number is returned.
        """
        dc = DiskCollector()
        writes = dc.get_writes_bytes()
        self.assertIsInstance(writes, (int, float))

    def test_disk_get_writes_ops_is_integer(self):
        """
        @max-romagnoli
        Tests if an integer is returned.
        """
        dc = DiskCollector()
        write_ops = dc.get_writes_ops()
        self.assertIsInstance(write_ops, int)

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
