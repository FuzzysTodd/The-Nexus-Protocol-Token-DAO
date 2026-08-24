from _typeshed import Incomplete
from argparse import ArgumentParser

class AttentionMaskFormat:
    MaskIndexEnd: int
    MaskIndexEndAndStart: int
    AttentionMask: int
    NoMask: int

class FusionOptions:
    """Options of fusion in graph optimization"""
    enable_gelu: bool
    enable_layer_norm: bool
    enable_attention: bool
    use_multi_head_attention: bool
    disable_multi_head_attention_bias: bool
    enable_skip_layer_norm: bool
    enable_embed_layer_norm: bool
    enable_bias_skip_layer_norm: bool
    enable_bias_gelu: bool
    enable_gelu_approximation: bool
    enable_qordered_matmul: bool
    enable_shape_inference: bool
    enable_gemm_fast_gelu: bool
    group_norm_channels_last: bool
    attention_mask_format: Incomplete
    enable_nhwc_conv: bool
    enable_group_norm: bool
    enable_bias_splitgelu: bool
    enable_packed_qkv: bool
    enable_packed_kv: bool
    enable_bias_add: bool
    def __init__(self, model_type) -> None: ...
    def use_raw_attention_mask(self, use_raw_mask: bool = True) -> None: ...
    def disable_attention_mask(self) -> None: ...
    @staticmethod
    def parse(args): ...
    @staticmethod
    def add_arguments(parser: ArgumentParser): ...
