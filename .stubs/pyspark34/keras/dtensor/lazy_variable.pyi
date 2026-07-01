from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.ops import resource_variable_ops

class LazyInitVariable(resource_variable_ops.BaseResourceVariable):
    """Lazily initialized variables.

    The major use case for this class is to serve as a memory efficient
    alternative for tf.Variable. The resource handle of this class is point to
    nothing, which mean it will raise error when its value is fetched in a eager
    context. Having said that, it will perform like a normal tf.Variable when
    using with graph tensor, like KerasTensor produced from tf.keras.Input.
    """
    def __init__(self, initial_value: Incomplete | None = None, trainable: Incomplete | None = None, collections: Incomplete | None = None, validate_shape: bool = True, caching_device: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, variable_def: Incomplete | None = None, import_scope: Incomplete | None = None, constraint: Incomplete | None = None, distribute_strategy: Incomplete | None = None, synchronization: Incomplete | None = None, aggregation: Incomplete | None = None, shape: Incomplete | None = None, **kwargs) -> None: ...
    def initialize(self) -> None: ...
    def create_and_initialize(self) -> None: ...

def lazy_init_scope() -> Generator[None, None, None]: ...
def disable_init_variable_creator() -> Generator[None, None, None]: ...
