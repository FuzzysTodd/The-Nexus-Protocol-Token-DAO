import jaxlib.mlir.ir as ir
import numpy as np
from .hlo_helpers import custom_call as custom_call
from _typeshed import Incomplete
from jaxlib import xla_client as xla_client

FftType: Incomplete

def dynamic_ducc_fft_hlo(result_type: ir.Type, input: ir.Value, *, input_dtype: np.dtype, ndims: int, input_shape: ir.Value, strides_in: ir.Value, strides_out: ir.Value, scale: ir.Value, fft_type: FftType, fft_lengths: list[int], result_shape: ir.Value):
    """DUCC FFT kernel for CPU, with support for dynamic shapes."""
