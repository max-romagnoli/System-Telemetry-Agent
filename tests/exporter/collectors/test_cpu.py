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
        TODO: @mccooeyc11
        Test whether CPU temperature is a reasonable value (20-100 C)
        """

        

    def test_str(self):
        """
        @mccooeyc11
        Test whether the string representation of CPU metrics is correct
        """
        cpu_collector = CPUCollector()
        utilization = cpu_collector.get_utilization()
        frequency = cpu_collector.get_frequency()
        temp = cpu_collector.get_temperature().__str__()
        expected_output = f"CPU utilization: {utilization}%\n CPU frequency: {frequency}MHz\n CPU temperature: {temp}°C\n"
        self.assertEqual(str(cpu_collector), expected_output)


if __name__ == '__main__':
    unittest.main()

