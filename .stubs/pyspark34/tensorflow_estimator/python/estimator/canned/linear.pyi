import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator
from tensorflow_estimator.python.estimator.canned import optimizers as optimizers
from tensorflow_estimator.python.estimator.canned.linear_optimizer.python.utils import sdca_ops as sdca_ops
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.head import binary_class_head as binary_class_head, head_utils as head_utils, regression_head as regression_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class LinearSDCA:
    '''Stochastic Dual Coordinate Ascent helper for linear estimators.

  Objects of this class are intended to be provided as the optimizer argument
  (though LinearSDCA objects do not implement the `tf.train.Optimizer`
  interface)
  when creating `tf.estimator.LinearClassifier` or
  `tf.estimator.LinearRegressor`.

  SDCA can only be used with `LinearClassifier` and `LinearRegressor` under the
  following conditions:

    - Feature columns are of type V2.
    - Multivalent categorical columns are not normalized. In other words the
      `sparse_combiner` argument in the estimator constructor should be "sum".
    - For classification: binary label.
    - For regression: one-dimensional label.

  Example usage:

  ```python
  real_feature_column = numeric_column(...)
  sparse_feature_column = categorical_column_with_hash_bucket(...)
  linear_sdca = tf.estimator.experimental.LinearSDCA(
      example_id_column=\'example_id\',
      num_loss_partitions=1,
      num_table_shards=1,
      symmetric_l2_regularization=2.0)
  classifier = tf.estimator.LinearClassifier(
      feature_columns=[real_feature_column, sparse_feature_column],
      weight_column=...,
      optimizer=linear_sdca)
  classifier.train(input_fn_train, steps=50)
  classifier.evaluate(input_fn=input_fn_eval)
  ```

  Here the expectation is that the `input_fn_*` functions passed to train and
  evaluate return a pair (dict, label_tensor) where dict has `example_id_column`
  as `key` whose value is a `Tensor` of shape [batch_size] and dtype string.
  num_loss_partitions defines sigma\' in eq (11) of [3]. Convergence of (global)
  loss is guaranteed if `num_loss_partitions` is larger or equal to the product
  `(#concurrent train ops/per worker) x (#workers)`. Larger values for
  `num_loss_partitions` lead to slower convergence. The recommended value for
  `num_loss_partitions` in `tf.estimator` (where currently there is one process
  per worker) is the number of workers running the train steps. It defaults to 1
  (single machine).
  `num_table_shards` defines the number of shards for the internal state
  table, typically set to match the number of parameter servers for large
  data sets.

  The SDCA algorithm was originally introduced in [1] and it was followed by
  the L1 proximal step [2], a distributed version [3] and adaptive sampling [4].
  [1] www.jmlr.org/papers/volume14/shalev-shwartz13a/shalev-shwartz13a.pdf
  [2] https://arxiv.org/pdf/1309.2375.pdf
  [3] https://arxiv.org/pdf/1502.03508.pdf
  [4] https://arxiv.org/pdf/1502.08053.pdf
  Details specific to this implementation are provided in:
  https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/linear_optimizer/doc/sdca.ipynb
  '''
    def __init__(self, example_id_column, num_loss_partitions: int = 1, num_table_shards: Incomplete | None = None, symmetric_l1_regularization: float = 0.0, symmetric_l2_regularization: float = 1.0, adaptive: bool = False) -> None:
        """Construct a new SDCA optimizer for linear estimators.

    Args:
      example_id_column: The column name containing the example ids.
      num_loss_partitions: Number of workers.
      num_table_shards: Number of shards of the internal state table, typically
        set to match the number of parameter servers.
      symmetric_l1_regularization: A float value, must be greater than or equal
        to zero.
      symmetric_l2_regularization: A float value, must be greater than zero and
        should typically be greater than 1.
      adaptive: A boolean indicating whether to use adaptive sampling.
    """
    def get_train_step(self, state_manager, weight_column_name, loss_type, feature_columns, features, targets, bias_var, global_step):
        """Returns the training operation of an SdcaModel optimizer."""

def linear_logit_fn_builder_v2(units, feature_columns, sparse_combiner: str = 'sum'):
    '''Function builder for a linear logit_fn.

  Args:
    units: An int indicating the dimension of the logit layer.
    feature_columns: An iterable containing all the feature columns used by the
      model.
    sparse_combiner: A string specifying how to reduce if a categorical column
      is multivalent.  One of "mean", "sqrtn", and "sum".

  Returns:
    A logit_fn (see below).

  '''
