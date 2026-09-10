import numpy as np
from _typeshed import Incomplete
from jax._src.config import config as config
from jax._src.lib import xla_client as xla_client
from jax._src.lib.mlir import ir as ir

logger: Incomplete

def add_flag_prefixes(flag_prefixes: list[str]) -> None:
    """Add flag prefixes to include in the cache key. Call prior to get().
  """
def clear_flag_prefixes() -> None:
    """Clear flag prefixes added by add_flag_prefixes().
  """
def get_flag_prefixes() -> list[str]:
    """Return flag prefixes added by add_flag_prefixes().
  """
def get(module: ir.Module, devices: np.ndarray, compile_options: xla_client.CompileOptions, backend: xla_client.Client, compression_algorithm: str = 'zstandard', produce_original_cache_key: bool = True) -> str:
    """Creates a hashed string to use as a key to the compilation cache.

  Creates a cache key that is a hex-encoded string of a unique hash based on
  the arguments. The hex-encoded string is 256 characters long.

  Args:
    module: the input program
    devices: an array of accelerator devices that the program will run on
    compile_options: options passed to the XLA compiler
    backend: description of the platform (e.g., TPU version)
    compression_algorithm: a string representing the compression algorithm used
      for the executable before persisting in the cache
    produce_original_cache_key: if True, the original cache-key generation
      algorithm is run, else the new one. This is transient; once the migration
      is complete, this parameter and the original algorithm will be removed.
      (New one not implemented as yet.)

  Typical return value example:
   'jit__psum-14ac577cdb2ef6d986078b4054cc9893a9a14a16dbb0d8f37b89167c1f1aacdf'
  """
