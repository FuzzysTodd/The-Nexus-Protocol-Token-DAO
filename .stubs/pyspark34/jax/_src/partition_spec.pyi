from _typeshed import Incomplete

class _UnconstrainedPartitionSingleton: ...

class PartitionSpec(tuple):
    """Tuple describing how to partition an array across a mesh of devices.

  Each element is either ``None``, a string, or a tuple of strings.
  See the documentation of :class:`jax.sharding.NamedSharding` for more details.

  This class exists so JAX's pytree utilities can distinguish a partition
  specifications from tuples that should be treated as pytrees.
  """
    UNCONSTRAINED: Incomplete
    def __init__(self, *partitions) -> None: ...
    def __new__(cls, *partitions): ...
    def __reduce__(self): ...
