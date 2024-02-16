# Here are tests about functions from collectors,Add tests if needed.
import psutil
from ... import CPUCollector

def test_cpu_get_frequency():
    frequency = CPUCollector.get_frequency()
    assert isinstance(frequency, (int, float)) #Tests whether to return a number.
