from _typeshed import Incomplete
from keras import backend as backend
from keras.distribute import distributed_file_utils as distributed_file_utils, worker_training_state as worker_training_state
from keras.optimizers import optimizer as optimizer
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule
from keras.utils import generic_utils as generic_utils, io_utils as io_utils, tf_utils as tf_utils, version_utils as version_utils
from keras.utils.data_utils import Sequence as Sequence
from keras.utils.generic_utils import Progbar as Progbar
from keras.utils.mode_keys import ModeKeys as ModeKeys

def configure_callbacks(callbacks, model, do_validation: bool = False, batch_size: Incomplete | None = None, epochs: Incomplete | None = None, steps_per_epoch: Incomplete | None = None, samples: Incomplete | None = None, verbose: int = 1, count_mode: str = 'steps', mode=...):
    """Configures callbacks for use in various training loops.

    Args:
        callbacks: List of Callbacks.
        model: Model being trained.
        do_validation: Whether or not validation loop will be run.
        batch_size: Number of samples per batch.
        epochs: Number of epoch to train.
        steps_per_epoch: Number of batches to run per training epoch.
        samples: Number of training samples.
        verbose: int, 0 or 1. Keras logging verbosity to pass to ProgbarLogger.
        count_mode: One of 'steps' or 'samples'. Per-batch or per-sample count.
        mode: String. One of ModeKeys.TRAIN, ModeKeys.TEST, or ModeKeys.PREDICT.
          Which loop mode to configure callbacks for.

    Returns:
        Instance of CallbackList used to control all Callbacks.
    """
def set_callback_parameters(callback_list, model, do_validation: bool = False, batch_size: Incomplete | None = None, epochs: Incomplete | None = None, steps_per_epoch: Incomplete | None = None, samples: Incomplete | None = None, verbose: int = 1, mode=...) -> None:
    """Sets callback parameters.

    Args:
        callback_list: CallbackList instance.
        model: Model being trained.
        do_validation: Whether or not validation loop will be run.
        batch_size: Number of samples per batch.
        epochs: Number of epoch to train.
        steps_per_epoch: Number of batches to run per training epoch.
        samples: Number of training samples.
        verbose: int, 0 or 1. Keras logging verbosity to pass to ProgbarLogger.
        mode: String. One of ModeKeys.TRAIN, ModeKeys.TEST, or ModeKeys.PREDICT.
          Which loop mode to configure callbacks for.
    """
def make_logs(model, logs, outputs, mode, prefix: str = ''):
    """Computes logs for sending to `on_batch_end` methods."""

