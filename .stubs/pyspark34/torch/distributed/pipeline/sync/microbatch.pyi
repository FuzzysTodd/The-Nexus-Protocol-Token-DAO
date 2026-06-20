import typing
from _typeshed import Incomplete
from torch import Tensor
from typing import Any, Callable, List, Sequence

__all__ = ['NoChunk', 'Batch', 'check', 'scatter', 'gather']

Tensors = Sequence[Tensor]
TensorOrTensors = Tensor | Tensors
Function = Callable[[TensorOrTensors], List[Any] | Tensor]

class NoChunk:
    """
    Wrapper for a Tensor in :meth:`Pipe.forward` indicating that the tensor
    should not be chunked on the batch dimension and instead be replicated
    as-is across all micro-batches. This is useful for tensors which might
    not have any 'batch' semantics for the model.
    """
    def __init__(self, inp: Tensor) -> None: ...
    @property
    def tensor(self): ...

class Batch:
    """
    An abstraction representing a microbatch in the pipeline.
    """
    atomic: Incomplete
    def __init__(self, values: List[Any] | Tensor) -> None: ...
    @property
    def tensor(self) -> Tensor:
        """Retrieves the underlying tensor."""
    @property
    def values(self):
        """Retreives the underlying values for the batch"""
    def find_tensor_idx(self):
        """
        Retrieves the index of first tensor found.
        """
    def get_device(self):
        """
        Retrieves the device for this microbatch.
        """
    def call(self, function: Function) -> Batch:
        """Calls a function on the microbatch. It also wraps
        the output with :class:`Batch`.
        """
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int): ...
    @typing.overload
    def __setitem__(self, index: int, value: Tensor) -> None: ...
    @typing.overload
    def __setitem__(self, index: slice, value: Tensors) -> None: ...

def check(first_device, *inputs) -> None:
    """
    Checks whether the input contains at least one tensor and each tensor is
    on the same device as the first partition.

    Raises:
        ValueError: input does not contain at least one tensor

    """
def scatter(*inputs, chunks: int) -> List[Batch]:
    """Splits an input mini-batch into multiple micro-batches."""
def gather(outputs: List[Batch]):
    """Concatenates output micro-batches into a mini-batch."""
