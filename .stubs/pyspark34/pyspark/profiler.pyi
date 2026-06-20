import pstats
from _typeshed import Incomplete
from memory_profiler import CodeMap, LineProfiler
from pyspark.accumulators import AccumulatorParam as AccumulatorParam
from pyspark.context import SparkContext as SparkContext
from typing import Any, Callable, Dict, List, Tuple, Type

has_memory_profiler: bool
MemoryTuple = Tuple[float, float, int]
LineProfile = Tuple[int, MemoryTuple | None]
CodeMapDict = Dict[str, List[LineProfile]]

class ProfilerCollector:
    """
    This class keeps track of different profilers on a per
    stage/UDF basis. Also this is used to create new profilers for
    the different stages/UDFs.
    """
    profiler_cls: Incomplete
    udf_profiler_cls: Incomplete
    memory_profiler_cls: Incomplete
    profile_dump_path: Incomplete
    profilers: Incomplete
    def __init__(self, profiler_cls: Type['Profiler'], udf_profiler_cls: Type['Profiler'], memory_profiler_cls: Type['Profiler'], dump_path: str | None = None) -> None: ...
    def new_profiler(self, ctx: SparkContext) -> Profiler:
        """Create a new profiler using class `profiler_cls`"""
    def new_udf_profiler(self, ctx: SparkContext) -> Profiler:
        """Create a new profiler using class `udf_profiler_cls`"""
    def new_memory_profiler(self, ctx: SparkContext) -> Profiler:
        """Create a new profiler using class `memory_profiler_cls`"""
    def add_profiler(self, id: int, profiler: Profiler) -> None:
        """Add a profiler for RDD/UDF `id`"""
    def dump_profiles(self, path: str) -> None:
        """Dump the profile stats into directory `path`"""
    def show_profiles(self) -> None:
        """Print the profile stats to stdout"""

class Profiler:
    '''
    PySpark supports custom profilers, this is to allow for different profilers to
    be used as well as outputting to different formats than what is provided in the
    BasicProfiler.

    A custom profiler has to define or inherit the following methods:
        profile - will produce a system profile of some sort.
        stats - return the collected stats.
        dump - dumps the profiles to a path
        add - adds a profile to the existing accumulated profile

    The profiler class is chosen when creating a SparkContext

    Examples
    --------
    >>> from pyspark import SparkConf, SparkContext
    >>> from pyspark import BasicProfiler
    >>> class MyCustomProfiler(BasicProfiler):
    ...     def show(self, id):
    ...         print("My custom profiles for RDD:%s" % id)
    ...
    >>> conf = SparkConf().set("spark.python.profile", "true")
    >>> sc = SparkContext(\'local\', \'test\', conf=conf, profiler_cls=MyCustomProfiler)
    >>> sc.parallelize(range(1000)).map(lambda x: 2 * x).take(10)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> sc.parallelize(range(1000)).count()
    1000
    >>> sc.show_profiles()
    My custom profiles for RDD:1
    My custom profiles for RDD:3
    >>> sc.stop()

    Notes
    -----
    This API is a developer API.
    '''
    def __init__(self, ctx: SparkContext) -> None: ...
    def profile(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Do profiling on the function `func`"""
    def stats(self) -> pstats.Stats | Dict:
        """Return the collected profiling stats"""
    def show(self, id: int) -> None:
        """Print the profile stats to stdout"""
    def dump(self, id: int, path: str) -> None:
        """Dump the profile into path"""

class CodeMapForUDF(CodeMap):
    def add(self, code: Any, toplevel_code: Any | None = None, *, sub_lines: List | None = None, start_line: int | None = None) -> None: ...

class UDFLineProfiler(LineProfiler):
    code_map: Incomplete
    enable_count: int
    max_mem: Incomplete
    prevlines: Incomplete
    backend: Incomplete
    prev_lineno: Incomplete
    def __init__(self, **kw: Any) -> None: ...
    def __call__(self, func: Callable[..., Any] | None = None, precision: int = 1, *, sub_lines: List | None = None, start_line: int | None = None) -> Callable[..., Any]: ...
    def add_function(self, func: Callable[..., Any], *, sub_lines: List | None = None, start_line: int | None = None) -> None:
        """Record line profiling information for the given Python function."""

class PStatsParam(AccumulatorParam[pstats.Stats | None]):
    """PStatsParam is used to merge pstats.Stats"""
    @staticmethod
    def zero(value: pstats.Stats | None) -> None: ...
    @staticmethod
    def addInPlace(value1: pstats.Stats | None, value2: pstats.Stats | None) -> pstats.Stats | None: ...

class MemUsageParam(AccumulatorParam[CodeMapDict | None]):
    """MemUsageParam is used to merge memory usage code map"""
    @staticmethod
    def zero(value: CodeMapDict | None) -> None: ...
    @staticmethod
    def addInPlace(value1: CodeMapDict | None, value2: CodeMapDict | None) -> CodeMapDict | None: ...

class BasicProfiler(Profiler):
    """
    BasicProfiler is the default profiler, which is implemented based on
    cProfile and Accumulator
    """
    def __init__(self, ctx: SparkContext) -> None: ...
    def profile(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Runs and profiles the method to_profile passed in. A profile object is returned."""
    def stats(self) -> pstats.Stats: ...
    def show(self, id: int) -> None:
        """Print the profile stats to stdout, id is the RDD id"""
    def dump(self, id: int, path: str) -> None:
        """Dump the profile into path, id is the RDD id"""

class UDFBasicProfiler(BasicProfiler):
    """
    UDFBasicProfiler is the profiler for Python/Pandas UDFs.
    """
    def show(self, id: int) -> None:
        """Print the profile stats to stdout, id is the PythonUDF id"""
    def dump(self, id: int, path: str) -> None:
        """Dump the profile into path, id is the PythonUDF id"""

class MemoryProfiler(Profiler):
    """
    MemoryProfiler, which is implemented based on memory profiler and Accumulator
    """
    def __init__(self, ctx: SparkContext) -> None: ...
    def profile(self, sub_lines: List | None, start_line: int | None, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Runs and profiles the method func passed in. A profile object is returned."""
    def stats(self) -> CodeMapDict:
        """Return the collected memory profiles"""
    def show(self, id: int) -> None:
        """Print the profile stats to stdout, id is the PythonUDF id"""
    def dump(self, id: int, path: str) -> None:
        """Dump the memory profile into path, id is the PythonUDF id"""
