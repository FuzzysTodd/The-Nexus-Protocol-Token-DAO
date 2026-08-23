from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras import backend as backend
from tensorflow.python.ops import array_ops as array_ops

def convert_data_format(data_format, ndim): ...
def normalize_tuple(value, n, name):
    '''Transforms a single integer or iterable of integers into an integer tuple.

  Args:
    value: The value to validate and convert. Could an int, or any iterable of
      ints.
    n: The size of the tuple to be returned.
    name: The name of the argument being validated, e.g. "strides" or
      "kernel_size". This is only used to format error messages.

  Returns:
    A tuple of n integers.

  Raises:
    ValueError: If something else than an int/long or iterable thereof was
      passed.
  '''
def conv_output_length(input_length, filter_size, padding, stride, dilation: int = 1):
    '''Determines output length of a convolution given input length.

  Args:
      input_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full", "causal"
      stride: integer.
      dilation: dilation rate, integer.

  Returns:
      The output length (integer).
  '''
def conv_input_length(output_length, filter_size, padding, stride):
    '''Determines input length of a convolution given output length.

  Args:
      output_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.

  Returns:
      The input length (integer).
  '''
def deconv_output_length(input_length, filter_size, padding, output_padding: Incomplete | None = None, stride: int = 0, dilation: int = 1):
    '''Determines output length of a transposed convolution given input length.

  Args:
      input_length: Integer.
      filter_size: Integer.
      padding: one of `"same"`, `"valid"`, `"full"`.
      output_padding: Integer, amount of padding along the output dimension. Can
        be set to `None` in which case the output length is inferred.
      stride: Integer.
      dilation: Integer.

  Returns:
      The output length (integer).
  '''
def normalize_data_format(value): ...
def normalize_padding(value): ...
def conv_kernel_mask(input_shape, kernel_shape, strides, padding):
    '''Compute a mask representing the connectivity of a convolution operation.

  Assume a convolution with given parameters is applied to an input having N
  spatial dimensions with `input_shape = (d_in1, ..., d_inN)` to produce an
  output with shape `(d_out1, ..., d_outN)`. This method returns a boolean array
  of shape `(d_in1, ..., d_inN, d_out1, ..., d_outN)` with `True` entries
  indicating pairs of input and output locations that are connected by a weight.

  Example:

    >>> input_shape = (4,)
    >>> kernel_shape = (2,)
    >>> strides = (1,)
    >>> padding = "valid"
    >>> conv_kernel_mask(input_shape, kernel_shape, strides, padding)
    array([[ True, False, False],
           [ True,  True, False],
           [False,  True,  True],
           [False, False,  True]])

    where rows and columns correspond to inputs and outputs respectively.


  Args:
    input_shape: tuple of size N: `(d_in1, ..., d_inN)`, spatial shape of the
      input.
    kernel_shape: tuple of size N, spatial shape of the convolutional kernel /
      receptive field.
    strides: tuple of size N, strides along each spatial dimension.
    padding: type of padding, string `"same"` or `"valid"`.
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.

  Returns:
    A boolean 2N-D `np.ndarray` of shape
    `(d_in1, ..., d_inN, d_out1, ..., d_outN)`, where `(d_out1, ..., d_outN)`
    is the spatial shape of the output. `True` entries in the mask represent
    pairs of input-output locations that are connected by a weight.

  Raises:
    ValueError: if `input_shape`, `kernel_shape` and `strides` don\'t have the
        same number of dimensions.
    NotImplementedError: if `padding` is not in {`"same"`, `"valid"`}.
  '''
