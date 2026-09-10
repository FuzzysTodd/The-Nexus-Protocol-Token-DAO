import dataclasses
import enum
from torch.utils.benchmark.utils import common
from typing import Any, Callable, Dict, Generator, NamedTuple, Tuple

__all__ = ['FunctionCount', 'FunctionCounts', 'CallgrindStats', 'CopyIfCallgrind']

class FunctionCount(NamedTuple):
    count: int
    function: str

@dataclasses.dataclass(repr=False, eq=False, frozen=True)
class FunctionCounts:
    """Container for manipulating Callgrind results.

    It supports:
        1) Addition and subtraction to combine or diff results.
        2) Tuple-like indexing.
        3) A `denoise` function which strips CPython calls which are known to
           be non-deterministic and quite noisy.
        4) Two higher order methods (`filter` and `transform`) for custom
           manipulation.
    """
    inclusive: bool
    truncate_rows: bool = ...
    def __iter__(self) -> Generator[FunctionCount, None, None]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, item: Any) -> FunctionCount | FunctionCounts: ...
    def __add__(self, other: FunctionCounts) -> FunctionCounts: ...
    def __sub__(self, other: FunctionCounts) -> FunctionCounts: ...
    def __mul__(self, other: int | float) -> FunctionCounts: ...
    def transform(self, map_fn: Callable[[str], str]) -> FunctionCounts:
        """Apply `map_fn` to all of the function names.

        This can be used to regularize function names (e.g. stripping irrelevant
        parts of the file path), coalesce entries by mapping multiple functions
        to the same name (in which case the counts are added together), etc.
        """
    def filter(self, filter_fn: Callable[[str], bool]) -> FunctionCounts:
        """Keep only the elements where `filter_fn` applied to function name returns True."""
    def sum(self) -> int: ...
    def denoise(self) -> FunctionCounts:
        """Remove known noisy instructions.

        Several instructions in the CPython interpreter are rather noisy. These
        instructions involve unicode to dictionary lookups which Python uses to
        map variable names. FunctionCounts is generally a content agnostic
        container, however this is sufficiently important for obtaining
        reliable results to warrant an exception."""
    def __init__(self, _data, inclusive, truncate_rows, _linewidth) -> None: ...

@dataclasses.dataclass(repr=False, eq=False, frozen=True)
class CallgrindStats:
    """Top level container for Callgrind results collected by Timer.

    Manipulation is generally done using the FunctionCounts class, which is
    obtained by calling `CallgrindStats.stats(...)`. Several convenience
    methods are provided as well; the most significant is
    `CallgrindStats.as_standardized()`.
    """
    task_spec: common.TaskSpec
    number_per_run: int
    built_with_debug_symbols: bool
    baseline_inclusive_stats: FunctionCounts
    baseline_exclusive_stats: FunctionCounts
    stmt_inclusive_stats: FunctionCounts
    stmt_exclusive_stats: FunctionCounts
    stmt_callgrind_out: str | None
    def stats(self, inclusive: bool = False) -> FunctionCounts:
        """Returns detailed function counts.

        Conceptually, the FunctionCounts returned can be thought of as a tuple
        of (count, path_and_function_name) tuples.

        `inclusive` matches the semantics of callgrind. If True, the counts
        include instructions executed by children. `inclusive=True` is useful
        for identifying hot spots in code; `inclusive=False` is useful for
        reducing noise when diffing counts from two different runs. (See
        CallgrindStats.delta(...) for more details)
        """
    def counts(self, *, denoise: bool = False) -> int:
        """Returns the total number of instructions executed.

        See `FunctionCounts.denoise()` for an explanation of the `denoise` arg.
        """
    def delta(self, other: CallgrindStats, inclusive: bool = False) -> FunctionCounts:
        '''Diff two sets of counts.

        One common reason to collect instruction counts is to determine the
        the effect that a particular change will have on the number of instructions
        needed to perform some unit of work. If a change increases that number, the
        next logical question is "why". This generally involves looking at what part
        if the code increased in instruction count. This function automates that
        process so that one can easily diff counts on both an inclusive and
        exclusive basis.
        '''
    def as_standardized(self) -> CallgrindStats:
        """Strip library names and some prefixes from function strings.

        When comparing two different sets of instruction counts, on stumbling
        block can be path prefixes. Callgrind includes the full filepath
        when reporting a function (as it should). However, this can cause
        issues when diffing profiles. If a key component such as Python
        or PyTorch was built in separate locations in the two profiles, which
        can result in something resembling::

            23234231 /tmp/first_build_dir/thing.c:foo(...)
             9823794 /tmp/first_build_dir/thing.c:bar(...)
              ...
               53453 .../aten/src/Aten/...:function_that_actually_changed(...)
              ...
             -9823794 /tmp/second_build_dir/thing.c:bar(...)
            -23234231 /tmp/second_build_dir/thing.c:foo(...)

        Stripping prefixes can ameliorate this issue by regularizing the
        strings and causing better cancellation of equivalent call sites
        when diffing.
        """
    def __init__(self, task_spec, number_per_run, built_with_debug_symbols, baseline_inclusive_stats, baseline_exclusive_stats, stmt_inclusive_stats, stmt_exclusive_stats, stmt_callgrind_out) -> None: ...

