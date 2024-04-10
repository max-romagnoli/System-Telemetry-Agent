import re
import unittest
from exporter.collectors.network import NetworkCollector

class TestNetworkCollector(unittest.TestCase):

    def test_get_unit(self):
        """
        @cindyariyo
        Test if bytes are coverted to Mb.
        """
        bytes = 345214
        mb = (bytes * 8) / 1000000
        network_collector = NetworkCollector()
        units = network_collector.get_unit(bytes)
        self.assertEqual(units, mb)

    def test_get_unit_is_not_none(self):
        """
        @dalesv
        Makes sure return is not None
        """
        bytes = 345214
        network_collector = NetworkCollector()
        val = network_collector.get_unit(bytes)
        self.assertFalse(val is None)

    def test_get_traffic_in_is_not_negative(self): 
        """
        @cindyariyo
        test if method returns traffic >= 0
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        self.assertTrue(traffic_in >= 0)

    def test_traffic_in_is_appropriate_size(self):
        """
        @dalesv
        test if method returns traffic is not obscenely high
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        self.assertTrue(traffic_in < 150000000000)
        # 50 Giga Bytes/s is max, as 11.5 GB/s is a NASA computer

    def test_traffic_in_is_not_none(self):
        """
        @dalesv
        Makes sure return is not None
        """
        network_collector = NetworkCollector()
        val = network_collector.get_traffic_in()
        self.assertFalse(val is None)

    def test_get_traffic_out_is_not_negative(self): 
        """ 
        @cindyariyo
        test if method returns traffic >= 0
        """
        network_collector = NetworkCollector()
        traffic_out = network_collector.get_traffic_out()
        self.assertTrue(traffic_out >= 0)

    def test_traffic_out_is_appropriate_size(self):
        """
        @dalesv
        test if method returns traffic is not obscenely high
        """
        network_collector = NetworkCollector()
        traffic_out = network_collector.get_traffic_in()
        self.assertTrue(traffic_out < 150000000000)
        # 50 Giga Bytes/s is max, as 11.5 GB/s is a NASA computer
    
    def test_traffic_out_is_not_none(self):
        """
        @dalesv
        Makes sure return is not None
        """
        network_collector = NetworkCollector()
        val = network_collector.get_traffic_out()
        self.assertFalse(val is None)

    def test_get_traffic_in(self):
        """
        @cindyariyo
        Test if bytes are received and returned in Megabits/s.
        """
        network_collector = NetworkCollector()
        traffic_in = network_collector.get_traffic_in()
        self.assertIsInstance(traffic_in, float)
    
    def test_get_traffic_out(self):
        """
        @cindyariyo
        Test if bytes are sent and returned in Megabits/s.
        """
        network_collector = NetworkCollector()
        traffic_out = network_collector.get_traffic_out()
        self.assertIsInstance(traffic_out, float)

    def test_get_rate_traffic_in(self):
        """
        Test if bytes are sent and returned in Megabits/s.
        """  
        network_collector = NetworkCollector()
        rate_traffic_in = network_collector.get_rate_traffic_in()
        self.assertIsInstance(rate_traffic_in, float)

    def test_get_rate_traffic_out(self):
        """
        Test if bytes are sent and returned in Megabits/s.
        """  
        network_collector = NetworkCollector()
        rate_traffic_out = network_collector.get_rate_traffic_out()
        self.assertIsInstance(rate_traffic_out, float)      

    def test__str__(self):
        """
        @cindyariyo
        Test if a string representation of networking metrics is returned.
        """
        network_collector = NetworkCollector()
        self.assertRegex(network_collector.__str__(), r"Inbound Traffic: \d+(\.\d+) Mb/s, Outbound Traffic: \d+(\.\d+) Mb/s")

    def test_str_is_not_none(self):
        """
        @dalesv
        Makes sure return is not None
        """
        network_collector = NetworkCollector()
        val = network_collector.__str__()
        self.assertFalse(val is None)
        
if __name__ == '__main__':
    unittest.main()