def conv_kernel_idxs(input_shape, kernel_shape, strides, padding, filters_in, filters_out, data_format) -> Generator[Incomplete, None, Incomplete]:
    '''Yields output-input tuples of indices in a CNN layer.

  The generator iterates over all `(output_idx, input_idx)` tuples, where
    `output_idx` is an integer index in a flattened tensor representing a single
    output image of a convolutional layer that is connected (via the layer
    weights) to the respective single input image at `input_idx`

  Example:

    >>> input_shape = (2, 2)
    >>> kernel_shape = (2, 1)
    >>> strides = (1, 1)
    >>> padding = "valid"
    >>> filters_in = 1
    >>> filters_out = 1
    >>> data_format = "channels_last"
    >>> list(conv_kernel_idxs(input_shape, kernel_shape, strides, padding,
    ...                       filters_in, filters_out, data_format))
    [(0, 0), (0, 2), (1, 1), (1, 3)]

  Args:
    input_shape: tuple of size N: `(d_in1, ..., d_inN)`, spatial shape of the
      input.
    kernel_shape: tuple of size N, spatial shape of the convolutional kernel /
      receptive field.
    strides: tuple of size N, strides along each spatial dimension.
    padding: type of padding, string `"same"` or `"valid"`.
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    filters_in: `int`, number if filters in the input to the layer.
    filters_out: `int\', number if filters in the output of the layer.
    data_format: string, "channels_first" or "channels_last".

  Yields:
    The next tuple `(output_idx, input_idx)`, where
    `output_idx` is an integer index in a flattened tensor representing a single
    output image of a convolutional layer that is connected (via the layer
    weights) to the respective single input image at `input_idx`.

  Raises:
      ValueError: if `data_format` is neither
      `"channels_last"` nor `"channels_first"`, or if number of strides, input,
      and kernel number of dimensions do not match.

      NotImplementedError: if `padding` is neither `"same"` nor `"valid"`.
  '''
def conv_connected_inputs(input_shape, kernel_shape, output_position, strides, padding):
    '''Return locations of the input connected to an output position.

  Assume a convolution with given parameters is applied to an input having N
  spatial dimensions with `input_shape = (d_in1, ..., d_inN)`. This method
  returns N ranges specifying the input region that was convolved with the
  kernel to produce the output at position
  `output_position = (p_out1, ..., p_outN)`.

  Example:

    >>> input_shape = (4, 4)
    >>> kernel_shape = (2, 1)
    >>> output_position = (1, 1)
    >>> strides = (1, 1)
    >>> padding = "valid"
    >>> conv_connected_inputs(input_shape, kernel_shape, output_position,
    ...                       strides, padding)
    [range(1, 3), range(1, 2)]

  Args:
    input_shape: tuple of size N: `(d_in1, ..., d_inN)`, spatial shape of the
      input.
    kernel_shape: tuple of size N, spatial shape of the convolutional kernel /
      receptive field.
    output_position: tuple of size N: `(p_out1, ..., p_outN)`, a single position
      in the output of the convolution.
    strides: tuple of size N, strides along each spatial dimension.
    padding: type of padding, string `"same"` or `"valid"`.
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.

  Returns:
    N ranges `[[p_in_left1, ..., p_in_right1], ...,
              [p_in_leftN, ..., p_in_rightN]]` specifying the region in the
    input connected to output_position.
  '''
def conv_output_shape(input_shape, kernel_shape, strides, padding):
    '''Return the output shape of an N-D convolution.

  Forces dimensions where input is empty (size 0) to remain empty.

  Args:
    input_shape: tuple of size N: `(d_in1, ..., d_inN)`, spatial shape of the
      input.
    kernel_shape: tuple of size N, spatial shape of the convolutional kernel /
      receptive field.
    strides: tuple of size N, strides along each spatial dimension.
    padding: type of padding, string `"same"` or `"valid"`.
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.

  Returns:
    tuple of size N: `(d_out1, ..., d_outN)`, spatial shape of the output.
  '''
def squeeze_batch_dims(inp, op, inner_rank):
    """Returns `unsqueeze_batch(op(squeeze_batch(inp)))`.

  Where `squeeze_batch` reshapes `inp` to shape
  `[prod(inp.shape[:-inner_rank])] + inp.shape[-inner_rank:]`
  and `unsqueeze_batch` does the reverse reshape but on the output.

  Args:
    inp: A tensor with dims `batch_shape + inner_shape` where `inner_shape`
      is length `inner_rank`.
    op: A callable that takes a single input tensor and returns a single.
      output tensor.
    inner_rank: A python integer.

  Returns:
    `unsqueeze_batch_op(squeeze_batch(inp))`.
  """
