# Here are tests about functions from collectors,Add tests if needed.
import psutil
from .cpu import get_frequency

def test_cpu_get_frequency():
    assert isinstance(frequency, (int, float)) #Tests whether to return a number.
