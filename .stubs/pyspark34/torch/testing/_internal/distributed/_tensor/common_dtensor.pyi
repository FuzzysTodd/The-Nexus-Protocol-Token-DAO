import torch
from _typeshed import Incomplete
from dataclasses import dataclass
from torch.distributed._tensor import DeviceMesh as DeviceMesh, Replicate as Replicate, Shard as Shard, distribute_tensor as distribute_tensor, redistribute as redistribute
from torch.distributed._tensor.api import DTensor as DTensor
from torch.distributed._tensor.placement_types import Placement as Placement
from torch.testing._internal.common_distributed import MultiProcessTestCase as MultiProcessTestCase, MultiThreadedTestCase as MultiThreadedTestCase, TEST_SKIPS as TEST_SKIPS, skip_if_lt_x_gpu as skip_if_lt_x_gpu
from torch.utils._pytree import TreeSpec as TreeSpec, tree_flatten as tree_flatten, tree_unflatten as tree_unflatten
from typing import Callable, Dict, Generator, List, Sequence, Tuple, TypeVar

DEVICE_TYPE: Incomplete
NUM_DEVICES: int
T = TypeVar('T')

def skip_unless_torch_gpu(method: T) -> T:
    """
    Test decorator which skips the test unless there's a GPU available to torch.

    >>> # xdoctest: +SKIP
    >>> @skip_unless_torch_gpu
    >>> def test_some_method(self) -> None:
    >>>   ...
    """

@dataclass
class RedistributeProfile:
    num_calls: int
    def __init__(self, num_calls) -> None: ...

def redistribute_profiler() -> Generator[RedistributeProfile, None, None]: ...

class DTensorTestBase(MultiProcessTestCase):
    @property
    def world_size(self) -> int: ...
    def build_device_mesh(self) -> DeviceMesh: ...
    def init_pg(self, backend: str = 'nccl') -> None: ...
    def destroy_pg(self) -> None: ...
    def setUp(self) -> None: ...
TestFunc = Callable[[object], object]

def with_comms(func: TestFunc) -> TestFunc: ...

class DTensorOpTestBase(MultiThreadedTestCase):
    @property
    def world_size(self) -> int: ...
    @property
    def device_type(self) -> str: ...
    def build_device_mesh(self): ...
    def setUp(self) -> None: ...

class DTensorConverter:
    hit: int
    miss: int
    mesh: Incomplete
    args: Incomplete
    kwargs: Incomplete
    flatten_args: Incomplete
    flatten_args_spec: Incomplete
    flatten_kwargs: Incomplete
    flatten_kwargs_spec: Incomplete
    sharding_combs: Incomplete
    def __init__(self, mesh: DeviceMesh, args: Tuple[object, ...], kwargs: Dict[str, object]) -> None: ...
    def successful(self) -> bool: ...
    def is_supported_tensor(self, t: torch.Tensor) -> bool: ...
    def gen_sharding_choices_for_arg(self, arg: torch.Tensor) -> Sequence[Placement]: ...
    def __iter__(self) -> DTensorConverter: ...
    def __next__(self) -> Tuple[Tuple[object, ...], Dict[str, object]]: ...
    def to_dist_tensor(self, t: torch.Tensor, mesh: DeviceMesh, placements: List[Placement]) -> torch.Tensor: ...
