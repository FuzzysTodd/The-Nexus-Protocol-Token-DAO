import torch
from ..copy import Context as CopyContext, Copy as Copy
from ..phony import get_phony as get_phony
from ..stream import AbstractStream as AbstractStream, get_device as get_device
from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import Tuple

class Portal:
    """A portal for a tensor."""
    grad: Incomplete
    def __init__(self, tensor: Tensor | None, tensor_life: int) -> None: ...
    def blue(self) -> Tensor:
        """Creates a :class:`PortalBlue` which hides the underlying tensor from
        the autograd engine.

        Join the returning phony to the main lane of the autograd graph to
        assure the correct backpropagation::

            PortalBlue --+
                         |
            ---------- Join --

        """
    def orange(self, phony: Tensor) -> Tensor | None:
        """Creates a :class:`PortalOrange` which retrieves the hidden tensor
        without losing ability of backpropagation.

        Give a phony forked from the main lane of an autograd graph::

                +-- PortalOrange --+
                |                  |
            -- Fork --------- f(a, b) --

        """
    def copy(self, prev_stream: AbstractStream, next_stream: AbstractStream, phony: Tensor) -> Tensor:
        """Copies the hidden tensor by a :class:`PortalCopy`.

        Give a phony and use the returning phony to keep backpropagation::

                +-- PortalCopy --+
                |                |
            -- Fork ---------- Join --

        """
    def check_tensor_life(self) -> None: ...
    tensor_life: Incomplete
    tensor: Incomplete
    def put_tensor(self, tensor: Tensor | None, tensor_life: int) -> None:
        """Stores a tensor into this portal."""
    def use_tensor(self) -> Tensor | None:
        """Retrieves the underlying tensor and decreases the tensor  life. When
        the life becomes 0, it the tensor will be removed.
        """
    def put_grad(self, grad: Tensor) -> None:
        """Stores a gradient into this portal."""
    def use_grad(self) -> Tensor:
        """Retrieves and removes the underlying gradient. The gradient is
        always ephemeral.
        """

class Context(CopyContext):
    portal: Portal

class PortalBlue(torch.autograd.Function):
    """Hides a tensor from the autograd engine by a :class:`Portal`."""
    @staticmethod
    def forward(ctx: Context, portal: Portal, tensor: Tensor) -> Tensor: ...
    @staticmethod
    def backward(ctx: Context, grad_phony: Tensor) -> Tuple[None, Tensor]: ...

class PortalOrange(torch.autograd.Function):
    """Retrieves the hidden tensor from a :class:`Portal`."""
    @staticmethod
    def forward(ctx: Context, portal: Portal, phony: Tensor) -> Tensor: ...
    @staticmethod
    def backward(ctx: Context, grad: Tensor) -> Tuple[None, None]: ...

class PortalCopy(torch.autograd.Function):
    """Copies the hidden tensor in a :class:`Portal`. It replaces the hidden
    tensor with copied one.
    """
    @staticmethod
    def forward(ctx: Context, portal: Portal, prev_stream: AbstractStream, next_stream: AbstractStream, phony: Tensor) -> Tensor: ...
    @staticmethod
    def backward(ctx: Context, grad_phony: Tensor) -> Tuple[None, None, None, None]: ...