class Serialization(enum.Enum):
    PICKLE: int
    TORCH: int
    TORCH_JIT: int

class CopyIfCallgrind:
    """Signal that a global may be replaced with a deserialized copy.

    See `GlobalsBridge` for why this matters.
    """
    def __init__(self, value: Any, *, setup: str | None = None) -> None: ...
    @property
    def value(self) -> Any: ...
    @property
    def setup(self) -> str | None: ...
    @property
    def serialization(self) -> Serialization: ...
    @staticmethod
    def unwrap_all(globals: Dict[str, Any]) -> Dict[str, Any]: ...

class GlobalsBridge:
    '''Handle the transfer of (certain) globals when collecting Callgrind statistics.

    Key takeaway: Any globals passed must be wrapped in `CopyIfCallgrind` to
                  work with `Timer.collect_callgrind`.

    Consider the following code snippet:
    ```
        import pickle
        import timeit

        class Counter:
            value = 0

            def __call__(self):
                self.value += 1

        counter = Counter()
        timeit.Timer("counter()", globals={"counter": counter}).timeit(10)
        print(counter.value)  # 10

        timeit.Timer(
            "counter()",
            globals={"counter": pickle.loads(pickle.dumps(counter))}
        ).timeit(20)
        print(counter.value)  # Still 10
    ```

    In the first case, `stmt` is executed using the objects in `globals`;
    however, the addition of serialization and deserialization changes the
    semantics and may meaningfully change behavior.

    This is a practical consideration when collecting Callgrind statistics.
    Unlike `exec` based execution (which `timeit` uses under the hood) which
    can share in-memory data structures with the caller, Callgrind collection
    requires an entirely new process in order to run under Valgrind. This means
    that any data structures used for statement execution will have to be
    serialized and deserialized in the subprocess.

    In order to avoid surprising semantics from (user invisible) process
    boundaries, what can be passed through `globals` is severely restricted
    for `Timer.collect_callgrind`. It is expected that most setup should be
    achievable (albeit perhaps less ergonomically) by passing a `setup`
    string.

    There are, however, exceptions. One such class are TorchScripted functions.
    Because they require a concrete file with source code it is not possible
    to define them using a `setup` string. Another group are torch.nn.Modules,
    whose construction can be complex and prohibitively cumbersome to coerce
    into a `setup` string. Finally, most builtin types are sufficiently well
    behaved and sufficiently common to warrant allowing as well. (e.g.
    `globals={"n": 1}` is very convenient.)

    Fortunately, all have well defined serialization semantics. This class
    is responsible for enabling the Valgrind subprocess to use elements in
    `globals` so long as they are an allowed type.

    Caveats:
        The user is required to acknowledge this serialization by wrapping
        elements in `globals` with `CopyIfCallgrind`.

        While ScriptFunction and ScriptModule are expected to save and load
        quite robustly, it is up to the user to ensure that an nn.Module can
        un-pickle successfully.

        `torch.Tensor` and `np.ndarray` are deliberately excluded. The
        serialization/deserialization process perturbs the representation of a
        tensor in ways that could result in incorrect measurements. For example,
        if a tensor lives in pinned CPU memory, this fact would not be preserved
        by a dump, and that will in turn change the performance of certain CUDA
        operations.
    '''
    def __init__(self, globals: Dict[str, Any], data_dir: str) -> None: ...
    def construct(self) -> str: ...

class _ValgrindWrapper:
    def __init__(self) -> None: ...
    def collect_callgrind(self, task_spec: common.TaskSpec, globals: Dict[str, Any], *, number: int, repeats: int, collect_baseline: bool, is_python: bool, retain_out_file: bool) -> Tuple[CallgrindStats, ...]:
        """Collect stats, and attach a reference run which can be used to filter interpreter overhead."""

# Names in __all__ with no definition:
#   FunctionCount
