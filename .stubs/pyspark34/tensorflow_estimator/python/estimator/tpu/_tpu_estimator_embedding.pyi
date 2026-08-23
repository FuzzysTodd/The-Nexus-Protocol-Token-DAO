from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from typing import NamedTuple

def get_full_variable_names(graph, table_to_config_dict, optimization_parameters: Incomplete | None = None):
    """Return embedding variable names and slot variables which are consistent with CPU runs."""
def get_configs_from_feature_columns(feature_columns):
    """Create configs for TPUEmbedding etc from a list of feature columns.

  Args:
    feature_columns: a list of supported feature columns.

  Returns:
    A tuple of dicts, the first maps tables to their config, the second maps
    features to their config, the third maps learning rate key to callback that
    takes global step and outputs dynamic learning rate.
  """

class EmbeddingConfigSpec(NamedTuple('EmbeddingConfigSpec', [('feature_columns', Incomplete), ('tensor_core_feature_columns', Incomplete), ('optimization_parameters', Incomplete), ('clipping_limit', Incomplete), ('pipeline_execution_with_tensor_core', Incomplete), ('experimental_gradient_multiplier_fn', Incomplete), ('feature_to_config_dict', Incomplete), ('table_to_config_dict', Incomplete), ('partition_strategy', Incomplete), ('profile_data_directory', Incomplete)])):
    """Class to keep track of the specification for TPU embeddings.

  Pass this class to `tf.estimator.tpu.TPUEstimator` via the
  `embedding_config_spec` parameter. At minimum you need to specify
  `feature_columns` and `optimization_parameters`. The feature columns passed
  should be created with some combination of
  `tf.tpu.experimental.embedding_column` and
  `tf.tpu.experimental.shared_embedding_columns`.

  TPU embeddings do not support arbitrary Tensorflow optimizers and the
  main optimizer you use for your model will be ignored for the embedding table
  variables. Instead TPU embeddigns support a fixed set of predefined optimizers
  that you can select from and set the parameters of. These include adagrad,
  adam and stochastic gradient descent. Each supported optimizer has a
  `Parameters` class in the `tf.tpu.experimental` namespace.

  ```
  column_a = tf.feature_column.categorical_column_with_identity(...)
  column_b = tf.feature_column.categorical_column_with_identity(...)
  column_c = tf.feature_column.categorical_column_with_identity(...)
  tpu_shared_columns = tf.tpu.experimental.shared_embedding_columns(
      [column_a, column_b], 10)
  tpu_non_shared_column = tf.tpu.experimental.embedding_column(
      column_c, 10)
  tpu_columns = [tpu_non_shared_column] + tpu_shared_columns
  ...
  def model_fn(features):
    dense_features = tf.keras.layers.DenseFeature(tpu_columns)
    embedded_feature = dense_features(features)
    ...

  estimator = tf.estimator.tpu.TPUEstimator(
      model_fn=model_fn,
      ...
      embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          column=tpu_columns,
          optimization_parameters=(
              tf.estimator.tpu.experimental.AdagradParameters(0.1))))
  ```

  @compatibility(TF2)
  TPU Estimator manages its own TensorFlow graph and session, so it is not
  compatible with TF2 behaviors. We recommend that you migrate to the newer
  `tf.distribute.TPUStrategy`. See the
  [TPU guide](https://www.tensorflow.org/guide/tpu) for details.
  @end_compatibility
  """
    def __new__(cls, feature_columns: Incomplete | None = None, optimization_parameters: Incomplete | None = None, clipping_limit: Incomplete | None = None, pipeline_execution_with_tensor_core: bool = False, experimental_gradient_multiplier_fn: Incomplete | None = None, feature_to_config_dict: Incomplete | None = None, table_to_config_dict: Incomplete | None = None, partition_strategy: str = 'div', profile_data_directory: Incomplete | None = None):
        '''Creates an `EmbeddingConfigSpec` instance.

    Args:
      feature_columns: All embedding `FeatureColumn`s used by model.
      optimization_parameters: An instance of `AdagradParameters`,
        `AdamParameters` or `StochasticGradientDescentParameters`. This
        optimizer will be applied to all embedding variables specified by
        `feature_columns`.
      clipping_limit: (Optional) Clipping limit (absolute value).
      pipeline_execution_with_tensor_core: setting this to `True` makes training
        faster, but trained model will be different if step N and step N+1
        involve the same set of embedding IDs. Please see
        `tpu_embedding_configuration.proto` for details.
      experimental_gradient_multiplier_fn: (Optional) A Fn taking global step as
        input returning the current multiplier for all embedding gradients.
      feature_to_config_dict: A dictionary mapping feature names to instances of
        the class `FeatureConfig`. Either features_columns or the pair of
        `feature_to_config_dict` and `table_to_config_dict` must be specified.
      table_to_config_dict: A dictionary mapping feature names to instances of
        the class `TableConfig`. Either features_columns or the pair of
        `feature_to_config_dict` and `table_to_config_dict` must be specified.
      partition_strategy: A string, determining how tensors are sharded to the
        tpu hosts. See `tf.nn.safe_embedding_lookup_sparse` for more details.
        Allowed value are `"div"` and `"mod"\'. If `"mod"` is used, evaluation
        and exporting the model to CPU will not work as expected.
      profile_data_directory: Directory where embedding lookup statistics are
        stored. These statistics summarize information about the inputs to the
        embedding lookup operation, in particular, the average number of
        embedding IDs per example and how well the embedding IDs are load
        balanced across the system. The lookup statistics are used during TPU
        initialization for embedding table partitioning. Collection of lookup
        statistics is done at runtime by  profiling the embedding inputs, only a
        small fraction of input samples are profiled to minimize host CPU
        overhead. Once a suitable number of samples are profiled, the lookup
        statistics are saved to table-specific files in the profile data
        directory generally at the end of a TPU training loop. The filename
        corresponding to each table is obtained by hashing table specific
        parameters (e.g., table name and number of features) and global
        configuration parameters (e.g., sharding strategy and task count). The
        same profile data directory can be shared among several models to reuse
        embedding lookup statistics.

    Returns:
      An `EmbeddingConfigSpec` instance.

    Raises:
      ValueError: If the feature_columns are not specified.
      TypeError: If the feature columns are not of ths correct type (one of
        _SUPPORTED_FEATURE_COLUMNS, _TPU_EMBEDDING_COLUMN_CLASSES OR
        _EMBEDDING_COLUMN_CLASSES).
      ValueError: If `optimization_parameters` is not one of the required types.
    '''

class EmbeddingConfig:
    """This is the internal immutable object for embedding config.

  `_EmbeddingConfig` is responsible to _translate_ user provided
  `EmbeddingConfigSpec` to internal data structures, mostly constructor
  arguments of `TPUEmbedding`.
  """
    dummy_table_variables: Incomplete
    def __init__(self, embedding_config_spec, train_batch_size, eval_batch_size, num_hosts, num_cores, run_config) -> None: ...
    def get_grad_multiplier(self): ...
    def has_embedding_tables(self): ...
    def get_tpu_embedding(self, mode): ...

def split_inputs(ctx, features, labels, num_cores_per_batch: int = 1):
    """Splits the dense and sparse tensors inside the features and labels."""
def get_tpu_embedding_columns(feature_columns):
    """Get feature columns meant to use TPU embedding.

  Args:
    feature_columns: a list of feature columns.

  Returns:
    A list of feature columns which can be placed on TPU embedding.
  """
