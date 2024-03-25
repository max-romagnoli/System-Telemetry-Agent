import unittest
from exporter.collectors.cpu import CPUCollector

class TestCPUCollector(unittest.TestCase):

    def test_get_utilization(self):
        """
        @mccooeyc11
        Test whether CPU utilization is within an acceptable range (0-100%)
        """
        cpu_collector = CPUCollector()
        utilization = cpu_collector.get_utilization()
        self.assertIsInstance(utilization, float)
        self.assertTrue(0.0 <= utilization <= 100.0)

    def test_get_freq(self):
        """
        @mccooeyc11
        Test whether CPU frequency is a positive number
        """
        cpu_collector = CPUCollector()
        freq = cpu_collector.get_frequency()
        self.assertIsInstance(freq, float)
        self.assertTrue(freq > 0.0)

    def test_temp(self):
        """
        @mccooeyc11
        Test whether CPU temperature is a reasonable value (20-100 C)
        """
        cpu_collector = CPUCollector()
        temp = cpu_collector.get_temperature()
        if temp:
            self.assertIsInstance(temp, float)
            self.assertTrue(20 <= temp <= 100)
        else:
            self.assertIsNone(temp)

    def test_str(self):
        """
        @mccooeyc11
        Test whether the string representation of CPU metrics is correct
        """
        cpu_collector = CPUCollector()
        output_str = str(cpu_collector)
        self.assertTrue('CPU utilization: ' in output_str)
        self.assertTrue('%\n' in output_str)
        self.assertTrue('CPU frequency: ' in output_str)
        self.assertTrue('MHz\n' in output_str)
        self.assertTrue('CPU temperature: ' in output_str)

    def test_get_utilization_by_core(self): 
        """
        @l3331l4
        Test whether CPU utilization by core is within an acceptable range
        """
        cpu_collector = CPUCollector()
        cpu_percent, core_utilizations = cpu_collector.get_utilization_by_core()
        self.assertTrue(all(0 <= util <= 100 for util in cpu_percent))
        self.assertTrue(all(0 <= util <= 100 for util in core_utilizations))

if __name__ == '__main__':
    unittest.main()

