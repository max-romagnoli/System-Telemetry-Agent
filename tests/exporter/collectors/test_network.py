import unittest
from exporter.collectors.network import NetworkCollector

class TestNetworkCollector(unittest.TestCase):

    def test_get_unit(self):
        """
        Test if bytes are coverted to Mb.
        """
        bytes = 345214
        mb = (bytes * 8) / 1000000
        network_collector = NetworkCollector()
        units = network_collector.get_unit(bytes)
        self.assertEqual(units, mb)

    def test_get_traffic_in_is_not_negative(self): 
        """
        test if method returns traffic >= 0
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        self.assertTrue(traffic_in >= 0)

    def test_get_traffic_out_is_not_negative(self): 
        """ 
        test if method returns traffic >= 0
        """
        network_collector = NetworkCollector()
        traffic_out = network_collector.get_traffic_out()
        self.assertTrue(traffic_out >= 0)


    def test_get_traffic_in(self):
        """
        Test if bytes are received and returned in Mb/s.
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        self.assertIsInstance(traffic_in, float)
    
    def test_get_traffic_out(self):
        """
        Test if bytes are sent and returned in Mb/s.
        """
        network_collector = NetworkCollector()
        traffic_out = network_collector.get_traffic_out()
        self.assertIsInstance(traffic_out, float)

    def test__str__(self):
        """
        Test if a string representation of networking metrics is returned.
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        traffic_out = network_collector.get_traffic_out()
        self.assertEqual(network_collector.__str__(), f"Inbound Traffic: {traffic_in} Mb/s, Outbound Traffic: {traffic_out} Mb/s")
        
if __name__ == '__main__':
    unittest.main()
