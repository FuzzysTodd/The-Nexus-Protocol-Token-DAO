from ...utils import logging as logging
from _typeshed import Incomplete
from torch import nn
from torch.autograd import Function

logger: Incomplete

class QuantEmbedding(nn.Module):
    """
    Quantized version of `torch.nn.Embedding`. Adds quantization-specific arguments on top of `torch.nn.Embedding`.

    Args:
        weight_bit (`int`, *optional*, defaults to `8`):
            Bitwidth for the quantized weight.
        momentum (`float`, *optional*, defaults to `0.95`):
            Momentum for updating the activation quantization range.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
    """
    num_: Incomplete
    dim: Incomplete
    padding_idx: Incomplete
    max_norm: Incomplete
    norm_type: Incomplete
    scale_grad_by_freq: Incomplete
    sparse: Incomplete
    weight: Incomplete
    weight_bit: Incomplete
    momentum: Incomplete
    quant_mode: Incomplete
    percentile_mode: bool
    weight_function: Incomplete
    def __init__(self, num_embeddings, embedding_dim, padding_idx: Incomplete | None = None, max_norm: Incomplete | None = None, norm_type: float = 2.0, scale_grad_by_freq: bool = False, sparse: bool = False, _weight: Incomplete | None = None, weight_bit: int = 8, momentum: float = 0.95, quant_mode: bool = False) -> None: ...
    weight_scaling_factor: Incomplete
    weight_integer: Incomplete
    def forward(self, x, positions: Incomplete | None = None, incremental_state: Incomplete | None = None): ...

class QuantAct(nn.Module):
    """
    Quantizes the given activation.

    Args:
        activation_bit (`int`):
            Bitwidth for the quantized activation.
        act_range_momentum (`float`, *optional*, defaults to `0.95`):
            Momentum for updating the activation quantization range.
        per_channel (`bool`, *optional*, defaults to `False`):
            Whether to or not use channel-wise quantization.
        channel_len (`int`, *optional*):
            Specify the channel length when set the *per_channel* True.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
    """
    activation_bit: Incomplete
    act_range_momentum: Incomplete
    quant_mode: Incomplete
    per_channel: Incomplete
    percentile: bool
    act_function: Incomplete
    def __init__(self, activation_bit, act_range_momentum: float = 0.95, per_channel: bool = False, channel_len: Incomplete | None = None, quant_mode: bool = False) -> None: ...
    x_min: Incomplete
    x_max: Incomplete
    act_scaling_factor: Incomplete
    def forward(self, x, pre_act_scaling_factor: Incomplete | None = None, identity: Incomplete | None = None, identity_scaling_factor: Incomplete | None = None, specified_min: Incomplete | None = None, specified_max: Incomplete | None = None): ...

class QuantLinear(nn.Module):
    """
    Quantized version of `torch.nn.Linear`. Adds quantization-specific arguments on top of `torch.nn.Linear`.

    Args:
        weight_bit (`int`, *optional*, defaults to `8`):
            Bitwidth for the quantized weight.
        bias_bit (`int`, *optional*, defaults to `32`):
            Bitwidth for the quantized bias.
        per_channel (`bool`, *optional*, defaults to `False`):
            Whether or not to use channel-wise quantization.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
    """
    in_features: Incomplete
    out_features: Incomplete
    weight: Incomplete
    bias: Incomplete
    weight_bit: Incomplete
    quant_mode: Incomplete
    per_channel: Incomplete
    bias_bit: Incomplete
    percentile_mode: bool
    weight_function: Incomplete
    def __init__(self, in_features, out_features, bias: bool = True, weight_bit: int = 8, bias_bit: int = 32, per_channel: bool = False, quant_mode: bool = False) -> None: ...
    fc_scaling_factor: Incomplete
    weight_integer: Incomplete
    bias_integer: Incomplete
    def forward(self, x, prev_act_scaling_factor: Incomplete | None = None): ...

class IntGELU(nn.Module):
    '''
    Quantized version of `torch.nn.GELU`. Adds quantization-specific arguments on top of `torch.nn.GELU`.

    Args:
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
        force_dequant (`str`, *optional*, defaults to `"none"`):
            Force dequantize the layer if either "gelu" or "nonlinear" is given.
    '''
    quant_mode: Incomplete
    activation_fn: Incomplete
    k: float
    const: int
    coeff: Incomplete
    def __init__(self, quant_mode: bool = True, force_dequant: str = 'none') -> None: ...
    def int_erf(self, x_int, scaling_factor): ...
    def forward(self, x, scaling_factor: Incomplete | None = None): ...

class IntSoftmax(nn.Module):
    '''
    Quantized version of `torch.nn.Softmax`. Adds quantization-specific arguments on top of `torch.nn.Softmax`.

    Args:
        output_bit (`int`):
            Bitwidth for the layer output activation.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
        force_dequant (`str`, *optional*, defaults to `"none"`):
            Force dequantize the layer if either "softmax" or "nonlinear" is given.
    '''
    output_bit: Incomplete
    max_bit: int
    quant_mode: Incomplete
    act: Incomplete
    x0: float
    const: int
    coef: Incomplete
    def __init__(self, output_bit, quant_mode: bool = False, force_dequant: str = 'none') -> None: ...
    def int_polynomial(self, x_int, scaling_factor): ...
    def int_exp(self, x_int, scaling_factor): ...
    def forward(self, x, scaling_factor): ...

