import torch
from _typeshed import Incomplete
from torch.distributed._tensor import DTensor as DT

__all__ = ['TensorParallelMultiheadAttention']

class TensorParallelMultiheadAttention(torch.nn.Module):
    """
    Multi-head Attention block from Transformer models.
    Since we need some customizations for the attention layer,
    we are writing a customized but mathematically equivalent
    attention module as defined in torch.nn.

    Note that:
    We now only support the case when it's self attention with
    limited input args and we also assume that the input tensor
    has a dimension of three. Although we do implement the logic
    for multihead attention, it was not fully tested.
    """
    device: Incomplete
    num_heads: Incomplete
    hidden_size: Incomplete
    hidden_size_per_attention_head: Incomplete
    scale: Incomplete
    qkv: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    proj: Incomplete
    tp_size: Incomplete
    norm_factor: Incomplete
    self_attention: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, bias: bool = True, add_bias_kv: bool = False, add_zero_attn: bool = False, kdim: int | None = None, vdim: int | None = None, batch_first: bool = False, device: torch.device | None = None, dtype: torch.dtype | None = None, tp_size: int = 1, self_attention: bool = True) -> None: ...
    def forward(self, query: torch.Tensor | DT, key: torch.Tensor | DT, value: torch.Tensor | DT, key_padding_mask: torch.Tensor | None = None, need_weights: bool = True, attn_mask: torch.Tensor | None = None, average_attn_weights: bool = True) -> torch.Tensor | DT: ...
    def copy(self, that: torch.nn.MultiheadAttention) -> None: ...
