from _typeshed import Incomplete
from enum import Enum
from torch._C._profiler import _ExperimentalConfig
from torch.autograd import ProfilerActivity
from typing import Any, Callable, Iterable

__all__ = ['supported_activities', 'ProfilerAction', 'schedule', 'tensorboard_trace_handler', 'profile', 'ExecutionGraphObserver']

def supported_activities():
    """
    Returns a set of supported profiler tracing activities.

    Note: profiler uses CUPTI library to trace on-device CUDA kernels.
    In case when CUDA is enabled but CUPTI is not available, passing
    ``ProfilerActivity.CUDA`` to profiler results in using the legacy CUDA
    profiling code (same as in the legacy ``torch.autograd.profiler``).
    This, in turn, results in including CUDA time in the profiler table output,
    but not in the JSON trace.
    """

class _KinetoProfile:
    """Low-level profiler wrap the autograd profile

    Args:
        activities (iterable): list of activity groups (CPU, CUDA) to use in profiling, supported values:
            ``torch.profiler.ProfilerActivity.CPU``, ``torch.profiler.ProfilerActivity.CUDA``.
            Default value: ProfilerActivity.CPU and (when available) ProfilerActivity.CUDA.
        record_shapes (bool): save information about operator's input shapes.
        profile_memory (bool): track tensor memory allocation/deallocation.
        with_stack (bool): record source information (file and line number) for the ops.
        with_flops (bool): use formula to estimate the FLOPS of specific operators
            (matrix multiplication and 2D convolution).
        with_modules (bool): record module hierarchy (including function names)
            corresponding to the callstack of the op. e.g. If module A's forward call's
            module B's forward which contains an aten::add op,
            then aten::add's module hierarchy is A.B
            Note that this support exist, at the moment, only for TorchScript models
            and not eager mode models.

        experimental_config (_ExperimentalConfig) : A set of experimental options
            used by profiler libraries like Kineto. Note, backward compatibility is not guaranteed.

    .. note::
        This API is experimental and subject to change in the future.

        Enabling shape and stack tracing results in additional overhead.
        When record_shapes=True is specified, profiler will temporarily hold references to the tensors;
        that may further prevent certain optimizations that depend on the reference count and introduce
        extra tensor copies.
    """
    activities: Incomplete
    record_shapes: Incomplete
    with_flops: Incomplete
    profile_memory: Incomplete
    with_stack: Incomplete
    with_modules: Incomplete
    experimental_config: Incomplete
    profiler: Incomplete
    def __init__(self, *, activities: Iterable[ProfilerActivity] | None = None, record_shapes: bool = False, profile_memory: bool = False, with_stack: bool = False, with_flops: bool = False, with_modules: bool = False, experimental_config: _ExperimentalConfig | None = None) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def prepare_trace(self) -> None: ...
    def start_trace(self) -> None: ...
    def stop_trace(self) -> None: ...
    def export_chrome_trace(self, path: str):
        """
        Exports the collected trace in Chrome JSON format.
        """
    def export_stacks(self, path: str, metric: str = 'self_cpu_time_total'):
        '''Save stack traces in a file in a format suitable for visualization.

        Args:
            path (str): save stacks file to this location;
            metric (str): metric to use: "self_cpu_time_total" or "self_cuda_time_total"

        .. note::
            Example of using FlameGraph tool:

            - git clone https://github.com/brendangregg/FlameGraph
            - cd FlameGraph
            - ./flamegraph.pl --title "CPU time" --countname "us." profiler.stacks > perf_viz.svg
        '''
    def key_averages(self, group_by_input_shape: bool = False, group_by_stack_n: int = 0):
        """Averages events, grouping them by operator name and (optionally) input shapes and
        stack.

        .. note::
            To use shape/stack functionality make sure to set record_shapes/with_stack
            when creating profiler context manager.
        """
    def events(self):
        """
        Returns the list of unaggregated profiler events,
        to be used in the trace callback or after the profiling is finished
        """
    def add_metadata(self, key: str, value: str):
        """
        Adds a user defined metadata with a string key and a string value
        into the trace file
        """
    def add_metadata_json(self, key: str, value: str):
        """
        Adds a user defined metadata with a string key and a valid json value
        into the trace file
        """

