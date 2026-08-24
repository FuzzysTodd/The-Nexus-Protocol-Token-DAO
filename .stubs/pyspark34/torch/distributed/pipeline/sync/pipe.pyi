import torch
from _typeshed import Incomplete
from collections import OrderedDict
from torch import Tensor, nn
from torch.distributed.rpc import RRef
from typing import Any, Iterable, List, Sequence

__all__ = ['Pipe', 'BalanceError', 'PipeSequential', 'WithDevice']

Devices = Iterable[Device] | List[Device]
Tensors = Sequence[Tensor]
TensorOrTensors = Tensor | Tensors
NamedModules = OrderedDict[str, Module]

class BalanceError(ValueError): ...

class PipeSequential(nn.Sequential):
    """
    Pipe variant of ``nn.Sequential`` which supports multiple inputs.
    """
    def forward(self, *inputs): ...

class WithDevice(nn.Module):
    '''
    Wraps an ``nn.Module`` which is part of ``nn.Sequential`` passed into :class:`Pipe`
    that overrides the device for that module. In cases where :class:`Pipe`
    can\'t implicitly determine the device for the module and places it on CPU,
    this wrapper can be used to override the implicit behavior and explicitly
    specify which device a module should run on.

    The provided module is also moved to the given device via ``.to(device)``
    by :class:`Pipe`

    Args:
        module(:class:`torch.nn.Module`): The module to be wrapped.
        device(:class:`torch.device`): The device to run the module on.

    Example::
        >>> # xdoctest: +SKIP("distributed")
        >>> fc1 = nn.Linear(16, 8).cuda(0)
        >>> fc2 = nn.Linear(8, 4).cuda(1)
        >>> dropout = nn.Dropout()
        >>>
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
        >>> # Dropout does not have any parameters/buffers, but we want to
        >>> # run it on cuda:1 to avoid any GPU to CPU transfers.
        >>> model = nn.Sequential(fc1, fc2, WithDevice(dropout, \'cuda:1\'))
        >>> # xdoctest: +SKIP("Needs RPC framework init")
        >>> model = Pipe(model, chunks=8)
    '''
    def __init__(self, module: nn.Module, device: torch.device) -> None: ...
    def forward(self, *args, **kwargs): ...
    @property
    def module(self): ...
    @property
    def device(self): ...

