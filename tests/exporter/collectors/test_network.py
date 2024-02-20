import unittest
from exporter.collectors.network import NetworkCollector

class TestNetworkCollector(unittest.TestCase):

    def test_get_traffic_in(self):
        """
        Test if bytes are received and returned in Mb/s
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        self.assertIsInstance(traffic_in, float)
    
    def test_get_traffic_out(self):
        """
        Test if bytes are sent and returned in Mb/s
        """
        network_collector = NetworkCollector()
        traffic_out = network_collector.get_traffic_out()
        self.assertIsInstance(traffic_out, float)

    def test__str__(self):
        """
        Test if a string representation of all networking metrics is returned
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        traffic_out = network_collector.get_traffic_out()
        self.assertEqual(network_collector.__str__(), f"Inbound Traffic: {traffic_in} Mb/s, Outbound Traffic: {traffic_out} Mb/s")
        
if __name__ == '__main__':
    unittest.main()