class ProfilerAction(Enum):
    """
    Profiler actions that can be taken at the specified intervals
    """
    NONE: int
    WARMUP: int
    RECORD: int
    RECORD_AND_SAVE: int

def schedule(*, wait: int, warmup: int, active: int, repeat: int = 0, skip_first: int = 0) -> Callable:
    """
    Returns a callable that can be used as profiler ``schedule`` argument. The profiler will skip
    the first ``skip_first`` steps, then wait for ``wait`` steps, then do the warmup for the next ``warmup`` steps,
    then do the active recording for the next ``active`` steps and then repeat the cycle starting with ``wait`` steps.
    The optional number of cycles is specified with the ``repeat`` parameter, the zero value means that
    the cycles will continue until the profiling is finished.
    """
def tensorboard_trace_handler(dir_name: str, worker_name: str | None = None, use_gzip: bool = False):
    """
    Outputs tracing files to directory of ``dir_name``, then that directory can be
    directly delivered to tensorboard as logdir.
    ``worker_name`` should be unique for each worker in distributed scenario,
    it will be set to '[hostname]_[pid]' by default.
    """

class profile(_KinetoProfile):
    '''Profiler context manager.

    Args:
        activities (iterable): list of activity groups (CPU, CUDA) to use in profiling, supported values:
            ``torch.profiler.ProfilerActivity.CPU``, ``torch.profiler.ProfilerActivity.CUDA``.
            Default value: ProfilerActivity.CPU and (when available) ProfilerActivity.CUDA.
        schedule (Callable): callable that takes step (int) as a single parameter and returns
            ``ProfilerAction`` value that specifies the profiler action to perform at each step.
        on_trace_ready (Callable): callable that is called at each step when ``schedule``
            returns ``ProfilerAction.RECORD_AND_SAVE`` during the profiling.
        record_shapes (bool): save information about operator\'s input shapes.
        profile_memory (bool): track tensor memory allocation/deallocation.
        with_stack (bool): record source information (file and line number) for the ops.
        with_flops (bool): use formula to estimate the FLOPs (floating point operations) of specific operators
            (matrix multiplication and 2D convolution).
        with_modules (bool): record module hierarchy (including function names)
            corresponding to the callstack of the op. e.g. If module A\'s forward call\'s
            module B\'s forward which contains an aten::add op,
            then aten::add\'s module hierarchy is A.B
            Note that this support exist, at the moment, only for TorchScript models
            and not eager mode models.
        experimental_config (_ExperimentalConfig) : A set of experimental options
            used for Kineto library features. Note, backward compatibility is not guaranteed.

        use_cuda (bool):
            .. deprecated:: 1.8.1
                use ``activities`` instead.

    .. note::
        Use :func:`~torch.profiler.schedule` to generate the callable schedule.
        Non-default schedules are useful when profiling long training jobs
        and allow the user to obtain multiple traces at the different iterations
        of the training process.
        The default schedule simply records all the events continuously for the
        duration of the context manager.

    .. note::
        Use :func:`~torch.profiler.tensorboard_trace_handler` to generate result files for TensorBoard:

        ``on_trace_ready=torch.profiler.tensorboard_trace_handler(dir_name)``

        After profiling, result files can be found in the specified directory. Use the command:

        ``tensorboard --logdir dir_name``

        to see the results in TensorBoard.
        For more information, see
        `PyTorch Profiler TensorBoard Plugin <https://github.com/pytorch/kineto/tree/master/tb_plugin>`__

    .. note::
        Enabling shape and stack tracing results in additional overhead.
        When record_shapes=True is specified, profiler will temporarily hold references to the tensors;
        that may further prevent certain optimizations that depend on the reference count and introduce
        extra tensor copies.

    Examples:

    .. code-block:: python

        with torch.profiler.profile(
            activities=[
                torch.profiler.ProfilerActivity.CPU,
                torch.profiler.ProfilerActivity.CUDA,
            ]
        ) as p:
            code_to_profile()
        print(p.key_averages().table(
            sort_by="self_cuda_time_total", row_limit=-1))

    Using the profiler\'s ``schedule``, ``on_trace_ready`` and ``step`` functions:

    .. code-block:: python

        # Non-default profiler schedule allows user to turn profiler on and off
        # on different iterations of the training loop;
        # trace_handler is called every time a new trace becomes available
        def trace_handler(prof):
            print(prof.key_averages().table(
                sort_by="self_cuda_time_total", row_limit=-1))
            # prof.export_chrome_trace("/tmp/test_trace_" + str(prof.step_num) + ".json")

        with torch.profiler.profile(
            activities=[
                torch.profiler.ProfilerActivity.CPU,
                torch.profiler.ProfilerActivity.CUDA,
            ],

            # In this example with wait=1, warmup=1, active=2, repeat=1,
            # profiler will skip the first step/iteration,
            # start warming up on the second, record
            # the third and the forth iterations,
            # after which the trace will become available
            # and on_trace_ready (when set) is called;
            # the cycle repeats starting with the next step

            schedule=torch.profiler.schedule(
                wait=1,
                warmup=1,
                active=2,
                repeat=1),
            on_trace_ready=trace_handler
            # on_trace_ready=torch.profiler.tensorboard_trace_handler(\'./log\')
            # used when outputting for tensorboard
            ) as p:
                for iter in range(N):
                    code_iteration_to_profile(iter)
                    # send a signal to the profiler that the next iteration has started
                    p.step()
    '''
    schedule: Incomplete
    record_steps: bool
    on_trace_ready: Incomplete
    step_num: int
    current_action: Incomplete
    step_rec_fn: Incomplete
    action_map: Incomplete
    def __init__(self, *, activities: Iterable[ProfilerActivity] | None = None, schedule: Callable[[int], ProfilerAction] | None = None, on_trace_ready: Callable[..., Any] | None = None, record_shapes: bool = False, profile_memory: bool = False, with_stack: bool = False, with_flops: bool = False, with_modules: bool = False, experimental_config: _ExperimentalConfig | None = None, use_cuda: bool | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def step(self) -> None:
        """
        Signals the profiler that the next profiling step has started.
        """

class ExecutionGraphObserver:
    """Execution Graph Observer

    Each process can have a single ExecutionGraphObserver instance. The observer
    can be added to record function callbacks via calling register_callback()
    explicitly. Without calling unregister_callback(), repeated calls to
    register_callback() will not add additional observers to record function
    callbacks. Once an ExecutionGraphObserver is created, the start() and stop()
    methods control when the event data is recorded.

    Deleting or calling unregister_callback() will remove the observer from the
    record function callbacks, finalize the output file, and will stop
    incurring any overheads.
    """
    def __init__(self) -> None:
        """
        Initializes the default states.
        """
    def __del__(self) -> None:
        """
        Calls unregister_callback() to make sure to finalize outputs.
        """
    def register_callback(self, output_file_path: str):
        """
        Adds EG observer to record function callbacks. The the data will be
        written to output_file_path.
        """
    def unregister_callback(self) -> None:
        """
        Removes EG observer from record function callbacks.
        """
    @property
    def is_registered(self):
        """
        Return if the execution graph observer is registered.
        """
    def start(self) -> None:
        """
        Starts to capture.
        """
    def stop(self) -> None:
        """
        Stops to capture.
        """
    def get_output_file_path(self) -> str:
        """
        Returns the output file name.
        """
