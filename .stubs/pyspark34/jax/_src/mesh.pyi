import contextlib
import functools
import numpy as np
import threading
from _typeshed import Incomplete
from collections.abc import Hashable, Sequence
from jax._src import util as util
from jax._src.lib import xla_client as xc, xla_extension_version as xla_extension_version
from typing import Any, NamedTuple

MeshAxisName = Any
ResourceAxisName = Hashable

class Loop(NamedTuple):
    name: ResourceAxisName
    length: int

def show_axes(axes): ...

class ResourceEnv(NamedTuple):
    physical_mesh: Mesh
    loops: tuple[Loop, ...]
    def with_mesh(self, mesh: Mesh): ...
    def with_extra_loop(self, loop: Loop): ...
    @property
    def physical_resource_axes(self) -> set[ResourceAxisName]: ...
    @property
    def loop_resource_axes(self) -> set[ResourceAxisName]: ...
    @property
    def resource_axes(self) -> set[ResourceAxisName]: ...
    @property
    def shape(self): ...
    @property
    def local_shape(self): ...

class Mesh(contextlib.ContextDecorator):
    """Declare the hardware resources available in the scope of this manager.

  In particular, all ``axis_names`` become valid resource names inside the
  managed block and can be used e.g. in the ``in_axis_resources`` argument of
  :py:func:`jax.experimental.pjit.pjit`. Also see JAX's multi-process programming
  model (https://jax.readthedocs.io/en/latest/multi_process.html)
  and the Distributed arrays and automatic parallelization tutorial
  (https://jax.readthedocs.io/en/latest/notebooks/Distributed_arrays_and_automatic_parallelization.html)

  If you are compiling in multiple threads, make sure that the
  ``with Mesh`` context manager is inside the function that the threads will
  execute.

  Args:
    devices: A NumPy ndarray object containing JAX device objects (as
      obtained e.g. from :py:func:`jax.devices`).
    axis_names: A sequence of resource axis names to be assigned to the
      dimensions of the ``devices`` argument. Its length should match the
      rank of ``devices``.

  Example:

    >>> from jax.experimental.pjit import pjit
    >>> from jax.sharding import Mesh
    >>> from jax.sharding import PartitionSpec as P
    >>> import numpy as np
    ...
    >>> inp = np.arange(16).reshape((8, 2))
    >>> devices = np.array(jax.devices()).reshape(4, 2)
    ...
    >>> # Declare a 2D mesh with axes `x` and `y`.
    >>> global_mesh = Mesh(devices, ('x', 'y'))
    >>> # Use the mesh object directly as a context manager.
    >>> with global_mesh:
    ...   out = pjit(lambda x: x, in_shardings=None, out_shardings=None)(inp)

    >>> # Initialize the Mesh and use the mesh as the context manager.
    >>> with Mesh(devices, ('x', 'y')) as global_mesh:
    ...   out = pjit(lambda x: x, in_shardings=None, out_shardings=None)(inp)

    >>> # Also you can use it as `with ... as ...`.
    >>> global_mesh = Mesh(devices, ('x', 'y'))
    >>> with global_mesh as m:
    ...   out = pjit(lambda x: x, in_shardings=None, out_shardings=None)(inp)

    >>> # You can also use it as `with Mesh(...)`.
    >>> with Mesh(devices, ('x', 'y')):
    ...   out = pjit(lambda x: x, in_shardings=None, out_shardings=None)(inp)
  """
    devices: np.ndarray
    axis_names: tuple[MeshAxisName, ...]
    def __new__(cls, devices: np.ndarray | Sequence[xc.Device], axis_names: str | Sequence[MeshAxisName]): ...
    def __reduce__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __setattr__(self, name, value) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None): ...
    @property
    def shape(self): ...
    @property
    def size(self): ...
    @property
    def empty(self): ...
    @functools.cached_property
    def is_multi_process(self): ...
    @property
    def local_mesh(self): ...
    @functools.cached_property
    def device_ids(self): ...
    @functools.cached_property
    def local_devices(self): ...

EMPTY_ENV: Incomplete

class _ThreadResourcesLocalState(threading.local):
    stack: Incomplete
    env: Incomplete
    def __init__(self) -> None: ...

thread_resources: Incomplete
