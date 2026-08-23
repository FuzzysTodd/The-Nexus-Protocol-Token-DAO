from ._multiprocessing_helpers import mp as mp
from ._parallel_backends import AutoBatchingMixin as AutoBatchingMixin, FallbackToBackend as FallbackToBackend, LokyBackend as LokyBackend, MultiprocessingBackend as MultiprocessingBackend, ParallelBackendBase as ParallelBackendBase, SequentialBackend as SequentialBackend, ThreadingBackend as ThreadingBackend
from ._utils import eval_expr as eval_expr
from .disk import memstr_to_bytes as memstr_to_bytes
from .externals import loky as loky
from .logger import Logger as Logger, short_format_time as short_format_time
from _typeshed import Incomplete

IS_PYPY: Incomplete
BACKENDS: Incomplete
DEFAULT_BACKEND: str
MAYBE_AVAILABLE_BACKENDS: Incomplete
DEFAULT_THREAD_BACKEND: str
EXTERNAL_BACKENDS: Incomplete
default_parallel_config: Incomplete
VALID_BACKEND_HINTS: Incomplete
VALID_BACKEND_CONSTRAINTS: Incomplete

def get_active_backend(prefer=..., require=..., verbose=...):
    """Return the active default backend"""

class parallel_config:
    '''Set the default backend or configuration for :class:`~joblib.Parallel`.

    This is an alternative to directly passing keyword arguments to the
    :class:`~joblib.Parallel` class constructor. It is particularly useful when
    calling into library code that uses joblib internally but does not expose
    the various parallel configuration arguments in its own API.

    Parameters
    ----------
    backend : str or ParallelBackendBase instance, default=None
        If ``backend`` is a string it must match a previously registered
        implementation using the :func:`~register_parallel_backend` function.

        By default the following backends are available:

        - \'loky\': single-host, process-based parallelism (used by default),
        - \'threading\': single-host, thread-based parallelism,
        - \'multiprocessing\': legacy single-host, process-based parallelism.

        \'loky\' is recommended to run functions that manipulate Python objects.
        \'threading\' is a low-overhead alternative that is most efficient for
        functions that release the Global Interpreter Lock: e.g. I/O-bound
        code or CPU-bound code in a few calls to native code that explicitly
        releases the GIL. Note that on some rare systems (such as pyodide),
        multiprocessing and loky may not be available, in which case joblib
        defaults to threading.

        In addition, if the ``dask`` and ``distributed`` Python packages are
        installed, it is possible to use the \'dask\' backend for better
        scheduling of nested parallel calls without over-subscription and
        potentially distribute parallel calls over a networked cluster of
        several hosts.

        It is also possible to use the distributed \'ray\' backend for
        distributing the workload to a cluster of nodes. See more details
        in the Examples section below.

        Alternatively the backend can be passed directly as an instance.

    n_jobs : int, default=None
        The maximum number of concurrently running jobs, such as the number
        of Python worker processes when ``backend="loky"`` or the size of the
        thread-pool when ``backend="threading"``.
        If -1 all CPUs are used. If 1 is given, no parallel computing code
        is used at all, which is useful for debugging. For ``n_jobs`` below -1,
        (n_cpus + 1 + n_jobs) are used. Thus for ``n_jobs=-2``, all
        CPUs but one are used.
        ``None`` is a marker for \'unset\' that will be interpreted as
        ``n_jobs=1`` in most backends.

    verbose : int, default=0
        The verbosity level: if non zero, progress messages are
        printed. Above 50, the output is sent to stdout.
        The frequency of the messages increases with the verbosity level.
        If it more than 10, all iterations are reported.

    temp_folder : str, default=None
        Folder to be used by the pool for memmapping large arrays
        for sharing memory with worker processes. If None, this will try in
        order:

        - a folder pointed by the ``JOBLIB_TEMP_FOLDER`` environment
          variable,
        - ``/dev/shm`` if the folder exists and is writable: this is a
          RAM disk filesystem available by default on modern Linux
          distributions,
        - the default system temporary folder that can be
          overridden with ``TMP``, ``TMPDIR`` or ``TEMP`` environment
          variables, typically ``/tmp`` under Unix operating systems.

    max_nbytes int, str, or None, optional, default=\'1M\'
        Threshold on the size of arrays passed to the workers that
        triggers automated memory mapping in temp_folder. Can be an int
        in Bytes, or a human-readable string, e.g., \'1M\' for 1 megabyte.
        Use None to disable memmapping of large arrays.

    mmap_mode: {None, \'r+\', \'r\', \'w+\', \'c\'}, default=\'r\'
        Memmapping mode for numpy arrays passed to workers. None will
        disable memmapping, other modes defined in the numpy.memmap doc:
        https://numpy.org/doc/stable/reference/generated/numpy.memmap.html
        Also, see \'max_nbytes\' parameter documentation for more details.

    prefer: str in {\'processes\', \'threads\'} or None, default=None
        Soft hint to choose the default backend.
        The default process-based backend is \'loky\' and the default
        thread-based backend is \'threading\'. Ignored if the ``backend``
        parameter is specified.

    require: \'sharedmem\' or None, default=None
        Hard constraint to select the backend. If set to \'sharedmem\',
        the selected backend will be single-host and thread-based.

    inner_max_num_threads : int, default=None
        If not None, overwrites the limit set on the number of threads
        usable in some third-party library threadpools like OpenBLAS,
        MKL or OpenMP. This is only used with the ``loky`` backend.

    backend_params : dict
        Additional parameters to pass to the backend constructor when
        backend is a string.

    Notes
    -----
    Joblib tries to limit the oversubscription by limiting the number of
    threads usable in some third-party library threadpools like OpenBLAS, MKL
    or OpenMP. The default limit in each worker is set to
    ``max(cpu_count() // effective_n_jobs, 1)`` but this limit can be
    overwritten with the ``inner_max_num_threads`` argument which will be used
    to set this limit in the child processes.

    .. versionadded:: 1.3

    Examples
    --------
    >>> from operator import neg
    >>> with parallel_config(backend=\'threading\'):
    ...     print(Parallel()(delayed(neg)(i + 1) for i in range(5)))
    ...
    [-1, -2, -3, -4, -5]

    To use the \'ray\' joblib backend add the following lines:

    >>> from ray.util.joblib import register_ray  # doctest: +SKIP
    >>> register_ray()  # doctest: +SKIP
    >>> with parallel_config(backend="ray"):  # doctest: +SKIP
    ...     print(Parallel()(delayed(neg)(i + 1) for i in range(5)))
    [-1, -2, -3, -4, -5]

    '''
    old_parallel_config: Incomplete
    parallel_config: Incomplete
    def __init__(self, backend=..., *, n_jobs=..., verbose=..., temp_folder=..., max_nbytes=..., mmap_mode=..., prefer=..., require=..., inner_max_num_threads: Incomplete | None = None, **backend_params) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def unregister(self) -> None: ...

