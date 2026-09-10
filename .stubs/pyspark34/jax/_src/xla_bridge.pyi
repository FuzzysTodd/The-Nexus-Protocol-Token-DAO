import dataclasses
from _typeshed import Incomplete
from collections.abc import Mapping
from jax._src import config as jax_config, distributed as distributed, traceback_util as traceback_util, util as util
from jax._src.config import config as config
from jax._src.lib import cuda_versions as cuda_versions, xla_client as xla_client, xla_extension as xla_extension, xla_extension_version as xla_extension_version
from typing import Any

logger: Incomplete
jax_plugins: Any | None
XlaBackend: Incomplete
BACKEND_TARGET: Incomplete
CUDA_VISIBLE_DEVICES: Incomplete

def tpu_client_timer_callback(timer_secs: float) -> xla_client.Client | None: ...

BackendFactory: Incomplete

@dataclasses.dataclass
class BackendRegistration:
    factory: BackendFactory
    priority: int
    fail_quietly: bool = ...
    experimental: bool = ...
    def __init__(self, factory, priority, fail_quietly, experimental) -> None: ...

def register_backend_factory(name: str, factory: BackendFactory, *, priority: int = 0, fail_quietly: bool = True, experimental: bool = False) -> None: ...
def make_gpu_client(*, platform_name: str, visible_devices_flag: jax_config.FlagHolder[str]) -> xla_client.Client: ...
def discover_pjrt_plugins() -> None:
    """Discovers plugins in the namespace package `jax_plugins` and import them.

  There are two methods used to discover plugin modules. They are intended
  to be used together by implementors in order to cover all packaging and
  development cases:

  1. Define a globally unique module under the `jax_plugins` namespace
     package (i.e. just create a `jax_plugins` directory and define your
     module below it).
  2. If building a package via pyproject.toml or setup.py, advertise your
     plugin module name by including an entry-point under the `jax_plugins`
     group which points to your full module name.

  During Jax startup, Jax will load each module discovered in such a way and
  call its `initialize()` function. It is expected that this function should
  register its concrete plugin name/implementations via call(s) to
  `jax._src.xla_bridge.register_plugin(name, priority=, library_paty=,
  options=)`. Since `initialize()` functions are called for all installed
  plugins, they should avoid doing expensive, non-registration related work.

  TODO: We should provide a variant of `register_plugin` which allows the
  library_path and options to be resolved via a callback. This would enable
  light-weight plugin registration in cases where options need to be derived
  from heavy-weight system initialization.
  """
def register_plugin(plugin_name: str, *, priority: int = 400, library_path: str | None = None, options: Mapping[str, str | int | list[int] | float | bool] | None = None) -> None:
    """Registers a backend factory for the PJRT plugin.

  Args:
    plugin_name: the name of the plugin.
    priority: the priority this plugin should be registered in jax backends.
      Default to be 400.
    library_path: Optional. The full path to the .so file of the plugin.
      Required when the plugin is dynamically linked.
    options: Optional. It is used when creating a PJRT plugin client.
  """
def register_pjrt_plugin_factories_from_env() -> None:
    '''Registers backend factories for PJRT plugins.

  A backend factory will be registered for every PJRT plugin in the input
  string, in the format of \'name1:path1,name2:path2\' (\'name1;path1,name2;path2\'
  for windows). The path can be a path to the plugin library or a path to the
  plugin configuration json file. The json file needs to have a "library_path"
  field for the plugin library path. It can have an optional "create_option"
  field for the options used when creating a PJRT plugin client. The value of
  "create_option" is key-value pairs. Please see xla_client._NameValueMapping
  for the supported types of values.

  TPU PJRT plugin will be loaded and registered separately in make_tpu_client.
  '''
def is_known_platform(platform: str) -> bool: ...
def canonicalize_platform(platform: str) -> str:
    '''Replaces platform aliases with their concrete equivalent.

  In particular, replaces "gpu" with either "cuda" or "rocm", depending on which
  hardware is actually present. We want to distinguish "cuda" and "rocm" for
  purposes such as MLIR lowering rules, but in many cases we don\'t want to
  force users to care.
  '''
