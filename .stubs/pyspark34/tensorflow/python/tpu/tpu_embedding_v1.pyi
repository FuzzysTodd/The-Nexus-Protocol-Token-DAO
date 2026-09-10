from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context, tpu_strategy as tpu_strategy
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, embedding_ops as embedding_ops, math_ops as math_ops, sparse_ops as sparse_ops, variables as tf_variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.tpu import tpu as tpu, tpu_embedding_base as tpu_embedding_base, tpu_embedding_v2_utils as tpu_embedding_v2_utils
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Dict, Iterable, Optional, Union

class TPUEmbeddingV0(tpu_embedding_base.TPUEmbeddingBase):
    """The TPUEmbedding mid level API running on TPU without Embedding accelerator.

  NOTE: This mid level API is not intended for large embedding table lookup.
  Embedding tables will be replicated across devices rather than sharding
  across them. To do large embedding table lookup, please use the
  `tpu.experimental.embedding.TPUEmbedding` class. This class is an alternative
  way to do embedding lookups when the TPU doesn't support any version of
  embedding feature. See
  `tpu.experimental.tpu_hardware_feature.embedding_feature` for a detailed
  explanation.

  This class has to be created under the `TPUStrategy`, Otherwise a RuntimeError
  will be raised.
  ```python
  strategy = tf.distribute.TPUStrategy(...)
  with strategy.scope():
    embedding = tf.tpu.experimental.embedding.TPUEmbeddingV0(
        feature_config=feature_config,
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))
  ```
  When creating a distributed dataset that is to be passed to the lookup
  operation a special input option must be specified:

  ```python
  distributed_dataset = (
      strategy.distribute_datasets_from_function(
          dataset_fn=...,
          options=tf.distribute.InputOptions(
              experimental_fetch_to_device=False))
  dataset_iterator = iter(distributed_dataset)
  ```

  Below is an example of a training and evaluation step:

  ```python
  optimizer = tf.keras.optimizers.SGD(0.1)

  @tf.function
  def training_step(dataset_iterator, num_steps):
    def tpu_step(embedding_features):
      with tf.GradientTape() as tape:
        tape.watch(embedding.embedding_table.values())
        activation = embedding(embedding_features)
        model_output = model(activations)
        loss = ...  # some function of labels and model_output

      embedding_gradients = tape.gradient(loss,
                                          embedding.embedding_table.values())
      optimizer.apply_gradients(list(zip(gradients,
                                mid_level_api.embedding_tables.values())))
      # Insert your model gradient and optimizer application here

    for _ in tf.range(num_steps):
      strategy.run(tpu_step, args=(next(dataset_iterator), ))

  @tf.function
  def evalution_step(dataset_iterator, num_steps):
    def tpu_step(embedding_features):
      activations = embedding(embedding_features)
      model_output = model(activations)
      # Insert your evaluation code here.

    for _ in tf.range(num_steps):
      strategy.run(tpu_step, args=(next(dataset_iterator), ))
  ```

  NOTE: The optimizer used here is a Keras optimizer. In order to make the slot
  variable creation stay consistent between Keras optimizers and
  embedding optimizers, the `slot_variable_creation_fn` argument of the
  embedding optimizers has to be passed with the Keras `add_slot` function. Also
  note that the slot names might be slightly different between them.

  ```python
  optimizer = tf.keras.optimizers.Adagrad(learning_rate=0.1)

  def slot_variable_creation_fn(table, slot_names, slot_initializers):
      slots = {}
      for slot, initializer in zip(slot_names, slot_initializers):
        slots[slot] = optimizer.add_slot(table, slot, initializer)
      return slots

  embedding_optimizer = tf.experimental.embedding.Adagrad(
      learning_rate=0.1,
      slot_variable_creation_fn=slot_variable_creation_fn)

  # Use the embedding optimizer to create mid level api and keras optimizer to
  # apply gradients.
  ```
  """
    def __init__(self, feature_config: Union[tpu_embedding_v2_utils.FeatureConfig, Iterable], optimizer: Optional[tpu_embedding_v2_utils._Optimizer]) -> None: ...
    @property
    def embedding_tables(self) -> Dict[tpu_embedding_v2_utils.TableConfig, tf_variables.Variable]:
        """Returns a dict of embedding tables, keyed by `TableConfig`."""
    def embedding_lookup(self, features: Any, weights: Optional[Any] = None) -> Any:
        """Apply embedding lookup on TPUs using Tensorcore.

    Note that all the sparse and ragged tensors will be converted to dense
    tensors on CPU and then passed to the TPU to do embedding look up. Large
    embedding lookup is not supported by this API, use the TPUEmbedding mid
    level api instead.

    Args:
      features: a nested structure of Tensors, SparseTensors or RaggedTensors.
      weights: a nested structure of Tensors, SparseTensors or RaggedTensors or
        None for no weights. If not None, structure must match that of inputs,
        but entries are allowed to be None.

    Returns:
      A nested structure of Tensors with the same structure as inputs.
    """
