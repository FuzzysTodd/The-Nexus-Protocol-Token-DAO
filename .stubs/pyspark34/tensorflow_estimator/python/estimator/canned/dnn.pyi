import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator
from tensorflow_estimator.python.estimator.canned import optimizers as optimizers
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.head import head_utils as head_utils, regression_head as regression_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

def dnn_logit_fn_builder(units, hidden_units, feature_columns, activation_fn, dropout, input_layer_partitioner, batch_norm):
    """Function builder for a dnn logit_fn.

  Args:
    units: An int indicating the dimension of the logit layer.  In the MultiHead
      case, this should be the sum of all component Heads' logit dimensions.
    hidden_units: Iterable of integer number of hidden units per layer.
    feature_columns: Iterable of `feature_column._FeatureColumn` model inputs.
    activation_fn: Activation function applied to each layer.
    dropout: When not `None`, the probability we will drop out a given
      coordinate.
    input_layer_partitioner: Partitioner for input layer.
    batch_norm: Whether to use batch normalization after each hidden layer.

  Returns:
    A logit_fn (see below).

  Raises:
    ValueError: If units is not an int.
  """
def dnn_logit_fn_builder_v2(units, hidden_units, feature_columns, activation_fn, dropout, batch_norm):
    """Function builder for a dnn logit_fn.

  Args:
    units: An int indicating the dimension of the logit layer.  In the MultiHead
      case, this should be the sum of all component Heads' logit dimensions.
    hidden_units: Iterable of integer number of hidden units per layer.
    feature_columns: Iterable of `feature_column._FeatureColumn` model inputs.
    activation_fn: Activation function applied to each layer.
    dropout: When not `None`, the probability we will drop out a given
      coordinate.
    batch_norm: Whether to use batch normalization after each hidden layer.

  Returns:
    A logit_fn (see below).

  Raises:
    ValueError: If units is not an int.
  """

class _DNNModel(tf.keras.Model):
    """A DNN Model."""
    def __init__(self, units, hidden_units, feature_columns, activation_fn, dropout, input_layer_partitioner, batch_norm, name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, features, mode): ...

class _DNNModelV2(tf.keras.Model):
    """A DNN Model."""
    def __init__(self, units, hidden_units, feature_columns, activation_fn, dropout, batch_norm, name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, features, mode): ...

def dnn_model_fn_v2(features, labels, mode, head, hidden_units, feature_columns, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, config: Incomplete | None = None, use_tpu: bool = False, batch_norm: bool = False):
    """Deep Neural Net model_fn v2.

  This function is different than _dnn_model_fn_v1 in the way it handles the
  optimizer when a String optimizer name is passed.

  Args:
    features: dict of `Tensor`.
    labels: `Tensor` of shape [batch_size, 1] or [batch_size] labels of dtype
      `int32` or `int64` in the range `[0, n_classes)`.
    mode: Defines whether this is training, evaluation or prediction. See
      `ModeKeys`.
    head: A `base_head.Head` instance.
    hidden_units: Iterable of integer number of hidden units per layer.
    feature_columns: Iterable of `feature_column._FeatureColumn` model inputs.
    optimizer: String, `tf.keras.optimizers.Optimizer` object, or callable that
      creates the optimizer to use for training. If not specified, will use the
      Adagrad optimizer. If it is String, the default learning rate of the
      optimizer will be used. If it is String, and optimizer does not have a
      default learning rate, then, a fixed learning rate of 0.05 is used.
    activation_fn: Activation function applied to each layer.
    dropout: When not `None`, the probability we will drop out a given
      coordinate.
    config: `RunConfig` object to configure the runtime settings.
    use_tpu: Whether to make a DNN model able to run on TPU. Will make function
      return a `_TPUEstimatorSpec` instance and disable variable partitioning.
    batch_norm: Whether to use batch normalization after each hidden layer.

  Returns:
    An `EstimatorSpec` instance.

  Raises:
    ValueError: If features has the wrong type.
  """

