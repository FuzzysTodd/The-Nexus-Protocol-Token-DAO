import abc
import torch
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from torch.nn import Module
from typing import Any, Tuple

__all__ = ['FakeQuantizeBase', 'FakeQuantize', 'FixedQParamsFakeQuantize', 'FusedMovingAvgObsFakeQuantize', 'disable_fake_quant', 'disable_observer', 'enable_fake_quant', 'enable_observer', 'default_fake_quant', 'default_weight_fake_quant', 'default_dynamic_fake_quant', 'default_fixed_qparams_range_neg1to1_fake_quant', 'default_fixed_qparams_range_0to1_fake_quant', 'default_symmetric_fixed_qparams_fake_quant', 'default_affine_fixed_qparams_fake_quant', 'default_per_channel_weight_fake_quant', 'default_embedding_fake_quant', 'default_embedding_fake_quant_4bit', 'default_histogram_fake_quant', 'default_fused_act_fake_quant', 'default_fused_wt_fake_quant', 'default_fused_per_channel_wt_fake_quant', 'fused_wt_fake_quant_range_neg_127_to_127', 'fused_per_channel_wt_fake_quant_range_neg_127_to_127']

class FakeQuantizeBase(ABC, Module, metaclass=abc.ABCMeta):
    """ Base fake quantize module
    Any fake quantize implementation should derive from this class.

    Concrete fake quantize module should follow the same API. In forward, they will update
    the statistics of the observed Tensor and fake quantize the input. They should also provide a
    `calculate_qparams` function that computes the quantization parameters given
    the collected statistics.

    """
    fake_quant_enabled: torch.Tensor
    observer_enabled: torch.Tensor
    def __init__(self) -> None: ...
    @abstractmethod
    def forward(self, x): ...
    @abstractmethod
    def calculate_qparams(self, **kwargs): ...
    def enable_fake_quant(self, enabled: bool = True) -> None: ...
    def disable_fake_quant(self) -> None: ...
    def enable_observer(self, enabled: bool = True) -> None: ...
    def disable_observer(self) -> None: ...
    @classmethod
    def with_args(cls, **kwargs): ...

class FakeQuantize(FakeQuantizeBase):
    """ Simulate the quantize and dequantize operations in training time.
    The output of this module is given by::

        x_out = (
          clamp(round(x/scale + zero_point), quant_min, quant_max) - zero_point
        ) * scale

    * :attr:`scale` defines the scale factor used for quantization.

    * :attr:`zero_point` specifies the quantized value to which 0 in floating point maps to

    * :attr:`fake_quant_enabled` controls the application of fake quantization on tensors, note that
      statistics can still be updated.

    * :attr:`observer_enabled` controls statistics collection on tensors

    * :attr:`dtype` specifies the quantized dtype that is being emulated with fake-quantization,
        allowable values are torch.qint8 and torch.quint8.

    Args:

        observer (module): Module for observing statistics on input tensors and calculating scale
          and zero-point.
        observer_kwargs (optional): Arguments for the observer module

    Attributes:

        activation_post_process (Module): User provided module that collects statistics on the input tensor and
          provides a method to calculate scale and zero-point.

    """
    scale: torch.Tensor
    zero_point: torch.Tensor
    activation_post_process: Incomplete
    quant_min: Incomplete
    quant_max: Incomplete
    dtype: Incomplete
    qscheme: Incomplete
    ch_axis: Incomplete
    is_per_channel: Incomplete
    def __init__(self, observer=..., quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, **observer_kwargs) -> None: ...
    def calculate_qparams(self): ...
    def forward(self, X): ...
    def extra_repr(self): ...

class FixedQParamsFakeQuantize(FakeQuantize):
    """ Simulate quantize and dequantize with fixed quantization
    parameters in training time. Only per tensor quantization
    is supported.
    """
    scale: Incomplete
    zero_point: Incomplete
    def __init__(self, observer) -> None: ...
    def calculate_qparams(self): ...
    def extra_repr(self): ...

class FusedMovingAvgObsFakeQuantize(FakeQuantize):
    """Fused module that is used to observe the input tensor (compute min/max), compute
    scale/zero_point and fake_quantize the tensor.
    This module uses calculation similar MovingAverageMinMaxObserver for the inputs,
    to compute the min/max values in order to compute the scale/zero_point.
    The qscheme input in the observer is used to differentiate between symmetric/affine
    quantization scheme.

    The output of this module is given by
    x_out = (clamp(round(x/scale + zero_point), quant_min, quant_max)-zero_point)*scale

    Similar to :class:`~torch.ao.quantization.FakeQuantize`, and accepts the same attributes as the
    base class.

    """
    is_symmetric_quant: Incomplete
    def __init__(self, observer: Any = ..., quant_min: int = 0, quant_max: int = 255, **observer_kwargs: Any) -> None: ...
    def calculate_qparams(self) -> Tuple[torch.Tensor, torch.Tensor]: ...
    def extra_repr(self) -> str: ...
    def forward(self, X: torch.Tensor) -> torch.Tensor: ...

default_fake_quant: Incomplete
default_weight_fake_quant: Incomplete
default_dynamic_fake_quant: Incomplete
default_fixed_qparams_range_neg1to1_fake_quant: Incomplete
default_fixed_qparams_range_0to1_fake_quant: Incomplete
default_symmetric_fixed_qparams_fake_quant = default_fixed_qparams_range_neg1to1_fake_quant
default_affine_fixed_qparams_fake_quant = default_fixed_qparams_range_0to1_fake_quant
default_per_channel_weight_fake_quant: Incomplete
default_embedding_fake_quant: Incomplete
default_embedding_fake_quant_4bit: Incomplete
default_histogram_fake_quant: Incomplete
default_fused_act_fake_quant: Incomplete
default_fused_wt_fake_quant: Incomplete
default_fused_per_channel_wt_fake_quant: Incomplete
fused_wt_fake_quant_range_neg_127_to_127: Incomplete
fused_per_channel_wt_fake_quant_range_neg_127_to_127: Incomplete

def disable_fake_quant(mod) -> None:
    """
    Disable fake quantization for this module, if applicable. Example usage::

      # model is any PyTorch model
      model.apply(torch.ao.quantization.disable_fake_quant)

    """
def enable_fake_quant(mod) -> None:
    """
    Enable fake quantization for this module, if applicable. Example usage::

      # model is any PyTorch model
      model.apply(torch.ao.quantization.enable_fake_quant)

    """
def disable_observer(mod) -> None:
    """
    Disable observation for this module, if applicable. Example usage::

      # model is any PyTorch model
      model.apply(torch.ao.quantization.disable_observer)

    """
def enable_observer(mod) -> None:
    """
    Enable observation for this module, if applicable. Example usage::

      # model is any PyTorch model
      model.apply(torch.ao.quantization.enable_observer)

    """
