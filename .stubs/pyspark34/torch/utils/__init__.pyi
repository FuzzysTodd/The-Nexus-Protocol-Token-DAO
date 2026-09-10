from ._crash_handler import disable_minidumps as disable_minidumps, enable_minidumps as enable_minidumps, enable_minidumps_on_exceptions as enable_minidumps_on_exceptions
from .backend_registration import rename_privateuse1_backend as rename_privateuse1_backend
from .cpp_backtrace import get_cpp_backtrace as get_cpp_backtrace
from .throughput_benchmark import ThroughputBenchmark as ThroughputBenchmark
from _typeshed import Incomplete

def set_module(obj, mod) -> None: ...

cmake_prefix_path: Incomplete
