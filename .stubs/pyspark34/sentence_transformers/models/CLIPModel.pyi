import torch
from _typeshed import Incomplete
from torch import nn
from typing import List, Tuple

__all__ = ['available_models', 'load', 'tokenize']

class CLIPModel(nn.Module):
    tokenizer: Incomplete
    def __init__(self, tokenizer_path: str, model_name: str = 'ViT-B/32') -> None: ...
    def tokenize(self, texts: List[str] | List[Tuple[str, str]]): ...
    def forward(self, features): ...
    def save(self, output_path: str): ...
    @staticmethod
    def load(input_path: str): ...

def available_models() -> List[str]:
    """Returns the names of available CLIP models"""
def load(name: str, device: str | torch.device = ..., jit: bool = False):
    """Load a CLIP model

    Parameters
    ----------
    name : str
        A model name listed by `clip.available_models()`, or the path to a model checkpoint containing the state_dict

    device : Union[str, torch.device]
        The device to put the loaded model

    jit : bool
        Whether to load the optimized JIT model (default) or more hackable non-JIT model.

    Returns
    -------
    model : torch.nn.Module
        The CLIP model

    preprocess : Callable[[PIL.Image], torch.Tensor]
        A torchvision transform that converts a PIL image into a tensor that the returned model can take as its input
    """
def tokenize(tokenizer, texts: str | List[str], context_length: int = 77) -> torch.LongTensor:
    """
    Returns the tokenized representation of given input string(s)

    Parameters
    ----------
    texts : Union[str, List[str]]
        An input string or a list of input strings to tokenize

    context_length : int
        The context length to use; all CLIP models use 77 as the context length

    Returns
    -------
    A two-dimensional tensor containing the resulting tokens, shape = [number of input strings, context_length]
    """

class Bottleneck(nn.Module):
    expansion: int
    conv1: Incomplete
    bn1: Incomplete
    conv2: Incomplete
    bn2: Incomplete
    avgpool: Incomplete
    conv3: Incomplete
    bn3: Incomplete
    relu: Incomplete
    downsample: Incomplete
    stride: Incomplete
    def __init__(self, inplanes, planes, stride: int = 1) -> None: ...
    def forward(self, x: torch.Tensor): ...

class AttentionPool2d(nn.Module):
    positional_embedding: Incomplete
    k_proj: Incomplete
    q_proj: Incomplete
    v_proj: Incomplete
    c_proj: Incomplete
    num_heads: Incomplete
    def __init__(self, spacial_dim: int, embed_dim: int, num_heads: int, output_dim: int = None) -> None: ...
    def forward(self, x): ...

class ModifiedResNet(nn.Module):
    '''
    A ResNet class that is similar to torchvision\'s but contains the following changes:
    - There are now 3 "stem" convolutions as opposed to 1, with an average pool instead of a max pool.
    - Performs anti-aliasing strided convolutions, where an avgpool is prepended to convolutions with stride > 1
    - The final pooling layer is a QKV attention instead of an average pool
    '''
    output_dim: Incomplete
    input_resolution: Incomplete
    conv1: Incomplete
    bn1: Incomplete
    conv2: Incomplete
    bn2: Incomplete
    conv3: Incomplete
    bn3: Incomplete
    avgpool: Incomplete
    relu: Incomplete
    layer1: Incomplete
    layer2: Incomplete
    layer3: Incomplete
    layer4: Incomplete
    attnpool: Incomplete
    def __init__(self, layers, output_dim, heads, input_resolution: int = 224, width: int = 64) -> None: ...
    def forward(self, x): ...

class LayerNorm(nn.LayerNorm):
    """Subclass torch's LayerNorm to handle fp16."""
    def forward(self, x: torch.Tensor): ...

class QuickGELU(nn.Module):
    def forward(self, x: torch.Tensor): ...

class ResidualAttentionBlock(nn.Module):
    attn: Incomplete
    ln_1: Incomplete
    mlp: Incomplete
    ln_2: Incomplete
    attn_mask: Incomplete
    def __init__(self, d_model: int, n_head: int, attn_mask: torch.Tensor = None) -> None: ...
    def attention(self, x: torch.Tensor): ...
    def forward(self, x: torch.Tensor): ...

class Transformer(nn.Module):
    width: Incomplete
    layers: Incomplete
    resblocks: Incomplete
    def __init__(self, width: int, layers: int, heads: int, attn_mask: torch.Tensor = None) -> None: ...
    def forward(self, x: torch.Tensor): ...

class VisualTransformer(nn.Module):
    input_resolution: Incomplete
    output_dim: Incomplete
    conv1: Incomplete
    class_embedding: Incomplete
    positional_embedding: Incomplete
    ln_pre: Incomplete
    transformer: Incomplete
    ln_post: Incomplete
    proj: Incomplete
    def __init__(self, input_resolution: int, patch_size: int, width: int, layers: int, heads: int, output_dim: int) -> None: ...
    def forward(self, x: torch.Tensor): ...

class CLIP(nn.Module):
    context_length: Incomplete
    visual: Incomplete
    transformer: Incomplete
    vocab_size: Incomplete
    token_embedding: Incomplete
    positional_embedding: Incomplete
    ln_final: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def __init__(self, embed_dim: int, image_resolution: int, vision_layers: Tuple[int, int, int, int] | int, vision_width: int, vision_patch_size: int, context_length: int, vocab_size: int, transformer_width: int, transformer_heads: int, transformer_layers: int) -> None: ...
    def initialize_parameters(self) -> None: ...
    def build_attention_mask(self): ...
    @property
    def dtype(self): ...
    def encode_image(self, image): ...
    def encode_text(self, text): ...
    def forward(self, image, text): ...

class SimpleTokenizer:
    byte_encoder: Incomplete
    byte_decoder: Incomplete
    tokenizer_data: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    pat: Incomplete
    def __init__(self, bpe_path: str) -> None: ...
    def save(self, output_path): ...
    def bpe(self, token): ...
    def encode(self, text): ...
    def decode(self, tokens): ...
