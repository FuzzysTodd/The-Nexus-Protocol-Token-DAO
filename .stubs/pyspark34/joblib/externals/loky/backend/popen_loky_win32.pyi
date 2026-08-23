from _typeshed import Incomplete
from multiprocessing.popen_spawn_win32 import Popen as _Popen

__all__ = ['Popen']

class Popen(_Popen):
    """
    Start a subprocess to run the code of a process object.

    We differ from cpython implementation with the way we handle environment
    variables, in order to be able to modify then in the child processes before
    importing any library, in order to control the number of threads in C-level
    threadpools.

    We also use the loky preparation data, in particular to handle main_module
    inits and the loky resource tracker.
    """
    method: str
    pid: Incomplete
    returncode: Incomplete
    sentinel: Incomplete
    finalizer: Incomplete
    def __init__(self, process_obj) -> None: ...
