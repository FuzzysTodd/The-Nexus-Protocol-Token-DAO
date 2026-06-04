from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context, tpu_strategy as tpu_strategy
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, embedding_ops as embedding_ops, math_ops as math_ops, sparse_ops as sparse_ops, variables as tf_variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.tpu import tpu_embedding_base as tpu_embedding_base, tpu_embedding_v2_utils as tpu_embedding_v2_utils
from tensorflow.python.types import core as core
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Dict, Iterable, Optional, Union

class TPUEmbeddingForServing(tpu_embedding_base.TPUEmbeddingBase):
    """The TPUEmbedding mid level API running on CPU for serving.

  Note: This class is intended to be used for embedding tables that are trained
  on TPU and to be served on CPU. Therefore the class should be only initialized
  under non-TPU strategy. Otherwise an error will be raised.

  You can first train your model using the TPUEmbedding class and save the
  checkpoint. Then use this class to restore the checkpoint to do serving.

  First train a model and save the checkpoint.
  ```python
  model = model_fn(...)
  strategy = tf.distribute.TPUStrategy(...)
  with strategy.scope():
    embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        feature_config=feature_config,
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))

  # Your custom training code.

  checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
  checkpoint.save(...)

  ```

  Then restore the checkpoint and do serving.
  ```python

  # Restore the model on CPU.
  model = model_fn(...)
  embedding = tf.tpu.experimental.embedding.TPUEmbeddingForServing(
        feature_config=feature_config,
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))

  checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
  checkpoint.restore(...)

  result = embedding(...)
  table = embedding.embedding_table
  ```

  NOTE: This class can also be used to do embedding training on CPU. But it
  requires the conversion between keras optimizer and embedding optimizers so
  that the slot variables can stay consistent between them.
  """
    def __init__(self, feature_config: Union[tpu_embedding_v2_utils.FeatureConfig, Iterable], optimizer: Optional[tpu_embedding_v2_utils._Optimizer]) -> None:
        """Creates the TPUEmbeddingForServing mid level API object.

    ```python
    embedding = tf.tpu.experimental.embedding.TPUEmbeddingForServing(
        feature_config=tf.tpu.experimental.embedding.FeatureConfig(
            table=tf.tpu.experimental.embedding.TableConfig(
                dim=...,
                vocabulary_size=...)))
    ```

    Args:
      feature_config: A nested structure of
        `tf.tpu.experimental.embedding.FeatureConfig` configs.
      optimizer: An instance of one of `tf.tpu.experimental.embedding.SGD`,
        `tf.tpu.experimental.embedding.Adagrad` or
        `tf.tpu.experimental.embedding.Adam`. When not created under TPUStrategy
        may be set to None to avoid the creation of the optimizer slot
        variables, useful for optimizing memory consumption when exporting the
        model for serving where slot variables aren't needed.

    Raises:
      RuntimeError: If created under TPUStrategy.
    """
    @property
    def embedding_tables(self) -> Dict[tpu_embedding_v2_utils.TableConfig, tf_variables.Variable]:
        """Returns a dict of embedding tables, keyed by `TableConfig`."""
    def embedding_lookup(self, features: Any, weights: Optional[Any] = None) -> Any:
        """Apply standard lookup ops on CPU.

    Args:
      features: A nested structure of `tf.Tensor`s, `tf.SparseTensor`s or
        `tf.RaggedTensor`s, with the same structure as `feature_config`. Inputs
        will be downcast to `tf.int32`. Only one type out of `tf.SparseTensor`
        or `tf.RaggedTensor` is supported per call.
      weights: If not `None`, a nested structure of `tf.Tensor`s,
        `tf.SparseTensor`s or `tf.RaggedTensor`s, matching the above, except
        that the tensors should be of float type (and they will be downcast to
        `tf.float32`). For `tf.SparseTensor`s we assume the `indices` are the
        same for the parallel entries from `features` and similarly for
        `tf.RaggedTensor`s we assume the row_splits are the same.

    Returns:
      A nested structure of Tensors with the same structure as input features.
    """

def cpu_embedding_lookup(inputs: Any, weights: Optional[Any], tables: Dict[tpu_embedding_v2_utils.TableConfig, tf_variables.Variable], feature_config: Union[tpu_embedding_v2_utils.FeatureConfig, Iterable]) -> Any:
    """Apply standard lookup ops with `tf.tpu.experimental.embedding` configs.

  This function is a utility which allows using the
  `tf.tpu.experimental.embedding` config objects with standard lookup functions.
  This can be used when exporting a model which uses
  `tf.tpu.experimental.embedding.TPUEmbedding` for serving on CPU. In particular
  `tf.tpu.experimental.embedding.TPUEmbedding` only supports lookups on TPUs and
  should not be part of your serving graph.

  Note that TPU specific options (such as `max_sequence_length`) in the
  configuration objects will be ignored.

  In the following example we take a trained model (see the documentation for
  `tf.tpu.experimental.embedding.TPUEmbedding` for the context) and create a
  saved model with a serving function that will perform the embedding lookup and
  pass the results to your model:

  ```python
  model = model_fn(...)
  embedding = tf.tpu.experimental.embedding.TPUEmbedding(
      feature_config=feature_config,
      batch_size=1024,
      optimizer=tf.tpu.experimental.embedding.SGD(0.1))
  checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
  checkpoint.restore(...)

  @tf.function(input_signature=[{'feature_one': tf.TensorSpec(...),
                                 'feature_two': tf.TensorSpec(...),
                                 'feature_three': tf.TensorSpec(...)}])
  def serve_tensors(embedding_features):
    embedded_features = tf.tpu.experimental.embedding.serving_embedding_lookup(
        embedding_features, None, embedding.embedding_tables,
        feature_config)
    return model(embedded_features)

  model.embedding_api = embedding
  tf.saved_model.save(model,
                      export_dir=...,
                      signatures={'serving_default': serve_tensors})

  ```

  NOTE: It's important to assign the embedding API object to a member of your
  model as `tf.saved_model.save` only supports saving variables as one
  `Trackable` object. Since the model's weights are in `model` and the
  embedding table are managed by `embedding`, we assign `embedding` to an
  attribute of `model` so that tf.saved_model.save can find the embedding
  variables.

  NOTE: The same `serve_tensors` function and `tf.saved_model.save` call will
  work directly from training.

  Args:
    inputs: a nested structure of Tensors, SparseTensors or RaggedTensors.
    weights: a nested structure of Tensors, SparseTensors or RaggedTensors or
      None for no weights. If not None, structure must match that of inputs, but
      entries are allowed to be None.
    tables: a dict of mapping TableConfig objects to Variables.
    feature_config: a nested structure of FeatureConfig objects with the same
      structure as inputs.

  Returns:
    A nested structure of Tensors with the same structure as inputs.
  """
