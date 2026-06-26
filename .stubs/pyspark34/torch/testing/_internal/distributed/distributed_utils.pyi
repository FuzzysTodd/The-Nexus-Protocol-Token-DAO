import torch.distributed as dist
from _typeshed import Incomplete
from collections.abc import Generator

class MockProcessGroup(dist.ProcessGroup):
    def __init__(self, rank, world) -> None: ...
    def getBackendName(self): ...

def create_mock_pg(prefix_store, rank, world_size, timeout): ...
def mock_init_dist(rank, world_size) -> None: ...
def with_dist(rank: int = 0, world_size: int = 2) -> Generator[None, None, None]:
    """
    Context manager that initializer c10d with a fake process group.
    """
def with_fake_comms(func: Incomplete | None = None, rank: int = 0, world_size: int = 2):
    """
    Function wrapper that inits a fake process group designed for testing.
    Right now only querying for world size is available
    """
