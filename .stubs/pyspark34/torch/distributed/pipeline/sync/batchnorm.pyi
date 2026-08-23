from _typeshed import Incomplete
from torch import Tensor, nn
from torch.nn.modules.batchnorm import _BatchNorm
from typing import TypeVar

__all__ = ['DeferredBatchNorm']

TModule = TypeVar('TModule', bound=nn.Module)

class DeferredBatchNorm(_BatchNorm):
    """A BatchNorm layer tracks multiple micro-batches to update running
    statistics per mini-batch.
    """
    sum: Tensor
    sum_squares: Tensor
    running_mean: Tensor
    running_var: Tensor
    num_batches_tracked: Tensor
    counter: int
    tracked: int
    chunks: Incomplete
    def __init__(self, num_features: int, eps: float = 1e-05, momentum: float = 0.1, affine: bool = True, chunks: int = 1) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    @classmethod
    def convert_deferred_batch_norm(cls, module: TModule, chunks: int = 1) -> TModule:
        """Converts a :class:`nn.BatchNorm` or underlying
        :class:`nn.BatchNorm`s into :class:`DeferredBatchNorm`::

            from torchvision.models.resnet import resnet101
            from torchpipe.batchnorm import DeferredBatchNorm
            model = resnet101()
            model = DeferredBatchNorm.convert_deferred_batch_norm(model)

        """
