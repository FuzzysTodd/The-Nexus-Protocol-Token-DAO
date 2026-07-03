import torch
from torch._prims_common import NumberType, TensorLikeType

__all__ = ['alpha_dropout', 'celu', 'dropout', 'elu', 'hardshrink', 'hardtanh', 'hinge_embedding_loss', 'huber_loss', 'l1_loss', 'log_softmax', 'margin_ranking_loss', 'mish', 'nll_loss', 'mse_loss', 'poisson_nll_loss', 'prelu', 'relu', 'relu6', 'selu', 'softmax', 'softmin', 'softplus', 'softshrink', 'tanhshrink', 'threshold', 'triplet_margin_loss', 'glu', 'pairwise_distance', 'pdist']

def alpha_dropout(self, p: float = 0.5, training: bool = False, inplace: bool = False) -> TensorLikeType: ...
def celu(a: TensorLikeType, alpha: NumberType | None = None, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.celu
    """
def dropout(a: TensorLikeType, p: float = 0.5, training: bool = True, inplace: bool = False) -> TensorLikeType: ...
def elu(a: TensorLikeType, alpha: NumberType = 1.0, scale: NumberType = 1.0, input_scale: NumberType = 1.0, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.elu
    """
def relu(a: TensorLikeType, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.relu
    """
def mish(a: TensorLikeType, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.mish
    """
def selu(a: TensorLikeType, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.selu
    """
def softmax(a: TensorLikeType, dim: int | None = None, _stacklevel: int = 3, dtype: torch.dtype | None = None) -> TensorLikeType: ...
def softmin(a: TensorLikeType, dim: int | None = None, _stacklevel: int = 3, dtype: torch.dtype | None = None) -> TensorLikeType: ...
def softplus(a: TensorLikeType, beta: NumberType | None = None, threshold: NumberType = 20, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.softplus
    """
def hardshrink(a: TensorLikeType, lambd: float = 0.5): ...
def softshrink(a: TensorLikeType, lambd: float = 0.5): ...
def l1_loss(input: TensorLikeType, target: TensorLikeType, size_average: bool | None = None, reduce: bool | None = None, reduction: str = 'mean') -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.l1_loss
    """
def log_softmax(a: TensorLikeType, dim: int | None = None, _stacklevel: int = 3, dtype: torch.dtype | None = None) -> TensorLikeType: ...
def margin_ranking_loss(input1: TensorLikeType, input2: TensorLikeType, target: TensorLikeType, margin: float = 0.0, reduction: str = 'mean') -> TensorLikeType: ...
def mse_loss(input: TensorLikeType, target: TensorLikeType, size_average: bool | None = None, reduce: bool | None = None, reduction: str = 'mean') -> TensorLikeType: ...
def hinge_embedding_loss(input: TensorLikeType, target: TensorLikeType, margin: float = 1.0, reduction: str = 'mean') -> TensorLikeType: ...
def nll_loss(input: TensorLikeType, target: TensorLikeType, weight: TensorLikeType | None = None, size_average: bool | None = None, ignore_index: int = -100, reduce: bool | None = None, reduction: str = 'mean') -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.nll_loss
    """
def huber_loss(input: TensorLikeType, target: TensorLikeType, reduction: str | int = 'mean', delta: float = 1.0) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.huber_loss
    """
def tanhshrink(a: TensorLikeType) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.tanhshrink
    """
def threshold(a: TensorLikeType, threshold: NumberType, value: bool | int | float, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.threshold
    """
def triplet_margin_loss(anchor: TensorLikeType, positive: TensorLikeType, negative: TensorLikeType, margin: float = 1.0, p: float = 2, eps: float = 1e-06, swap: bool = False, size_average: bool | None = None, reduce: bool | None = None, reduction: str = 'mean') -> TensorLikeType: ...
def hardtanh(a: TensorLikeType, min_val: NumberType = -1, max_val: NumberType = 1, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.hardtanh
    """
def poisson_nll_loss(input: TensorLikeType, target: TensorLikeType, log_input: bool = True, full: bool = False, size_average: bool | None = None, eps: float = 1e-08, reduce: bool | None = None, reduction: str = 'mean') -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.poisson_nll_loss
    """
def prelu(a: TensorLikeType, weight: TensorLikeType) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.prelu
    """
def relu6(a: TensorLikeType, inplace: bool = False) -> TensorLikeType:
    """
    Reference implementation of torch.nn.functional.relu6
    """
def glu(a: TensorLikeType, dim: int = -1) -> TensorLikeType: ...
def pairwise_distance(x1: TensorLikeType, x2: TensorLikeType, p: NumberType = 2.0, eps: NumberType = 1e-06, keepdim: bool = False) -> TensorLikeType: ...
def pdist(a: TensorLikeType, p: float = 2) -> TensorLikeType: ...