def expand_platform_alias(platform: str) -> list[str]:
    '''Expands, e.g., "gpu" to ["cuda", "rocm"].

  This is used for convenience reasons: we expect cuda and rocm to act similarly
  in many respects since they share most of the same code.
  '''
def is_gpu(platform): ...
def backends() -> dict[str, xla_client.Client]: ...
def get_backend(platform: None | str | xla_client.Client = None) -> xla_client.Client: ...
def get_device_backend(device: xla_client.Device | None = None) -> xla_client.Client:
    """Returns the Backend associated with `device`, or the default Backend."""
def device_count(backend: str | xla_client.Client | None = None) -> int:
    """Returns the total number of devices.

  On most platforms, this is the same as :py:func:`jax.local_device_count`.
  However, on multi-process platforms where different devices are associated
  with different processes, this will return the total number of devices across
  all processes.

  Args:
    backend: This is an experimental feature and the API is likely to change.
      Optional, a string representing the xla backend: ``'cpu'``, ``'gpu'``, or
      ``'tpu'``.

  Returns:
    Number of devices.

  """
def local_device_count(backend: str | xla_client.Client | None = None) -> int:
    """Returns the number of devices addressable by this process."""
def devices(backend: str | xla_client.Client | None = None) -> list[xla_client.Device]:
    """Returns a list of all devices for a given backend.

  .. currentmodule:: jaxlib.xla_extension

  Each device is represented by a subclass of :class:`Device` (e.g.
  :class:`CpuDevice`, :class:`GpuDevice`). The length of the returned list is
  equal to ``device_count(backend)``. Local devices can be identified by
  comparing :attr:`Device.process_index` to the value returned by
  :py:func:`jax.process_index`.

  If ``backend`` is ``None``, returns all the devices from the default backend.
  The default backend is generally ``'gpu'`` or ``'tpu'`` if available,
  otherwise ``'cpu'``.

  Args:
    backend: This is an experimental feature and the API is likely to change.
      Optional, a string representing the xla backend: ``'cpu'``, ``'gpu'``, or
      ``'tpu'``.

  Returns:
    List of Device subclasses.
  """
def default_backend() -> str:
    """Returns the platform name of the default XLA backend."""
def local_devices(process_index: int | None = None, backend: str | xla_client.Client | None = None, host_id: int | None = None) -> list[xla_client.Device]:
    """Like :py:func:`jax.devices`, but only returns devices local to a given process.

  If ``process_index`` is ``None``, returns devices local to this process.

  Args:
    process_index: the integer index of the process. Process indices can be
      retrieved via ``len(jax.process_count())``.
    backend: This is an experimental feature and the API is likely to change.
      Optional, a string representing the xla backend: ``'cpu'``, ``'gpu'``, or
      ``'tpu'``.

  Returns:
    List of Device subclasses.
  """
def process_index(backend: str | xla_client.Client | None = None) -> int:
    """Returns the integer process index of this process.

  On most platforms, this will always be 0. This will vary on multi-process
  platforms though.

  Args:
    backend: This is an experimental feature and the API is likely to change.
      Optional, a string representing the xla backend: ``'cpu'``, ``'gpu'``, or
      ``'tpu'``.

  Returns:
    Integer process index.
  """
def host_id(backend: str | xla_client.Client | None = None) -> int: ...
def process_count(backend: str | xla_client.Client | None = None) -> int:
    """Returns the number of JAX processes associated with the backend."""
def host_count(backend: str | xla_client.Client | None = None) -> int: ...
def host_ids(backend: str | xla_client.Client | None = None) -> list[int]: ...
def using_pjrt_c_api(backend: Incomplete | None = None): ...
def make_pjrt_tpu_topology(topology_name: str = '', **kwargs): ...