def linear_logit_fn_builder(units, feature_columns, sparse_combiner: str = 'sum'):
    '''Function builder for a linear logit_fn.

  Args:
    units: An int indicating the dimension of the logit layer.
    feature_columns: An iterable containing all the feature columns used by the
      model.
    sparse_combiner: A string specifying how to reduce if a categorical column
      is multivalent.  One of "mean", "sqrtn", and "sum".

  Returns:
    A logit_fn (see below).

  '''

class _SDCAUpdateWeightsHook(tf.compat.v1.train.SessionRunHook):
    """SessionRunHook to update and shrink SDCA model weights."""
    def __init__(self, sdca_model, train_op) -> None: ...
    def begin(self) -> None:
        """Construct the update_weights op.

    The op is implicitly added to the default graph.
    """
    def before_run(self, run_context):
        """Return the update_weights op so that it is executed during this run."""

class LinearClassifierV2(estimator.EstimatorV2):
    '''Linear classifier model.

  Train a linear model to classify instances into one of multiple possible
  classes. When number of possible classes is 2, this is binary classification.

  Example:

  ```python
  categorical_column_a = categorical_column_with_hash_bucket(...)
  categorical_column_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_x_categorical_feature_b = crossed_column(...)

  # Estimator using the default optimizer.
  estimator = tf.estimator.LinearClassifier(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b])

  # Or estimator using the FTRL optimizer with regularization.
  estimator = tf.estimator.LinearClassifier(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      optimizer=tf.keras.optimizers.Ftrl(
        learning_rate=0.1,
        l1_regularization_strength=0.001
      ))

  # Or estimator using an optimizer with a learning rate decay.
  estimator = tf.estimator.LinearClassifier(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      optimizer=lambda: tf.keras.optimizers.Ftrl(
          learning_rate=tf.exponential_decay(
              learning_rate=0.1,
              global_step=tf.get_global_step(),
              decay_steps=10000,
              decay_rate=0.96))

  # Or estimator with warm-starting from a previous checkpoint.
  estimator = tf.estimator.LinearClassifier(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      warm_start_from="/path/to/checkpoint/dir")


  # Input builders
  def input_fn_train:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass
  def input_fn_eval:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass
  def input_fn_predict:
    # Returns tf.data.Dataset of (x, None) tuple.
    pass
  estimator.train(input_fn=input_fn_train)
  metrics = estimator.evaluate(input_fn=input_fn_eval)
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
    otherwise there will be a `KeyError`:

  * if `weight_column` is not `None`, a feature with `key=weight_column` whose
    value is a `Tensor`.
  * for each `column` in `feature_columns`:
    - if `column` is a `SparseColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedSparseColumn`, two features: the first with
      `key` the id column name, the second with `key` the weight column name.
      Both features\' `value` must be a `SparseTensor`.
    - if `column` is a `RealValuedColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss is calculated by using softmax cross entropy.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, feature_columns, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., sparse_combiner: str = 'sum') -> None:
        '''Construct a `LinearClassifier` estimator object.

    Args:
      feature_columns: An iterable containing all the feature columns used by
        the model. All items in the set should be instances of classes derived
        from `FeatureColumn`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      n_classes: number of label classes. Default is binary classification. Note
        that class labels are integers representing the class index (i.e. values
        from 0 to n_classes-1). For arbitrary label values (e.g. string labels),
        convert to class indices first.
      weight_column: A string or a `_NumericColumn` created by
        `tf.feature_column.numeric_column` defining feature column representing
        weights. It is used to down weight or boost examples during training. It
        will be multiplied by the loss of the example. If it is a string, it is
        used as a key to fetch weight tensor from the `features`. If it is a
        `_NumericColumn`, raw tensor is fetched by key `weight_column.key`, then
        weight_column.normalizer_fn is applied on it to get weight tensor.
      label_vocabulary: A list of strings represents possible label values. If
        given, labels must be string type and have any value in
        `label_vocabulary`. If it is not given, that means labels are already
        encoded as integer or float within [0, 1] for `n_classes=2` and encoded
        as integer values in {0, 1,..., n_classes-1} for `n_classes`>2 . Also
        there will be errors if vocabulary is not provided and labels are
        string.
      optimizer: An instance of `tf.keras.optimizers.*` or
        `tf.estimator.experimental.LinearSDCA` used to train the model. Can also
        be a string (one of \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or
        callable. Defaults to FTRL optimizer.
      config: `RunConfig` object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights and biases are warm-started, and it is assumed that vocabularies
        and Tensor names are unchanged.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
      sparse_combiner: A string specifying how to reduce if a categorical column
        is multivalent.  One of "mean", "sqrtn", and "sum" -- these are
        effectively different ways to do example-level normalization, which can
        be useful for bag-of-words features. for more details, see
        `tf.feature_column.linear_model`.

    Returns:
      A `LinearClassifier` estimator.

    Raises:
      ValueError: if n_classes < 2.
    '''

class LinearClassifier(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, feature_columns, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, partitioner: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., sparse_combiner: str = 'sum') -> None: ...

class LinearEstimatorV2(estimator.EstimatorV2):
    """An estimator for TensorFlow linear models with user-specified head.

  Example:

  ```python
  categorical_column_a = categorical_column_with_hash_bucket(...)
  categorical_column_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_x_categorical_feature_b = crossed_column(...)

  # Estimator using the default optimizer.
  estimator = tf.estimator.LinearEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b])

  # Or estimator using an optimizer with a learning rate decay.
  estimator = tf.estimator.LinearEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      optimizer=lambda: tf.keras.optimizers.Ftrl(
          learning_rate=tf.compat.v1.train.exponential_decay(
              learning_rate=0.1,
              global_step=tf.compat.v1.train.get_global_step(),
              decay_steps=10000,
              decay_rate=0.96))

  # Or estimator using the FTRL optimizer with regularization.
  estimator = tf.estimator.LinearEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b])
      optimizer=tf.keras.optimizers.Ftrl(
          learning_rate=0.1,
          l1_regularization_strength=0.001
      ))

  def input_fn_train:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label's class
    # index.
    pass
  def input_fn_eval:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label's class
    # index.
    pass
  def input_fn_predict:
    # Returns tf.data.Dataset of (x, None) tuple.
    pass
  estimator.train(input_fn=input_fn_train, steps=100)
  metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

  * if `weight_column` is not `None`, a feature with `key=weight_column` whose
    value is a `Tensor`.
  * for each `column` in `feature_columns`:
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss and predicted output are determined by the specified head.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  """
    def __init__(self, head, feature_columns, model_dir: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, sparse_combiner: str = 'sum', warm_start_from: Incomplete | None = None) -> None:
        '''Initializes a `LinearEstimator` instance.

    Args:
      head: A `Head` instance constructed with a method such as
        `tf.estimator.MultiLabelHead`.
      feature_columns: An iterable containing all the feature columns used by
        the model. All items in the set should be instances of classes derived
        from `FeatureColumn`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      optimizer: An instance of `tf.keras.optimizers.*` used to train the model.
        Can also be a string (one of \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\',
        \'SGD\'), or callable. Defaults to FTRL optimizer.
      config: `RunConfig` object to configure the runtime settings.
      sparse_combiner: A string specifying how to reduce if a categorical column
        is multivalent.  One of "mean", "sqrtn", and "sum" -- these are
        effectively different ways to do example-level normalization, which can
        be useful for bag-of-words features. for more details, see
        `tf.feature_column.linear_model`.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights and biases are warm-started, and it is assumed that vocabularies
        and Tensor names are unchanged.
    '''

class LinearEstimator(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, head, feature_columns, model_dir: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, partitioner: Incomplete | None = None, sparse_combiner: str = 'sum', warm_start_from: Incomplete | None = None) -> None:
        '''Initializes a `LinearEstimator` instance.

    Args:
      head: A `_Head` instance constructed with a method such as
        `tf.contrib.estimator.multi_label_head`.
      feature_columns: An iterable containing all the feature columns used by
        the model. All items in the set should be instances of classes derived
        from `FeatureColumn`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      optimizer: An instance of `tf.Optimizer` used to train the model. Can also
        be a string (one of \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or
        callable. Defaults to FTRL optimizer.
      config: `RunConfig` object to configure the runtime settings.
      partitioner: Optional. Partitioner for input layer.
      sparse_combiner: A string specifying how to reduce if a categorical column
        is multivalent.  One of "mean", "sqrtn", and "sum" -- these are
        effectively different ways to do example-level normalization, which can
        be useful for bag-of-words features. for more details, see
        `tf.feature_column.linear_model`.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights and biases are warm-started, and it is assumed that vocabularies
        and Tensor names are unchanged.
    '''

class LinearRegressorV2(estimator.EstimatorV2):
    '''An estimator for TensorFlow Linear regression problems.

  Train a linear regression model to predict label value given observation of
  feature values.

  Example:

  ```python
  categorical_column_a = categorical_column_with_hash_bucket(...)
  categorical_column_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_x_categorical_feature_b = crossed_column(...)

  # Estimator using the default optimizer.
  estimator = tf.estimator.LinearRegressor(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b])

  # Or estimator using the FTRL optimizer with regularization.
  estimator = tf.estimator.LinearRegressor(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      optimizer=tf.keras.optimizers.Ftrl(
        learning_rate=0.1,
        l1_regularization_strength=0.001
      ))

  # Or estimator using an optimizer with a learning rate decay.
  estimator = tf.estimator.LinearRegressor(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      optimizer=lambda: tf.keras.optimizers.Ftrl(
          learning_rate=tf.compat.v1.train.exponential_decay(
              learning_rate=0.1,
              global_step=tf.compat.v1.train.get_global_step(),
              decay_steps=10000,
              decay_rate=0.96))

  # Or estimator with warm-starting from a previous checkpoint.
  estimator = tf.estimator.LinearRegressor(
      feature_columns=[categorical_column_a,
                       categorical_feature_a_x_categorical_feature_b],
      warm_start_from="/path/to/checkpoint/dir")


  # Input builders
  def input_fn_train:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass
  def input_fn_eval:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass
  def input_fn_predict:
    # Returns tf.data.Dataset of (x, None) tuple.
    pass
  estimator.train(input_fn=input_fn_train)
  metrics = estimator.evaluate(input_fn=input_fn_eval)
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
    otherwise there will be a KeyError:

  * if `weight_column` is not `None`, a feature with `key=weight_column` whose
    value is a `Tensor`.
  * for each `column` in `feature_columns`:
    - if `column` is a `SparseColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedSparseColumn`, two features: the first with
      `key` the id column name, the second with `key` the weight column name.
      Both features\' `value` must be a `SparseTensor`.
    - if `column` is a `RealValuedColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss is calculated by using mean squared error.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, feature_columns, model_dir: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., sparse_combiner: str = 'sum') -> None:
        '''Initializes a `LinearRegressor` instance.

    Args:
      feature_columns: An iterable containing all the feature columns used by
        the model. All items in the set should be instances of classes derived
        from `FeatureColumn`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      label_dimension: Number of regression targets per example. This is the
        size of the last dimension of the labels and logits `Tensor` objects
        (typically, these have shape `[batch_size, label_dimension]`).
      weight_column: A string or a `NumericColumn` created by
        `tf.feature_column.numeric_column` defining feature column representing
        weights. It is used to down weight or boost examples during training. It
        will be multiplied by the loss of the example. If it is a string, it is
        used as a key to fetch weight tensor from the `features`. If it is a
        `NumericColumn`, raw tensor is fetched by key `weight_column.key`, then
        weight_column.normalizer_fn is applied on it to get weight tensor.
      optimizer: An instance of `tf.keras.optimizers.*` or
        `tf.estimator.experimental.LinearSDCA` used to train the model. Can also
        be a string (one of \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or
        callable. Defaults to FTRL optimizer.
      config: `RunConfig` object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights and biases are warm-started, and it is assumed that vocabularies
        and Tensor names are unchanged.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM`.
      sparse_combiner: A string specifying how to reduce if a categorical column
        is multivalent.  One of "mean", "sqrtn", and "sum" -- these are
        effectively different ways to do example-level normalization, which can
        be useful for bag-of-words features. for more details, see
        `tf.feature_column.linear_model`.
    '''

class LinearRegressor(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, feature_columns, model_dir: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, partitioner: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., sparse_combiner: str = 'sum') -> None: ...

class _LinearModelLayer(tf.keras.layers.Layer):
    """Layer that contains logic for `LinearModel`."""
    bias: Incomplete
    def __init__(self, feature_columns, units: int = 1, sparse_combiner: str = 'sum', trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None: ...
    def build(self, _) -> None: ...
    def call(self, features): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class LinearModel(tf.keras.Model):
    '''Produces a linear prediction `Tensor` based on given `feature_columns`.

  This layer generates a weighted sum based on output dimension `units`.
  Weighted sum refers to logits in classification problems. It refers to the
  prediction itself for linear regression problems.

  Note on supported columns: `LinearLayer` treats categorical columns as
  `indicator_column`s. To be specific, assume the input as `SparseTensor` looks
  like:

  ```python
    shape = [2, 2]
    {
        [0, 0]: "a"
        [1, 0]: "b"
        [1, 1]: "c"
    }
  ```
  `linear_model` assigns weights for the presence of "a", "b", "c\' implicitly,
  just like `indicator_column`, while `input_layer` explicitly requires wrapping
  each of categorical columns with an `embedding_column` or an
  `indicator_column`.

  Example of usage:

  ```python
  price = numeric_column(\'price\')
  price_buckets = bucketized_column(price, boundaries=[0., 10., 100., 1000.])
  keywords = categorical_column_with_hash_bucket("keywords", 10K)
  keywords_price = crossed_column(\'keywords\', price_buckets, ...)
  columns = [price_buckets, keywords, keywords_price ...]
  linear_model = LinearLayer(columns)

  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  prediction = linear_model(features)
  ```
  '''
    layer: Incomplete
    def __init__(self, feature_columns, units: int = 1, sparse_combiner: str = 'sum', trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None:
        '''Constructs a LinearLayer.

    Args:
      feature_columns: An iterable containing the FeatureColumns to use as
        inputs to your model. All items should be instances of classes derived
        from `_FeatureColumn`s.
      units: An integer, dimensionality of the output space. Default value is 1.
      sparse_combiner: A string specifying how to reduce if a categorical column
        is multivalent. Except `numeric_column`, almost all columns passed to
        `linear_model` are considered as categorical columns.  It combines each
        categorical column independently. Currently "mean", "sqrtn" and "sum"
        are supported, with "sum" the default for linear model. "sqrtn" often
        achieves good accuracy, in particular with bag-of-words columns.
          * "sum": do not normalize features in the column
          * "mean": do l1 normalization on features in the column
          * "sqrtn": do l2 normalization on features in the column
        For example, for two features represented as the categorical columns:

          ```python
          # Feature 1

          shape = [2, 2]
          {
              [0, 0]: "a"
              [0, 1]: "b"
              [1, 0]: "c"
          }

          # Feature 2

          shape = [2, 3]
          {
              [0, 0]: "d"
              [1, 0]: "e"
              [1, 1]: "f"
              [1, 2]: "g"
          }
          ```

        with `sparse_combiner` as "mean", the linear model outputs conceptually
        are
        ```
        y_0 = 1.0 / 2.0 * ( w_a + w_ b) + w_c + b_0
        y_1 = w_d + 1.0 / 3.0 * ( w_e + w_ f + w_g) + b_1
        ```
        where `y_i` is the output, `b_i` is the bias, and `w_x` is the weight
        assigned to the presence of `x` in the input features.
      trainable: If `True` also add the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
      name: Name to give to the Linear Model. All variables and ops created will
        be scoped by this name.
      **kwargs: Keyword arguments to construct a layer.

    Raises:
      ValueError: if an item in `feature_columns` is neither a `DenseColumn`
        nor `CategoricalColumn`.
    '''
    def call(self, features):
        """Returns a `Tensor` the represents the predictions of a linear model.

    Args:
      features: A mapping from key to tensors. `_FeatureColumn`s look up via
        these keys. For example `numeric_column('price')` will look at 'price'
        key in this dict. Values are `Tensor` or `SparseTensor` depending on
        corresponding `_FeatureColumn`.

    Returns:
      A `Tensor` which represents predictions/logits of a linear model. Its
      shape is (batch_size, units) and its dtype is `float32`.

    Raises:
      ValueError: If features are not a dictionary.
    """
    @property
    def bias(self): ...
