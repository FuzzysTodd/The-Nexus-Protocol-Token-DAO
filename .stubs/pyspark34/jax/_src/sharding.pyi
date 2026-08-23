import functools
from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from jax._src import util as util

Shape = tuple[int, ...]
Device: Incomplete
Index = tuple[slice, ...]
XLADeviceAssignment = Sequence[Device]

class Sharding:
    """Describes how a :class:`jax.Array` is laid out across devices.
  """
    @property
    def device_set(self) -> set[Device]:
        """The set of devices that this :class:`Sharding` spans.

    In multi-controller JAX, the set of devices is global, i.e., includes
    non-addressable devices from other processes.
    """
    def devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index | None]:
        """Returns a mapping from devices to the array slices each contains.

    The mapping includes all global devices, i.e., including
    non-addressable devices from other processes.
    """
    def shard_shape(self, global_shape: Shape) -> Shape:
        """Returns the shape of the data on each device.

    The shard shape returned by this function is calculated from
    ``global_shape`` and the properties of the sharding.
    """
    def is_equivalent_to(self, other: Sharding, ndim: int) -> bool:
        """Returns ``True`` if two shardings are equivalent.

    Two shardings are equivalent if they place the same logical array shards on
    the same devices.

    For example, a :class:`NamedSharding` may be equivalent
    to a :class:`PositionalSharding` if both place the same shards of the array
    on the same devices.
    """
    @property
    def is_fully_replicated(self) -> bool:
        """Is this sharding fully replicated?

    A sharding is fully replicated if each device has a complete copy of the
    entire data.
    """
    @property
    def is_fully_addressable(self) -> bool:
        '''Is this sharding fully addressable?

    A sharding is fully addressable if the current process can address all of
    the devices named in the :class:`Sharding`. ``is_fully_addressable`` is
    equivalent to "is_local" in multi-process JAX.
    '''
    @property
    def memory_kind(self) -> str | None:
        """Returns the memory kind of the sharding."""
    def with_memory_kind(self, kind: str) -> Sharding:
        """Returns a new Sharding instance with the specified memory kind."""
    @functools.cached_property
    def addressable_devices(self) -> set[Device]:
        """The set of devices in the :class:`Sharding` that are addressable by the
       current process.
    """
    def addressable_devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index | None]:
        """A mapping from addressable devices to the slice of array data each contains.

    ``addressable_devices_indices_map`` contains that part of
    ``device_indices_map`` that applies to the addressable devices.
    """
