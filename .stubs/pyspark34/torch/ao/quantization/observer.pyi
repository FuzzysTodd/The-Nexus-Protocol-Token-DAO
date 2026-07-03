import abc
import torch
import torch.nn as nn
from _typeshed import Incomplete
from abc import abstractmethod

__all__ = ['default_affine_fixed_qparams_observer', 'default_debug_observer', 'default_dynamic_quant_observer', 'default_fixed_qparams_range_0to1_observer', 'default_fixed_qparams_range_neg1to1_observer', 'default_float_qparams_observer', 'default_float_qparams_observer_4bit', 'default_histogram_observer', 'default_observer', 'default_per_channel_weight_observer', 'default_placeholder_observer', 'default_reuse_input_observer', 'default_symmetric_fixed_qparams_observer', 'default_weight_observer', 'get_observer_state_dict', 'load_observer_state_dict', 'per_channel_weight_observer_range_neg_127_to_127', 'weight_observer_range_neg_127_to_127', 'FixedQParamsObserver', 'HistogramObserver', 'MinMaxObserver', 'MovingAverageMinMaxObserver', 'MovingAveragePerChannelMinMaxObserver', 'NoopObserver', 'ObserverBase', 'PerChannelMinMaxObserver', 'PlaceholderObserver', 'RecordingObserver', 'ReuseInputObserver', 'UniformQuantizationObserverBase']

class _PartialWrapper:
    p: Incomplete
    callable_args: Incomplete
    def __init__(self, p) -> None: ...
    def __call__(self, *args, **keywords): ...
    def with_args(self, **kwargs): ...
    def with_callable_args(self, **kwargs): ...

class ObserverBase(ABC, nn.Module, metaclass=abc.ABCMeta):
    """Base observer Module.
    Any observer implementation should derive from this class.

    Concrete observers should follow the same API. In forward, they will update
    the statistics of the observed Tensor. And they should provide a
    `calculate_qparams` function that computes the quantization parameters given
    the collected statistics.

    Args:
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec.
    """
    dtype: Incomplete
    def __init__(self, dtype) -> None: ...
    @abstractmethod
    def forward(self, x): ...
    @abstractmethod
    def calculate_qparams(self, **kwargs): ...
    with_args: Incomplete
    with_callable_args: Incomplete

class UniformQuantizationObserverBase(ObserverBase, metaclass=abc.ABCMeta):
    """Common base for all observers using uniform quantization to calculate
    scale and zero_point.

    Args:
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec.
        qscheme: Quantization scheme to be used.
        reduce_range: Reduces the range of the quantized data type by 1 bit.
                      This is sometimes required to avoid instruction overflow.
        quant_min: Minimum quantization value. If unspecified, it will follow the 8-bit setup.
        quant_max: Maximum quantization value. If unspecified, it will follow the 8-bit setup.
        eps: Epsilon value for float32, Defaults to `torch.finfo(torch.float32).eps`.

    .. warning::

        :attr:`dtype` can only take ``torch.qint8`` or ``torch.quint8``.

    .. warning::

        :attr:`qscheme` can only take one of the following options:

        - ``torch.per_tensor_affine``
        - ``torch.per_tensor_symmetric``
        - ``torch.per_channel_affine``
        - ``torch.per_channel_symmetric``
    """
    eps: torch.Tensor
    qscheme: Incomplete
    reduce_range: Incomplete
    has_customized_qrange: Incomplete
    def __init__(self, dtype=..., qscheme=..., reduce_range: bool = False, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, factory_kwargs: Incomplete | None = None, eps=...) -> None: ...
    def reset_min_max_vals(self) -> None: ...

