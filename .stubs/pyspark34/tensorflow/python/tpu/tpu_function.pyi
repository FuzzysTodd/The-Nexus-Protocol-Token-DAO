import threading
from collections.abc import Generator

class TpuContext(threading.local):
    """A context object holding state about the TPU computation being built."""
    def __init__(self) -> None:
        """Creates a new TpuContext."""
    @property
    def number_of_shards(self): ...
    def set_number_of_shards(self, number_of_shards) -> None: ...

def tpu_shard_context(number_of_shards) -> Generator[None, None, None]:
    """A context manager setting current number of shards."""
def get_tpu_context(): ...
def on_device_training_loop(func): ...
