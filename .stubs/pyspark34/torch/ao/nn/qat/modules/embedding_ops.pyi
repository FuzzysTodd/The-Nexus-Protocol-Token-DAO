import torch.nn as nn
from _typeshed import Incomplete
from torch import Tensor

__all__ = ['Embedding', 'EmbeddingBag']

class Embedding(nn.Embedding):
    """
    An embedding bag module attached with FakeQuantize modules for weight,
    used for quantization aware training.

    We adopt the same interface as `torch.nn.Embedding`, please see
    https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding
    for documentation.

    Similar to `torch.nn.Embedding`, with FakeQuantize modules initialized to
    default.

    Attributes:
        weight: fake quant module for weight
    """
    qconfig: Incomplete
    weight_fake_quant: Incomplete
    def __init__(self, num_embeddings, embedding_dim, padding_idx: Incomplete | None = None, max_norm: Incomplete | None = None, norm_type: float = 2.0, scale_grad_by_freq: bool = False, sparse: bool = False, _weight: Incomplete | None = None, device: Incomplete | None = None, dtype: Incomplete | None = None, qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input) -> Tensor: ...
    @classmethod
    def from_float(cls, mod):
        """Create a qat module from a float module

            Args: `mod` a float module, either produced by torch.ao.quantization utilities
            or directly from user
        """
    def to_float(self): ...

class EmbeddingBag(nn.EmbeddingBag):
    """
    An embedding bag module attached with FakeQuantize modules for weight,
    used for quantization aware training.

    We adopt the same interface as `torch.nn.EmbeddingBag`, please see
    https://pytorch.org/docs/stable/generated/torch.nn.EmbeddingBag.html#torch.nn.EmbeddingBag
    for documentation.

    Similar to `torch.nn.EmbeddingBag`, with FakeQuantize modules initialized to
    default.

    Attributes:
        weight: fake quant module for weight
    """
    qconfig: Incomplete
    weight_fake_quant: Incomplete
    def __init__(self, num_embeddings, embedding_dim, max_norm: Incomplete | None = None, norm_type: float = 2.0, scale_grad_by_freq: bool = False, mode: str = 'mean', sparse: bool = False, _weight: Incomplete | None = None, include_last_offset: bool = False, padding_idx: Incomplete | None = None, qconfig: Incomplete | None = None, device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input, offsets: Incomplete | None = None, per_sample_weights: Incomplete | None = None) -> Tensor: ...
    @classmethod
    def from_float(cls, mod):
        """Create a qat module from a float module

            Args: `mod` a float module, either produced by torch.ao.quantization utilities
            or directly from user
        """
    def to_float(self): ...
