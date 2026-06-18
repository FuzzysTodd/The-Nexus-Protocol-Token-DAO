from _typeshed import Incomplete
from contextlib import ContextDecorator as _ContextDecorator
from torch.autograd.profiler_util import EventList as EventList, FunctionEvent as FunctionEvent, MemRecordsAcc as MemRecordsAcc
from typing import Any

__all__ = ['profile', 'record_function', 'emit_itt', 'emit_nvtx', 'load_nvprof', 'EnforceUnique', 'parse_nvprof_trace', 'KinetoStepTracker', 'EventList', 'FunctionEvent', 'MemRecordsAcc']

class _ContextDecorator:
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __call__(self, func): ...

class profile:
    '''Context manager that manages autograd profiler state and holds a summary of results.
    Under the hood it just records events of functions being executed in C++ and
    exposes those events to Python. You can wrap any code into it and it will
    only report runtime of PyTorch functions.
    Note: profiler is thread local and is automatically propagated into the async tasks

    Args:
        enabled (bool, optional): Setting this to False makes this context manager a no-op.

        use_cuda (bool, optional): Enables timing of CUDA events as well using the cudaEvent API.
            Adds approximately 4us of overhead to each tensor operation.

        record_shapes (bool, optional): If shapes recording is set, information
            about input dimensions will be collected. This allows one to see which
            dimensions have been used under the hood and further group by them
            using prof.key_averages(group_by_input_shape=True). Please note that
            shape recording might skew your profiling data. It is recommended to
            use separate runs with and without shape recording to validate the timing.
            Most likely the skew will be negligible for bottom most events (in a case
            of nested function calls). But for higher level functions the total
            self cpu time might be artificially increased because of the shape
            collection.

        with_flops (bool, optional): If with_flops is set, the profiler will estimate
            the FLOPs (floating point operations) value using the operator\'s input shape.
            This allows one to estimate the hardware performance. Currently,
            this option only works for the matrix multiplication and 2D convolution operators.

        profile_memory (bool, optional): track tensor memory allocation/deallocation.

        with_stack (bool, optional): record source information (file and line number) for the ops.

        with_modules (bool): record module hierarchy (including function names)
            corresponding to the callstack of the op. e.g. If module A\'s forward call\'s
            module B\'s forward which contains an aten::add op,
            then aten::add\'s module hierarchy is A.B
            Note that this support exist, at the moment, only for TorchScript models
            and not eager mode models.

        use_kineto (bool, optional): experimental, enable profiling with Kineto profiler.

        use_cpu (bool, optional): profile CPU events; setting to ``False`` requires
            ``use_kineto=True`` and can be used to lower the overhead for GPU-only profiling.

        experimental_config (_ExperimentalConfig) : A set of experimental options
            used by profiler libraries like Kineto. Note, backward compatibility is not guaranteed.


    .. warning:
        Enabling memory profiling or source attribution incurs additional profiler
        overhead

    .. warning:
        This context managers should not be called recursively, i.e. no nested
        instances are allowed

    .. warning:
        Due to some CUDA multiprocessing limitations (multiprocessing-cuda-note_),
        one cannot use the profiler with ``use_cuda = True`` to benchmark
        DataLoaders with ``num_workers > 0``. If you wish to benchmark data loading,
        please use ``use_cuda = False`` or ``num_workers = 0``.

    Example:
        >>> # xdoctest: +SKIP
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_AUTOGRAD_PROFILER)
        >>> x = torch.randn((1, 1), requires_grad=True)
        >>> with torch.autograd.profiler.profile() as prof:
        >>>     for _ in range(100):  # any normal python code, really!
        >>>         y = x ** 2
        >>>         y.backward()
        >>> # NOTE: some columns were removed for brevity
        >>> print(prof.key_averages().table(sort_by="self_cpu_time_total"))
        -----------------------------------  ---------------  ---------------  ---------------
        Name                                 Self CPU total   CPU time avg     Number of Calls
        -----------------------------------  ---------------  ---------------  ---------------
        mul                                  32.048ms         32.048ms         200
        pow                                  27.041ms         27.041ms         200
        PowBackward0                         9.727ms          55.483ms         100
        torch::autograd::AccumulateGrad      9.148ms          9.148ms          100
        torch::autograd::GraphRoot           691.816us        691.816us        100
        -----------------------------------  ---------------  ---------------  ---------------

    '''
    enabled: Incomplete
    use_cuda: Incomplete
    function_events: Incomplete
    entered: bool
    record_shapes: Incomplete
    with_flops: Incomplete
    profile_memory: Incomplete
    with_stack: Incomplete
    with_modules: Incomplete
    use_cpu: Incomplete
    experimental_config: Incomplete
    kineto_results: Incomplete
    kineto_activities: Incomplete
    profiler_kind: Incomplete
    def __init__(self, enabled: bool = True, *, use_cuda: bool = False, record_shapes: bool = False, with_flops: bool = False, profile_memory: bool = False, with_stack: bool = False, with_modules: bool = False, use_kineto: bool = False, use_cpu: bool = True, experimental_config: Incomplete | None = None) -> None: ...
    def config(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def table(self, sort_by: Incomplete | None = None, row_limit: int = 100, max_src_column_width: int = 75, max_name_column_width: int = 55, max_shapes_column_width: int = 80, header: Incomplete | None = None, top_level_events_only: bool = False): ...
    def export_chrome_trace(self, path): ...
    def export_stacks(self, path: str, metric: str = 'self_cpu_time_total'): ...
    def key_averages(self, group_by_input_shape: bool = False, group_by_stack_n: int = 0): ...
    def total_average(self): ...
    @property
    def self_cpu_time_total(self):
        """ Returns total time spent on CPU obtained as a sum of
        all self times across all the events.
        """

class record_function(_ContextDecorator):
    '''Context manager/function decorator that adds a label to a block of
    Python code (or function) when running autograd profiler. It is
    useful when tracing the code profile.

    Args:
        name (str): Label assigned to the block of code.
        node_id (int): ID of node, for distributed profiling. Unset in
        non-distributed cases.

    Example:
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_AUTOGRAD_PROFILER)
        >>> x = torch.randn((1, 1), requires_grad=True)
        >>> with torch.autograd.profiler.profile() as prof:
        ...     y = x ** 2
        ...     with torch.autograd.profiler.record_function("label-z"): # label the block
        ...         z = y ** 3
        ...     y.backward()
        ...
        >>> # xdoctest: +IGNORE_WANT
        >>> # NOTE: some columns were removed for brevity
        >>> print(prof.key_averages().table(sort_by="self_cpu_time_total"))
        -----------------------------------  ---------------  ---------------  ---------------
        Name                                 Self CPU total %  CPU time avg     Number of Calls
        -----------------------------------  ---------------  ---------------  ---------------
        pow                                  60.77%           47.470us         3
        mul                                  21.73%           25.465us         2
        PowBackward0                         12.03%           121.891us        1
        torch::autograd::AccumulateGrad      2.70%            6.324us          1
        label-z                              2.13%            12.421us         1
        torch::autograd::GraphRoot           0.64%            1.503us          1
        -----------------------------------  ---------------  ---------------  ---------------
        Self CPU time total: 234.344us
        CUDA time total: 0.000us

    '''
    name: Incomplete
    args: Incomplete
    run_callbacks_on_exit: bool
    record: Incomplete
    def __init__(self, name: str, args: str | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...

class emit_itt:
    '''Context manager that makes every autograd operation emit an ITT range.

    It is useful when running the program under Intel(R) VTune Profiler::

        vtune <--vtune-flags> <regular command here>

    The Instrumentation and Tracing Technology (ITT) API enables your application to generate and
    control the collection of trace data during its execution across different Intel tools.
    This context manager is to annotate Intel(R) VTune Profiling trace. With help of this context manager,
    you will be able to see labled ranges in Intel(R) VTune Profiler GUI.

    .. warning:
        This context manager should not be called recursively, i.e. at most one
        instance should be enabled at any given time.

    Args:
        enabled (bool, optional): Setting ``enabled=False`` makes this context manager a no-op.
            Default: ``True``.
        record_shapes (bool, optional): If ``record_shapes=True``, the itt range wrapping
            each autograd op will append information about the sizes of Tensor arguments received
            by that op, in the following format:
            ``[[arg0.size(0), arg0.size(1), ...], [arg1.size(0), arg1.size(1), ...], ...]``
            Non-tensor arguments will be represented by ``[]``.
            Arguments will be listed in the order they are received by the backend op.
            Please note that this order may not match the order in which those arguments were passed
            on the Python side.  Also note that shape recording may increase the overhead of itt range creation.
            Default: ``False``

    Example:
        >>> # xdoctest: +SKIP("Undefined variables")
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_AUTOGRAD_PROFILER)
        >>> with torch.autograd.profiler.emit_itt():
        ...     model(x)

    '''
    enabled: Incomplete
    entered: bool
    record_shapes: Incomplete
    def __init__(self, enabled: bool = True, record_shapes: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...

class emit_nvtx:
    '''Context manager that makes every autograd operation emit an NVTX range.

    It is useful when running the program under nvprof::

        nvprof --profile-from-start off -o trace_name.prof -- <regular command here>

    Unfortunately, there\'s no way to force nvprof to flush the data it collected
    to disk, so for CUDA profiling one has to use this context manager to annotate
    nvprof traces and wait for the process to exit before inspecting them.
    Then, either NVIDIA Visual Profiler (nvvp) can be used to visualize the timeline, or
    :func:`torch.autograd.profiler.load_nvprof` can load the results for inspection
    e.g. in Python REPL.

    .. warning:
        This context manager should not be called recursively, i.e. at most one
        instance should be enabled at any given time.

    Args:
        enabled (bool, optional): Setting ``enabled=False`` makes this context manager a no-op.
            Default: ``True``.
        record_shapes (bool, optional): If ``record_shapes=True``, the nvtx range wrapping
            each autograd op will append information about the sizes of Tensor arguments received
            by that op, in the following format:
            ``[[arg0.size(0), arg0.size(1), ...], [arg1.size(0), arg1.size(1), ...], ...]``
            Non-tensor arguments will be represented by ``[]``.
            Arguments will be listed in the order they are received by the backend op.
            Please note that this order may not match the order in which those arguments were passed
            on the Python side.  Also note that shape recording may increase the overhead of nvtx range creation.
            Default: ``False``

    Example:
        >>> # xdoctest: +SKIP("undefined variables")
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_AUTOGRAD_PROFILER)
        >>> with torch.cuda.profiler.profile():
        ...     model(x)  # Warmup CUDA memory allocator and profiler
        ...     with torch.autograd.profiler.emit_nvtx():
        ...         model(x)

    **Forward-backward correlation**

    When viewing a profile created using :class:`emit_nvtx` in the Nvidia Visual Profiler,
    correlating each backward-pass op with the corresponding forward-pass op can be difficult.
    To ease this task, :class:`emit_nvtx` appends sequence number information to the ranges it
    generates.

    During the forward pass, each function range is decorated with ``seq=<N>``.  ``seq`` is a running
    counter, incremented each time a new backward Function object is created and stashed for backward.
    Thus, the ``seq=<N>`` annotation associated with each forward function range tells you that
    if a backward Function object is created by this forward function,
    the backward object will receive sequence number N.
    During the backward pass, the top-level range wrapping each C++ backward Function\'s
    ``apply()`` call is decorated with ``stashed seq=<M>``.  ``M`` is the sequence number that
    the backward object was created with.  By comparing ``stashed seq`` numbers in backward with ``seq``
    numbers in forward, you can track down which forward op created each backward Function.

    Any functions executed during the backward pass are also decorated with ``seq=<N>``.  During
    default backward (with ``create_graph=False``) this information is irrelevant, and in fact,
    ``N`` may simply be 0 for all such functions.  Only the top-level ranges associated with
    backward Function objects\' ``apply()`` methods are useful, as a way to correlate these Function
    objects with the earlier forward pass.

    **Double-backward**

    If, on the other hand, a backward pass with ``create_graph=True`` is underway (in other words,
    if you are setting up for a double-backward), each function\'s execution during backward
    is given a nonzero, useful ``seq=<N>``.  Those functions may themselves create Function objects
    to be executed later during double-backward, just as the original functions in the forward pass did.
    The relationship between backward and double-backward is conceptually the same as the relationship
    between forward and backward: The functions still emit current-sequence-number-tagged ranges,
    the Function objects they create still stash those sequence numbers, and during the eventual
    double-backward, the Function objects\' ``apply()`` ranges are still tagged with ``stashed seq``
    numbers, which can be compared to `seq` numbers from the backward pass.

    .. warning:
        The sequence number is thread-local, and some forward functions don\'t create an associated
        backward Function object (instead delegating that to sub-functions further down the call chain).
        For these reasons, the correspondence of stashed sequence numbers in
        backward Function ``apply()`` ranges with `seq` numbers in forward-pass ranges is
        not guaranteed to be 1 to 1.  The sequence numbers alone may not be enough to fully
        disambiguate which forward function created which
        backward Function object.  You may need to make a judgment based on analytic knowledge of what
        the expected correspondence should be.
    '''
    enabled: Incomplete
    entered: bool
    record_shapes: Incomplete
    def __init__(self, enabled: bool = True, record_shapes: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...

def load_nvprof(path):
    """Opens an nvprof trace file and parses autograd annotations.

    Args:
        path (str): path to nvprof trace
    """

class EnforceUnique:
    """Raises an error if a key is seen more than once."""
    seen: Incomplete
    def __init__(self) -> None: ...
    def see(self, *key) -> None: ...

def parse_nvprof_trace(path): ...

class KinetoStepTracker:
    '''Provides an abstraction for incrementing the step count globally.
    Previously, we only had one place to mark that a step() has occurred
    in the program via pytorch profiler step(). We will now add step hooks
    in the Optimizer class https://github.com/pytorch/pytorch/issues/88446

    - This could mean programs that already call profiler.step() every
      iteration can end up double incrementing step count.
    - If a model uses multiple optimizers we can also have double or more
      counting of the step.

    We fix this by adding a layer of abstraction before calling step()
    to the kineto library. The idea is to maintain steps per requester in a dict:
    ```
    {
       "ProfilerStep": 100,  # triggered by profiler step() call
       "Optimizer1Step": 100,   # Optimizer 1 or 2 are just examples, could be SGD, Adam etc
       "Optimizer2Step": 100,
    }
    ```
    To figure out the global step count just take the max of dict values (100).

    If one of the count increments the max will go up.
    ```
    {
       "ProfilerStep": 100,
       "Optimizer1Step": 101,   # Optimizer1 got incremented first say
       "Optimizer2Step": 100,
    }
    ```
    Then global step count is 101
    We only call the kineto step() function when global count increments.

    NOTE: Please do not use the KinetoStepTracker in modules beside the Optimizer
    for now. The result could be incorrect increments of the step count.
    '''
    @classmethod
    def init_step_count(cls, requester: str): ...
    @classmethod
    def erase_step_count(cls, requester: str) -> bool: ...
    @classmethod
    def increment_step(cls, requester: str) -> int:
        """Increments the step count for the requester.
        Additionally if the max over all step counts has incremented then
        trigger the _kineto_step()
        returns global step count
        """
    @classmethod
    def current_step(cls) -> int: ...
