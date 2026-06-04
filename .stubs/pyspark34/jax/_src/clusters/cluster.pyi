from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src.cloud_tpu_init import running_in_cloud_tpu_vm as running_in_cloud_tpu_vm

logger: Incomplete

class ClusterEnv:
    """Interface for defining a cluster environment.

  To enable auto bootrapping (aka :func:`jax.distributed.initialize()`),
  cluster environments need to derive from :class:`ClusterEnv` and implement
  :func:`is_env_present`, :func:`get_coordinator_address`,
  :func:`get_process_count`, and :func:`get_process_id`.
  :class:`ClusterEnv` subclasses are automatically detected when imported.
  """
    def __init_subclass__(cls, **kwargs) -> None: ...
    @classmethod
    def auto_detect_unset_distributed_params(cls, coordinator_address: str | None, num_processes: int | None, process_id: int | None, local_device_ids: Sequence[int] | None) -> tuple[str | None, int | None, int | None, Sequence[int] | None]: ...
    @classmethod
    def is_env_present(cls) -> bool:
        """Returns True if process is running in this cluster environment.
    """
    @classmethod
    def get_coordinator_address(cls) -> str:
        '''Returns address and port used by JAX to bootstrap.

    Process id 0 will open a tcp socket at "hostname:port" where
    all the processes will connect to initialize the distributed JAX service.
    The selected port needs to be free.
    :func:`get_coordinator_address` needs to return the same hostname and port on all the processes.

    Returns:
      "hostname:port"
    '''
    @classmethod
    def get_process_count(cls) -> int: ...
    @classmethod
    def get_process_id(cls) -> int: ...
    @classmethod
    def get_local_process_id(cls) -> int | None:
        """ Get index of current process inside a host.

    The method is only useful to support single device per process.
    In that case, each process will see a local device whose ID is
    the same as its local process ID.
    If None, JAX will not restrict the visible devices.
    """
