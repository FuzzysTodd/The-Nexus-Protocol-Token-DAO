from _typeshed import Incomplete

profiler: Incomplete

def process_id():
    """get the identifier (process id) for the current process"""
def thread_id():
    """get the identifier for the current thread"""

class profiled:
    """decorator for profiling a function (does not call enable profiling)"""
    prefix: Incomplete
    suffix: Incomplete
    sort: Incomplete
    pid: Incomplete
    def __init__(self, gen: Incomplete | None = None, prefix: str = 'id-', suffix: str = '.prof') -> None:
        """y=gen(), with y an indentifier (e.g. current_process().pid)

Important class members:
    prefix\t- string prefix for pstats filename [default: 'id-']
    suffix      - string suffix for pstats filename [default: '.prof']
    pid         - function for obtaining id of current process/thread
    sort        - integer index of column in pstats output for sorting

Example:
    >>> import time
    >>> import random
    >>> import pathos.profile as pr
    >>>
    >>> config = dict(gen=pr.process_id)
    >>> @pr.profiled(**config)
    ... def work(i):
    ...     x = random.random()
    ...     time.sleep(x)
    ...     return (i,x)
    ...
    >>> pr.enable_profiling()
    >>> # profile the work (not the map internals); write to file for pstats
    >>> for i in map(work, range(-10,0)):
    ...     print(i)
    ...

NOTE: If gen is a bool or string, then sort=gen and pid is not used.
      Otherwise, pid=gen and sort is not used. Output can be ordered
      by setting gen to one of the following:
      'calls'      - call count
      'cumulative' - cumulative time
      'cumtime'    - cumulative time
      'file'       - file name
      'filename'   - file name
      'module'     - file name
      'ncalls'     - call count
      'pcalls'     - primitive call count
      'line'       - line number
      'name'       - function name
      'nfl'        - name/file/line
      'stdname'    - standard name
      'time'       - internal time
      'tottime'    - internal time
        """
    def __call__(self, f): ...

def not_profiled(f):
    """decorator to remove profiling (due to 'profiled') from a function"""
def enable_profiling(*args) -> None:
    """initialize a profiler instance in the current thread/process"""
def start_profiling(*args) -> None:
    """begin profiling everything in the current thread/process"""
def stop_profiling(*args) -> None:
    """stop profiling everything in the current thread/process"""
def disable_profiling(*args) -> None:
    """remove the profiler instance from the current thread/process"""
def clear_stats(*args) -> None:
    """clear all stored profiling results from the current thread/process"""
def get_stats(*args):
    """get all stored profiling results for the current thread/process"""
def print_stats(*args, **kwds) -> None:
    """print all stored profiling results for the current thread/process"""
def dump_stats(*args, **kwds) -> None:
    """dump all stored profiling results for the current thread/process

Notes:
    see ``pathos.profile.profiled`` for settings for ``*args`` and ``**kwds``
    """

class profile:
    """decorator for profiling a function (will enable profiling)"""
    config: Incomplete
    pipe: Incomplete
    def __init__(self, sort: Incomplete | None = None, **config) -> None:
        """sort is integer index of column in pstats output for sorting

Important class members:
    pipe        - pipe instance in which profiling is active

Example:
    >>> import time
    >>> import random
    >>> import pathos.profile as pr
    >>>
    ... def work():
    ...     x = random.random()
    ...     time.sleep(x)
    ...     return x
    ...
    >>> # profile the work; print pstats info
    >>> pr.profile()(work)
             4 function calls in 0.136 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.136    0.136 <stdin>:1(work)
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
            1    0.136    0.136    0.136    0.136 {time.sleep}

    0.1350568110491419
    >>>

NOTE: pipe provided should come from pool built with nodes=1. Other
      configuration keywords (config) are passed to 'pr.profiled'.
      Output can be ordered by setting sort to one of the following:
      'calls'      - call count
      'cumulative' - cumulative time
      'cumtime'    - cumulative time
      'file'       - file name
      'filename'   - file name
      'module'     - file name
      'ncalls'     - call count
      'pcalls'     - primitive call count
      'line'       - line number
      'name'       - function name
      'nfl'        - name/file/line
      'stdname'    - standard name
      'time'       - internal time
      'tottime'    - internal time
        """
    def __call__(self, function, *args, **kwds): ...
