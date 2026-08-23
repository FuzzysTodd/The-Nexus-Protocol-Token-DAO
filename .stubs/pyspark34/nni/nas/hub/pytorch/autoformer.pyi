import nni.nas.nn.pytorch as nn
import torch
from .utils.fixed import FixedFactory as FixedFactory
from .utils.pretrained import load_pretrained_weight as load_pretrained_weight
from _typeshed import Incomplete
from nni.nas import basic_unit as basic_unit, model_wrapper as model_wrapper
from nni.nas.fixed import no_fixed_arch as no_fixed_arch
from nni.nas.nn.pytorch.choice import ValueChoiceX as ValueChoiceX
from nni.nas.oneshot.pytorch.supermodule._valuechoice_utils import traverse_all_options as traverse_all_options
from nni.nas.oneshot.pytorch.supermodule.operation import MixedOperation as MixedOperation
from typing import Any, Tuple

TIMM_INSTALLED: bool

class RelativePosition2D(nn.Module):
    head_embed_dim: Incomplete
    legnth: Incomplete
    embeddings_table_v: Incomplete
    embeddings_table_h: Incomplete
    def __init__(self, head_embed_dim, length: int = 14) -> None: ...
    def forward(self, length_q, length_k): ...

class RelativePositionAttention(nn.Module):
    """
    This class is designed to support the relative position in attention.
    The pytorch built-in nn.MultiheadAttention() does not support relative position embedding.
    Different from the absolute position embedding, the relative position embedding considers
    encode the relative distance between input tokens and learn the pairwise relations of them.
    It is commonly calculated via a look-up table with learnable parameters interacting with queries
    and keys in self-attention modules.
    """
    num_heads: Incomplete
    head_dim: Incomplete
    scale: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    attn_drop: Incomplete
    proj: Incomplete
    proj_drop: Incomplete
    rpe: Incomplete
    rel_pos_embed_k: Incomplete
    rel_pos_embed_v: Incomplete
    def __init__(self, embed_dim, num_heads, attn_drop: float = 0.0, proj_drop: float = 0.0, qkv_bias: bool = False, qk_scale: Incomplete | None = None, rpe_length: int = 14, rpe: bool = False, head_dim: int = 64) -> None: ...
    def forward(self, x): ...

class TransformerEncoderLayer(nn.Module):
    """
    This class is designed to support the RelativePositionAttention().
    The pytorch build-in nn.TransformerEncoderLayer() does not support customed attention.
    """
    normalize_before: Incomplete
    drop_path: Incomplete
    dropout: Incomplete
    attn: Incomplete
    attn_layer_norm: Incomplete
    ffn_layer_norm: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, embed_dim, num_heads, mlp_ratio: int | float | nn.ValueChoice = 4.0, qkv_bias: bool = False, qk_scale: Incomplete | None = None, rpe: bool = False, drop_rate: float = 0.0, attn_drop: float = 0.0, proj_drop: float = 0.0, drop_path: float = 0.0, pre_norm: bool = True, rpe_length: int = 14, head_dim: int = 64) -> None: ...
    def maybe_layer_norm(self, layer_norm, x, before: bool = False, after: bool = False): ...
    def forward(self, x):
        """
        Args:
            x (Tensor): input to the layer of shape `(batch, patch_num , sample_embed_dim)`
        Returns:
            encoded output of shape `(batch, patch_num, sample_embed_dim)`
        """

class ClsToken(nn.Module):
    """ Concat class token with dim=embed_dim before patch embedding.
    """
    cls_token: Incomplete
    def __init__(self, embed_dim: int) -> None: ...
    def forward(self, x): ...

class MixedClsToken(MixedOperation, ClsToken):
    """ Mixed class token concat operation.

    Supported arguments are:

    - ``embed_dim``

    Prefix of cls_token will be sliced.
    """
    bound_type = ClsToken
    argument_list: Incomplete
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, embed_dim, **kwargs) -> Any: ...
    def forward_with_args(self, embed_dim, inputs: torch.Tensor) -> torch.Tensor: ...

class AbsPosEmbed(nn.Module):
    """ Add absolute position embedding on patch embedding.
    """
    pos_embed: Incomplete
    def __init__(self, length: int, embed_dim: int) -> None: ...
    def forward(self, x): ...

