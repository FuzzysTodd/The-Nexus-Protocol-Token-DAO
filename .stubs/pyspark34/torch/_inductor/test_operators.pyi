from torch import Tensor as Tensor
from torch.autograd import Function as Function

class Realize(Function):
    @staticmethod
    def forward(ctx, x): ...
    @staticmethod
    def backward(ctx, grad_output): ...

def realize(x: Tensor) -> Tensor: ...