class CallbackList:
    """Container abstracting a list of callbacks."""
    callbacks: Incomplete
    def __init__(self, callbacks: Incomplete | None = None, add_history: bool = False, add_progbar: bool = False, model: Incomplete | None = None, **params) -> None:
        """Container for `Callback` instances.

        This object wraps a list of `Callback` instances, making it possible
        to call them all at once via a single endpoint
        (e.g. `callback_list.on_epoch_end(...)`).

        Args:
          callbacks: List of `Callback` instances.
          add_history: Whether a `History` callback should be added, if one does
            not already exist in the `callbacks` list.
          add_progbar: Whether a `ProgbarLogger` callback should be added, if
            one does not already exist in the `callbacks` list.
          model: The `Model` these callbacks are used with.
          **params: If provided, parameters will be passed to each `Callback`
            via `Callback.set_params`.
        """
    def append(self, callback) -> None: ...
    params: Incomplete
    def set_params(self, params) -> None: ...
    model: Incomplete
    def set_model(self, model) -> None: ...
    def on_batch_begin(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None:
        """Calls the `on_epoch_begin` methods of its callbacks.

        This function should only be called during TRAIN mode.

        Args:
            epoch: Integer, index of epoch.
            logs: Dict. Currently no data is passed to this argument for this
               method but that may change in the future.
        """
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None:
        """Calls the `on_epoch_end` methods of its callbacks.

        This function should only be called during TRAIN mode.

        Args:
            epoch: Integer, index of epoch.
            logs: Dict, metric results for this training epoch, and for the
              validation epoch if validation is performed. Validation result
              keys are prefixed with `val_`.
        """
    def on_train_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """Calls the `on_train_batch_begin` methods of its callbacks.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict, contains the return value of `model.train_step`.
              Typically, the values of the `Model`'s metrics are returned.
              Example: `{'loss': 0.2, 'accuracy': 0.7}`.
        """
    def on_train_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Calls the `on_train_batch_end` methods of its callbacks.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Aggregated metric results up until this batch.
        """
    def on_test_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """Calls the `on_test_batch_begin` methods of its callbacks.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict, contains the return value of `model.test_step`.
              Typically, the values of the `Model`'s metrics are returned.
              Example: `{'loss': 0.2, 'accuracy': 0.7}`.
        """
    def on_test_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Calls the `on_test_batch_end` methods of its callbacks.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Aggregated metric results up until this batch.
        """
    def on_predict_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """Calls the `on_predict_batch_begin` methods of its callbacks.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict, contains the return value of `model.predict_step`,
              it typically returns a dict with a key 'outputs' containing
              the model's outputs.
        """
    def on_predict_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Calls the `on_predict_batch_end` methods of its callbacks.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Aggregated metric results up until this batch.
        """
    def on_train_begin(self, logs: Incomplete | None = None) -> None:
        """Calls the `on_train_begin` methods of its callbacks.

        Args:
            logs: Dict. Currently, no data is passed via this argument
              for this method, but that may change in the future.
        """
    def on_train_end(self, logs: Incomplete | None = None) -> None:
        """Calls the `on_train_end` methods of its callbacks.

        Args:
            logs: Dict. Currently, no data is passed via this argument
              for this method, but that may change in the future.
        """
    def on_test_begin(self, logs: Incomplete | None = None) -> None:
        """Calls the `on_test_begin` methods of its callbacks.

        Args:
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_test_end(self, logs: Incomplete | None = None) -> None:
        """Calls the `on_test_end` methods of its callbacks.

        Args:
            logs: Dict. Currently, no data is passed via this argument
              for this method, but that may change in the future.
        """
    def on_predict_begin(self, logs: Incomplete | None = None) -> None:
        """Calls the 'on_predict_begin` methods of its callbacks.

        Args:
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_predict_end(self, logs: Incomplete | None = None) -> None:
        """Calls the `on_predict_end` methods of its callbacks.

        Args:
            logs: Dict. Currently, no data is passed via this argument
              for this method, but that may change in the future.
        """
    def __iter__(self): ...
    def make_logs(self, model, logs, outputs, mode, prefix: str = ''):
        """Computes logs for sending to `on_batch_end` methods."""

class Callback:
    """Abstract base class used to build new callbacks.

    Callbacks can be passed to keras methods such as `fit`, `evaluate`, and
    `predict` in order to hook into the various stages of the model training and
    inference lifecycle.

    To create a custom callback, subclass `keras.callbacks.Callback` and
    override the method associated with the stage of interest. See
    https://www.tensorflow.org/guide/keras/custom_callback for more information.

    Example:

    >>> training_finished = False
    >>> class MyCallback(tf.keras.callbacks.Callback):
    ...   def on_train_end(self, logs=None):
    ...     global training_finished
    ...     training_finished = True
    >>> model = tf.keras.Sequential([
    ...     tf.keras.layers.Dense(1, input_shape=(1,))])
    >>> model.compile(loss='mean_squared_error')
    >>> model.fit(tf.constant([[1.0]]), tf.constant([[1.0]]),
    ...           callbacks=[MyCallback()])
    >>> assert training_finished == True

    If you want to use `Callback` objects in a custom training loop:

    1. You should pack all your callbacks into a single `callbacks.CallbackList`
       so they can all be called together.
    2. You will need to manually call all the `on_*` methods at the appropriate
       locations in your loop. Like this:

    Example:
    ```python
       callbacks =  tf.keras.callbacks.CallbackList([...])
       callbacks.append(...)
       callbacks.on_train_begin(...)
       for epoch in range(EPOCHS):
         callbacks.on_epoch_begin(epoch)
         for i, data in dataset.enumerate():
           callbacks.on_train_batch_begin(i)
           batch_logs = model.train_step(data)
           callbacks.on_train_batch_end(i, batch_logs)
         epoch_logs = ...
         callbacks.on_epoch_end(epoch, epoch_logs)
       final_logs=...
       callbacks.on_train_end(final_logs)
    ```

    Attributes:
        params: Dict. Training parameters
            (eg. verbosity, batch size, number of epochs...).
        model: Instance of `keras.models.Model`.
            Reference of the model being trained.

    The `logs` dictionary that callback methods
    take as argument will contain keys for quantities relevant to
    the current batch or epoch (see method-specific docstrings).
    """
    validation_data: Incomplete
    model: Incomplete
    def __init__(self) -> None: ...
    params: Incomplete
    def set_params(self, params) -> None: ...
    def set_model(self, model) -> None: ...
    def on_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """A backwards compatibility alias for `on_train_batch_begin`."""
    def on_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """A backwards compatibility alias for `on_train_batch_end`."""
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None:
        """Called at the start of an epoch.

        Subclasses should override for any actions to run. This function should
        only be called during TRAIN mode.

        Args:
            epoch: Integer, index of epoch.
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None:
        """Called at the end of an epoch.

        Subclasses should override for any actions to run. This function should
        only be called during TRAIN mode.

        Args:
            epoch: Integer, index of epoch.
            logs: Dict, metric results for this training epoch, and for the
              validation epoch if validation is performed. Validation result
              keys are prefixed with `val_`. For training epoch, the values of
              the `Model`'s metrics are returned. Example:
              `{'loss': 0.2, 'accuracy': 0.7}`.
        """
    def on_train_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """Called at the beginning of a training batch in `fit` methods.

        Subclasses should override for any actions to run.

        Note that if the `steps_per_execution` argument to `compile` in
        `tf.keras.Model` is set to `N`, this method will only be called every
        `N` batches.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_train_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Called at the end of a training batch in `fit` methods.

        Subclasses should override for any actions to run.

        Note that if the `steps_per_execution` argument to `compile` in
        `tf.keras.Model` is set to `N`, this method will only be called every
        `N` batches.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Aggregated metric results up until this batch.
        """
    def on_test_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """Called at the beginning of a batch in `evaluate` methods.

        Also called at the beginning of a validation batch in the `fit`
        methods, if validation data is provided.

        Subclasses should override for any actions to run.

        Note that if the `steps_per_execution` argument to `compile` in
        `tf.keras.Model` is set to `N`, this method will only be called every
        `N` batches.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_test_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Called at the end of a batch in `evaluate` methods.

        Also called at the end of a validation batch in the `fit`
        methods, if validation data is provided.

        Subclasses should override for any actions to run.

        Note that if the `steps_per_execution` argument to `compile` in
        `tf.keras.Model` is set to `N`, this method will only be called every
        `N` batches.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Aggregated metric results up until this batch.
        """
    def on_predict_batch_begin(self, batch, logs: Incomplete | None = None) -> None:
        """Called at the beginning of a batch in `predict` methods.

        Subclasses should override for any actions to run.

        Note that if the `steps_per_execution` argument to `compile` in
        `tf.keras.Model` is set to `N`, this method will only be called every
        `N` batches.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_predict_batch_end(self, batch, logs: Incomplete | None = None) -> None:
        """Called at the end of a batch in `predict` methods.

        Subclasses should override for any actions to run.

        Note that if the `steps_per_execution` argument to `compile` in
        `tf.keras.Model` is set to `N`, this method will only be called every
        `N` batches.

        Args:
            batch: Integer, index of batch within the current epoch.
            logs: Dict. Aggregated metric results up until this batch.
        """
    def on_train_begin(self, logs: Incomplete | None = None) -> None:
        """Called at the beginning of training.

        Subclasses should override for any actions to run.

        Args:
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_train_end(self, logs: Incomplete | None = None) -> None:
        """Called at the end of training.

        Subclasses should override for any actions to run.

        Args:
            logs: Dict. Currently the output of the last call to
              `on_epoch_end()` is passed to this argument for this method but
              that may change in the future.
        """
    def on_test_begin(self, logs: Incomplete | None = None) -> None:
        """Called at the beginning of evaluation or validation.

        Subclasses should override for any actions to run.

        Args:
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_test_end(self, logs: Incomplete | None = None) -> None:
        """Called at the end of evaluation or validation.

        Subclasses should override for any actions to run.

        Args:
            logs: Dict. Currently the output of the last call to
              `on_test_batch_end()` is passed to this argument for this method
              but that may change in the future.
        """
    def on_predict_begin(self, logs: Incomplete | None = None) -> None:
        """Called at the beginning of prediction.

        Subclasses should override for any actions to run.

        Args:
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """
    def on_predict_end(self, logs: Incomplete | None = None) -> None:
        """Called at the end of prediction.

        Subclasses should override for any actions to run.

        Args:
            logs: Dict. Currently no data is passed to this argument for this
              method but that may change in the future.
        """

class BaseLogger(Callback):
    """Callback that accumulates epoch averages of metrics.

    This callback is automatically applied to every Keras model.

    Args:
        stateful_metrics: Iterable of string names of metrics that
            should *not* be averaged over an epoch.
            Metrics in this list will be logged as-is in `on_epoch_end`.
            All others will be averaged in `on_epoch_end`.
    """
    stateful_metrics: Incomplete
    def __init__(self, stateful_metrics: Incomplete | None = None) -> None: ...
    seen: int
    totals: Incomplete
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

class TerminateOnNaN(Callback):
    """Callback that terminates training when a NaN loss is encountered."""
    def __init__(self) -> None: ...
    def on_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...

class ProgbarLogger(Callback):
    '''Callback that prints metrics to stdout.

    Args:
        count_mode: One of `"steps"` or `"samples"`.
            Whether the progress bar should
            count samples seen or steps (batches) seen.
        stateful_metrics: Iterable of string names of metrics that
            should *not* be averaged over an epoch.
            Metrics in this list will be logged as-is.
            All others will be averaged over time (e.g. loss, etc).
            If not provided, defaults to the `Model`\'s metrics.

    Raises:
        ValueError: In case of invalid `count_mode`.
    '''
    use_steps: bool
    stateful_metrics: Incomplete
    seen: int
    progbar: Incomplete
    target: Incomplete
    verbose: int
    epochs: int
    def __init__(self, count_mode: str = 'samples', stateful_metrics: Incomplete | None = None) -> None: ...
    def set_params(self, params) -> None: ...
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_test_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_predict_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_test_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_predict_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_test_end(self, logs: Incomplete | None = None) -> None: ...
    def on_predict_end(self, logs: Incomplete | None = None) -> None: ...

class History(Callback):
    """Callback that records events into a `History` object.

    This callback is automatically applied to
    every Keras model. The `History` object
    gets returned by the `fit` method of models.

    Example:

    >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    >>> model.compile(tf.keras.optimizers.SGD(), loss='mse')
    >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
    ...                     epochs=10, verbose=1)
    >>> print(history.params)
    {'verbose': 1, 'epochs': 10, 'steps': 1}
    >>> # check the keys of history object
    >>> print(history.history.keys())
    dict_keys(['loss'])

    """
    history: Incomplete
    def __init__(self) -> None: ...
    epoch: Incomplete
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

class ModelCheckpoint(Callback):
    '''Callback to save the Keras model or model weights at some frequency.

    `ModelCheckpoint` callback is used in conjunction with training using
    `model.fit()` to save a model or weights (in a checkpoint file) at some
    interval, so the model or weights can be loaded later to continue the
    training from the state saved.

    A few options this callback provides include:

    - Whether to only keep the model that has achieved the "best performance" so
      far, or whether to save the model at the end of every epoch regardless of
      performance.
    - Definition of \'best\'; which quantity to monitor and whether it should be
      maximized or minimized.
    - The frequency it should save at. Currently, the callback supports saving
      at the end of every epoch, or after a fixed number of training batches.
    - Whether only weights are saved, or the whole model is saved.

    Note: If you get `WARNING:tensorflow:Can save best model only with <name>
    available, skipping` see the description of the `monitor` argument for
    details on how to get this right.

    Example:

    ```python
    model.compile(loss=..., optimizer=...,
                  metrics=[\'accuracy\'])

    EPOCHS = 10
    checkpoint_filepath = \'/tmp/checkpoint\'
    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_filepath,
        save_weights_only=True,
        monitor=\'val_accuracy\',
        mode=\'max\',
        save_best_only=True)

    # Model weights are saved at the end of every epoch, if it\'s the best seen
    # so far.
    model.fit(epochs=EPOCHS, callbacks=[model_checkpoint_callback])

    # The model weights (that are considered the best) are loaded into the
    # model.
    model.load_weights(checkpoint_filepath)
    ```

    Args:
        filepath: string or `PathLike`, path to save the model file. e.g.
          filepath = os.path.join(working_dir, \'ckpt\', file_name). `filepath`
          can contain named formatting options, which will be filled the value
          of `epoch` and keys in `logs` (passed in `on_epoch_end`). For example:
          if `filepath` is `weights.{epoch:02d}-{val_loss:.2f}.hdf5`, then the
          model checkpoints will be saved with the epoch number and the
          validation loss in the filename. The directory of the filepath should
          not be reused by any other callbacks to avoid conflicts.
        monitor: The metric name to monitor. Typically the metrics are set by
          the `Model.compile` method. Note:

          * Prefix the name with `"val_`" to monitor validation metrics.
          * Use `"loss"` or "`val_loss`" to monitor the model\'s total loss.
          * If you specify metrics as strings, like `"accuracy"`, pass the same
            string (with or without the `"val_"` prefix).
          * If you pass `metrics.Metric` objects, `monitor` should be set to
            `metric.name`
          * If you\'re not sure about the metric names you can check the contents
            of the `history.history` dictionary returned by
            `history = model.fit()`
          * Multi-output models set additional prefixes on the metric names.

        verbose: Verbosity mode, 0 or 1. Mode 0 is silent, and mode 1
          displays messages when the callback takes an action.
        save_best_only: if `save_best_only=True`, it only saves when the model
          is considered the "best" and the latest best model according to the
          quantity monitored will not be overwritten. If `filepath` doesn\'t
          contain formatting options like `{epoch}` then `filepath` will be
          overwritten by each new better model.
        mode: one of {\'auto\', \'min\', \'max\'}. If `save_best_only=True`, the
          decision to overwrite the current save file is made based on either
          the maximization or the minimization of the monitored quantity.
          For `val_acc`, this should be `max`, for `val_loss` this should be
          `min`, etc. In `auto` mode, the mode is set to `max` if the quantities
          monitored are \'acc\' or start with \'fmeasure\' and are set to `min` for
          the rest of the quantities.
        save_weights_only: if True, then only the model\'s weights will be saved
          (`model.save_weights(filepath)`), else the full model is saved
          (`model.save(filepath)`).
        save_freq: `\'epoch\'` or integer. When using `\'epoch\'`, the callback
          saves the model after each epoch. When using integer, the callback
          saves the model at end of this many batches. If the `Model` is
          compiled with `steps_per_execution=N`, then the saving criteria will
          be checked every Nth batch. Note that if the saving isn\'t aligned to
          epochs, the monitored metric may potentially be less reliable (it
          could reflect as little as 1 batch, since the metrics get reset every
          epoch). Defaults to `\'epoch\'`.
        options: Optional `tf.train.CheckpointOptions` object if
          `save_weights_only` is true or optional `tf.saved_model.SaveOptions`
          object if `save_weights_only` is false.
        initial_value_threshold: Floating point initial "best" value of the
          metric to be monitored. Only applies if `save_best_value=True`. Only
          overwrites the model weights already saved if the performance of
          current model is better than this value.
        **kwargs: Additional arguments for backwards compatibility. Possible key
          is `period`.
    '''
    monitor: Incomplete
    verbose: Incomplete
    filepath: Incomplete
    save_best_only: Incomplete
    save_weights_only: Incomplete
    save_freq: Incomplete
    epochs_since_last_save: int
    best: Incomplete
    load_weights_on_restart: Incomplete
    period: Incomplete
    monitor_op: Incomplete
    def __init__(self, filepath, monitor: str = 'val_loss', verbose: int = 0, save_best_only: bool = False, save_weights_only: bool = False, mode: str = 'auto', save_freq: str = 'epoch', options: Incomplete | None = None, initial_value_threshold: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

class BackupAndRestore(Callback):
    '''Callback to back up and restore the training state.

    `BackupAndRestore` callback is intended to recover training from an
    interruption that has happened in the middle of a `Model.fit` execution, by
    backing up the training states in a temporary checkpoint file (with the help
    of a `tf.train.CheckpointManager`), at the end of each epoch. Each backup
    overwrites the previously written checkpoint file, so at any given time
    there is at most one such checkpoint file for backup/restoring purpose.

    If training restarts before completion, the training state (which includes
    the `Model` weights and epoch number) is restored to the most recently saved
    state at the beginning of a new `Model.fit` run. At the completion of a
    `Model.fit` run, the temporary checkpoint file is deleted.

    Note that the user is responsible to bring jobs back after the interruption.
    This callback is important for the backup and restore mechanism for fault
    tolerance purpose, and the model to be restored from a previous checkpoint
    is expected to be the same as the one used to back up. If user changes
    arguments passed to compile or fit, the checkpoint saved for fault tolerance
    can become invalid.

    Note:

    1. This callback is not compatible with eager execution disabled.
    2. A checkpoint is saved at the end of each epoch. After restoring,
    `Model.fit` redoes any partial work during the unfinished epoch in which the
    training got restarted (so the work done before the interruption doesn\'t
    affect the final model state).
    3. This works for both single worker and multi-worker modes. When
    `Model.fit` is used with `tf.distribute`, it supports
    `tf.distribute.MirroredStrategy`,
    `tf.distribute.MultiWorkerMirroredStrategy`, `tf.distribute.TPUStrategy`,
    and `tf.distribute.experimental.ParameterServerStrategy`.

    Example:

    >>> class InterruptingCallback(tf.keras.callbacks.Callback):
    ...   def on_epoch_begin(self, epoch, logs=None):
    ...     if epoch == 4:
    ...       raise RuntimeError(\'Interrupting!\')
    >>> callback = tf.keras.callbacks.BackupAndRestore(backup_dir="/tmp/backup")
    >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    >>> model.compile(tf.keras.optimizers.SGD(), loss=\'mse\')
    >>> try:
    ...   model.fit(np.arange(100).reshape(5, 20), np.zeros(5), epochs=10,
    ...             batch_size=1, callbacks=[callback, InterruptingCallback()],
    ...             verbose=0)
    ... except:
    ...   pass
    >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
    ...                     epochs=10, batch_size=1, callbacks=[callback],
    ...                     verbose=0)
    >>> # Only 6 more epochs are run, since first training got interrupted at
    >>> # zero-indexed epoch 4, second training will continue from 4 to 9.
    >>> len(history.history[\'loss\'])
    6

    Besides the option to save at the end of every epoch or every N steps, if
    you are doing distributed training with
    `tf.distribute.MultiWorkerMirroredStrategy` on Google Cloud Platform or
    Google Borg, you can also use the `save_before_preemption` argument
    to enable saving a checkpoint right before a worker gets preempted
    by other jobs and training gets interrupted. See
    `tf.distribute.experimental.PreemptionCheckpointHandler` for more details.

    Args:
        backup_dir: String, path to store the checkpoint.
          e.g. `backup_dir = os.path.join(working_dir, \'backup\')`.
          This is the directory in which the system stores temporary files to
          recover the model from jobs terminated unexpectedly. The directory
          cannot be reused elsewhere to store other files, e.g. by the
          `BackupAndRestore` callback of another training run,
          or by another callback
          (e.g. `ModelCheckpoint`) of the same training.
        save_freq: `\'epoch\'`, integer, or `False`. When set to `\'epoch\'`
          the callback saves the checkpoint at the end of each epoch.
          When set to an integer, the callback saves the checkpoint every
          `save_freq` batches. Set `save_freq` to `False` if only using
          preemption checkpointing (with `save_before_preemption=True`).
        delete_checkpoint: Boolean, default to True. This `BackupAndRestore`
          callback works by saving a checkpoint to back up the training state.
          If `delete_checkpoint=True`, the checkpoint will be deleted after
          training is finished. Use `False` if you\'d like to keep the checkpoint
          for future usage.
        save_before_preemption: A boolean value instructing whether to turn on
          the automatic checkpoint saving for preemption/maintenance events.
          This only supports
          `tf.distribute.MultiWorkerMirroredStrategy` on Google Cloud Platform
          or Google Borg for now.
    '''
    backup_dir: Incomplete
    save_freq: Incomplete
    delete_checkpoint: Incomplete
    save_before_preemption: Incomplete
    def __init__(self, backup_dir, save_freq: str = 'epoch', delete_checkpoint: bool = True, save_before_preemption: bool = False) -> None: ...
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_begin(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_train_end(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

class BackupAndRestoreExperimental(BackupAndRestore):
    """Deprecated. Please use `tf.keras.callbacks.BackupAndRestore` instead.

    Caution: `tf.keras.callbacks.experimental.BackupAndRestore` endpoint is
      deprecated and will be removed in a future release. Please use
      `tf.keras.callbacks.BackupAndRestore`.
    """
    def __init__(self, *args, **kwargs) -> None: ...

class EarlyStopping(Callback):
    '''Stop training when a monitored metric has stopped improving.

    Assuming the goal of a training is to minimize the loss. With this, the
    metric to be monitored would be `\'loss\'`, and mode would be `\'min\'`. A
    `model.fit()` training loop will check at end of every epoch whether
    the loss is no longer decreasing, considering the `min_delta` and
    `patience` if applicable. Once it\'s found no longer decreasing,
    `model.stop_training` is marked True and the training terminates.

    The quantity to be monitored needs to be available in `logs` dict.
    To make it so, pass the loss or metrics at `model.compile()`.

    Args:
      monitor: Quantity to be monitored.
      min_delta: Minimum change in the monitored quantity
          to qualify as an improvement, i.e. an absolute
          change of less than min_delta, will count as no
          improvement.
      patience: Number of epochs with no improvement
          after which training will be stopped.
      verbose: Verbosity mode, 0 or 1. Mode 0 is silent, and mode 1
          displays messages when the callback takes an action.
      mode: One of `{"auto", "min", "max"}`. In `min` mode,
          training will stop when the quantity
          monitored has stopped decreasing; in `"max"`
          mode it will stop when the quantity
          monitored has stopped increasing; in `"auto"`
          mode, the direction is automatically inferred
          from the name of the monitored quantity.
      baseline: Baseline value for the monitored quantity.
          Training will stop if the model doesn\'t show improvement over the
          baseline.
      restore_best_weights: Whether to restore model weights from
          the epoch with the best value of the monitored quantity.
          If False, the model weights obtained at the last step of
          training are used. An epoch will be restored regardless
          of the performance relative to the `baseline`. If no epoch
          improves on `baseline`, training will run for `patience`
          epochs and restore weights from the best epoch in that set.
      start_from_epoch: Number of epochs to wait before starting
          to monitor improvement. This allows for a warm-up period in which
          no improvement is expected and thus training will not be stopped.


    Example:

    >>> callback = tf.keras.callbacks.EarlyStopping(monitor=\'loss\', patience=3)
    >>> # This callback will stop the training when there is no improvement in
    >>> # the loss for three consecutive epochs.
    >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    >>> model.compile(tf.keras.optimizers.SGD(), loss=\'mse\')
    >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
    ...                     epochs=10, batch_size=1, callbacks=[callback],
    ...                     verbose=0)
    >>> len(history.history[\'loss\'])  # Only 4 epochs are run.
    4
    '''
    monitor: Incomplete
    patience: Incomplete
    verbose: Incomplete
    baseline: Incomplete
    min_delta: Incomplete
    wait: int
    stopped_epoch: int
    restore_best_weights: Incomplete
    best_weights: Incomplete
    start_from_epoch: Incomplete
    monitor_op: Incomplete
    def __init__(self, monitor: str = 'val_loss', min_delta: int = 0, patience: int = 0, verbose: int = 0, mode: str = 'auto', baseline: Incomplete | None = None, restore_best_weights: bool = False, start_from_epoch: int = 0) -> None: ...
    best: Incomplete
    best_epoch: int
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_train_end(self, logs: Incomplete | None = None) -> None: ...
    def get_monitor_value(self, logs): ...

class RemoteMonitor(Callback):
    '''Callback used to stream events to a server.

    Requires the `requests` library.
    Events are sent to `root + \'/publish/epoch/end/\'` by default. Calls are
    HTTP POST, with a `data` argument which is a
    JSON-encoded dictionary of event data.
    If `send_as_json=True`, the content type of the request will be
    `"application/json"`.
    Otherwise the serialized JSON will be sent within a form.

    Args:
      root: String; root url of the target server.
      path: String; path relative to `root` to which the events will be sent.
      field: String; JSON field under which the data will be stored.
          The field is used only if the payload is sent within a form
          (i.e. send_as_json is set to False).
      headers: Dictionary; optional custom HTTP headers.
      send_as_json: Boolean; whether the request should be
          sent as `"application/json"`.
    '''
    root: Incomplete
    path: Incomplete
    field: Incomplete
    headers: Incomplete
    send_as_json: Incomplete
    def __init__(self, root: str = 'http://localhost:9000', path: str = '/publish/epoch/end/', field: str = 'data', headers: Incomplete | None = None, send_as_json: bool = False) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

class LearningRateScheduler(Callback):
    """Learning rate scheduler.

    At the beginning of every epoch, this callback gets the updated learning
    rate value from `schedule` function provided at `__init__`, with the current
    epoch and current learning rate, and applies the updated learning rate on
    the optimizer.

    Args:
      schedule: a function that takes an epoch index (integer, indexed from 0)
          and current learning rate (float) as inputs and returns a new
          learning rate as output (float).
      verbose: int. 0: quiet, 1: update messages.

    Example:

    >>> # This function keeps the initial learning rate for the first ten epochs
    >>> # and decreases it exponentially after that.
    >>> def scheduler(epoch, lr):
    ...   if epoch < 10:
    ...     return lr
    ...   else:
    ...     return lr * tf.math.exp(-0.1)
    >>>
    >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    >>> model.compile(tf.keras.optimizers.SGD(), loss='mse')
    >>> round(model.optimizer.lr.numpy(), 5)
    0.01

    >>> callback = tf.keras.callbacks.LearningRateScheduler(scheduler)
    >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
    ...                     epochs=15, callbacks=[callback], verbose=0)
    >>> round(model.optimizer.lr.numpy(), 5)
    0.00607

    """
    schedule: Incomplete
    verbose: Incomplete
    def __init__(self, schedule, verbose: int = 0) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

def keras_model_summary(name, data, step: Incomplete | None = None):
    """Writes a Keras model as JSON to as a Summary.

    Writing the Keras model configuration allows the TensorBoard graph plugin to
    render a conceptual graph, as opposed to graph of ops. In case the model
    fails to serialize as JSON, it ignores and returns False.

    Args:
      name: A name for this summary. The summary tag used for TensorBoard will
        be this name prefixed by any active name scopes.
      data: A Keras Model to write.
      step: Explicit `int64`-castable monotonic step value for this summary. If
        omitted, this defaults to `tf.summary.experimental.get_step()`, which
        must not be None.

    Returns:
      True on success, or False if no summary was written because no default
      summary writer was available.

    Raises:
      ValueError: if a default writer exists, but no step was provided and
        `tf.summary.experimental.get_step()` is None.
    """

class TensorBoard(Callback, version_utils.TensorBoardVersionSelector):
    '''Enable visualizations for TensorBoard.

    TensorBoard is a visualization tool provided with TensorFlow.

    This callback logs events for TensorBoard, including:

    * Metrics summary plots
    * Training graph visualization
    * Weight histograms
    * Sampled profiling

    When used in `Model.evaluate`, in addition to epoch summaries, there will be
    a summary that records evaluation metrics vs `Model.optimizer.iterations`
    written. The metric names will be prepended with `evaluation`, with
    `Model.optimizer.iterations` being the step in the visualized TensorBoard.

    If you have installed TensorFlow with pip, you should be able
    to launch TensorBoard from the command line:

    ```
    tensorboard --logdir=path_to_your_logs
    ```

    You can find more information about TensorBoard
    [here](https://www.tensorflow.org/get_started/summaries_and_tensorboard).

    Args:
        log_dir: the path of the directory where to save the log files to be
          parsed by TensorBoard. e.g. log_dir = os.path.join(working_dir,
          \'logs\') This directory should not be reused by any other callbacks.
        histogram_freq: frequency (in epochs) at which to compute
          weight histograms for the layers of the model. If set to 0, histograms
          won\'t be computed. Validation data (or split) must be specified for
          histogram visualizations.
        write_graph: whether to visualize the graph in TensorBoard. The log file
          can become quite large when write_graph is set to True.
        write_images: whether to write model weights to visualize as image in
          TensorBoard.
        write_steps_per_second: whether to log the training steps per second
          into TensorBoard. This supports both epoch and batch frequency
          logging.
        update_freq: `\'batch\'` or `\'epoch\'` or integer. When using `\'epoch\'`,
          writes the losses and metrics to TensorBoard after every epoch.
          If using an integer, let\'s say `1000`, all metrics and losses
          (including custom ones added by `Model.compile`) will be logged to
          TensorBoard every 1000 batches. `\'batch\'` is a synonym for `1`,
          meaning that they will be written every batch.
          Note however that writing too frequently to TensorBoard can slow down
          your training, especially when used with `tf.distribute.Strategy` as
          it will incur additional synchronization overhead.
          Use with `ParameterServerStrategy` is not supported.
          Batch-level summary writing is also available via `train_step`
          override. Please see
          [TensorBoard Scalars tutorial](https://www.tensorflow.org/tensorboard/scalars_and_keras#batch-level_logging)  # noqa: E501
          for more details.
        profile_batch: Profile the batch(es) to sample compute characteristics.
          profile_batch must be a non-negative integer or a tuple of integers.
          A pair of positive integers signify a range of batches to profile.
          By default, profiling is disabled.
        embeddings_freq: frequency (in epochs) at which embedding layers will be
          visualized. If set to 0, embeddings won\'t be visualized.
        embeddings_metadata: Dictionary which maps embedding layer names to the
          filename of a file in which to save metadata for the embedding layer.
          In case the same metadata file is to be
          used for all embedding layers, a single filename can be passed.

    Examples:

    Basic usage:

    ```python
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
    model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
    # Then run the tensorboard command to view the visualizations.
    ```

    Custom batch-level summaries in a subclassed Model:

    ```python
    class MyModel(tf.keras.Model):

      def build(self, _):
        self.dense = tf.keras.layers.Dense(10)

      def call(self, x):
        outputs = self.dense(x)
        tf.summary.histogram(\'outputs\', outputs)
        return outputs

    model = MyModel()
    model.compile(\'sgd\', \'mse\')

    # Make sure to set `update_freq=N` to log a batch-level summary every N
    # batches.  In addition to any `tf.summary` contained in `Model.call`,
    # metrics added in `Model.compile` will be logged every N batches.
    tb_callback = tf.keras.callbacks.TensorBoard(\'./logs\', update_freq=1)
    model.fit(x_train, y_train, callbacks=[tb_callback])
    ```

    Custom batch-level summaries in a Functional API Model:

    ```python
    def my_summary(x):
      tf.summary.histogram(\'x\', x)
      return x

    inputs = tf.keras.Input(10)
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Lambda(my_summary)(x)
    model = tf.keras.Model(inputs, outputs)
    model.compile(\'sgd\', \'mse\')

    # Make sure to set `update_freq=N` to log a batch-level summary every N
    # batches. In addition to any `tf.summary` contained in `Model.call`,
    # metrics added in `Model.compile` will be logged every N batches.
    tb_callback = tf.keras.callbacks.TensorBoard(\'./logs\', update_freq=1)
    model.fit(x_train, y_train, callbacks=[tb_callback])
    ```

    Profiling:

    ```python
    # Profile a single batch, e.g. the 5th batch.
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=\'./logs\', profile_batch=5)
    model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])

    # Profile a range of batches, e.g. from 10 to 20.
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=\'./logs\', profile_batch=(10,20))
    model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
    ```
    '''
    log_dir: Incomplete
    histogram_freq: Incomplete
    write_graph: Incomplete
    write_images: Incomplete
    write_steps_per_second: Incomplete
    update_freq: Incomplete
    embeddings_freq: Incomplete
    embeddings_metadata: Incomplete
    def __init__(self, log_dir: str = 'logs', histogram_freq: int = 0, write_graph: bool = True, write_images: bool = False, write_steps_per_second: bool = False, update_freq: str = 'epoch', profile_batch: int = 0, embeddings_freq: int = 0, embeddings_metadata: Incomplete | None = None, **kwargs) -> None: ...
    model: Incomplete
    def set_model(self, model) -> None:
        """Sets Keras model and writes graph if specified."""
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_train_end(self, logs: Incomplete | None = None) -> None: ...
    def on_test_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_test_end(self, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_begin(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_train_batch_end(self, batch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_begin(self, epoch, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None:
        """Runs metrics and histogram summaries at epoch end."""

class ReduceLROnPlateau(Callback):
    """Reduce learning rate when a metric has stopped improving.

    Models often benefit from reducing the learning rate by a factor
    of 2-10 once learning stagnates. This callback monitors a
    quantity and if no improvement is seen for a 'patience' number
    of epochs, the learning rate is reduced.

    Example:

    ```python
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                                  patience=5, min_lr=0.001)
    model.fit(X_train, Y_train, callbacks=[reduce_lr])
    ```

    Args:
        monitor: quantity to be monitored.
        factor: factor by which the learning rate will be reduced.
          `new_lr = lr * factor`.
        patience: number of epochs with no improvement after which learning rate
          will be reduced.
        verbose: int. 0: quiet, 1: update messages.
        mode: one of `{'auto', 'min', 'max'}`. In `'min'` mode,
          the learning rate will be reduced when the
          quantity monitored has stopped decreasing; in `'max'` mode it will be
          reduced when the quantity monitored has stopped increasing; in
          `'auto'` mode, the direction is automatically inferred from the name
          of the monitored quantity.
        min_delta: threshold for measuring the new optimum, to only focus on
          significant changes.
        cooldown: number of epochs to wait before resuming normal operation
          after lr has been reduced.
        min_lr: lower bound on the learning rate.
    """
    monitor: Incomplete
    factor: Incomplete
    min_lr: Incomplete
    min_delta: Incomplete
    patience: Incomplete
    verbose: Incomplete
    cooldown: Incomplete
    cooldown_counter: int
    wait: int
    best: int
    mode: Incomplete
    monitor_op: Incomplete
    def __init__(self, monitor: str = 'val_loss', factor: float = 0.1, patience: int = 10, verbose: int = 0, mode: str = 'auto', min_delta: float = 0.0001, cooldown: int = 0, min_lr: int = 0, **kwargs) -> None: ...
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...
    def in_cooldown(self): ...

class CSVLogger(Callback):
    """Callback that streams epoch results to a CSV file.

    Supports all values that can be represented as a string,
    including 1D iterables such as `np.ndarray`.

    Example:

    ```python
    csv_logger = CSVLogger('training.log')
    model.fit(X_train, Y_train, callbacks=[csv_logger])
    ```

    Args:
        filename: Filename of the CSV file, e.g. `'run/log.csv'`.
        separator: String used to separate elements in the CSV file.
        append: Boolean. True: append if file exists (useful for continuing
            training). False: overwrite existing file.
    """
    sep: Incomplete
    filename: Incomplete
    append: Incomplete
    writer: Incomplete
    keys: Incomplete
    append_header: bool
    def __init__(self, filename, separator: str = ',', append: bool = False) -> None: ...
    csv_file: Incomplete
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None): ...
    def on_train_end(self, logs: Incomplete | None = None) -> None: ...

class LambdaCallback(Callback):
    """Callback for creating simple, custom callbacks on-the-fly.

    This callback is constructed with anonymous functions that will be called
    at the appropriate time (during `Model.{fit | evaluate | predict}`).
    Note that the callbacks expects positional arguments, as:

    - `on_epoch_begin` and `on_epoch_end` expect two positional arguments:
      `epoch`, `logs`
    - `on_batch_begin` and `on_batch_end` expect two positional arguments:
      `batch`, `logs`
    - `on_train_begin` and `on_train_end` expect one positional argument:
      `logs`

    Args:
        on_epoch_begin: called at the beginning of every epoch.
        on_epoch_end: called at the end of every epoch.
        on_batch_begin: called at the beginning of every batch.
        on_batch_end: called at the end of every batch.
        on_train_begin: called at the beginning of model training.
        on_train_end: called at the end of model training.

    Example:

    ```python
    # Print the batch number at the beginning of every batch.
    batch_print_callback = LambdaCallback(
        on_batch_begin=lambda batch,logs: print(batch))

    # Stream the epoch loss to a file in JSON format. The file content
    # is not well-formed JSON but rather has a JSON object per line.
    import json
    json_log = open('loss_log.json', mode='wt', buffering=1)
    json_logging_callback = LambdaCallback(
        on_epoch_end=lambda epoch, logs: json_log.write(
            json.dumps({'epoch': epoch, 'loss': logs['loss']}) + '\\n'),
        on_train_end=lambda logs: json_log.close()
    )

    # Terminate some processes after having finished model training.
    processes = ...
    cleanup_callback = LambdaCallback(
        on_train_end=lambda logs: [
            p.terminate() for p in processes if p.is_alive()])

    model.fit(...,
              callbacks=[batch_print_callback,
                         json_logging_callback,
                         cleanup_callback])
    ```
    """
    on_epoch_begin: Incomplete
    on_epoch_end: Incomplete
    on_batch_begin: Incomplete
    on_batch_end: Incomplete
    on_train_begin: Incomplete
    on_train_end: Incomplete
    def __init__(self, on_epoch_begin: Incomplete | None = None, on_epoch_end: Incomplete | None = None, on_batch_begin: Incomplete | None = None, on_batch_end: Incomplete | None = None, on_train_begin: Incomplete | None = None, on_train_end: Incomplete | None = None, **kwargs) -> None: ...
