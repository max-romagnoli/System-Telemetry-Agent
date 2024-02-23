import unittest
from exporter.collectors.ram import RAMCollector

class TestRAMCollector(unittest.TestCase):

    def test_get_utilization(self):
        """
        @Leila
        Test whether RAM utilization is within the range (0-100%)
        """
        ram_collector = RAMCollector()
        utilization = ram_collector.get_utilization()
        self.assertIsInstance(utilization, float)
        self.assertTrue(0.0 <= utilization <= 100.0)

    def test_get_memory(self):
        """
        @Leila
        Test whether the total memory installed is a positive number
        """
        ram_collector = RAMCollector()
        memory = ram_collector.get_memory()
        self.assertIsInstance(memory, int)
        self.assertTrue(memory > 0)

    def test_str(self):
        """
        @Leila
        Test whether the string representation of RAM metrics is correct
        """
        ram_collector = RAMCollector()
        utilization = ram_collector.get_utilization()
        memory = ram_collector.get_memory()
        expected_output = f"RAM Utilization: {utilization}%\nTotal Memory: {memory} bytes"
        self.assertEqual(str(ram_collector), expected_output)


if __name__ == '__main__':
    unittest.main()
