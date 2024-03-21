import re
import unittest
from exporter.collectors.ram import RAMCollector

class TestRAMCollector(unittest.TestCase):

    def test_get_utilization(self):
        """
        @l3331l4
        Test whether RAM utilization is within the range (0-100%)
        """
        ram_collector = RAMCollector()
        utilization = ram_collector.get_utilization()
        self.assertIsInstance(utilization, float)
        self.assertTrue(0.0 <= utilization <= 100.0)

    def test_get_memory(self):
        """
        @l3331l4
        Test whether the total memory installed is a positive number
        """
        ram_collector = RAMCollector()
        memory = ram_collector.get_memory()
        self.assertIsInstance(memory, int)
        self.assertTrue(memory > 0)

    def test_get_available_memory(self):
        """
        @ljdzed
        Test whether the total memory available is a positive number
        """
        ram_collector = RAMCollector()
        memory = ram_collector.get_memory_available()
        self.assertIsInstance(memory, int)
        self.assertTrue(memory >= 0)

    def test_get_used_memory(self):
        """
        @ljdzed
        Test whether the total memory used is a positive number
        """
        ram_collector = RAMCollector()
        memory = ram_collector.get_memory_used()
        self.assertIsInstance(memory, int)
        self.assertTrue(memory >= 0)

 
    def test_str(self):
        """
        @l3331l4 
        @ljdzed
        Test whether the string representation of RAM metrics is correct
        """
        ram_collector = RAMCollector()
        
        
        expected_pattern = r"^RAM Utilization: \d+(\.\d+)?%\nTotal Memory: \d+ bytes\nUsed Memory: \d+ bytes\nAvailable Memory: \d+ bytes$"
        
        
        self.assertRegex(str(ram_collector), expected_pattern, 'ram_collector output does not match the expected format.')


if __name__ == '__main__':
    unittest.main()
