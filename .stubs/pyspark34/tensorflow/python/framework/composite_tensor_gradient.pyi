import abc
from tensorflow.python.framework import composite_tensor as composite_tensor
from tensorflow.python.util import nest as nest
from typing import Protocol

class CompositeTensorGradient(metaclass=abc.ABCMeta):
    """Class used to help compute gradients for CompositeTensors.

  This abstract base class defines two methods: `get_gradient_components`, which
  returns the components of a value that should be included in gradients; and
  `replace_gradient_components`, which replaces the gradient components in a
  value.  These methods can be used to compute the gradient of a `y` with
  respect to `x` (`grad(y, x)`) as follows:

  * If `y` is a `CompositeTensor` with `CompositeTensorGradient` `cg` =
    `y.__composite_gradient__`, then `grad(y, x)` =
    `grad(cg.get_gradient_components(y), x)`.

  * If `x` is a `CompositeTensor` with `CompositeTensorGradient` `cg` =
    'x.__composite_gradient__', then `grad(y, x)` =
    `cg.replace_gradient_components(x, grad(y, cg.get_gradient_components(x))`.
  """
    @abc.abstractmethod
    def get_gradient_components(self, value):
        """Returns the components of `value` that should be included in gradients.

    This method may not call TensorFlow ops, since any new ops added to the
    graph would not be propertly tracked by the gradient mechanisms.

    Args:
      value: A `CompositeTensor` value.

    Returns:
      A nested structure of `Tensor` or `IndexedSlices`.
    """
    @abc.abstractmethod
    def replace_gradient_components(self, value, component_grads):
        """Replaces the gradient components in `value` with `component_grads`.

    Args:
      value: A value with its gradient components compatible with
        `component_grads`.
      component_grads: A nested structure of `Tensor` or `IndexedSlices` or
        `None` (for unconnected gradients).

    Returns:
      A copy of `value`, where the components that should be included in
      gradients have been replaced by `component_grads`; or `None` (if
      `component_grads` includes `None`).
    """

class CompositeTensorGradientProtocol(Protocol):
    """Protocol for adding gradient support to CompositeTensors."""
    __composite_gradient__: CompositeTensorGradient

class WithValuesCompositeTensorGradient(CompositeTensorGradient):
    """CompositeTensorGradient based on `T.values` and `T.with_values`."""
    def get_gradient_components(self, value): ...
    def replace_gradient_components(self, value, component_grads): ...

def get_flat_tensors_for_gradients(xs):
    """Returns a flat list of Tensors that should be differentiated for `xs`.

  Args:
    xs: A list of `Tensor`s or `CompositeTensor`s.

  Returns:
    A flat list of `Tensor`s constructed from `xs`, where `Tensor` values are
    left as-is, and `CompositeTensor`s are replaced with
    `_get_tensors_for_gradient(x)`.
  """
def replace_flat_tensors_for_gradients(xs, flat_grads):
    """Replaces Tensors that should be differentiated in `xs` with `flat_grads`.

  Args:
    xs: A list of `Tensor`s or `CompositeTensor`s.
    flat_grads: A list of `Tensor`.

  Returns:
    A list of `Tensor` or `CompositeTensor`.
  """