class MixedAbsPosEmbed(MixedOperation, AbsPosEmbed):
    """ Mixed absolute position embedding add operation.

    Supported arguments are:

    - ``embed_dim``

    Prefix of pos_embed will be sliced.
    """
    bound_type = AbsPosEmbed
    argument_list: Incomplete
    def super_init_argument(self, name: str, value_choice: ValueChoiceX): ...
    def slice_param(self, embed_dim, **kwargs) -> Any: ...
    def forward_with_args(self, embed_dim, inputs: torch.Tensor) -> torch.Tensor: ...

class AutoformerSpace(nn.Module):
    """
    The search space that is proposed in `Autoformer <https://arxiv.org/abs/2107.00651>`__.
    There are four searchable variables: depth, embedding dimension, heads number and MLP ratio.

    Parameters
    ----------
    search_embed_dim : list of int
        The search space of embedding dimension.
    search_mlp_ratio : list of float
        The search space of MLP ratio.
    search_num_heads : list of int
        The search space of number of heads.
    search_depth: list of int
        The search space of depth.
    img_size : int
        Size of input image.
    patch_size : int
        Size of image patch.
    in_chans : int
        Number of channels of the input image.
    num_classes : int
        Number of classes for classifier.
    qkv_bias : bool
        Whether to use bias item in the qkv embedding.
    drop_rate : float
        Drop rate of the MLP projection in MSA and FFN.
    attn_drop_rate : float
        Drop rate of attention.
    drop_path_rate : float
        Drop path rate.
    pre_norm : bool
        Whether to use pre_norm. Otherwise post_norm is used.
    global_pool : bool
        Whether to use global pooling to generate the image representation. Otherwise the cls_token is used.
    abs_pos : bool
        Whether to use absolute positional embeddings.
    qk_scale : float
        The scaler on score map in self-attention.
    rpe : bool
        Whether to use relative position encoding.
    """
    patch_embed: Incomplete
    patches_num: Incomplete
    global_pool: Incomplete
    cls_token: Incomplete
    pos_embed: Incomplete
    blocks: Incomplete
    norm: Incomplete
    head: Incomplete
    def __init__(self, search_embed_dim: Tuple[int, ...] = (192, 216, 240), search_mlp_ratio: Tuple[float, ...] = (3.0, 3.5, 4.0), search_num_heads: Tuple[int, ...] = (3, 4), search_depth: Tuple[int, ...] = (12, 13, 14), img_size: int = 224, patch_size: int = 16, in_chans: int = 3, num_classes: int = 1000, qkv_bias: bool = False, drop_rate: float = 0.0, attn_drop_rate: float = 0.0, drop_path_rate: float = 0.0, pre_norm: bool = True, global_pool: bool = False, abs_pos: bool = True, qk_scale: float | None = None, rpe: bool = True) -> None: ...
    @classmethod
    def get_extra_mutation_hooks(cls): ...
    @classmethod
    def preset(cls, name: str):
        """Get the model space config proposed in paper."""
    @classmethod
    def load_strategy_checkpoint(cls, name: str, download: bool = True, progress: bool = True):
        """
        Load the related strategy checkpoints.

        Parameters
        ----------
        name : str
            Search space size, must be one of {'random-one-shot-tiny', 'random-one-shot-small', 'random-one-shot-base'}.
        download : bool
            Whether to download supernet weights. Default is ``True``.
        progress : bool
            Whether to display the download progress. Default is ``True``.

        Returns
        -------
        BaseStrategy
            The loaded strategy.
        """
    @classmethod
    def load_searched_model(cls, name: str, pretrained: bool = False, download: bool = True, progress: bool = True) -> nn.Module:
        """
        Load the searched subnet model.

        Parameters
        ----------
        name : str
            Search space size, must be one of {'autoformer-tiny', 'autoformer-small', 'autoformer-base'}.
        pretrained : bool
            Whether initialized with pre-trained weights. Default is ``False``.
        download : bool
            Whether to download supernet weights. Default is ``True``.
        progress : bool
            Whether to display the download progress. Default is ``True``.

        Returns
        -------
        nn.Module
            The subnet model.
        """
    def forward(self, x): ...
