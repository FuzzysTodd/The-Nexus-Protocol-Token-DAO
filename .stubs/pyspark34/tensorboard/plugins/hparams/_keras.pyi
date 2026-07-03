import tensorflow as tf
from _typeshed import Incomplete
from tensorboard.plugins.hparams import api_pb2 as api_pb2, summary as summary, summary_v2 as summary_v2

class Callback(tf.keras.callbacks.Callback):
    """Callback for logging hyperparameters to TensorBoard.

    NOTE: This callback only works in TensorFlow eager mode.
    """
    def __init__(self, writer, hparams, trial_id: Incomplete | None = None) -> None:
        """Create a callback for logging hyperparameters to TensorBoard.

        As with the standard `tf.keras.callbacks.TensorBoard` class, each
        callback object is valid for only one call to `model.fit`.

        Args:
          writer: The `SummaryWriter` object to which hparams should be
            written, or a logdir (as a `str`) to be passed to
            `tf.summary.create_file_writer` to create such a writer.
          hparams: A `dict` mapping hyperparameters to the values used in
            this session. Keys should be the names of `HParam` objects used
            in an experiment, or the `HParam` objects themselves. Values
            should be Python `bool`, `int`, `float`, or `string` values,
            depending on the type of the hyperparameter.
          trial_id: An optional `str` ID for the set of hyperparameter
            values used in this trial. Defaults to a hash of the
            hyperparameters.

        Raises:
          ValueError: If two entries in `hparams` share the same
            hyperparameter name.
        """
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_train_end(self, logs: Incomplete | None = None) -> None: ...
