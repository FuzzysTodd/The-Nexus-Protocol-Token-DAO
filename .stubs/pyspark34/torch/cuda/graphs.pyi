import torch
from _typeshed import Incomplete

def is_current_stream_capturing():
    """
    Returns True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

    If a CUDA context does not exist on the current device, returns False without initializing the context.
    """
def graph_pool_handle():
    """
    Returns an opaque token representing the id of a graph memory pool.
    See :ref:`Graph memory management<graph-memory-management>`.

    .. warning::
        This API is in beta and may change in future releases.
    """

class CUDAGraph(torch._C._CUDAGraph):
    """
    Wrapper around a CUDA graph.

    .. warning::
        This API is in beta and may change in future releases.
    """
    def __new__(cls): ...
    def capture_begin(self, pool: Incomplete | None = None) -> None:
        """
        Begins capturing CUDA work on the current stream.

        Typically, you shouldn't call ``capture_begin`` yourself.
        Use :class:`~torch.cuda.graph` or :func:`~torch.cuda.make_graphed_callables`,
        which call ``capture_begin`` internally.

        Arguments:
            pool (optional): Token (returned by :func:`~torch.cuda.graph_pool_handle` or
                :meth:`other_Graph_instance.pool()<torch.cuda.CUDAGraph.pool>`) that hints this graph may share memory
                with the indicated pool.  See :ref:`Graph memory management<graph-memory-management>`.
        """
    def capture_end(self) -> None:
        """
        Ends CUDA graph capture on the current stream.
        After ``capture_end``, ``replay`` may be called on this instance.

        Typically, you shouldn't call ``capture_end`` yourself.
        Use :class:`~torch.cuda.graph` or :func:`~torch.cuda.make_graphed_callables`,
        which call ``capture_end`` internally.
        """
    def replay(self) -> None:
        """
        Replays the CUDA work captured by this graph.
        """
    def reset(self) -> None:
        """
        Deletes the graph currently held by this instance.
        """
    def pool(self):
        """
        Returns an opaque token representing the id of this graph's memory pool.
        This id can optionally be passed to another graph's ``capture_begin``,
        which hints the other graph may share the same memory pool.
        """
    def enable_debug_mode(self):
        """
        Enables debugging mode for CUDAGraph.debug_dump.
        """
    def debug_dump(self, debug_path):
        """
        Arguments:
            debug_path (required): Path to dump the graph to.

        Calls a debugging function to dump the graph if the debugging is
        enabled via CUDAGraph.enable_debug_mode()
        """

class graph:
    """
    Context-manager that captures CUDA work into a :class:`torch.cuda.CUDAGraph`
    object for later replay.

    See :ref:`CUDA Graphs <cuda-graph-semantics>` for a general introduction,
    detailed use, and constraints.

    Arguments:
        cuda_graph (torch.cuda.CUDAGraph): Graph object used for capture.
        pool (optional): Opaque token (returned by a call to :func:`~torch.cuda.graph_pool_handle()` or
            :meth:`other_Graph_instance.pool()<torch.cuda.CUDAGraph.pool>`) hinting this graph's capture
            may share memory from the specified pool. See :ref:`Graph memory management<graph-memory-management>`.
        stream (torch.cuda.Stream, optional): If supplied, will be set as the current stream in the context.
            If not supplied, ``graph`` sets its own internal side stream as the current stream in the context.

    .. note::
        For effective memory sharing, if you pass a ``pool`` used by a previous capture and the previous capture
        used an explicit ``stream`` argument, you should pass the same ``stream`` argument to this capture.

    .. warning::
        This API is in beta and may change in future releases.
    """
    default_capture_stream: Incomplete
    pool: Incomplete
    capture_stream: Incomplete
    stream_ctx: Incomplete
    cuda_graph: Incomplete
    def __init__(self, cuda_graph, pool: Incomplete | None = None, stream: Incomplete | None = None) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def make_graphed_callables(callables, sample_args, num_warmup_iters: int = 3, allow_unused_input: bool = False):
    """
    Accepts callables (functions or :class:`nn.Module<torch.nn.Module>`\\ s)
    and returns graphed versions.

    Each graphed callable's forward pass runs its source callable's
    forward CUDA work as a CUDA graph inside a single autograd node.

    The graphed callable's forward pass also appends
    a backward node to the autograd graph. During backward, this node runs the
    callable's backward work as a CUDA graph.

    Therefore, each graphed callable should be a drop-in replacement for its source callable
    in an autograd-enabled training loop.

    See :ref:`Partial-network capture<partial-network-capture>` for detailed use and constraints.

    If you pass a tuple of several callables, their captures will use the same memory pool.
    See :ref:`Graph memory management<graph-memory-management>` for when this is appropriate.

    Arguments:
        callables (torch.nn.Module or Python function, or tuple of these): Callable or callables to graph.
            See :ref:`Graph memory management<graph-memory-management>` for when passing a tuple of callables
            is appropriate.  If you pass a tuple of callables, their order in the tuple must be the same order
            they'll run in the live workload.
        sample_args (tuple of Tensors, or tuple of tuples of Tensors): Samples args for each callable.
            If a single callable was passed, ``sample_args`` must be a single tuple of argument Tensors.
            If a tuple of callables was passed, ``sample_args`` must be tuple of tuples of argument Tensors.
        num_warmup_iters (int): The number of warmup iterations. Currently, ``DataDistributedParallel`` needs
            11 iterations for warm up. Default: ``3``.
        allow_unused_input (bool): If False, specifying inputs that were not used when computing outputs
            (and therefore their grad is always zero) is an error. Defaults to False.

    .. note::
        The ``requires_grad`` state of each Tensor in ``sample_args`` must match the state
        that's expected for the corresponding real input in the training loop.

    .. warning::
        This API is in beta and may change in future releases.

    .. warning::
        ``sample_args`` for each callable must contain only Tensors. Other types are not allowed.

    .. warning::
        Returned callables do not support higher order differentiation (e.g., double backward).

    .. warning::
        In any :class:`~torch.nn.Module` passed to :func:`~make_graphed_callables`, only parameters
        may be trainable. Buffers must have ``requires_grad=False``.

    .. warning::
        After you pass a :class:`torch.nn.Module` through :func:`~make_graphed_callables`,
        you may not add or remove any of that Module's parameters or buffers.

    .. warning::
        :class:`torch.nn.Module`\\s passed to :func:`~torch.cuda.make_graphed_callables` must not have module hooks
        registered on them at the time they are passed. However, registering hooks on modules *after* passing them
        through :func:`~torch.cuda.make_graphed_callables` is allowed.

    .. warning::
        When running a graphed callable, you must pass its arguments in the same order and format
        they appeared in that callable's ``sample_args``.

    .. warning::
        The automatic mixed precision is supported in :func:`~torch.cuda.make_graphed_callables` only with disabled
        caching. The context manager `torch.cuda.amp.autocast()` must have `cache_enabled=False`.
    """
