import threading
from _typeshed import Incomplete
from collections.abc import Hashable, Iterator
from jax._src import lib as lib, logging_config as logging_config
from jax._src.lib import jax_jit as jax_jit, transfer_guard_lib as transfer_guard_lib, xla_client as xla_client, xla_extension_version as xla_extension_version
from typing import Any, Callable, Generic, NamedTuple

logger: Incomplete

def bool_env(varname: str, default: bool) -> bool:
    """Read an environment variable and interpret it as a boolean.

  True values are (case insensitive): 'y', 'yes', 't', 'true', 'on', and '1';
  false values are 'n', 'no', 'f', 'false', 'off', and '0'.

  Args:
    varname: the name of the variable
    default: the default boolean value
  Raises: ValueError if the environment variable is anything else.
  """
def int_env(varname: str, default: int) -> int:
    """Read an environment variable and interpret it as an integer."""

UPGRADE_BOOL_HELP: str
UPGRADE_BOOL_EXTRA_DESC: str

class FlagHolder(Generic[_T]):
    def __init__(self, flags: NameSpace, name: str) -> None: ...
    @property
    def value(self) -> _T: ...

class Config:
    values: Incomplete
    meta: Incomplete
    FLAGS: Incomplete
    use_absl: bool
    def __init__(self) -> None: ...
    def update(self, name, val) -> None: ...
    def read(self, name): ...
    def add_option(self, name, default, opt_type, meta_args, meta_kwargs, update_hook: Callable[[Any], None] | None = None): ...
    def check_exists(self, name) -> None: ...
    def DEFINE_bool(self, name, default, *args, **kwargs) -> FlagHolder[bool]: ...
    def DEFINE_integer(self, name, default, *args, **kwargs) -> FlagHolder[int]: ...
    def DEFINE_float(self, name, default, *args, **kwargs) -> FlagHolder[float]: ...
    def DEFINE_string(self, name, default, *args, **kwargs) -> FlagHolder[str]: ...
    def DEFINE_enum(self, name, default, *args, **kwargs) -> FlagHolder[str]: ...
    absl_flags: Incomplete
    def config_with_absl(self): ...
    def complete_absl_config(self, absl_flags) -> None: ...
    def parse_flags_with_absl(self): ...
    def define_bool_state(self, name: str, default: bool, help: str, *, update_global_hook: Callable[[bool], None] | None = None, update_thread_local_hook: Callable[[bool | None], None] | None = None, upgrade: bool = False, extra_description: str = ''):
        '''Set up thread-local state and return a contextmanager for managing it.

    This function is a convenience wrapper. It defines a flag, environment
    variable, and corresponding thread-local state, which can be managed via the
    contextmanager it returns.

    The thread-local state value can be read via the ``config.<option_name>``
    attribute, where ``config`` is the singleton ``Config`` instance.

    Args:
      name: string, converted to lowercase to define the name of the config
        option (and absl flag). It is converted to uppercase to define the
        corresponding shell environment variable.
      default: boolean, a default value for the option.
      help: string, used to populate the flag help information as well as the
        docstring of the returned context manager.
      update_global_hook: a optional callback that is called with the updated
        value of the global state when it is altered or set initially.
      update_thread_local_hook: a optional callback that is called with the
        updated value of the thread-local state when it is altered or set
        initially.
      upgrade: optional indicator that this flag controls a canonical feature
        upgrade, so that it is `True` for the incoming functionality, `False`
        for the outgoing functionality to be deprecated.
      extra_description: string, optional: extra information to add to the
        summary description.

    Returns:
      A contextmanager to control the thread-local state value.

    Example:

      enable_foo = config.define_bool_state(
          name=\'jax_enable_foo\',
          default=False,
          help=\'Enable foo.\')

      # Now the JAX_ENABLE_FOO shell environment variable and --jax_enable_foo
      # command-line flag can be used to control the process-level value of
      # the configuration option, in addition to using e.g.
      # ``config.update("jax_enable_foo", True)`` directly. We can also use a
      # context manager:

      with enable_foo(True):
        ...

    The value of the thread-local state or flag can be accessed via
    ``config.jax_enable_foo``. Reading it via ``config.FLAGS.jax_enable_foo`` is
    an error.

    '''
    def define_enum_state(self, name: str, enum_values: list[str], default: str | None, help: str, update_global_hook: Callable[[str], None] | None = None, update_thread_local_hook: Callable[[str | None], None] | None = None):
        """Set up thread-local state and return a contextmanager for managing it.
    Args:
      name: string, converted to lowercase to define the name of the config
        option (and absl flag). It is converted to uppercase to define the
        corresponding shell environment variable.
      enum_values: list of strings representing the possible values for the
        option.
      default: optional string, default value.
      help: string, used to populate the flag help information as well as the
        docstring of the returned context manager.
    Returns:
      A contextmanager to control the thread-local state value.
    See docstring for ``define_bool_state``.
    """
    def define_int_state(self, name: str, default: int | None, help: str, update_global_hook: Callable[[str], None] | None = None, update_thread_local_hook: Callable[[str | None], None] | None = None):
        """Set up thread-local state and return a contextmanager for managing it.
    Args:
      name: string, converted to lowercase to define the name of the config
        option (and absl flag). It is converted to uppercase to define the
        corresponding shell environment variable.
      default: optional int, default value.
      help: string, used to populate the flag help information as well as the
        docstring of the returned context manager.
    Returns:
      A contextmanager to control the thread-local state value.
    See docstring for ``define_bool_state``.
    """
    def define_float_state(self, name: str, default: float | None, help: str, update_global_hook: Callable[[str], None] | None = None, update_thread_local_hook: Callable[[str | None], None] | None = None):
        """Set up thread-local state and return a contextmanager for managing it.
    Args:
      name: string, converted to lowercase to define the name of the config
        option (and absl flag). It is converted to uppercase to define the
        corresponding shell environment variable.
      default: optional float, default value.
      help: string, used to populate the flag help information as well as the
        docstring of the returned context manager.
    Returns:
      A contextmanager to control the thread-local state value.
    See docstring for ``define_bool_state``.
    """
    def define_string_state(self, name: str, default: str | None, help: str, update_global_hook: Callable[[str], None] | None = None, update_thread_local_hook: Callable[[str | None], None] | None = None):
        """Set up thread-local state and return a contextmanager for managing it.

    See docstring for ``define_bool_state``.

    Args:
      name: string, converted to lowercase to define the name of the config
        option (and absl flag). It is converted to uppercase to define the
        corresponding shell environment variable.
      default: string, a default value for the option.
      help: string, used to populate the flag help information as well as the
        docstring of the returned context manager.
      update_global_hook: an optional callback that is called with the updated
        value of the global state when it is altered or set initially.
      update_thread_local_hook: an optional callback that is called with the
        updated value of the thread-local state when it is altered or set
        initially.

    Returns:
      A contextmanager to control the thread-local state value.
    """
    def define_string_or_object_state(self, name: str, default: Any, help: str, update_global_hook: Callable[[Any], None] | None = None, update_thread_local_hook: Callable[[Any], None] | None = None, validate_new_val_hook: Callable[[Any], None] | None = None):
        """Set up thread-local state and return a contextmanager for managing it.

    Similar to ``define_string_state``, except the context manager will accept
    any object, not just a string. Any value passed via commandline flag or
    environment variable will be treated as a string.

    Args:
      name: string, converted to lowercase to define the name of the config
        option (and absl flag). It is converted to uppercase to define the
        corresponding shell environment variable.
      default: string, a default value for the option.
      help: string, used to populate the flag help information as well as the
        docstring of the returned context manager.
      update_global_hook: an optional callback that is called with the updated
        value of the global state when it is altered or set initially.
      update_thread_local_hook: an optional callback that is called with the
        updated value of the thread-local state when it is altered or set
        initially.
      validate_new_val_hook: an optional callback that is called with the new
        value on any update, and should raise an error if the new value is
        invalid.

    Returns:
      A contextmanager to control the thread-local state value.
    """