class MinMaxObserver(UniformQuantizationObserverBase):
    """Observer module for computing the quantization parameters based on the
    running min and max values.

    This observer uses the tensor min/max statistics to compute the quantization
    parameters. The module records the running minimum and maximum of incoming
    tensors, and uses this statistic to compute the quantization parameters.

    Args:
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec.
        qscheme: Quantization scheme to be used
        reduce_range: Reduces the range of the quantized data type by 1 bit
        quant_min: Minimum quantization value. If unspecified, it will follow the 8-bit setup.
        quant_max: Maximum quantization value. If unspecified, it will follow the 8-bit setup.
        eps: Epsilon value for float32, Defaults to `torch.finfo(torch.float32).eps`.

    Given running min/max as :math:`x_\\text{min}` and :math:`x_\\text{max}`,
    scale :math:`s` and zero point :math:`z` are computed as:

    The running minimum/maximum :math:`x_\\text{min/max}` is computed as:

    .. math::

        \\begin{array}{ll}
        x_\\text{min} &= \\begin{cases}
            \\min(X) & \\text{if~}x_\\text{min} = \\text{None} \\\\\n            \\min\\left(x_\\text{min}, \\min(X)\\right) & \\text{otherwise}
        \\end{cases}\\\\\n        x_\\text{max} &= \\begin{cases}
            \\max(X) & \\text{if~}x_\\text{max} = \\text{None} \\\\\n            \\max\\left(x_\\text{max}, \\max(X)\\right) & \\text{otherwise}
        \\end{cases}\\\\\n        \\end{array}

    where :math:`X` is the observed tensor.

    The scale :math:`s` and zero point :math:`z` are then computed as:

    .. math::

        \\begin{aligned}
            \\text{if Symmetric:}&\\\\\n            &s = 2 \\max(|x_\\text{min}|, x_\\text{max}) /
                \\left( Q_\\text{max} - Q_\\text{min} \\right) \\\\\n            &z = \\begin{cases}
                0 & \\text{if dtype is qint8} \\\\\n                128 & \\text{otherwise}
            \\end{cases}\\\\\n            \\text{Otherwise:}&\\\\\n                &s = \\left( x_\\text{max} - x_\\text{min}  \\right ) /
                    \\left( Q_\\text{max} - Q_\\text{min} \\right ) \\\\\n                &z = Q_\\text{min} - \\text{round}(x_\\text{min} / s)
        \\end{aligned}

    where :math:`Q_\\text{min}` and :math:`Q_\\text{max}` are the minimum and
    maximum of the quantized data type.

    .. warning:: :attr:`dtype` can only take ``torch.qint8`` or ``torch.quint8``.

    .. note:: If the running minimum equals to the running maximum, the scale
              and zero_point are set to 1.0 and 0.
    """
    min_val: torch.Tensor
    max_val: torch.Tensor
    def __init__(self, dtype=..., qscheme=..., reduce_range: bool = False, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, factory_kwargs: Incomplete | None = None, eps=...) -> None: ...
    def forward(self, x_orig):
        """Records the running minimum and maximum of ``x``."""
    def calculate_qparams(self):
        """Calculates the quantization parameters."""
    def extra_repr(self): ...
    def reset_min_max_vals(self) -> None:
        """Resets the min/max values."""

class MovingAverageMinMaxObserver(MinMaxObserver):
    """Observer module for computing the quantization parameters based on the
    moving average of the min and max values.

    This observer computes the quantization parameters based on the moving
    averages of minimums and maximums of the incoming tensors. The module
    records the average minimum and maximum of incoming tensors, and uses this
    statistic to compute the quantization parameters.

    Args:
        averaging_constant: Averaging constant for min/max.
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec.
        qscheme: Quantization scheme to be used
        reduce_range: Reduces the range of the quantized data type by 1 bit
        quant_min: Minimum quantization value. If unspecified, it will follow the 8-bit setup.
        quant_max: Maximum quantization value. If unspecified, it will follow the 8-bit setup.
        eps: Epsilon value for float32, Defaults to `torch.finfo(torch.float32).eps`.

    The moving average min/max is computed as follows

    .. math::

        \\begin{array}{ll}
                x_\\text{min} = \\begin{cases}
                    \\min(X) & \\text{if~}x_\\text{min} = \\text{None} \\\\\n                    (1 - c) x_\\text{min} + c \\min(X) & \\text{otherwise}
                \\end{cases}\\\\\n                x_\\text{max} = \\begin{cases}
                    \\max(X) & \\text{if~}x_\\text{max} = \\text{None} \\\\\n                    (1 - c) x_\\text{max} + c \\max(X) & \\text{otherwise}
                \\end{cases}\\\\\n        \\end{array}

    where :math:`x_\\text{min/max}` is the running average min/max, :math:`X` is
    is the incoming tensor, and :math:`c` is the ``averaging_constant``.

    The scale and zero point are then computed as in
    :class:`~torch.ao.quantization.observer.MinMaxObserver`.

    .. note:: Only works with ``torch.per_tensor_affine`` quantization scheme.

    .. note:: If the running minimum equals to the running maximum, the scale
              and zero_point are set to 1.0 and 0.
    """
    averaging_constant: Incomplete
    def __init__(self, averaging_constant: float = 0.01, dtype=..., qscheme=..., reduce_range: bool = False, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, eps=..., **kwargs) -> None: ...
    def forward(self, x_orig): ...

