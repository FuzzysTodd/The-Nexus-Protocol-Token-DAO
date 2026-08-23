import numpy as np
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Callable

logger: Incomplete
device_kind_handler_dict: dict[str, Callable[..., np.ndarray | None]]

def create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any] | None = None, *, contiguous_submeshes: bool = False) -> np.ndarray:
    """Creates a performant device mesh for jax.sharding.Mesh.

  Args:
    mesh_shape: shape of logical mesh, ordered by increasing network-intensity
      e.g. [replica, data, mdl] where mdl has the most network communication
      requirements.
    devices: optionally, the devices to construct a mesh for. Defaults to
      jax.devices().
    contiguous_submeshes: if True, this function will attempt to create a mesh
      where each process's local devices form a contiguous submesh. This is
      required when passing host local inputs to `pjit`. A ValueError will be
      raised if this function can't produce a suitable mesh.

  Raises:
    ValueError: if the number of devices doesn't equal the product of
      `mesh_shape`.

  Returns:
    A np.ndarray of JAX devices with mesh_shape as its shape that can be fed
    into jax.sharding.Mesh with good collective performance.
  """
def create_hybrid_device_mesh(mesh_shape: Sequence[int], dcn_mesh_shape: Sequence[int], devices: Sequence[Any] | None = None, *, process_is_granule: bool = False) -> np.ndarray:
    """Creates a device mesh for hybrid (e.g., ICI and DCN) parallelism.

  Args:
    mesh_shape: shape of the logical mesh for the faster/inner network, ordered
      by increasing network intensity, e.g. [replica, data, mdl] where mdl has
      the most network communication requirements.
    dcn_mesh_shape: shape of the logical mesh for the slower/outer network, in
      the same order as mesh_shape.
    devices: optionally, the devices to construct a mesh for. Defaults to
      jax.devices().
    process_is_granule: if True, this function will treat processes as the units
      of the slower/outer network. Otherwise it will look for slice_index
      attributes on devices and use slices as the units. Enabling this is meant
      as a fallback for platforms (e.g., GPU) that don't set slice_index.

  Raises:
    ValueError: if the number of slices to which the `devices` belong doesn't
      equal the product of `dcn_mesh_shape`, or if the number of devices
      belonging to any single slice does not equal the product of `mesh_shape`.

  Returns:
    A np.ndarray of JAX devices with mesh_shape * dcn_mesh_shape as its shape
    that can be fed into jax.sharding.Mesh for hybrid parallelism.
  """
