import torch
from .stream import AbstractStream
from torch import Tensor
from typing import Sequence, Tuple

__all__ = ['Context', 'Copy', 'Wait']

Tensors = Sequence[Tensor]

class Context:
    prev_stream: AbstractStream
    next_stream: AbstractStream

class Copy(torch.autograd.Function):
    """Copies tensors on specific streams."""
    @staticmethod
    def forward(ctx: Context, prev_stream: AbstractStream, next_stream: AbstractStream, *input) -> Tensors: ...
    @staticmethod
    def backward(ctx: Context, *grad_output: Tensor) -> Tuple[Tensor | None, ...]: ...

class Wait(torch.autograd.Function):
    """Synchronizes a stream to another stream.

    Place it just before you want to start an operation on the next stream,
    provided that all operations on the previous stream are done.

    """
    @staticmethod
    def forward(ctx: Context, prev_stream: AbstractStream, next_stream: AbstractStream, *input) -> Tensors: ...
    @staticmethod
    def backward(ctx: Context, *grad_input: Tensor) -> Tuple[Tensor | None, ...]: ...
