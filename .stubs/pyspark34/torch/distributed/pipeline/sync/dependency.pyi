import torch
from torch import Tensor
from typing import Tuple

__all__ = ['fork', 'Fork', 'join', 'Join']

def fork(input: Tensor) -> Tuple[Tensor, Tensor]:
    """Branches out from an autograd lane of the given tensor."""

class Fork(torch.autograd.Function):
    @staticmethod
    def forward(ctx: Fork, input: Tensor) -> Tuple[Tensor, Tensor]: ...
    @staticmethod
    def backward(ctx: Fork, grad_input: Tensor, grad_grad: Tensor) -> Tensor: ...

def join(input: Tensor, phony: Tensor) -> Tensor:
    """Merges two autograd lanes."""

class Join(torch.autograd.Function):
    @staticmethod
    def forward(ctx: Join, input: Tensor, phony: Tensor) -> Tensor: ...
    @staticmethod
    def backward(ctx: Join, grad_input: Tensor) -> Tuple[Tensor, None]: ...