class Pipe(Module):
    """Wraps an arbitrary :class:`nn.Sequential <torch.nn.Sequential>` module
    to train on using synchronous pipeline parallelism. If the module requires
    lots of memory and doesn't fit on a single GPU, pipeline parallelism is a
    useful technique to employ for training.

    The implementation is based on the torchgpipe_ paper.

    .. _torchgpipe: https://arxiv.org/abs/2004.09910

    Pipe combines pipeline parallelism with checkpointing to reduce peak
    memory required to train while minimizing device under-utilization.

    You should place all the modules on the appropriate devices and wrap them
    into an :class:`nn.Sequential <torch.nn.Sequential>` module defining the
    desired order of execution. If a module does not contain any
    parameters/buffers, it is assumed this module should be executed on CPU
    and appropriate input tensors to the module are moved to CPU before
    execution. This behavior can be overridden by the :class:`WithDevice`
    wrapper which can be used to explicitly specify which device a module
    should run on.

    Args:
        module (:class:`nn.Sequential <torch.nn.Sequential>`):
            sequential module to be parallelized using pipelining. Each module
            in the sequence has to have all of its parameters on a single
            device. Each module in the sequence has to either be an nn.Module
            or :class:`nn.Sequential <torch.nn.Sequential>` (to combine multiple
            sequential modules on a single device)
        chunks (int):
            number of micro-batches (default: ``1``)
        checkpoint (str):
            when to enable checkpointing, one of ``'always'``,
            ``'except_last'``, or ``'never'`` (default: ``'except_last'``).
            ``'never'`` disables checkpointing completely, ``'except_last'``
            enables checkpointing for all micro-batches except the last one
            and ``'always'`` enables checkpointing for all micro-batches.
        deferred_batch_norm (bool):
            whether to use deferred ``BatchNorm`` moving statistics (default:
            :data:`False`). If set to :data:`True`, we track statistics across
            multiple micro-batches to update the running statistics per
            mini-batch.

    Raises:
        TypeError:
            the module is not a :class:`nn.Sequential <torch.nn.Sequential>`.
        ValueError:
            invalid arguments

    Example::
        Pipeline of two FC layers across GPUs 0 and 1.

        >>> # Need to initialize RPC framework first.
        >>> # xdoctest: +SKIP
        >>> os.environ['MASTER_ADDR'] = 'localhost'
        >>> os.environ['MASTER_PORT'] = '29500'
        >>> torch.distributed.rpc.init_rpc('worker', rank=0, world_size=1)
        >>>
        >>> # Build pipe.
        >>> fc1 = nn.Linear(16, 8).cuda(0)
        >>> fc2 = nn.Linear(8, 4).cuda(1)
        >>> model = nn.Sequential(fc1, fc2)
        >>> model = Pipe(model, chunks=8)
        >>> input = torch.rand(16, 16).cuda(0)
        >>> output_rref = model(input)

    .. note::
        You can wrap a :class:`Pipe` model with
        :class:`torch.nn.parallel.DistributedDataParallel` only when the
        checkpoint parameter of :class:`Pipe` is ``'never'``.

    .. note::
        :class:`Pipe` only supports intra-node pipelining currently, but
        will be expanded to support inter-node pipelining in the future.
        The forward function returns an :class:`~torch.distributed.rpc.RRef`
        to allow for inter-node pipelining in the future, where the output
        might be on a remote host. For intra-node pipelinining you can use
        :meth:`~torch.distributed.rpc.RRef.local_value` to retrieve the
        output locally.

    .. warning::
        :class:`Pipe` is experimental and subject to change.
    """
    chunks: Incomplete
    checkpoint: Incomplete
    pipeline: Incomplete
    def __init__(self, module: nn.Sequential, chunks: int = 1, checkpoint: str = 'except_last', deferred_batch_norm: bool = False) -> None: ...
    def __len__(self) -> int:
        """Counts the length of the underlying sequential module."""
    def __getitem__(self, index: int) -> nn.Module:
        """Gets a layer in the underlying sequential module."""
    def __iter__(self) -> Iterable[nn.Module]:
        """Iterates over children of the underlying sequential module."""
    def cuda(self, device: Device | None = None) -> Pipe: ...
    def cpu(self) -> Pipe: ...
    def to(self, *args: Any, **kwargs: Any) -> Pipe: ...
    def forward(self, *inputs) -> RRef:
        """
        Processes a single input mini-batch through the pipe and returns an
        :class:`~torch.distributed.rpc.RRef` pointing to the output.
        :class:`Pipe` is a fairly transparent module wrapper. It doesn't
        modify the input and output signature of the underlying module. But
        there's type restriction. Input and output have to contain at least one
        tensor. This restriction is applied at partition boundaries too.

        The sequence of inputs are fed into the first stage of the pipeline as
        ``*inputs``. As a result the positional args for this function should
        match the positional args for the first stage of the pipeline. The same
        condition applies for output of one stage of the pipeline which is the
        input for the next stage.

        The input tensor is split into multiple micro-batches based on the
        ``chunks`` parameter used to initialize :class:`Pipe`. The batch size
        is assumed to be the first dimension of the tensor and if the batch
        size is less than ``chunks``, the number of micro-batches is equal to
        the batch size.

        Only tensors are split into multiple micro-batches, non-Tensor inputs
        are just replicated as-is in each micro-batch. For non-Tensor outputs
        in the last stage of the pipeline, they are aggregated as a ``List``
        and returned the user. For example, if you have 2 micro-batches
        returning the integer 5, the user would receive the consolidated
        output of `[5, 5]`

        All the input tensors need to be on the same device as the first
        partition of the pipeline.

        If a tensor is wrapped with the :class:`NoChunk` wrapper, the tensor
        is not split across micro-batches and is replicated as-is similar to
        non-tensors.

        Args:
            inputs: input mini-batch

        Returns:
            :class:`~torch.distributed.rpc.RRef` to the output of the mini-batch

        Raises:
            TypeError: input doesn't contain at least one tensor

        """