class PerChannelMinMaxObserver(UniformQuantizationObserverBase):
    """Observer module for computing the quantization parameters based on the
    running per channel min and max values.

    This observer uses the tensor min/max statistics to compute the per channel
    quantization parameters. The module records the running minimum and maximum
    of incoming tensors, and uses this statistic to compute the quantization
    parameters.

    Args:
        ch_axis: Channel axis
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec.
        qscheme: Quantization scheme to be used
        reduce_range: Reduces the range of the quantized data type by 1 bit
        quant_min: Minimum quantization value. If unspecified, it will follow the 8-bit setup.
        quant_max: Maximum quantization value. If unspecified, it will follow the 8-bit setup.
        eps: Epsilon value for float32, Defaults to `torch.finfo(torch.float32).eps`.

    The quantization parameters are computed the same way as in
    :class:`~torch.ao.quantization.observer.MinMaxObserver`, with the difference
    that the running min/max values are stored per channel.
    Scales and zero points are thus computed per channel as well.

    .. note:: If the running minimum equals to the running maximum, the scales
              and zero_points are set to 1.0 and 0.
    """
    min_val: torch.Tensor
    max_val: torch.Tensor
    ch_axis: Incomplete
    def __init__(self, ch_axis: int = 0, dtype=..., qscheme=..., reduce_range: bool = False, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, factory_kwargs: Incomplete | None = None, eps=...) -> None: ...
    def forward(self, x_orig): ...
    def calculate_qparams(self): ...
    def extra_repr(self): ...
    def reset_min_max_vals(self) -> None:
        """Resets the min/max values."""

class MovingAveragePerChannelMinMaxObserver(PerChannelMinMaxObserver):
    """Observer module for computing the quantization parameters based on the
    running per channel min and max values.

    This observer uses the tensor min/max statistics to compute the per channel
    quantization parameters. The module records the running minimum and maximum
    of incoming tensors, and uses this statistic to compute the quantization
    parameters.

    Args:
        averaging_constant: Averaging constant for min/max.
        ch_axis: Channel axis
        dtype: Quantized data type
        qscheme: Quantization scheme to be used
        reduce_range: Reduces the range of the quantized data type by 1 bit
        quant_min: Minimum quantization value. If unspecified, it will follow the 8-bit setup.
        quant_max: Maximum quantization value. If unspecified, it will follow the 8-bit setup.
        eps: Epsilon value for float32, Defaults to `torch.finfo(torch.float32).eps`.

    The quantization parameters are computed the same way as in
    :class:`~torch.ao.quantization.observer.MovingAverageMinMaxObserver`, with the
    difference that the running min/max values are stored per channel.
    Scales and zero points are thus computed per channel as well.

    .. note:: If the running minimum equals to the running maximum, the scales
              and zero_points are set to 1.0 and 0.
    """
    averaging_constant: Incomplete
    def __init__(self, averaging_constant: float = 0.01, ch_axis: int = 0, dtype=..., qscheme=..., reduce_range: bool = False, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, eps=..., **kwargs) -> None: ...
    def forward(self, x_orig): ...

class HistogramObserver(UniformQuantizationObserverBase):
    """
    The module records the running histogram of tensor values along with
    min/max values. ``calculate_qparams`` will calculate scale and zero_point.

    Args:
        bins: Number of bins to use for the histogram
        upsample_rate: Factor by which the histograms are upsampled, this is
                       used to interpolate histograms with varying ranges across observations
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec
        qscheme: Quantization scheme to be used
        reduce_range: Reduces the range of the quantized data type by 1 bit
        eps: Epsilon value for float32, Defaults to `torch.finfo(torch.float32).eps`.

    The scale and zero point are computed as follows:

    1. Create the histogram of the incoming inputs.
        The histogram is computed continuously, and the ranges per bin change
        with every new tensor observed.
    2. Search the distribution in the histogram for optimal min/max values.
        The search for the min/max values ensures the minimization of the
        quantization error with respect to the floating point model.
    3. Compute the scale and zero point the same way as in the
        :class:`~torch.ao.quantization.MinMaxObserver`
    """
    histogram: torch.Tensor
    min_val: torch.Tensor
    max_val: torch.Tensor
    bins: Incomplete
    dst_nbins: Incomplete
    upsample_rate: Incomplete
    def __init__(self, bins: int = 2048, upsample_rate: int = 128, dtype: torch.dtype = ..., qscheme=..., reduce_range: bool = False, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, factory_kwargs: Incomplete | None = None, eps=...) -> None: ...
    def forward(self, x_orig: torch.Tensor) -> torch.Tensor: ...
    def calculate_qparams(self): ...
    def extra_repr(self): ...

class FixedQParamsObserver(ObserverBase):
    """
    Observer that simulates quantize and dequantize with fixed
    quantization parameters in training time. Only per tensor
    quantization is supported.

    Args:
        `scale` (float): fixed scale for the observer
        `zero_point` (int): fixed zero point for the observer
        `dtype`, `qscheme`, `quant_min`, `quant_max`
    """
    scale: torch.Tensor
    zero_point: torch.Tensor
    quant_min: Incomplete
    quant_max: Incomplete
    dtype: Incomplete
    qscheme: Incomplete
    def __init__(self, scale, zero_point, dtype=..., qscheme=..., quant_min: int = 0, quant_max: int = 255) -> None: ...
    def forward(self, X): ...
    def calculate_qparams(self): ...