class NoDefault: ...

no_default: Incomplete

class _StateContextManager:
    __doc__: Incomplete
    def __init__(self, name, help, update_thread_local_hook, validate_new_val_hook: Callable[[Any], None] | None = None, extra_description: str = '', default_value: Any = ...) -> None: ...
    def __call__(self, new_val: Any = ...): ...

class _Unset: ...

unset: Incomplete

class NameSpace:
    def __init__(self, getter, setter) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, val) -> None: ...

config: Incomplete
flags = config
FLAGS: Incomplete

def DEFINE_bool(name, default, *args, **kwargs): ...
def DEFINE_integer(name, default, *args, **kwargs): ...
def DEFINE_float(name, default, *args, **kwargs): ...
def DEFINE_string(name, default, *args, **kwargs): ...
def DEFINE_enum(name, default, *args, **kwargs): ...

already_configured_with_absl: bool

class _GlobalExtraJitContext(NamedTuple):
    numpy_rank_promotion: str | None = ...
    numpy_dtype_promotion: str | None = ...
    default_matmul_precision: Any | None = ...
    dynamic_shapes: bool = ...
    threefry_partitionable: bool = ...
    softmax_custom_jvp: bool = ...

class _ThreadLocalExtraJitContext(NamedTuple):
    '''"A namedtuple containing states to add to the cache key.

  Just in time compilation (for jit, pmap, etc) behavior is configurable through
  global and thread-local options, used in the cache key.

  The initialization, which uses both config.py and core.py is done using
  `_update_thread_local_jit_state` in core.py to prevent circular imports.
  '''
    dynamic_trace_state: Any | None = ...
    axis_env_state: Hashable = ...
    mesh_context_manager: Hashable = ...
    numpy_rank_promotion: str | None = ...
    numpy_dtype_promotion: str | None = ...
    default_matmul_precision: Any | None = ...
    dynamic_shapes: bool = ...
    softmax_custom_jvp: bool = ...

