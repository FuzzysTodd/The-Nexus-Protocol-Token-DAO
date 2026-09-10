from _typeshed import Incomplete
from tensorflow.python.ops import gen_spectral_ops as gen_spectral_ops, manip_ops as manip_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

fft: Incomplete
ifft: Incomplete
fft2d: Incomplete
ifft2d: Incomplete
fft3d: Incomplete
ifft3d: Incomplete
rfft: Incomplete
irfft: Incomplete
rfft2d: Incomplete
irfft2d: Incomplete
rfft3d: Incomplete
irfft3d: Incomplete

def fftshift(x, axes: Incomplete | None = None, name: Incomplete | None = None):
    """Shift the zero-frequency component to the center of the spectrum.

  This function swaps half-spaces for all axes listed (defaults to all).
  Note that ``y[0]`` is the Nyquist component only if ``len(x)`` is even.

  @compatibility(numpy)
  Equivalent to numpy.fft.fftshift.
  https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftshift.html
  @end_compatibility

  For example:

  ```python
  x = tf.signal.fftshift([ 0.,  1.,  2.,  3.,  4., -5., -4., -3., -2., -1.])
  x.numpy() # array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])
  ```

  Args:
    x: `Tensor`, input tensor.
    axes: `int` or shape `tuple`, optional Axes over which to shift.  Default is
      None, which shifts all axes.
    name: An optional name for the operation.

  Returns:
    A `Tensor`, The shifted tensor.
  """
def ifftshift(x, axes: Incomplete | None = None, name: Incomplete | None = None):
    """The inverse of fftshift.

  Although identical for even-length x,
  the functions differ by one sample for odd-length x.

  @compatibility(numpy)
  Equivalent to numpy.fft.ifftshift.
  https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifftshift.html
  @end_compatibility

  For example:

  ```python
  x = tf.signal.ifftshift([[ 0.,  1.,  2.],[ 3.,  4., -4.],[-3., -2., -1.]])
  x.numpy() # array([[ 4., -4.,  3.],[-2., -1., -3.],[ 1.,  2.,  0.]])
  ```

  Args:
    x: `Tensor`, input tensor.
    axes: `int` or shape `tuple` Axes over which to calculate. Defaults to None,
      which shifts all axes.
    name: An optional name for the operation.

  Returns:
    A `Tensor`, The shifted tensor.
  """
