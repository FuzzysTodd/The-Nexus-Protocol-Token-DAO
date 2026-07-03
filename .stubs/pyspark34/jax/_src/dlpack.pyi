import enum
from _typeshed import Incomplete
from jax._src import array as array, xla_bridge as xla_bridge
from jax._src.lib import xla_client as xla_client, xla_extension_version as xla_extension_version
from jax._src.typing import Array as Array
from typing import Any

SUPPORTED_DTYPES: Incomplete

class DLDeviceType(enum.IntEnum):
    kDLCPU: int
    kDLCUDA: int
    kDLROCM: int

def to_dlpack(x: Array, take_ownership: bool = False, stream: int | Any | None = None):
    """Returns a DLPack tensor that encapsulates a :class:`~jax.Array` ``x``.

  Takes ownership of the contents of ``x``; leaves ``x`` in an invalid/deleted
  state.

  Args:
    x: a :class:`~jax.Array`, on either CPU or GPU.
    take_ownership: If ``True``, JAX hands ownership of the buffer to DLPack,
      and the consumer is free to mutate the buffer; the JAX buffer acts as if
      it were deleted. If ``False``, JAX retains ownership of the buffer; it is
      undefined behavior if the DLPack consumer writes to a buffer that JAX
      owns.
    stream: optional platform-dependent stream to wait on until the buffer is
      ready. This corresponds to the `stream` argument to ``__dlpack__``
      documented in https://dmlc.github.io/dlpack/latest/python_spec.html.
  """
def from_dlpack(external_array):
    """Returns a :class:`~jax.Array` representation of a DLPack tensor.

  The returned :class:`~jax.Array` shares memory with ``external_array``.

  Args:
    external_array: an array object that has __dlpack__ and __dlpack_device__
      methods, or a DLPack tensor on either CPU or GPU (legacy API).

  Returns:
    A jax.Array
  """
