# Here are tests about functions from collectors,Add tests if needed.
from exporter.collectors.cpu import CPUCollector


def test_cpu_get_frequency():
    """
    Tests if a number is returned.
    """
    frequency = CPUCollector.get_frequency()
    assert isinstance(frequency, (int, float)) #