class PlaceholderObserver(ObserverBase):
    """
    Observer that doesn't do anything and just passes its configuration to the
    quantized module's ``.from_float()``.

    Can be used for quantization to float16 which doesn't require determining
    ranges.

    Args:
        dtype: dtype argument to the `quantize` node needed to implement the
               reference model spec.
        quant_min: minimum value in quantized domain (TODO: align behavior with other observers)
        quant_min: maximum value in quantized domain
        custom_op_name: (temporary) specify this observer for an operator that doesn't require any observation
                        (Can be used in Graph Mode Passes for special case ops).
        compute_dtype (deprecated): if set, marks the future quantize function to use
                       dynamic quantization instead of static quantization.
                       This field is deprecated, use `is_dynamic=True` instead.
        is_dynamic: if True, the `quantize` function in the reference model
                    representation taking stats from this observer instance will
                    use dynamic quantization.
    """
    dtype: Incomplete
    quant_min: Incomplete
    quant_max: Incomplete
    custom_op: Incomplete
    is_dynamic: Incomplete
    def __init__(self, dtype=..., custom_op_name: str = '', compute_dtype: Incomplete | None = None, quant_min: Incomplete | None = None, quant_max: Incomplete | None = None, is_dynamic: bool = False) -> None: ...
    def forward(self, x): ...
    def calculate_qparams(self) -> None: ...

class RecordingObserver(ObserverBase):
    """
    The module is mainly for debug and records the tensor values during runtime.

    Args:
        dtype: Quantized data type
        qscheme: Quantization scheme to be used
        reduce_range: Reduces the range of the quantized data type by 1 bit
    """
    __annotations__: Incomplete
    tensor_val: Incomplete
    def __init__(self, dtype=..., **kwargs) -> None: ...
    def forward(self, x): ...
    def calculate_qparams(self) -> None: ...
    def get_tensor_value(self): ...

class NoopObserver(ObserverBase):
    """
    Observer that doesn't do anything and just passes its configuration to the
    quantized module's ``.from_float()``.

    Primarily used for quantization to float16 which doesn't require determining
    ranges.

    Args:
        dtype: Quantized data type
        custom_op_name: (temporary) specify this observer for an operator that doesn't require any observation
                        (Can be used in Graph Mode Passes for special case ops).
    """
    dtype: Incomplete
    custom_op: Incomplete
    def __init__(self, dtype=..., custom_op_name: str = '') -> None: ...
    def forward(self, x): ...
    def calculate_qparams(self) -> None: ...

class ReuseInputObserver(ObserverBase):
    """ This observer is used when we want to reuse the observer from the operator
    that produces the input Tensor, typically used for operators like reshape, e.g.
    ```
    x0 = ...
    x1 = x0.reshape()
    ```
    if we configure x0 to be observed by some observer, let's say MinMaxObserver,
    and reshape is configured with ReuseInputObserver, we'll reuse the observer instance
    for x0 for x1 (output of reshape). If x0 is not observed, we also won't observe x1.

    Note: this is only enabled in FX Graph Mode Quantization
    """
    def __init__(self) -> None: ...
    def forward(self, x): ...
    def calculate_qparams(self) -> None: ...

def get_observer_state_dict(mod):
    """
    Returns the state dict corresponding to the observer stats.
    Traverse the model state_dict and extract out the stats.
    """
def load_observer_state_dict(mod, obs_dict) -> None:
    """
    Given input model and a state_dict containing model observer stats,
    load the stats back into the model. The observer state_dict can be saved
    using torch.ao.quantization.get_observer_state_dict
    """

default_observer: Incomplete
default_placeholder_observer = PlaceholderObserver
default_debug_observer = RecordingObserver
default_weight_observer: Incomplete
weight_observer_range_neg_127_to_127: Incomplete
default_histogram_observer: Incomplete
default_per_channel_weight_observer: Incomplete
per_channel_weight_observer_range_neg_127_to_127: Incomplete
default_dynamic_quant_observer: Incomplete
default_float_qparams_observer: Incomplete
default_float_qparams_observer_4bit: Incomplete
default_fixed_qparams_range_neg1to1_observer: Incomplete
default_fixed_qparams_range_0to1_observer: Incomplete
default_symmetric_fixed_qparams_observer = default_fixed_qparams_range_neg1to1_observer
default_affine_fixed_qparams_observer = default_fixed_qparams_range_0to1_observer
default_reuse_input_observer = ReuseInputObserver