class parallel_backend(parallel_config):
    '''Change the default backend used by Parallel inside a with block.

    .. warning::
        It is advised to use the :class:`~joblib.parallel_config` context
        manager instead, which allows more fine-grained control over the
        backend configuration.

    If ``backend`` is a string it must match a previously registered
    implementation using the :func:`~register_parallel_backend` function.

    By default the following backends are available:

    - \'loky\': single-host, process-based parallelism (used by default),
    - \'threading\': single-host, thread-based parallelism,
    - \'multiprocessing\': legacy single-host, process-based parallelism.

    \'loky\' is recommended to run functions that manipulate Python objects.
    \'threading\' is a low-overhead alternative that is most efficient for
    functions that release the Global Interpreter Lock: e.g. I/O-bound code or
    CPU-bound code in a few calls to native code that explicitly releases the
    GIL. Note that on some rare systems (such as Pyodide),
    multiprocessing and loky may not be available, in which case joblib
    defaults to threading.

    You can also use the `Dask <https://docs.dask.org/en/stable/>`_ joblib
    backend to distribute work across machines. This works well with
    scikit-learn estimators with the ``n_jobs`` parameter, for example::

    >>> import joblib  # doctest: +SKIP
    >>> from sklearn.model_selection import GridSearchCV  # doctest: +SKIP
    >>> from dask.distributed import Client, LocalCluster # doctest: +SKIP

    >>> # create a local Dask cluster
    >>> cluster = LocalCluster()  # doctest: +SKIP
    >>> client = Client(cluster)  # doctest: +SKIP
    >>> grid_search = GridSearchCV(estimator, param_grid, n_jobs=-1)
    ... # doctest: +SKIP
    >>> with joblib.parallel_backend("dask", scatter=[X, y]):  # doctest: +SKIP
    ...     grid_search.fit(X, y)

    It is also possible to use the distributed \'ray\' backend for distributing
    the workload to a cluster of nodes. To use the \'ray\' joblib backend add
    the following lines::

     >>> from ray.util.joblib import register_ray  # doctest: +SKIP
     >>> register_ray()  # doctest: +SKIP
     >>> with parallel_backend("ray"):  # doctest: +SKIP
     ...     print(Parallel()(delayed(neg)(i + 1) for i in range(5)))
     [-1, -2, -3, -4, -5]

    Alternatively the backend can be passed directly as an instance.

    By default all available workers will be used (``n_jobs=-1``) unless the
    caller passes an explicit value for the ``n_jobs`` parameter.

    This is an alternative to passing a ``backend=\'backend_name\'`` argument to
    the :class:`~Parallel` class constructor. It is particularly useful when
    calling into library code that uses joblib internally but does not expose
    the backend argument in its own API.

    >>> from operator import neg
    >>> with parallel_backend(\'threading\'):
    ...     print(Parallel()(delayed(neg)(i + 1) for i in range(5)))
    ...
    [-1, -2, -3, -4, -5]

    Joblib also tries to limit the oversubscription by limiting the number of
    threads usable in some third-party library threadpools like OpenBLAS, MKL
    or OpenMP. The default limit in each worker is set to
    ``max(cpu_count() // effective_n_jobs, 1)`` but this limit can be
    overwritten with the ``inner_max_num_threads`` argument which will be used
    to set this limit in the child processes.

    .. versionadded:: 0.10

    See Also
    --------
    joblib.parallel_config : context manager to change the backend
        configuration.
    '''
    old_backend_and_jobs: Incomplete
    new_backend_and_jobs: Incomplete
    def __init__(self, backend, n_jobs: int = -1, inner_max_num_threads: Incomplete | None = None, **backend_params) -> None: ...
    def __enter__(self): ...

