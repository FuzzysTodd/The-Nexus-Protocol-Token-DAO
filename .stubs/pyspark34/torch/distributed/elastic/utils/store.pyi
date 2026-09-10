from typing import List

def get_all(store, rank: int, prefix: str, size: int):
    """
    Given a store and a prefix, the method goes through the array of keys
    of the following format: ``{prefix}{idx}``, where idx is in a range
    from 0 to size, and tries to retrieve the data.

    The Rank0 process waits at the end to make sure all other processes
    finished the procedure before exiting.

    Usage

    ::

     values = get_all(store, 'torchelastic/data', 3)
     value1 = values[0] # retrieves the data for key torchelastic/data0
     value2 = values[1] # retrieves the data for key torchelastic/data1
     value3 = values[2] # retrieves the data for key torchelastic/data2

    """
def synchronize(store, data: bytes, rank: int, world_size: int, key_prefix: str, barrier_timeout: float = 300) -> List[bytes]:
    """
    Synchronizes ``world_size`` agents between each other using the underlying c10d store.
    The ``data`` will be available on each of the agents.

    Note: The data on the path is not deleted, as a result there can be stale data if
        you use the same key_prefix twice.
    """
def barrier(store, rank: int, world_size: int, key_prefix: str, barrier_timeout: float = 300) -> None:
    """
    A global lock between agents.

    Note: Since the data is not removed from the store, the barrier can be used
        once per unique ``key_prefix``.
    """
