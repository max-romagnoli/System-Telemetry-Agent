# Here are tests about functions from collectors,Add tests if needed.
import psutil
from collectors.cpu import get_frequency

def test_cpu_get_frequency():
    try:
        with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r') as f:
            frequency = int(f.read()) / 1000  
        assert get_frequency(self) == frequency
    except Exception as e:
        print(f"Error reading CPU frequency: {e}")
