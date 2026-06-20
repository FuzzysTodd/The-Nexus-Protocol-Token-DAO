from .simulator_init import *
from .device_init import *
from numba import runtests as runtests
from numba.core import config as config
from numba.cuda.compiler import compile_ptx as compile_ptx, compile_ptx_for_current_device as compile_ptx_for_current_device

def test(*args, **kwargs): ...
