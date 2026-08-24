import jax
from collections.abc import Sequence
from jax._src.lax import convolution as convolution, lax as lax
from typing import Any

DType = Any

def conv_general_dilated_patches(lhs: jax.typing.ArrayLike, filter_shape: Sequence[int], window_strides: Sequence[int], padding: str | Sequence[tuple[int, int]], lhs_dilation: Sequence[int] | None = None, rhs_dilation: Sequence[int] | None = None, dimension_numbers: convolution.ConvGeneralDilatedDimensionNumbers | None = None, precision: lax.PrecisionType | None = None, preferred_element_type: DType | None = None) -> jax.Array:
    '''Extract patches subject to the receptive field of `conv_general_dilated`.

  Runs the input through a convolution with given parameters. The kernel of the
  convolution is constructed such that the output channel dimension `"C"`
  contains flattened image patches, so instead a single `"C"` dimension
  represents, for example, three dimensions `"chw"` collapsed. The order of
  these dimensions is `"c" + \'\'.join(c for c in rhs_spec if c not in \'OI\')`,
  where `rhs_spec == dimension_numbers[1]`, and the size of this `"C"`
  dimension is therefore the size of each patch, i.e.
  `np.prod(filter_shape) * lhs.shape[lhs_spec.index(\'C\')]`, where
  `lhs_spec == dimension_numbers[0]`.

  Docstring below adapted from `jax.lax.conv_general_dilated`.

  See Also:
    https://www.tensorflow.org/xla/operation_semantics#conv_convolution

  Args:
    lhs: a rank `n+2` dimensional input array.
    filter_shape: a sequence of `n` integers, representing the receptive window
      spatial shape in the order as specified in
      `rhs_spec = dimension_numbers[1]`.
    window_strides: a sequence of `n` integers, representing the inter-window
      strides.
    padding: either the string `\'SAME\'`, the string `\'VALID\'`, or a sequence of
      `n` `(low, high)` integer pairs that give the padding to apply before and
      after each spatial dimension.
    lhs_dilation: `None`, or a sequence of `n` integers, giving the
      dilation factor to apply in each spatial dimension of `lhs`. LHS dilation
      is also known as transposed convolution.
    rhs_dilation: `None`, or a sequence of `n` integers, giving the
      dilation factor to apply in each spatial dimension of `rhs`. RHS dilation
      is also known as atrous convolution.
    dimension_numbers: either `None`, or a 3-tuple
      `(lhs_spec, rhs_spec, out_spec)`, where each element is a string
      of length `n+2`. `None` defaults to `("NCHWD..., OIHWD..., NCHWD...")`.
    precision: Optional. Either ``None``, which means the default precision for
      the backend, or a :class:`~jax.lax.Precision` enum value (``Precision.DEFAULT``,
      ``Precision.HIGH`` or ``Precision.HIGHEST``).
    preferred_element_type: Optional. Either ``None``, which means the default
      accumulation type for the input types, or a datatype, indicating to
      accumulate results to and return a result with that datatype.

  Returns:
    A rank `n+2` array containing the flattened image patches in the output
    channel (`"C"`) dimension. For example if
    `dimension_numbers = ("NcHW", "OIwh", "CNHW")`, the output has dimension
    numbers `"CNHW" = "{cwh}NHW"`, with the size of dimension `"C"` equal to
    the size of each patch
    (`np.prod(filter_shape) * lhs.shape[lhs_spec.index(\'C\')]`).

  '''
def conv_general_dilated_local(lhs: jax.typing.ArrayLike, rhs: jax.typing.ArrayLike, window_strides: Sequence[int], padding: str | Sequence[tuple[int, int]], filter_shape: Sequence[int], lhs_dilation: Sequence[int] | None = None, rhs_dilation: Sequence[int] | None = None, dimension_numbers: convolution.ConvGeneralDilatedDimensionNumbers | None = None, precision: lax.PrecisionLike = None) -> jax.Array:
    '''General n-dimensional unshared convolution operator with optional dilation.

  Also known as locally connected layer, the operation is equivalent to
  convolution with a separate (unshared) `rhs` kernel used at each output
  spatial location. Docstring below adapted from `jax.lax.conv_general_dilated`.

  See Also:
    https://www.tensorflow.org/xla/operation_semantics#conv_convolution

  Args:
    lhs: a rank `n+2` dimensional input array.
    rhs: a rank `n+2` dimensional array of kernel weights. Unlike in regular
      CNNs, its spatial coordinates (`H`, `W`, ...) correspond to output spatial
      locations, while input spatial locations are fused with the input channel
      locations in the single `I` dimension, in the order of
      `"C" + \'\'.join(c for c in rhs_spec if c not in \'OI\')`, where
      `rhs_spec = dimension_numbers[1]`. For example, if `rhs_spec == "WHIO",
      the unfolded kernel shape is
      `"[output W][output H]{I[receptive window W][receptive window H]}O"`.
    window_strides: a sequence of `n` integers, representing the inter-window
      strides.
    padding: either the string `\'SAME\'`, the string `\'VALID\'`, or a sequence of
      `n` `(low, high)` integer pairs that give the padding to apply before and
      after each spatial dimension.
    filter_shape: a sequence of `n` integers, representing the receptive window
      spatial shape in the order as specified in
      `rhs_spec = dimension_numbers[1]`.
    lhs_dilation: `None`, or a sequence of `n` integers, giving the
      dilation factor to apply in each spatial dimension of `lhs`. LHS dilation
      is also known as transposed convolution.
    rhs_dilation: `None`, or a sequence of `n` integers, giving the
      dilation factor to apply in each input spatial dimension of `rhs`.
      RHS dilation is also known as atrous convolution.
    dimension_numbers: either `None`, a `ConvDimensionNumbers` object, or
      a 3-tuple `(lhs_spec, rhs_spec, out_spec)`, where each element is a string
      of length `n+2`.
    precision: Optional. Either ``None``, which means the default precision for
      the backend, a ``lax.Precision`` enum value (``Precision.DEFAULT``,
      ``Precision.HIGH`` or ``Precision.HIGHEST``) or a tuple of two
      ``lax.Precision`` enums indicating precision of ``lhs``` and ``rhs``.

  Returns:
    An array containing the unshared convolution result.

  In the string case of `dimension_numbers`, each character identifies by
  position:

  - the batch dimensions in `lhs`, `rhs`, and the output with the character
    \'N\',
  - the feature dimensions in `lhs` and the output with the character \'C\',
  - the input and output feature dimensions in rhs with the characters \'I\'
    and \'O\' respectively, and
  - spatial dimension correspondences between `lhs`, `rhs`, and the output using
    any distinct characters.

  For example, to indicate dimension numbers consistent with the `conv` function
  with two spatial dimensions, one could use `(\'NCHW\', \'OIHW\', \'NCHW\')`. As
  another example, to indicate dimension numbers consistent with the TensorFlow
  Conv2D operation, one could use `(\'NHWC\', \'HWIO\', \'NHWC\')`. When using the
  latter form of convolution dimension specification, window strides are
  associated with spatial dimension character labels according to the order in
  which the labels appear in the `rhs_spec` string, so that `window_strides[0]`
  is matched with the dimension corresponding to the first character
  appearing in rhs_spec that is not `\'I\'` or `\'O\'`.

  If `dimension_numbers` is `None`, the default is `(\'NCHW\', \'OIHW\', \'NCHW\')`
  (for a 2D convolution).
  '''
