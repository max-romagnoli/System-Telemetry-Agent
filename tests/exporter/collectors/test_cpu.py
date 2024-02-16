# Here are tests about functions from collectors,Add tests if needed.
import psutil
import sys
sys.path.append('/home/runner/work/System-Telemetry-Agent/System-Telemetry-Agent/exporter/collectors/cpu.py')
import CPUCollector

def test_cpu_get_frequency():
    frequency = CPUCollector.get_frequency()
    assert isinstance(frequency, (int, float)) #Tests whether to return a number.
