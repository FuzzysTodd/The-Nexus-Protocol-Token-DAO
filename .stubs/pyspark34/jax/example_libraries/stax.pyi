from _typeshed import Incomplete
from jax import lax as lax, random as random
from jax.nn import elu as elu, gelu as gelu, leaky_relu as leaky_relu, log_softmax as log_softmax, relu as relu, selu as selu, sigmoid as sigmoid, softmax as softmax, softplus as softplus, standardize as standardize
from jax.nn.initializers import glorot_normal as glorot_normal, normal as normal, ones as ones, zeros as zeros

glorot = glorot_normal
randn = normal
logsoftmax = log_softmax

def Dense(out_dim, W_init=..., b_init=...):
    """Layer constructor function for a dense (fully-connected) layer."""
def GeneralConv(dimension_numbers, out_chan, filter_shape, strides: Incomplete | None = None, padding: str = 'VALID', W_init: Incomplete | None = None, b_init=...):
    """Layer construction function for a general convolution layer."""

Conv: Incomplete

def GeneralConvTranspose(dimension_numbers, out_chan, filter_shape, strides: Incomplete | None = None, padding: str = 'VALID', W_init: Incomplete | None = None, b_init=...):
    """Layer construction function for a general transposed-convolution layer."""

Conv1DTranspose: Incomplete
ConvTranspose: Incomplete

def BatchNorm(axis=(0, 1, 2), epsilon: float = 1e-05, center: bool = True, scale: bool = True, beta_init=..., gamma_init=...):
    """Layer construction function for a batch normalization layer."""
def elementwise(fun, **fun_kwargs):
    """Layer that applies a scalar function elementwise on its inputs."""

Tanh: Incomplete
Relu: Incomplete
Exp: Incomplete
LogSoftmax: Incomplete
Softmax: Incomplete
Softplus: Incomplete
Sigmoid: Incomplete
Elu: Incomplete
LeakyRelu: Incomplete
Selu: Incomplete
Gelu: Incomplete
MaxPool: Incomplete
SumPool: Incomplete
AvgPool: Incomplete

def Flatten():
    """Layer construction function for flattening all but the leading dim."""

Flatten: Incomplete

def Identity():
    """Layer construction function for an identity layer."""

Identity: Incomplete

def FanOut(num):
    """Layer construction function for a fan-out layer."""
def FanInSum():
    """Layer construction function for a fan-in sum layer."""

FanInSum: Incomplete

def FanInConcat(axis: int = -1):
    """Layer construction function for a fan-in concatenation layer."""
def Dropout(rate, mode: str = 'train'):
    """Layer construction function for a dropout layer with given rate."""
def serial(*layers):
    """Combinator for composing layers in serial.

  Args:
    *layers: a sequence of layers, each an (init_fun, apply_fun) pair.

  Returns:
    A new layer, meaning an (init_fun, apply_fun) pair, representing the serial
    composition of the given sequence of layers.
  """
def parallel(*layers):
    """Combinator for composing layers in parallel.

  The layer resulting from this combinator is often used with the FanOut and
  FanInSum layers.

  Args:
    *layers: a sequence of layers, each an (init_fun, apply_fun) pair.

  Returns:
    A new layer, meaning an (init_fun, apply_fun) pair, representing the
    parallel composition of the given sequence of layers. In particular, the
    returned layer takes a sequence of inputs and returns a sequence of outputs
    with the same length as the argument `layers`.
  """
def shape_dependent(make_layer):
    """Combinator to delay layer constructor pair until input shapes are known.

  Args:
    make_layer: a one-argument function that takes an input shape as an argument
      (a tuple of positive integers) and returns an (init_fun, apply_fun) pair.

  Returns:
    A new layer, meaning an (init_fun, apply_fun) pair, representing the same
    layer as returned by `make_layer` but with its construction delayed until
    input shapes are known.
  """
