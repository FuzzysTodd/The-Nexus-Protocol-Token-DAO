import abc
import jax
import tensorstore as ts
from _typeshed import Incomplete
from collections.abc import Awaitable, Sequence
from jax._src import array as array, distributed as distributed, sharding as sharding, sharding_impls as sharding_impls, typing as typing
from typing import Any, Callable

TS_CONTEXT: Incomplete
logger: Incomplete

async def create_async_array_from_callback(global_shape: array.Shape, inp_sharding: sharding_impls.XLACompatibleSharding, data_callback: Callable[[array.Index, jax.Device], Awaitable[jax.Array]]): ...
def get_tensorstore_spec(ckpt_path: str, ocdbt: bool = False): ...

class _LimitInFlightBytes:
    """Limits in-flight bytes when reading/writing checkpoints per process."""
    def __init__(self, num_bytes) -> None: ...
    async def wait_for_bytes(self, requested_bytes): ...
    async def release_bytes(self, requested_bytes) -> None: ...

async def async_serialize(arr_inp, tensorstore_spec, commit_future: Incomplete | None = None, context=...): ...
def run_serialization(arrays, tensorstore_specs): ...
def estimate_read_memory_footprint(t: ts.TensorStore, domain: ts.IndexDomain) -> int: ...
async def async_deserialize(in_sharding: sharding_impls.XLACompatibleSharding, tensorstore_spec: ts.Spec | dict[str, Any], global_shape: Sequence[int] | None = None, dtype: Incomplete | None = None, byte_limiter: _LimitInFlightBytes | None = None, context=..., assume_metadata: bool = False): ...
def run_deserialization(shardings: Sequence[sharding.Sharding], tensorstore_specs: Sequence[dict[str, Any]], global_shapes: Sequence[array.Shape] | None = None, dtypes: Sequence[typing.DTypeLike] | None = None, concurrent_gb: int = 32): ...

class GlobalAsyncCheckpointManagerBase(metaclass=abc.ABCMeta):
    """Interface for checkpointing GDAs asynchronously.

  This class manages the state of an ongoing asynchronous checkpoint.

  For example, say a checkpoint happens on every step. If you checkpoint on
  step 1 and after some computation the model is on checkpoint 2. But step 1's
  checkpoint hasn't finished committing to the storage layer yet. So until that
  is finished, checkpoint for step 2 will need to be blocked. Maintaining a
  class allows to maintain that state.

  Example:

  Below is a simplified training loop:

  ```
  # Call this at the start of your program.
  jax.distributed.initialize()

  manager = GlobalAsyncCheckpointManager()

  # Restore checkpoint if available or initialize the train_state from
  # init_fn().
  train_state = manager.deserialize(...)

  while ...:
    if step % num_steps_between_checkpoints == 0:
      manager.serialize(train_state, temp_checkpoint_dir=...,
                        final_checkpoint_dir=...)
      train_state = train_step(train_state, input)
      # This is a non-blocking call.
      manager.check_for_errors()

  manager.serialize(train_state, temp_checkpoint_dir=...,
                    final_checkpoint_dir=...)
  # Wait before the end of the program for the checkpoint to finish. This is a
  # blocking call.
  manager.wait_until_finished()
  ```
  """
    @abc.abstractmethod
    def check_for_errors(self):
        """Checks if any errors have been raised in the child thread.

    This is a non-blocking call that can be called in the main thread.
    """
    @abc.abstractmethod
    def wait_until_finished(self):
        """Blocks until serialization has finished."""
    @abc.abstractmethod
    def serialize(self, arrays, tensorstore_specs, *, on_commit_callback: Callable[[], None]):
        """Serializes GDAs to TensorStore."""
    @abc.abstractmethod
    def deserialize(self, shardings: Sequence[sharding.Sharding], tensorstore_specs: Sequence[dict[str, Any]], global_shapes: Sequence[array.Shape] | None = None, dtypes: Sequence[typing.DTypeLike] | None = None):
        """Deserializes GDAs from TensorStore."""

class AsyncManager:
    def __init__(self, timeout_secs: int = 300) -> None: ...
    def __del__(self) -> None: ...
    def check_for_errors(self) -> None: ...
    def wait_until_finished(self) -> None: ...

class GlobalAsyncCheckpointManager(AsyncManager, GlobalAsyncCheckpointManagerBase):
    """Responsible for serializing GDAs via TensorStore."""
    def serialize(self, arrays, tensorstore_specs, *, on_commit_callback):
        """Serializes Arrays or Arrays via TensorStore asynchronously.

    TensorStore writes to a storage layer in 2 steps:
    *  Reading/copying from the source after which the source can be modified.
         * Returns a copy future.
    *  Writing/committing to the storage layer.
         * Returns a commit future.

    In asynchronous mode, the serialization waits for the commit future to
    finish in a separate thread allowing other computation to proceed.

    Args:
      arrays: Arrays or Arrays that should be serialized.
      tensorstore_specs: TensorStore specs that are used to serialize GDAs or
        Arrays.
      on_commit_callback: This callback will be executed after all processes
        have finished writing their checkpoints to disk. Filesystems where
        atomic rename operations are supported, you can rename from the
        temporary directory to the final directory. On GCS, you write to the
        final directory directly and in `on_commit_callback` you write a
        success file indicating that the serialization was successful because
        GCS does not support atomic rename operations.
    """
    def serialize_with_paths(self, arrays: Sequence[jax.Array], paths: Sequence[str], *, on_commit_callback): ...
    def deserialize(self, shardings: Sequence[sharding.Sharding], tensorstore_specs: Sequence[dict[str, Any]], global_shapes: Sequence[array.Shape] | None = None, dtypes: Sequence[typing.DTypeLike] | None = None, concurrent_gb: int = 32): ...
    def deserialize_with_paths(self, shardings: Sequence[sharding.Sharding], paths: Sequence[str], global_shapes: Sequence[array.Shape] | None = None, dtypes: Sequence[typing.DTypeLike] | None = None, concurrent_gb: int = 32): ...
