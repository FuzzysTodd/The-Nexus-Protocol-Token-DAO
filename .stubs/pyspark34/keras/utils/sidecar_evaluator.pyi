from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer

def list_checkpoint_attributes(ckpt_dir_or_file):
    '''Lists all the attributes in a checkpoint.

    Checkpoint keys are paths in a checkpoint graph, and attribute is the first
    element in the path. e.g. with a checkpoint key
    "optimizer/iter/.ATTRIBUTES/VARIABLE_VALUE", optimizer is the attribute. The
    attribute is also used to save/restore a variable in a checkpoint,
    e.g. tf.train.Checkpoint(optimizer=optimizer, model=model).

    Args:
      ckpt_dir_or_file: Directory with checkpoints file or path to checkpoint.

    Returns:
      Set of attributes in a checkpoint.
    '''

class SidecarEvaluator:
    '''A class designed for a dedicated evaluator task.

    `SidecarEvaluator` is expected to be run in a process on a separate machine
    from the training cluster. It is meant for the purpose of a dedicated
    evaluator, evaluating the metric results of a training cluster which has one
    or more workers performing the training, and saving checkpoints.

    The `SidecarEvaluator` API is compatible with both Custom Training Loop
    (CTL), and Keras `Model.fit` to be used in the training cluster. Using the
    model (with compiled metrics) provided at `__init__`, `SidecarEvaluator`
    repeatedly performs evaluation "epochs" when it finds a checkpoint that has
    not yet been used. Depending on the `steps` argument, an eval epoch is
    evaluation over all eval data, or up to certain number of steps (batches).
    See examples below for how the training program should save the checkpoints
    in order to be recognized by `SidecarEvaluator`.

    Since under the hood, `SidecarEvaluator` uses `model.evaluate` for
    evaluation, it also supports arbitrary Keras callbacks. That is, if one or
    more callbacks are provided, their `on_test_batch_begin` and
    `on_test_batch_end` methods are called at the start and end of a batch, and
    their `on_test_begin` and `on_test_end` are called at the start and end of
    an evaluation epoch. Note that `SidecarEvaluator` may skip some checkpoints
    because it always picks up the latest checkpoint available, and during an
    evaluation epoch, multiple checkpoints can be produced from the training
    side.

    Example:
    ```python
    model = tf.keras.models.Sequential(...)
    model.compile(metrics=tf.keras.metrics.SparseCategoricalAccuracy(
        name="eval_metrics"))
    data = tf.data.Dataset.from_tensor_slices(...)

    tf.keras.SidecarEvaluator(
        model=model,
        data=data,
        # dir for training-saved checkpoint
        checkpoint_dir=\'/tmp/checkpoint_dir\',
        steps=None,  # Eval until dataset is exhausted
        max_evaluations=None,  # The evaluation needs to be stopped manually
        callbacks=[tf.keras.callbacks.TensorBoard(log_dir=\'/tmp/log_dir\')]
    ).start()
    ```

    `SidecarEvaluator.start` writes a series of summary files which can be
    visualized by tensorboard (which provides a webpage link):

    ```bash
    $ tensorboard --logdir=/tmp/log_dir/validation
    ...
    TensorBoard 2.4.0a0 at http://host:port (Press CTRL+C to quit)
    ```

    If the training cluster uses a CTL, the `checkpoint_dir` should contain
    checkpoints that track both `model` and `optimizer`, to fulfill
    `SidecarEvaluator`\'s expectation. This can be done by a
    `tf.train.Checkpoint` and a `tf.train.CheckpointManager`:

    ```python
    # Same `checkpoint_dir` supplied to `SidecarEvaluator`.
    checkpoint_dir = ...
    checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
    checkpoint_manager = tf.train.CheckpointManager(
        checkpoint, checkpoint_dir=..., max_to_keep=...)
    checkpoint_manager.save()
    ```

    If the training cluster uses Keras `Model.fit` API, a
    `tf.keras.callbacks.ModelCheckpoint` should be used, with
    `save_weights_only=True`, and the `filepath` should have \'ckpt-{epoch}\'
    appended:

    ```python
    # Same `checkpoint_dir` supplied to `SidecarEvaluator`.
    checkpoint_dir = ...
    model_checkpoint = tf.keras.callbacks.ModelCheckpoint(
        filepath=os.path.join(checkpoint_dir, \'ckpt-{epoch}\'),
        save_weights_only=True)
    model.fit(dataset, epochs, callbacks=[model_checkpoint])
    ```
    '''
    model: Incomplete
    data: Incomplete
    checkpoint_dir: Incomplete
    max_evaluations: Incomplete
    steps: Incomplete
    callbacks: Incomplete
    def __init__(self, model, data, checkpoint_dir, steps: Incomplete | None = None, max_evaluations: Incomplete | None = None, callbacks: Incomplete | None = None) -> None:
        """Initializes an `SidecarEvaluator` object.

        Args:
          model: Model to use for evaluation. The model object used here should
            be a `tf.keras.Model`, and should be the same as the one that is
            used in training, where `tf.keras.Model`s are checkpointed. The
            model should have one or more metrics compiled before using
            `SidecarEvaluator`.
          data: The input data for evaluation. `SidecarEvaluator` supports all
            data types that Keras `model.evaluate` supports as the input data
            `x`, such as a `tf.data.Dataset`.
          checkpoint_dir: Directory where checkpoint files are saved.
          steps: Number of steps to perform evaluation for, when evaluating a
            single checkpoint file. If `None`, evaluation continues until the
            dataset is exhausted. For repeated evaluation dataset, user must
            specify `steps` to avoid infinite evaluation loop.
          max_evaluations: Maximum number of the checkpoint file to be
            evaluated, for `SidecarEvaluator` to know when to stop. The
            evaluator will stop after it evaluates a checkpoint filepath ending
            with '<ckpt_name>-<max_evaluations>'. If using
            `tf.train.CheckpointManager.save` for saving checkpoints, the kth
            saved checkpoint has the filepath suffix '<ckpt_name>-<k>' (k=1 for
            the first saved), and if checkpoints are saved every epoch after
            training, the filepath saved at the kth epoch would end with
            '<ckpt_name>-<k>. Thus, if training runs for n epochs, and the
            evaluator should end after the training finishes, use n for this
            parameter. Note that this is not necessarily equal to the number of
            total evaluations, since some checkpoints may be skipped if
            evaluation is slower than checkpoint creation. If `None`,
            `SidecarEvaluator` will evaluate indefinitely, and the user must
            terminate evaluator program themselves.
          callbacks: List of `keras.callbacks.Callback` instances to apply
            during evaluation. See
            [callbacks](/api_docs/python/tf/keras/callbacks).
        """
    def start(self) -> None:
        """Starts the evaluation loop."""

class SidecarEvaluatorExperimental(SidecarEvaluator):
    """Deprecated. Please use `tf.keras.utils.SidecarEvaluator` instead.

    Caution: `tf.keras.experimental.SidecarEvaluator` endpoint is
      deprecated and will be removed in a future release. Please use
      `tf.keras.utils.SidecarEvaluator`.
    """
    def __init__(self, *args, **kwargs) -> None: ...
