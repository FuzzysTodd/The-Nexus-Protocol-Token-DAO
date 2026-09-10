from _typeshed import Incomplete
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.ops import state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.training import checkpoint_ops as checkpoint_ops, checkpoint_utils as checkpoint_utils
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class VocabInfo(NamedTuple('VocabInfo', [('new_vocab', Incomplete), ('new_vocab_size', Incomplete), ('num_oov_buckets', Incomplete), ('old_vocab', Incomplete), ('old_vocab_size', Incomplete), ('backup_initializer', Incomplete), ('axis', Incomplete)])):
    """Vocabulary information for warm-starting.

  See `tf.estimator.WarmStartSettings` for examples of using
  VocabInfo to warm-start.

  Args:
    new_vocab: [Required] A path to the new vocabulary file (used with the model
      to be trained).
    new_vocab_size: [Required] An integer indicating how many entries of the new
      vocabulary will used in training.
    num_oov_buckets: [Required] An integer indicating how many OOV buckets are
      associated with the vocabulary.
    old_vocab: [Required] A path to the old vocabulary file (used with the
      checkpoint to be warm-started from).
    old_vocab_size: [Optional] An integer indicating how many entries of the old
      vocabulary were used in the creation of the checkpoint. If not provided,
      the entire old vocabulary will be used.
    backup_initializer: [Optional] A variable initializer used for variables
      corresponding to new vocabulary entries and OOV. If not provided, these
      entries will be zero-initialized.
    axis: [Optional] Denotes what axis the vocabulary corresponds to.  The
      default, 0, corresponds to the most common use case (embeddings or
      linear weights for binary classification / regression).  An axis of 1
      could be used for warm-starting output layers with class vocabularies.

  Returns:
    A `VocabInfo` which represents the vocabulary information for warm-starting.

  Raises:
    ValueError: `axis` is neither 0 or 1.

      Example Usage:
```python
      embeddings_vocab_info = tf.VocabInfo(
          new_vocab='embeddings_vocab',
          new_vocab_size=100,
          num_oov_buckets=1,
          old_vocab='pretrained_embeddings_vocab',
          old_vocab_size=10000,
          backup_initializer=tf.compat.v1.truncated_normal_initializer(
              mean=0.0, stddev=(1 / math.sqrt(embedding_dim))),
          axis=0)

      softmax_output_layer_kernel_vocab_info = tf.VocabInfo(
          new_vocab='class_vocab',
          new_vocab_size=5,
          num_oov_buckets=0,  # No OOV for classes.
          old_vocab='old_class_vocab',
          old_vocab_size=8,
          backup_initializer=tf.compat.v1.glorot_uniform_initializer(),
          axis=1)

      softmax_output_layer_bias_vocab_info = tf.VocabInfo(
          new_vocab='class_vocab',
          new_vocab_size=5,
          num_oov_buckets=0,  # No OOV for classes.
          old_vocab='old_class_vocab',
          old_vocab_size=8,
          backup_initializer=tf.compat.v1.zeros_initializer(),
          axis=0)

      #Currently, only axis=0 and axis=1 are supported.
  ```
  """
    def __new__(cls, new_vocab, new_vocab_size, num_oov_buckets, old_vocab, old_vocab_size: int = -1, backup_initializer: Incomplete | None = None, axis: int = 0): ...

def warm_start(ckpt_to_initialize_from, vars_to_warm_start: str = '.*', var_name_to_vocab_info: Incomplete | None = None, var_name_to_prev_var_name: Incomplete | None = None) -> None:
    '''Warm-starts a model using the given settings.

  If you are using a tf.estimator.Estimator, this will automatically be called
  during training.

  Args:
    ckpt_to_initialize_from: [Required] A string specifying the directory with
      checkpoint file(s) or path to checkpoint from which to warm-start the
      model parameters.
    vars_to_warm_start: [Optional] One of the following:

      - A regular expression (string) that captures which variables to
        warm-start (see tf.compat.v1.get_collection).  This expression will only
        consider variables in the TRAINABLE_VARIABLES collection -- if you need
        to warm-start non_TRAINABLE vars (such as optimizer accumulators or
        batch norm statistics), please use the below option.
      - A list of strings, each a regex scope provided to
        tf.compat.v1.get_collection with GLOBAL_VARIABLES (please see
        tf.compat.v1.get_collection).  For backwards compatibility reasons,
        this is separate from the single-string argument type.
      - A list of Variables to warm-start.  If you do not have access to the
        `Variable` objects at the call site, please use the above option.
      - `None`, in which case only TRAINABLE variables specified in
        `var_name_to_vocab_info` will be warm-started.

      Defaults to `\'.*\'`, which warm-starts all variables in the
      TRAINABLE_VARIABLES collection.  Note that this excludes variables such
      as accumulators and moving statistics from batch norm.
    var_name_to_vocab_info: [Optional] Dict of variable names (strings) to
      `tf.estimator.VocabInfo`. The variable names should be "full" variables,
      not the names of the partitions.  If not explicitly provided, the variable
      is assumed to have no (changes to) vocabulary.
    var_name_to_prev_var_name: [Optional] Dict of variable names (strings) to
      name of the previously-trained variable in `ckpt_to_initialize_from`. If
      not explicitly provided, the name of the variable is assumed to be same
      between previous checkpoint and current model.  Note that this has no
      effect on the set of variables that is warm-started, and only controls
      name mapping (use `vars_to_warm_start` for controlling what variables to
      warm-start).

  Raises:
    ValueError: If the WarmStartSettings contains prev_var_name or VocabInfo
      configuration for variable names that are not used.  This is to ensure
      a stronger check for variable configuration than relying on users to
      examine the logs.
  '''