class _ThreadLocalStateCache(threading.local):
    '''"A thread local cache for _ThreadLocalExtraJitContext

  The extra_jit_context in jax_jit.thread_local_state() may get updated and thus
  incurring dispatch overhead for comparing this python object during jit calls.
  We want to duduplicate the objects that have the same hash/equality to also
  have the same object ID, since the equality check is much faster if the object
  IDs match.
  '''
    canonicalize: Incomplete
    def __init__(self) -> None: ...

def update_thread_local_jit_state(**kw) -> None: ...

jax2tf_associative_scan_reductions: Incomplete
jax2tf_default_native_serialization: Incomplete
jax_serialization_version: Incomplete
jax_platforms: Incomplete
enable_checks: Incomplete
check_tracer_leaks: Incomplete
checking_leaks: Incomplete
debug_nans: Incomplete
debug_infs: Incomplete
log_compiles: Incomplete
log_checkpoint_residuals: Incomplete
parallel_functions_output_gda: Incomplete
pmap_shmap_merge: Incomplete
enable_memories: Incomplete
spmd_mode: Incomplete
distributed_debug: Incomplete
legacy_prng_key: Incomplete
enable_custom_prng: Incomplete
default_prng_impl: Incomplete
threefry_partitionable: Incomplete
softmax_custom_jvp: Incomplete
enable_custom_vjp_by_custom_transpose: Incomplete
raise_persistent_cache_errors: Incomplete
persistent_cache_min_compile_time_secs: Incomplete
compilation_cache_include_metadata_in_key: Incomplete
hlo_source_file_canonicalization_regex: Incomplete
include_full_tracebacks_in_locations: Incomplete
use_original_compilation_cache_key_generation: Incomplete
numpy_dtype_promotion: Incomplete
enable_x64: Incomplete
default_device: Incomplete
disable_jit: Incomplete
numpy_rank_promotion: Incomplete
default_matmul_precision: Incomplete
traceback_filtering: Incomplete
bcoo_cusparse_lowering: Incomplete
jax_xla_profile_version: Incomplete

def explicit_device_put_scope() -> Iterator[None]:
    """Indicates that the current context is an explicit device_put*() call."""
def explicit_device_get_scope() -> Iterator[None]:
    """Indicates that the current context is an explicit device_get() call."""

transfer_guard_host_to_device: Incomplete
transfer_guard_device_to_device: Incomplete
transfer_guard_device_to_host: Incomplete

def transfer_guard(new_val: str) -> Iterator[None]:
    """A contextmanager to control the transfer guard level for all transfers.

  For more information, see
  https://jax.readthedocs.io/en/latest/transfer_guard.html

  Args:
    new_val: The new thread-local transfer guard level for all transfers.

  Yields:
    None.
  """
