import threading
import torch
import torch.autograd
from .microbatch import Batch
from _typeshed import Incomplete
from torch import Tensor
from typing import Any, Deque, Generator, Protocol, Sequence, Tuple

__all__ = ['Function', 'checkpoint', 'Checkpointing', 'ThreadLocal', 'enable_checkpointing', 'enable_recomputing', 'is_checkpointing', 'is_recomputing', 'Context', 'save_rng_states', 'restore_rng_states', 'Checkpoint', 'Recompute']

Tensors = Sequence[Tensor]
TensorOrTensors = Tensor | Tensors
Recomputed = Tuple[TensorOrTensors, Tensors]
RNGStates = Tuple[Tensor, Tensor | None]

class Function(Protocol):
    def __call__(self, input: TensorOrTensors) -> TensorOrTensors: ...

def checkpoint(function: Function, input):
    """Makes a checkpoint with a simple interface like
    :func:`torch.utils.checkpoint.checkpoint`. It's only used to test or debug
    :class:`Checkpoint` and :class:`Recompute` without boilerplate.
    """

class Checkpointing:
    """Generates a pair of :class:`Checkpoint` and :class:`Recompute`."""
    function: Incomplete
    batch: Incomplete
    recomputed: Incomplete
    rng_states: Incomplete
    def __init__(self, function: Function, batch: Batch) -> None: ...
    def checkpoint(self) -> Batch:
        """Returns a batch applied by :class:`Checkpoint`."""
    def recompute(self, batch: Batch) -> None:
        """Applies :class:`Recompute` to the batch in place."""

class ThreadLocal(threading.local):
    is_checkpointing: bool
    is_recomputing: bool
    def __init__(self) -> None: ...

def enable_checkpointing() -> Generator[None, None, None]:
    """Makes :func:`is_checkpointing` return :data:`True` within a context."""
def enable_recomputing() -> Generator[None, None, None]:
    """Makes :func:`is_recomputing` return :data:`True` within a context."""
def is_checkpointing() -> bool:
    """Whether the current forward propagation is under checkpointing.

    Returns:
        bool: :data:`True` if it's under checkpointing.

    """
def is_recomputing() -> bool:
    """Whether the current forward propagation is under checkpoint
    recomputation. Use this to prevent duplicated side-effects at forward
    propagation::

        class Counter(nn.Module):
            def __init__(self):
                super().__init__()
                self.counter = 0

            def forward(self, input):
                if not is_recomputing():
                    self.counter += 1
                return input

    Returns:
        bool: :data:`True` if it's under checkpoint recomputation.

    .. seealso:: :ref:`Detecting Recomputation`

    """

class Context:
    """The common interface between the :class:`Checkpoint` and
    :class:`Recompute` context.
    """
    recomputed: Deque[Recomputed]
    rng_states: Deque[RNGStates]
    function: Function
    input_atomic: bool
    inputs: Sequence[Any]
    saved_tensors: Tuple[Tensor, ...]
    def save_for_backward(self, *tensors: Tensor) -> None: ...

def save_rng_states(device: torch.device, rng_states: Deque[RNGStates]) -> None:
    """:meth:`Checkpoint.forward` captures the current PyTorch's random number
    generator states at CPU and GPU to reuse in :meth:`Recompute.backward`.

    .. seealso:: :ref:`Referential Transparency`

    """
def restore_rng_states(device: torch.device, rng_states: Deque[RNGStates]) -> Generator[None, None, None]:
    """:meth:`Recompute.backward` restores the random number generator states
    captured by :func:`save_rng_states` within its context.

    .. seealso:: :ref:`Referential Transparency`

    """

class Checkpoint(torch.autograd.Function):
    @staticmethod
    def forward(ctx: Context, phony: Tensor, recomputed: Deque[Recomputed], rng_states: Deque[RNGStates], function: Function, input_atomic: bool, *inputs): ...
    @staticmethod
    def backward(ctx: Context, *grad_output: Tensor) -> Tuple[Tensor | None, ...]: ...

class Recompute(torch.autograd.Function):
    @staticmethod
    def forward(ctx: Context, phony: Tensor, recomputed: Deque[Recomputed], rng_states: Deque[RNGStates], function: Function, input_atomic: bool, *inputs) -> Tensor: ...
    @staticmethod
    def backward(ctx: Context, *grad_output: Tensor) -> Tuple[None, ...]: ...
