from jax._src import profiler as profiler
from typing import Any

def dumps(obj: Any) -> bytes:
    """See `pickle.dumps`. Used for serializing host callbacks in jaxlib."""
def loads(data: bytes) -> Any:
    """See `pickle.loads`."""