class IntLayerNorm(nn.Module):
    '''
    Quantized version of `torch.nn.LayerNorm`. Adds quantization-specific arguments on top of `torch.nn.LayerNorm`.

    Args:
        output_bit (`int`, *optional*, defaults to `8`):
            Bitwidth for the layer output activation.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
        force_dequant (`str`, *optional*, defaults to `"none"`):
            Force dequantize the layer if either "layernorm" or "nonlinear" is given.
    '''
    normalized_shape: Incomplete
    eps: Incomplete
    weight: Incomplete
    bias: Incomplete
    quant_mode: Incomplete
    output_bit: Incomplete
    max_bit: int
    dim_sqrt: Incomplete
    activation: Incomplete
    def __init__(self, normalized_shape, eps, output_bit: int = 8, quant_mode: bool = False, force_dequant: str = 'none') -> None: ...
    shift: Incomplete
    def set_shift(self, y_int) -> None: ...
    def overflow_fallback(self, y_int):
        """
        This fallback function is called when overflow is detected during training time, and adjusts the `self.shift`
        to avoid overflow in the subsequent runs.
        """
    def forward(self, x, scaling_factor: Incomplete | None = None): ...

def get_percentile_min_max(input, lower_percentile, upper_percentile, output_tensor: bool = False):
    """
    Calculate the percentile max and min values in a given tensor

    Args:
        input (`torch.Tensor`):
            The target tensor to calculate percentile max and min.
        lower_percentile (`float`):
            If 0.1, means we return the value of the smallest 0.1% value in the tensor as percentile min.
        upper_percentile (`float`):
            If 99.9, means we return the value of the largest 0.1% value in the tensor as percentile max.
        output_tensor (`bool`, *optional*, defaults to `False`):
            If True, this function returns tensors, otherwise it returns values.

    Returns:
        `Tuple(torch.Tensor, torch.Tensor)`: Percentile min and max value of *input*
    """
def linear_quantize(input, scale, zero_point, inplace: bool = False):
    """
    Quantize single-precision input tensor to integers with the given scaling factor and zeropoint.

    Args:
        input (`torch.Tensor`):
            Single-precision input tensor to be quantized.
        scale (`torch.Tensor`):
            Scaling factor for quantization.
        zero_pint (`torch.Tensor`):
            Shift for quantization.
        inplace (`bool`, *optional*, defaults to `False`):
            Whether to compute inplace or not.

    Returns:
        `torch.Tensor`: Linearly quantized value of *input* according to *scale* and *zero_point*.
    """
def symmetric_linear_quantization_params(num_bits, saturation_min, saturation_max, per_channel: bool = False):
    """
    Compute the scaling factor with the given quantization range for symmetric quantization.

    Args:
        saturation_min (`torch.Tensor`):
            Lower bound for quantization range.
        saturation_max (`torch.Tensor`):
            Upper bound for quantization range.
        per_channel (`bool`, *optional*, defaults to `False`):
            Whether to or not use channel-wise quantization.

    Returns:
        `torch.Tensor`: Scaling factor that linearly quantizes the given range between *saturation_min* and
        *saturation_max*.
    """

class SymmetricQuantFunction(Function):
    """
    Class to quantize the given floating-point values using symmetric quantization with given range and bitwidth.
    """
    @staticmethod
    def forward(ctx, x, k, percentile_mode, scale):
        """
        Args:
            x (`torch.Tensor`):
                Floating point tensor to be quantized.
            k (`int`):
                Quantization bitwidth.
            percentile_mode (`bool`):
                Whether or not to use percentile calibration.
            scale (`torch.Tensor`):
                Pre-calculated scaling factor for *x*. Note that the current implementation of SymmetricQuantFunction
                requires pre-calculated scaling factor.

        Returns:
            `torch.Tensor`: Symmetric-quantized value of *input*.
        """
    @staticmethod
    def backward(ctx, grad_output): ...

class floor_ste(Function):
    """
    Straight-through Estimator(STE) for torch.floor()
    """
    @staticmethod
    def forward(ctx, x): ...
    @staticmethod
    def backward(ctx, grad_output): ...

class round_ste(Function):
    """
    Straight-through Estimator(STE) for torch.round()
    """
    @staticmethod
    def forward(ctx, x): ...
    @staticmethod
    def backward(ctx, grad_output): ...

def batch_frexp(inputs, max_bit: int = 31):
    """
    Decompose the scaling factor into mantissa and twos exponent.

    Args:
        scaling_factor (`torch.Tensor`):
            Target scaling factor to decompose.

    Returns:
        ``Tuple(torch.Tensor, torch.Tensor)`: mantisa and exponent
    """

class FixedPointMul(Function):
    """
    Function to perform fixed-point arithmetic that can match integer arithmetic on hardware.

    Args:
        pre_act (`torch.Tensor`):
            Input tensor.
        pre_act_scaling_factor (`torch.Tensor`):
            Scaling factor of the input tensor *pre_act*.
        bit_num (`int`):
            Quantization bitwidth.
        z_scaling_factor (`torch.Tensor`):
            Scaling factor of the output tensor.
        identity (`torch.Tensor`, *optional*):
            Identity tensor, if exists.
        identity_scaling_factor (`torch.Tensor`, *optional*):
            Scaling factor of the identity tensor *identity*, if exists.

    Returns:
        `torch.Tensor`: Output tensor(*pre_act* if *identity* is not given, otherwise the addition of *pre_act* and
        *identity*), whose scale is rescaled to *z_scaling_factor*.
    """
    @staticmethod
    def forward(ctx, pre_act, pre_act_scaling_factor, bit_num, z_scaling_factor, identity: Incomplete | None = None, identity_scaling_factor: Incomplete | None = None): ...
    @staticmethod
    def backward(ctx, grad_output): ...
