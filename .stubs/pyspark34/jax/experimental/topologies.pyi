import abc
import jax
from _typeshed import Incomplete
from collections.abc import Sequence
from jax.experimental import mesh_utils as mesh_utils

Device: Incomplete

class TopologyDescription(abc.ABC):
    devices: Incomplete
    def __init__(self, devices: list[Device]) -> None: ...

def get_attached_topology(platform: Incomplete | None = None) -> TopologyDescription: ...
def get_topology_desc(topology_name: str = '', platform: str | None = None, **kwargs) -> TopologyDescription: ...
def make_mesh(topo: TopologyDescription, mesh_shape: Sequence[int], axis_names: tuple[str, ...], *, contiguous_submeshes: bool = False) -> jax.sharding.Mesh: ...