DEFAULT_MP_CONTEXT: Incomplete
method: Incomplete

class BatchedCalls:
    """Wrap a sequence of (func, args, kwargs) tuples as a single callable"""
    items: Incomplete
    def __init__(self, iterator_slice, backend_and_jobs, reducer_callback: Incomplete | None = None, pickle_cache: Incomplete | None = None) -> None: ...
    def __call__(self): ...
    def __reduce__(self): ...
    def __len__(self) -> int: ...

TASK_DONE: str
TASK_ERROR: str
TASK_PENDING: str

def cpu_count(only_physical_cores: bool = False):
    """Return the number of CPUs.

    This delegates to loky.cpu_count that takes into account additional
    constraints such as Linux CFS scheduler quotas (typically set by container
    runtimes such as docker) and CPU affinity (for instance using the taskset
    command on Linux).

    If only_physical_cores is True, do not take hyperthreading / SMT logical
    cores into account.
    """
def delayed(function):
    """Decorator used to capture the arguments of a function."""

class BatchCompletionCallBack:
    """Callback to keep track of completed results and schedule the next tasks.

    This callable is executed by the parent process whenever a worker process
    has completed a batch of tasks.

    It is used for progress reporting, to update estimate of the batch
    processing duration and to schedule the next batch of tasks to be
    processed.

    It is assumed that this callback will always be triggered by the backend
    right after the end of a task, in case of success as well as in case of
    failure.
    """
    dispatch_timestamp: Incomplete
    batch_size: Incomplete
    parallel: Incomplete
    parallel_call_id: Incomplete
    job: Incomplete
    status: Incomplete
    def __init__(self, dispatch_timestamp, batch_size, parallel) -> None: ...
    def register_job(self, job) -> None:
        """Register the object returned by `apply_async`."""
    def get_result(self, timeout):
        """Returns the raw result of the task that was submitted.

        If the task raised an exception rather than returning, this same
        exception will be raised instead.

        If the backend supports the retrieval callback, it is assumed that this
        method is only called after the result has been registered. It is
        ensured by checking that `self.status(timeout)` does not return
        TASK_PENDING. In this case, `get_result` directly returns the
        registered result (or raise the registered exception).

        For other backends, there are no such assumptions, but `get_result`
        still needs to synchronously retrieve the result before it can
        return it or raise. It will block at most `self.timeout` seconds
        waiting for retrieval to complete, after that it raises a TimeoutError.
        """
    def get_status(self, timeout):
        """Get the status of the task.

        This function also checks if the timeout has been reached and register
        the TimeoutError outcome when it is the case.
        """
    def __call__(self, out) -> None:
        """Function called by the callback thread after a job is completed."""

