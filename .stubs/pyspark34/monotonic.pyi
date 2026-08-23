import ctypes
import time

__all__ = ['monotonic']

monotonic = time.monotonic

class timespec(ctypes.Structure):
    """Time specification, as described in clock_gettime(3)."""
