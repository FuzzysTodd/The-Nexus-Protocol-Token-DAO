import torch
from _typeshed import Incomplete
from torch.ao.quantization.utils import determine_qparams as determine_qparams, validate_qmin_qmax as validate_qmin_qmax
from torch.library import Library as Library, impl as impl
from typing import Tuple

quantized_decomposed_lib: Incomplete

def quantize_per_tensor(input: torch.Tensor, scale: float, zero_point: int, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor:
    """ Affine quantization for the Tensor using the same quantization parameters to map
    from floating point to quantized values

    Args:
       input (torch.Tensor): original float32 Tensor
       scale (float): quantization parameter for affine quantization
       zero_point (int): quantization parameter for affine quantization
       quant_min (int): minimum quantized value for output Tensor
       quant_max (int): maximum quantized value for output Tensor
       dtype (torch.dtype): requested dtype (e.g. torch.uint8) for output Tensor

    Returns:
       Tensor with requested dtype (e.g. torch.uint8), note the quantization parameters
       are not stored in the Tensor, we are storing them in function arguments instead
    """
def quantize_per_tensor_tensor(input: torch.Tensor, scale: torch.Tensor, zero_point: torch.Tensor, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor:
    """ Affine quantization for the Tensor using the same quantization parameters to map
    from floating point to quantized values
    Same as `quantize_per_tensor` but scale and zero_point are Scalar Tensor instead of
    scalar values
    """
def quantize_per_tensor_tensor_meta(input, scale, zero_point, quant_min, quant_max, dtype): ...
def dequantize_per_tensor(input: torch.Tensor, scale: float, zero_point: int, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor:
    """ Affine dequantization for the Tensor using the same quantization parameters to map
    from quantized values to floating point values

    Args:
       input (torch.Tensor): Tensor with dtype matching `dtype` argument,
       e.g. (`torch.uint8`), it is a per tensor quantized Tensor if combined with
       quantization parameters in the argument of this function (scale/zero_point)

       scale (float): quantization parameter for affine quantization

       zero_point (int): quantization parameter for affine quantization

       quant_min (int): minimum quantized value for input Tensor (not used in computation,
       reserved for pattern matching)

       quant_max (int): maximum quantized value for input Tensor (not used in computation,
       reserved for pattern matching)

       dtype (torch.dtype): dtype for input Tensor (not used in computation,
       reserved for pattern matching)

    Returns:
       dequantized float32 Tensor
    """
def dequantize_per_tensor_tensor(input: torch.Tensor, scale: torch.Tensor, zero_point: torch.Tensor, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor:
    """ Affine dequantization for the Tensor using the same quantization parameters to map
    from quantized values to floating point values
    Same as `dequantize_per_tensor` but scale and zero_point are Scalar Tensor instead of
    scalar values
    """
def dequantize_per_tensor_tensor_meta(input, scale, zero_point, quant_min, quant_max, dtype): ...
def choose_qparams_tensor(input: torch.Tensor, qmin: int, qmax: int, dtype: torch.dtype) -> Tuple[torch.Tensor, torch.Tensor]:
    """ Given an input Tensor, derive the per tensor affine quantization parameter
    (scale and zero_point) for target quantized Tensor from the Tensor

    Args:
       input (torch.Tensor): floating point input Tensor
       quant_min (int): minimum quantized value for target quantized Tensor
       quant_max (int): maximum quantized value for target quantized Tensor
       dtype (torch.dtype): dtype for target quantized Tensor

    Returns:
       scale (float): quantization parameter for the target quantized Tensor
       zero_point (int): quantization parameter for the target quantized Tensor
    """
def choose_qparams_symmetric_tensor(input: torch.Tensor, qmin: int, qmax: int, dtype: torch.dtype) -> Tuple[torch.Tensor, torch.Tensor]:
    """ Given an input Tensor, derive the per tensor affine quantization parameter
    (scale and zero_point) for target quantized Tensor from the Tensor

    Args:
       input (torch.Tensor): floating point input Tensor
       quant_min (int): minimum quantized value for target quantized Tensor
       quant_max (int): maximum quantized value for target quantized Tensor
       dtype (torch.dtype): dtype for target quantized Tensor

    Returns:
       scale (float): quantization parameter for the target quantized Tensor
       zero_point (int): quantization parameter for the target quantized Tensor
    """
def choose_qparams_tensor_meta(input: torch.Tensor, quant_min: int, quant_max: int, dtype: torch.dtype) -> Tuple[torch.Tensor, torch.Tensor]: ...
def choose_qparams_symmetric_tensor_meta(input: torch.Tensor, quant_min: int, quant_max: int, dtype: torch.dtype) -> Tuple[torch.Tensor, torch.Tensor]: ...
def quantize_per_channel(input: torch.Tensor, scales: torch.Tensor, zero_points: torch.Tensor, axis: int, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor:
    """ Affine per channel quantization for the Tensor using the same quantization
    parameters for each channel/axis to map from floating point to quantized values

    Args:
       input (torch.Tensor): original float32 Tensor
       scales (torch.Tensor): a list of scale quantization parameter for
       affine quantization, one per channel
       zero_point (torch.Tensor): a list of zero_point quantization parameter for
       affine quantization, one per channel
       quant_min (int): minimum quantized value for output Tensor
       quant_max (int): maximum quantized value for output Tensor
       dtype (torch.dtype): requested dtype (e.g. torch.uint8) for output Tensor

    Returns:
       Tensor with requested dtype (e.g. torch.uint8), note the quantization parameters
       are not stored in the Tensor, we are storing them in function arguments instead
    """
def quantize_per_channel_meta(input: torch.Tensor, scales: torch.Tensor, zero_points: torch.Tensor, axis: int, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor: ...
def dequantize_per_channel(input: torch.Tensor, scales: torch.Tensor, zero_points: torch.Tensor, axis: int, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor:
    """ Affine per channel dequantization for the Tensor using the same quantization
    parameters for each channel/axis to map from quantized values to floating point values

    Args:
       input (torch.Tensor): Tensor with dtype matching `dtype` argument,
       e.g. (`torch.uint8`), it is a per channel quantized Tensor if combined with
       quantization parameter in the argument of this function (scales/zero_points/axis)

       scales (torch.Tensor): a list of scale quantization parameter for
       affine quantization, one per channel

       zero_points (torch.Tensor): a list of zero_point quantization parameter for
       affine quantization, one per channel

       quant_min (int): minimum quantized value for output Tensor (not used in computation,
       reserved for pattern matching)

       quant_max (int): maximum quantized value for output Tensor (not used in computation,
       reserved for pattern matching)

       dtype (torch.dtype): requested dtype for output Tensor (not used in computation,
       reserved for pattern matching)

    Returns:
       dequantized float32 Tensor
    """
def dequantize_per_channel_meta(input: torch.Tensor, scales: torch.Tensor, zero_points: torch.Tensor, axis: int, quant_min: int, quant_max: int, dtype: torch.dtype) -> torch.Tensor: ...