def register_parallel_backend(name, factory, make_default: bool = False) -> None:
    """Register a new Parallel backend factory.

    The new backend can then be selected by passing its name as the backend
    argument to the :class:`~Parallel` class. Moreover, the default backend can
    be overwritten globally by setting make_default=True.

    The factory can be any callable that takes no argument and return an
    instance of ``ParallelBackendBase``.

    Warning: this function is experimental and subject to change in a future
    version of joblib.

    .. versionadded:: 0.10
    """
def effective_n_jobs(n_jobs: int = -1):
    """Determine the number of jobs that can actually run in parallel

    n_jobs is the number of workers requested by the callers. Passing n_jobs=-1
    means requesting all available workers for instance matching the number of
    CPU cores on the worker host(s).

    This method should return a guesstimate of the number of workers that can
    actually perform work concurrently with the currently enabled default
    backend. The primary use case is to make it possible for the caller to know
    in how many chunks to slice the work.

    In general working on larger data chunks is more efficient (less scheduling
    overhead and better use of CPU cache prefetching heuristics) as long as all
    the workers have enough work to do.

    Warning: this function is experimental and subject to change in a future
    version of joblib.

    .. versionadded:: 0.10
    """

class Parallel(Logger):
    ''' Helper class for readable parallel mapping.

        Read more in the :ref:`User Guide <parallel>`.

        Parameters
        ----------
        n_jobs: int, default: None
            The maximum number of concurrently running jobs, such as the number
            of Python worker processes when backend="multiprocessing"
            or the size of the thread-pool when backend="threading".
            If -1 all CPUs are used.
            If 1 is given, no parallel computing code is used at all, and the
            behavior amounts to a simple python `for` loop. This mode is not
            compatible with `timeout`.
            For n_jobs below -1, (n_cpus + 1 + n_jobs) are used. Thus for
            n_jobs = -2, all CPUs but one are used.
            None is a marker for \'unset\' that will be interpreted as n_jobs=1
            unless the call is performed under a :func:`~parallel_config`
            context manager that sets another value for ``n_jobs``.
        backend: str, ParallelBackendBase instance or None, default: \'loky\'
            Specify the parallelization backend implementation.
            Supported backends are:

            - "loky" used by default, can induce some
              communication and memory overhead when exchanging input and
              output data with the worker Python processes. On some rare
              systems (such as Pyiodide), the loky backend may not be
              available.
            - "multiprocessing" previous process-based backend based on
              `multiprocessing.Pool`. Less robust than `loky`.
            - "threading" is a very low-overhead backend but it suffers
              from the Python Global Interpreter Lock if the called function
              relies a lot on Python objects. "threading" is mostly useful
              when the execution bottleneck is a compiled extension that
              explicitly releases the GIL (for instance a Cython loop wrapped
              in a "with nogil" block or an expensive call to a library such
              as NumPy).
            - finally, you can register backends by calling
              :func:`~register_parallel_backend`. This will allow you to
              implement a backend of your liking.

            It is not recommended to hard-code the backend name in a call to
            :class:`~Parallel` in a library. Instead it is recommended to set
            soft hints (prefer) or hard constraints (require) so as to make it
            possible for library users to change the backend from the outside
            using the :func:`~parallel_config` context manager.
        return_as: str in {\'list\', \'generator\'}, default: \'list\'
            If \'list\', calls to this instance will return a list, only when
            all results have been processed and retrieved.
            If \'generator\', it will return a generator that yields the results
            as soon as they are available, in the order the tasks have been
            submitted with.
            Future releases are planned to also support \'generator_unordered\',
            in which case the generator immediately yields available results
            independently of the submission order.
        prefer: str in {\'processes\', \'threads\'} or None, default: None
            Soft hint to choose the default backend if no specific backend
            was selected with the :func:`~parallel_config` context manager.
            The default process-based backend is \'loky\' and the default
            thread-based backend is \'threading\'. Ignored if the ``backend``
            parameter is specified.
        require: \'sharedmem\' or None, default None
            Hard constraint to select the backend. If set to \'sharedmem\',
            the selected backend will be single-host and thread-based even
            if the user asked for a non-thread based backend with
            :func:`~joblib.parallel_config`.
        verbose: int, optional
            The verbosity level: if non zero, progress messages are
            printed. Above 50, the output is sent to stdout.
            The frequency of the messages increases with the verbosity level.
            If it more than 10, all iterations are reported.
        timeout: float, optional
            Timeout limit for each task to complete.  If any task takes longer
            a TimeOutError will be raised. Only applied when n_jobs != 1
        pre_dispatch: {\'all\', integer, or expression, as in \'3*n_jobs\'}
            The number of batches (of tasks) to be pre-dispatched.
            Default is \'2*n_jobs\'. When batch_size="auto" this is reasonable
            default and the workers should never starve. Note that only basic
            arithmetics are allowed here and no modules can be used in this
            expression.
        batch_size: int or \'auto\', default: \'auto\'
            The number of atomic tasks to dispatch at once to each
            worker. When individual evaluations are very fast, dispatching
            calls to workers can be slower than sequential computation because
            of the overhead. Batching fast computations together can mitigate
            this.
            The ``\'auto\'`` strategy keeps track of the time it takes for a
            batch to complete, and dynamically adjusts the batch size to keep
            the time on the order of half a second, using a heuristic. The
            initial batch size is 1.
            ``batch_size="auto"`` with ``backend="threading"`` will dispatch
            batches of a single task at a time as the threading backend has
            very little overhead and using larger batch size has not proved to
            bring any gain in that case.
        temp_folder: str, optional
            Folder to be used by the pool for memmapping large arrays
            for sharing memory with worker processes. If None, this will try in
            order:

            - a folder pointed by the JOBLIB_TEMP_FOLDER environment
              variable,
            - /dev/shm if the folder exists and is writable: this is a
              RAM disk filesystem available by default on modern Linux
              distributions,
            - the default system temporary folder that can be
              overridden with TMP, TMPDIR or TEMP environment
              variables, typically /tmp under Unix operating systems.

            Only active when backend="loky" or "multiprocessing".
        max_nbytes int, str, or None, optional, 1M by default
            Threshold on the size of arrays passed to the workers that
            triggers automated memory mapping in temp_folder. Can be an int
            in Bytes, or a human-readable string, e.g., \'1M\' for 1 megabyte.
            Use None to disable memmapping of large arrays.
            Only active when backend="loky" or "multiprocessing".
        mmap_mode: {None, \'r+\', \'r\', \'w+\', \'c\'}, default: \'r\'
            Memmapping mode for numpy arrays passed to workers. None will
            disable memmapping, other modes defined in the numpy.memmap doc:
            https://numpy.org/doc/stable/reference/generated/numpy.memmap.html
            Also, see \'max_nbytes\' parameter documentation for more details.

        Notes
        -----

        This object uses workers to compute in parallel the application of a
        function to many different arguments. The main functionality it brings
        in addition to using the raw multiprocessing or concurrent.futures API
        are (see examples for details):

        * More readable code, in particular since it avoids
          constructing list of arguments.

        * Easier debugging:
            - informative tracebacks even when the error happens on
              the client side
            - using \'n_jobs=1\' enables to turn off parallel computing
              for debugging without changing the codepath
            - early capture of pickling errors

        * An optional progress meter.

        * Interruption of multiprocesses jobs with \'Ctrl-C\'

        * Flexible pickling control for the communication to and from
          the worker processes.

        * Ability to use shared memory efficiently with worker
          processes for large numpy-based datastructures.

        Note that the intended usage is to run one call at a time. Multiple
        calls to the same Parallel object will result in a ``RuntimeError``

        Examples
        --------

        A simple example:

        >>> from math import sqrt
        >>> from joblib import Parallel, delayed
        >>> Parallel(n_jobs=1)(delayed(sqrt)(i**2) for i in range(10))
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

        Reshaping the output when the function has several return
        values:

        >>> from math import modf
        >>> from joblib import Parallel, delayed
        >>> r = Parallel(n_jobs=1)(delayed(modf)(i/2.) for i in range(10))
        >>> res, i = zip(*r)
        >>> res
        (0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5)
        >>> i
        (0.0, 0.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0)

        The progress meter: the higher the value of `verbose`, the more
        messages:

        >>> from time import sleep
        >>> from joblib import Parallel, delayed
        >>> r = Parallel(n_jobs=2, verbose=10)(
        ...     delayed(sleep)(.2) for _ in range(10)) #doctest: +SKIP
        [Parallel(n_jobs=2)]: Done   1 tasks      | elapsed:    0.6s
        [Parallel(n_jobs=2)]: Done   4 tasks      | elapsed:    0.8s
        [Parallel(n_jobs=2)]: Done  10 out of  10 | elapsed:    1.4s finished

        Traceback example, note how the line of the error is indicated
        as well as the values of the parameter passed to the function that
        triggered the exception, even though the traceback happens in the
        child process:

        >>> from heapq import nlargest
        >>> from joblib import Parallel, delayed
        >>> Parallel(n_jobs=2)(
        ... delayed(nlargest)(2, n) for n in (range(4), \'abcde\', 3))
        ... # doctest: +SKIP
        -----------------------------------------------------------------------
        Sub-process traceback:
        -----------------------------------------------------------------------
        TypeError                                      Mon Nov 12 11:37:46 2012
        PID: 12934                                Python 2.7.3: /usr/bin/python
        ........................................................................
        /usr/lib/python2.7/heapq.pyc in nlargest(n=2, iterable=3, key=None)
            419         if n >= size:
            420             return sorted(iterable, key=key, reverse=True)[:n]
            421
            422     # When key is none, use simpler decoration
            423     if key is None:
        --> 424         it = izip(iterable, count(0,-1))           # decorate
            425         result = _nlargest(n, it)
            426         return map(itemgetter(0), result)          # undecorate
            427
            428     # General case, slowest method
         TypeError: izip argument #1 must support iteration
        _______________________________________________________________________


        Using pre_dispatch in a producer/consumer situation, where the
        data is generated on the fly. Note how the producer is first
        called 3 times before the parallel loop is initiated, and then
        called to generate new data on the fly:

        >>> from math import sqrt
        >>> from joblib import Parallel, delayed
        >>> def producer():
        ...     for i in range(6):
        ...         print(\'Produced %s\' % i)
        ...         yield i
        >>> out = Parallel(n_jobs=2, verbose=100, pre_dispatch=\'1.5*n_jobs\')(
        ...     delayed(sqrt)(i) for i in producer()) #doctest: +SKIP
        Produced 0
        Produced 1
        Produced 2
        [Parallel(n_jobs=2)]: Done 1 jobs     | elapsed:  0.0s
        Produced 3
        [Parallel(n_jobs=2)]: Done 2 jobs     | elapsed:  0.0s
        Produced 4
        [Parallel(n_jobs=2)]: Done 3 jobs     | elapsed:  0.0s
        Produced 5
        [Parallel(n_jobs=2)]: Done 4 jobs     | elapsed:  0.0s
        [Parallel(n_jobs=2)]: Done 6 out of 6 | elapsed:  0.0s remaining: 0.0s
        [Parallel(n_jobs=2)]: Done 6 out of 6 | elapsed:  0.0s finished

    '''
    verbose: Incomplete
    timeout: Incomplete
    pre_dispatch: Incomplete
    return_as: Incomplete
    return_generator: Incomplete
    n_jobs: Incomplete
    batch_size: Incomplete
    def __init__(self, n_jobs=..., backend=..., return_as: str = 'list', verbose=..., timeout: Incomplete | None = None, pre_dispatch: str = '2 * n_jobs', batch_size: str = 'auto', temp_folder=..., max_nbytes=..., mmap_mode=..., prefer=..., require=...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def dispatch_next(self) -> None:
        """Dispatch more data for parallel processing

        This method is meant to be called concurrently by the multiprocessing
        callback. We rely on the thread-safety of dispatch_one_batch to protect
        against concurrent consumption of the unprotected iterator.

        """
    def dispatch_one_batch(self, iterator):
        """Prefetch the tasks for the next batch and dispatch them.

        The effective size of the batch is computed here.
        If there are no more jobs to dispatch, return False, else return True.

        The iterator consumption and dispatching is protected by the same
        lock so calling this function should be thread safe.

        """
    def print_progress(self) -> None:
        """Display the process of the parallel execution only a fraction
           of time, controlled by self.verbose.
        """
    def __call__(self, iterable):
        """Main function to dispatch parallel tasks."""
