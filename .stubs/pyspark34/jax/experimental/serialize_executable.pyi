import jax
import pickle
from _typeshed import Incomplete
from jax._src.lib import xla_client as xc

def serialize(compiled: jax.stages.Compiled):
    """Serializes a compiled binary.

  Because pytrees are not serializable, they are returned so that
  the user can handle them properly.
  """
def deserialize_and_load(serialized, in_tree, out_tree, backend: str | xc.Client | None = None):
    """Constructs a jax.stages.Compiled from a serialized executable."""

class _JaxPjrtPickler(pickle.Pickler):
    device_types: Incomplete
    client_types: Incomplete
    def persistent_id(self, obj): ...

class _JaxPjrtUnpickler(pickle.Unpickler):
    backend: Incomplete
    devices_by_id: Incomplete
    def __init__(self, file, backend) -> None: ...
    def persistent_load(self, pid): ...
