from _typeshed import Incomplete
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management
from tensorflow.python.data.ops import iterator_ops as iterator_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, saver as saver_lib, session_run_hook as session_run_hook
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def make_saveable_from_iterator(iterator, external_state_policy: Incomplete | None = None):
    """Returns a SaveableObject for saving/restoring iterator state using Saver.

  Args:
    iterator: Iterator.
    external_state_policy: A string that identifies how to handle input
      pipelines that depend on external state. Possible values are
      'ignore': The external state is silently ignored.
      'warn': The external state is ignored, logging a warning.
      'fail': The operation fails upon encountering external state.
      By default we set it to 'fail'.

  Returns:
    A SaveableObject for saving/restoring iterator state using Saver.

  Raises:
    ValueError: If iterator does not support checkpointing.
    ValueError: If `external_state_policy` is not one of 'warn', 'ignore' or
      'fail'.

  For example:

  ```python
  with tf.Graph().as_default():
    ds = tf.data.Dataset.range(10)
    iterator = ds.make_initializable_iterator()
    # Build the iterator SaveableObject.
    saveable_obj = tf.data.experimental.make_saveable_from_iterator(iterator)
    # Add the SaveableObject to the SAVEABLE_OBJECTS collection so
    # it can be automatically saved using Saver.
    tf.compat.v1.add_to_collection(tf.GraphKeys.SAVEABLE_OBJECTS, saveable_obj)
    saver = tf.compat.v1.train.Saver()

    while continue_training:
      ... Perform training ...
      if should_save_checkpoint:
        saver.save()
  ```

  Note: When restoring the iterator, the existing iterator state is completely
  discarded. This means that any changes you may have made to the Dataset
  graph will be discarded as well! This includes the new Dataset graph
  that you may have built during validation. So, while running validation,
  make sure to run the initializer for the validation input pipeline after
  restoring the checkpoint.

  Note: Not all iterators support checkpointing yet. Attempting to save the
  state of an unsupported iterator will throw an error.
  """

class CheckpointInputPipelineHook(session_run_hook.SessionRunHook):
    '''Checkpoints input pipeline state every N steps or seconds.

  This hook saves the state of the iterators in the `Graph` so that when
  training is resumed the input pipeline continues from where it left off.
  This could potentially avoid overfitting in certain pipelines where the
  number of training steps per eval are small compared to the dataset
  size or if the training pipeline is pre-empted.

  Differences from `CheckpointSaverHook`:
  1. Saves only the input pipelines in the "iterators" collection and not the
     global variables or other saveable objects.
  2. Does not write the `GraphDef` and `MetaGraphDef` to the summary.

  Example of checkpointing the training pipeline:

  ```python
  est = tf.estimator.Estimator(model_fn)
  while True:
    est.train(
        train_input_fn,
        hooks=[tf.data.experimental.CheckpointInputPipelineHook(est)],
        steps=train_steps_per_eval)
    # Note: We do not pass the hook here.
    metrics = est.evaluate(eval_input_fn)
    if should_stop_the_training(metrics):
      break
  ```

  This hook should be used if the input pipeline state needs to be saved
  separate from the model checkpoint. Doing so may be useful for a few reasons:
  1. The input pipeline checkpoint may be large, if there are large shuffle
     or prefetch buffers for instance, and may bloat the checkpoint size.
  2. If the input pipeline is shared between training and validation, restoring
     the checkpoint during validation may override the validation input
     pipeline.

  For saving the input pipeline checkpoint alongside the model weights use
  `tf.data.experimental.make_saveable_from_iterator` directly to create a
  `SaveableObject` and add to the `SAVEABLE_OBJECTS` collection. Note, however,
  that you will need to be careful not to restore the training iterator during
  eval. You can do that by not adding the iterator to the SAVEABLE_OBJECTS
  collector when building the eval graph.
  '''
    def __init__(self, estimator, external_state_policy: Incomplete | None = None) -> None:
        """Initializes a `CheckpointInputPipelineHook`.

    If the input pipeline depends on external state (e.g. seeds for
    RandomUniform) beyond the input pipeline, this hook would be unable to
    serialize and deserialize that state. If its acceptable to ignore that state
    change the external_state_policy argument to 'warn' or 'ignore'. For e.g.

    ```python
    est = tf.estimator.Estimator(model_fn)
    while True:
      est.train(
          train_input_fn,
          hooks=[tf.data.experimental.CheckpointInputPipelineHook(
              est, external_state_policy='warn')],
          steps=train_steps_per_eval)
      # Note: We do not pass the hook here.
      metrics = est.evaluate(eval_input_fn)
      if should_stop_the_training(metrics):
        break
    ```

    Args:
      estimator: Estimator.
      external_state_policy: A string that identifies how to handle input
        pipelines that depend on external state. Possible values are
        'ignore': The external state is silently ignored.
        'warn': The external state is ignored, logging a warning.
        'fail': The operation fails upon encountering external state.
        By default we set it to 'fail'.

    Raises:
      ValueError: One of `save_steps` or `save_secs` should be set.
      ValueError: At most one of saver or scaffold should be set.
      ValueError: If `external_state_policy` is not one of 'warn', 'ignore' or
        'fail'.
    """
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
    def end(self, session) -> None: ...

class _CustomSaver(saver_lib.Saver):
    """`Saver` with a different default `latest_filename`.

  This is used in the `CheckpointInputPipelineHook` to avoid conflicts with
  the model ckpt saved by the `CheckpointSaverHook`.
  """
    def __init__(self, var_list, latest_filename, sharded: bool = False) -> None: ...
    def save(self, sess, save_path, global_step: Incomplete | None = None, latest_filename: Incomplete | None = None, meta_graph_suffix: str = 'meta', write_meta_graph: bool = True, write_state: bool = True, strip_default_attrs: bool = False): ...
