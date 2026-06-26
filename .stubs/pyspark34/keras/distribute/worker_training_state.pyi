from _typeshed import Incomplete
from keras import backend as backend
from keras.distribute import distributed_file_utils as distributed_file_utils
from keras.distribute.distributed_file_utils import support_on_demand_checkpoint_callback as support_on_demand_checkpoint_callback
from keras.utils import mode_keys as mode_keys

MAX_CHECKPOINT_TO_KEEP: int

class WorkerTrainingState:
    """Training state management class.

    This class provides apis for backing up and restoring the training state.
    This allows model and epoch and batch information to be saved periodically
    and restore for fault-tolerance, also known as preemption-recovery purpose.
    """
    CKPT_SAVED_EPOCH_UNUSED_VALUE: int
    CKPT_SAVED_BATCH_UNUSED_VALUE: int
    read_checkpoint_manager: Incomplete
    write_checkpoint_manager: Incomplete
    preemption_handler: Incomplete
    def __init__(self, model, checkpoint_dir, save_freq: str = 'epoch', save_before_preemption_arg: Incomplete | None = None) -> None: ...
    def back_up(self, epoch, batch: int = 0) -> None:
        """Back up the current state of training into a checkpoint file.

        Args:
          epoch: The current epoch information to be saved.
          batch: The current batch(step) information to be saved.
        """
    def backup_if_preempted(self) -> None: ...
    def restore(self) -> None:
        """Restore the training state from the backed up checkpoint file.

        Returns:
          True if the training state is successfully restored. False if the
          training state doesn't need to be restored, or error occurred so it
          can't.
        """
    def delete_backup(self) -> None:
        """Delete the backup directories.

        Delete the backup directories which should not exist after `fit()`
        successfully finishes.
        """
    def maybe_load_initial_counters_from_ckpt(self, steps_per_epoch, initial_epoch, mode):
        """Maybe load 1st epoch from checkpoint, considering worker recovery.

        When `_ckpt_saved_epoch` attribute exists and is not
        `CKPT_SAVED_EPOCH_UNUSED_VALUE`, this is under multi-worker training
        setting and indicates the worker is recovering from previous failure. In
        this case, infer `initial_epoch` from `self._ckpt_saved_epoch` to
        continue previous unfinished training from certain epoch.

        Args:
          steps_per_epoch: The number of steps per epoch value.
          initial_epoch: The original initial_epoch user passes in in `fit()`.
          mode: The mode for running `model.fit()`.

        Returns:
          If the training is recovering from previous failure under multi-worker
          training setting, return the (epoch, step) the training is supposed to
          continue at. Otherwise, return the `initial_epoch, initial_step` the
          user passes in.
        """