class DNNClassifierV2(estimator.EstimatorV2):
    '''A classifier for TensorFlow DNN models.

  Example:

  ```python
  categorical_feature_a = categorical_column_with_hash_bucket(...)
  categorical_feature_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_emb = embedding_column(
      categorical_column=categorical_feature_a, ...)
  categorical_feature_b_emb = embedding_column(
      categorical_column=categorical_feature_b, ...)

  estimator = tf.estimator.DNNClassifier(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256])

  # Or estimator using the ProximalAdagradOptimizer optimizer with
  # regularization.
  estimator = tf.estimator.DNNClassifier(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
      optimizer=tf.compat.v1.train.ProximalAdagradOptimizer(
        learning_rate=0.1,
        l1_regularization_strength=0.001
      ))

  # Or estimator using an optimizer with a learning rate decay.
  estimator = tf.estimator.DNNClassifier(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
      optimizer=lambda: tf.keras.optimizers.Adam(
          learning_rate=tf.compat.v1.train.exponential_decay(
              learning_rate=0.1,
              global_step=tf.compat.v1.train.get_global_step(),
              decay_steps=10000,
              decay_rate=0.96))

  # Or estimator with warm-starting from a previous checkpoint.
  estimator = tf.estimator.DNNClassifier(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
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
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features\' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss is calculated by using softmax cross entropy.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, hidden_units, feature_columns, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False) -> None:
        """Initializes a `DNNClassifier` instance.

    Args:
      hidden_units: Iterable of number hidden units per layer. All layers are
        fully connected. Ex. `[64, 32]` means first layer has 64 nodes and
        second one has 32.
      feature_columns: An iterable containing all the feature columns used by
        the model. All items in the set should be instances of classes derived
        from `_FeatureColumn`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      n_classes: Number of label classes. Defaults to 2, namely binary
        classification. Must be > 1.
      weight_column: A string or a `NumericColumn` created by
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
      optimizer: An instance of `tf.keras.optimizers.*` used to train the model.
        Can also be a string (one of 'Adagrad', 'Adam', 'Ftrl', 'RMSProp',
        SGD'), or callable. Defaults to Adagrad optimizer.
      activation_fn: Activation function applied to each layer. If `None`, will
        use `tf.nn.relu`.
      dropout: When not `None`, the probability we will drop out a given
        coordinate.
      config: `RunConfig` object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights are warm-started, and it is assumed that vocabularies and Tensor
        names are unchanged.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
      batch_norm: Whether to use batch normalization after each hidden layer.
    """

class DNNClassifier(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, hidden_units, feature_columns, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, input_layer_partitioner: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False) -> None: ...

class DNNEstimatorV2(estimator.EstimatorV2):
    '''An estimator for TensorFlow DNN models with user-specified head.

  Example:

  ```python
  sparse_feature_a = sparse_column_with_hash_bucket(...)
  sparse_feature_b = sparse_column_with_hash_bucket(...)

  sparse_feature_a_emb = embedding_column(sparse_id_column=sparse_feature_a,
                                          ...)
  sparse_feature_b_emb = embedding_column(sparse_id_column=sparse_feature_b,
                                          ...)

  estimator = tf.estimator.DNNEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[sparse_feature_a_emb, sparse_feature_b_emb],
      hidden_units=[1024, 512, 256])

  # Or estimator using the ProximalAdagradOptimizer optimizer with
  # regularization.
  estimator = tf.estimator.DNNEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[sparse_feature_a_emb, sparse_feature_b_emb],
      hidden_units=[1024, 512, 256],
      optimizer=tf.compat.v1.train.ProximalAdagradOptimizer(
        learning_rate=0.1,
        l1_regularization_strength=0.001
      ))

  # Or estimator using an optimizer with a learning rate decay.
  estimator = tf.estimator.DNNEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[sparse_feature_a_emb, sparse_feature_b_emb],
      hidden_units=[1024, 512, 256],
      optimizer=lambda: tf.keras.optimizers.Adam(
          learning_rate=tf.compat.v1.train.exponential_decay(
              learning_rate=0.1,
              global_step=tf.compat.v1.train.get_global_step(),
              decay_steps=10000,
              decay_rate=0.96))

  # Or estimator with warm-starting from a previous checkpoint.
  estimator = tf.estimator.DNNEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      feature_columns=[sparse_feature_a_emb, sparse_feature_b_emb],
      hidden_units=[1024, 512, 256],
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
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features\' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss and predicted output are determined by the specified head.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, head, hidden_units, feature_columns, model_dir: Incomplete | None = None, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, batch_norm: bool = False) -> None:
        """Initializes a `DNNEstimator` instance.

    Args:
      head: A `_Head` instance constructed with a method such as
        `tf.contrib.estimator.multi_label_head`.
      hidden_units: Iterable of number hidden units per layer. All layers are
        fully connected. Ex. `[64, 32]` means first layer has 64 nodes and
        second one has 32.
      feature_columns: An iterable containing all the feature columns used by
        the model. All items in the set should be instances of classes derived
        from `_FeatureColumn`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      optimizer: An instance of `tf.keras.optimizers.*` used to train the model.
        Can also be a string (one of 'Adagrad', 'Adam', 'Ftrl', 'RMSProp',
        SGD'), or callable. Defaults to Adagrad optimizer.
      activation_fn: Activation function applied to each layer. If `None`, will
        use `tf.nn.relu`.
      dropout: When not `None`, the probability we will drop out a given
        coordinate.
      config: `RunConfig` object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights are warm-started, and it is assumed that vocabularies and Tensor
        names are unchanged.
      batch_norm: Whether to use batch normalization after each hidden layer.
    """

class DNNEstimator(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, head, hidden_units, feature_columns, model_dir: Incomplete | None = None, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, input_layer_partitioner: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, batch_norm: bool = False) -> None: ...

class DNNRegressorV2(estimator.EstimatorV2):
    '''A regressor for TensorFlow DNN models.

  Example:

  ```python
  categorical_feature_a = categorical_column_with_hash_bucket(...)
  categorical_feature_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_emb = embedding_column(
      categorical_column=categorical_feature_a, ...)
  categorical_feature_b_emb = embedding_column(
      categorical_column=categorical_feature_b, ...)

  estimator = tf.estimator.DNNRegressor(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256])

  # Or estimator using the ProximalAdagradOptimizer optimizer with
  # regularization.
  estimator = tf.estimator.DNNRegressor(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
      optimizer=tf.compat.v1.train.ProximalAdagradOptimizer(
        learning_rate=0.1,
        l1_regularization_strength=0.001
      ))

  # Or estimator using an optimizer with a learning rate decay.
  estimator = tf.estimator.DNNRegressor(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
      optimizer=lambda: tf.keras.optimizers.Adam(
          learning_rate=tf.compat.v1.train.exponential_decay(
              learning_rate=0.1,
              global_step=tf.compat.v1.train.get_global_step(),
              decay_steps=10000,
              decay_rate=0.96))

  # Or estimator with warm-starting from a previous checkpoint.
  estimator = tf.estimator.DNNRegressor(
      feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
      hidden_units=[1024, 512, 256],
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
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features\' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss is calculated by using mean squared error.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, hidden_units, feature_columns, model_dir: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False) -> None:
        """Initializes a `DNNRegressor` instance.

    Args:
      hidden_units: Iterable of number hidden units per layer. All layers are
        fully connected. Ex. `[64, 32]` means first layer has 64 nodes and
        second one has 32.
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
      optimizer: An instance of `tf.keras.optimizers.*` used to train the model.
        Can also be a string (one of 'Adagrad', 'Adam', 'Ftrl', 'RMSProp',
        SGD'), or callable. Defaults to Adagrad optimizer.
      activation_fn: Activation function applied to each layer. If `None`, will
        use `tf.nn.relu`.
      dropout: When not `None`, the probability we will drop out a given
        coordinate.
      config: `RunConfig` object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights are warm-started, and it is assumed that vocabularies and Tensor
        names are unchanged.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
      batch_norm: Whether to use batch normalization after each hidden layer.
    """

class DNNRegressor(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, hidden_units, feature_columns, model_dir: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, optimizer: str = 'Adagrad', activation_fn=..., dropout: Incomplete | None = None, input_layer_partitioner: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False) -> None: ...
