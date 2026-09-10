import jax

def softmax(x: jax.Array, *, axis: int = -1, num_warps: int = 4, interpret: bool = False, debug: bool = False) -> jax.Array:
    """Computes the softmax of the input array along the specified axis.

  Args:
    x: input array
    axis: the axis along which to perform the computation
    num_warps: the number of warps to use for executing the Triton kernel
    interpret: whether to interpret the kernel using pallas
    debug: whether to use pallas in debug mode

  Returns:
    The result of the softmax operation over the specified axis of x.
  """
