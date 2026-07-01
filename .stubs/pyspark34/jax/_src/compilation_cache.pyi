import numpy as np
from _typeshed import Incomplete
from jax._src import cache_key as cache_key
from jax._src.compilation_cache_interface import CacheInterface as CacheInterface
from jax._src.gfile_cache import GFileCache as GFileCache
from jax._src.lib import xla_client as xla_client
from jax._src.lib.mlir import ir as ir

logger: Incomplete

def initialize_cache(path) -> None:
    """Creates a global cache object.

  Should only be called once per process.

  Will throw an assertion error if called a second time with a different path.

  Args:
    path: path for the cache directory.
  """
def get_executable_and_time(cache_key: str, compile_options, backend) -> tuple[xla_client.LoadedExecutable | None, int | None]:
    """Returns the cached executable and its compilation time if present, or None
  otherwise.
  """
def put_executable_and_time(cache_key: str, module_name: str, executable: xla_client.LoadedExecutable, backend, compile_time: int) -> None:
    """Adds the 'executable' and its compilation time to the cache repository,
  possibly evicting older entries.
  """
def get_cache_key(module: ir.Module, devices: np.ndarray, compile_options, backend, produce_original_cache_key: bool = True) -> str: ...
def is_initialized(): ...
def reset_cache() -> None: ...
def combine_executable_and_time(serialized_executable: bytes, compile_time: int) -> bytes:
    """Given the serialized executable and the compilation time, produce a cache
  entry in the format shown below.

  The cache entry is of the form:
  Byte:     0    1    2    3    4 ...
  Content:  compilation time    serialized executable
            (big-endian int)
  """
def extract_executable_and_time(exectuable_and_time: bytes) -> tuple[bytes, int]:
    """Given the cache entry in the format shown below, extract the serialized
  executable and the compilation time.

  The cache entry 'executable_and_time' is of the form:
  Byte:     0    1    2    3    4 ...
  Content:  compilation time    serialized executable
            (big-endian int)
  """
