from _typeshed import Incomplete
from tensorflow.python.framework import smart_cond as smart_cond, tensor_shape as tensor_shape
from tensorflow.python.ops.signal import fft_ops as fft_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def dct(input, type: int = 2, n: Incomplete | None = None, axis: int = -1, norm: Incomplete | None = None, name: Incomplete | None = None):
    """Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

  Types I, II, III and IV are supported.
  Type I is implemented using a length `2N` padded `tf.signal.rfft`.
  Type II is implemented using a length `2N` padded `tf.signal.rfft`, as
   described here: [Type 2 DCT using 2N FFT padded (Makhoul)]
   (https://dsp.stackexchange.com/a/10606).
  Type III is a fairly straightforward inverse of Type II
   (i.e. using a length `2N` padded `tf.signal.irfft`).
   Type IV is calculated through 2N length DCT2 of padded signal and
  picking the odd indices.

  @compatibility(scipy)
  Equivalent to [scipy.fftpack.dct]
   (https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.dct.html)
   for Type-I, Type-II, Type-III and Type-IV DCT.
  @end_compatibility

  Args:
    input: A `[..., samples]` `float32`/`float64` `Tensor` containing the
      signals to take the DCT of.
    type: The DCT type to perform. Must be 1, 2, 3 or 4.
    n: The length of the transform. If length is less than sequence length,
      only the first n elements of the sequence are considered for the DCT.
      If n is greater than the sequence length, zeros are padded and then
      the DCT is computed as usual.
    axis: For future expansion. The axis to compute the DCT along. Must be `-1`.
    norm: The normalization to apply. `None` for no normalization or `'ortho'`
      for orthonormal normalization.
    name: An optional name for the operation.

  Returns:
    A `[..., samples]` `float32`/`float64` `Tensor` containing the DCT of
    `input`.

  Raises:
    ValueError: If `type` is not `1`, `2`, `3` or `4`, `axis` is
      not `-1`, `n` is not `None` or greater than 0,
      or `norm` is not `None` or `'ortho'`.
    ValueError: If `type` is `1` and `norm` is `ortho`.

  [dct]: https://en.wikipedia.org/wiki/Discrete_cosine_transform
  """
def idct(input, type: int = 2, n: Incomplete | None = None, axis: int = -1, norm: Incomplete | None = None, name: Incomplete | None = None):
    """Computes the 1D [Inverse Discrete Cosine Transform (DCT)][idct] of `input`.

  Currently Types I, II, III, IV are supported. Type III is the inverse of
  Type II, and vice versa.

  Note that you must re-normalize by 1/(2n) to obtain an inverse if `norm` is
  not `'ortho'`. That is:
  `signal == idct(dct(signal)) * 0.5 / signal.shape[-1]`.
  When `norm='ortho'`, we have:
  `signal == idct(dct(signal, norm='ortho'), norm='ortho')`.

  @compatibility(scipy)
  Equivalent to [scipy.fftpack.idct]
   (https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.idct.html)
   for Type-I, Type-II, Type-III and Type-IV DCT.
  @end_compatibility

  Args:
    input: A `[..., samples]` `float32`/`float64` `Tensor` containing the
      signals to take the DCT of.
    type: The IDCT type to perform. Must be 1, 2, 3 or 4.
    n: For future expansion. The length of the transform. Must be `None`.
    axis: For future expansion. The axis to compute the DCT along. Must be `-1`.
    norm: The normalization to apply. `None` for no normalization or `'ortho'`
      for orthonormal normalization.
    name: An optional name for the operation.

  Returns:
    A `[..., samples]` `float32`/`float64` `Tensor` containing the IDCT of
    `input`.

  Raises:
    ValueError: If `type` is not `1`, `2` or `3`, `n` is not `None, `axis` is
      not `-1`, or `norm` is not `None` or `'ortho'`.

  [idct]:
  https://en.wikipedia.org/wiki/Discrete_cosine_transform#Inverse_transforms
  """
