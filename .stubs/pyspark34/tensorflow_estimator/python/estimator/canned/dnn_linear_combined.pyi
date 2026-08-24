from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator
from tensorflow_estimator.python.estimator.canned import dnn as dnn, linear as linear, optimizers as optimizers
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.head import head_utils as head_utils, regression_head as regression_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class DNNLinearCombinedClassifierV2(estimator.EstimatorV2):
    '''An estimator for TensorFlow Linear and DNN joined classification models.

  Note: This estimator is also known as wide-n-deep.

  Example:

  ```python
  numeric_feature = numeric_column(...)
  categorical_column_a = categorical_column_with_hash_bucket(...)
  categorical_column_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_x_categorical_feature_b = crossed_column(...)
  categorical_feature_a_emb = embedding_column(
      categorical_column=categorical_feature_a, ...)
  categorical_feature_b_emb = embedding_column(
      categorical_id_column=categorical_feature_b, ...)

  estimator = tf.estimator.DNNLinearCombinedClassifier(
      # wide settings
      linear_feature_columns=[categorical_feature_a_x_categorical_feature_b],
      linear_optimizer=tf.keras.optimizers.Ftrl(...),
      # deep settings
      dnn_feature_columns=[
          categorical_feature_a_emb, categorical_feature_b_emb,
          numeric_feature],
      dnn_hidden_units=[1000, 500, 100],
      dnn_optimizer=tf.keras.optimizers.Adagrad(...),
      # warm-start settings
      warm_start_from="/path/to/checkpoint/dir")

  # To apply L1 and L2 regularization, you can set dnn_optimizer to:
  tf.compat.v1.train.ProximalAdagradOptimizer(
      learning_rate=0.1,
      l1_regularization_strength=0.001,
      l2_regularization_strength=0.001)
  # To apply learning rate decay, you can set dnn_optimizer to a callable:
  lambda: tf.keras.optimizers.Adam(
      learning_rate=tf.compat.v1.train.exponential_decay(
          learning_rate=0.1,
          global_step=tf.compat.v1.train.get_global_step(),
          decay_steps=10000,
          decay_rate=0.96)
  # It is the same for linear_optimizer.

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
  estimator.train(input_fn=input_fn_train, steps=100)
  metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

  * for each `column` in `dnn_feature_columns` + `linear_feature_columns`:
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
    def __init__(self, model_dir: Incomplete | None = None, linear_feature_columns: Incomplete | None = None, linear_optimizer: str = 'Ftrl', dnn_feature_columns: Incomplete | None = None, dnn_optimizer: str = 'Adagrad', dnn_hidden_units: Incomplete | None = None, dnn_activation_fn=..., dnn_dropout: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False, linear_sparse_combiner: str = 'sum') -> None:
        '''Initializes a DNNLinearCombinedClassifier instance.

    Args:
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      linear_feature_columns: An iterable containing all the feature columns
        used by linear part of the model. All items in the set must be instances
        of classes derived from `FeatureColumn`.
      linear_optimizer: An instance of `tf.keras.optimizers.*` used to apply
        gradients to the linear part of the model. Can also be a string (one of
        \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or callable. Defaults to
        FTRL optimizer.
      dnn_feature_columns: An iterable containing all the feature columns used
        by deep part of the model. All items in the set must be instances of
        classes derived from `FeatureColumn`.
      dnn_optimizer: An instance of `tf.keras.optimizers.*` used to apply
        gradients to the deep part of the model. Can also be a string (one of
        \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or callable. Defaults to
        Adagrad optimizer.
      dnn_hidden_units: List of hidden units per layer. All layers are fully
        connected.
      dnn_activation_fn: Activation function applied to each layer. If None,
        will use `tf.nn.relu`.
      dnn_dropout: When not None, the probability we will drop out a given
        coordinate.
      n_classes: Number of label classes. Defaults to 2, namely binary
        classification. Must be > 1.
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
      config: RunConfig object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights are warm-started, and it is assumed that vocabularies and Tensor
        names are unchanged.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
      batch_norm: Whether to use batch normalization after each hidden layer.
      linear_sparse_combiner: A string specifying how to reduce the linear model
        if a categorical column is multivalent.  One of "mean", "sqrtn", and
        "sum" -- these are effectively different ways to do example-level
        normalization, which can be useful for bag-of-words features.  For more
        details, see `tf.feature_column.linear_model`.

    Raises:
      ValueError: If both linear_feature_columns and dnn_features_columns are
        empty at the same time.
    '''

class DNNLinearCombinedClassifier(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, model_dir: Incomplete | None = None, linear_feature_columns: Incomplete | None = None, linear_optimizer: str = 'Ftrl', dnn_feature_columns: Incomplete | None = None, dnn_optimizer: str = 'Adagrad', dnn_hidden_units: Incomplete | None = None, dnn_activation_fn=..., dnn_dropout: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, input_layer_partitioner: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False, linear_sparse_combiner: str = 'sum') -> None: ...

class DNNLinearCombinedEstimatorV2(estimator.EstimatorV2):
    """An estimator for TensorFlow Linear and DNN joined models with custom head.

  Note: This estimator is also known as wide-n-deep.

  Example:

  ```python
  numeric_feature = numeric_column(...)
  categorical_column_a = categorical_column_with_hash_bucket(...)
  categorical_column_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_x_categorical_feature_b = crossed_column(...)
  categorical_feature_a_emb = embedding_column(
      categorical_column=categorical_feature_a, ...)
  categorical_feature_b_emb = embedding_column(
      categorical_column=categorical_feature_b, ...)

  estimator = tf.estimator.DNNLinearCombinedEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3),
      # wide settings
      linear_feature_columns=[categorical_feature_a_x_categorical_feature_b],
      linear_optimizer=tf.keras.optimizers.Ftrl(...),
      # deep settings
      dnn_feature_columns=[
          categorical_feature_a_emb, categorical_feature_b_emb,
          numeric_feature],
      dnn_hidden_units=[1000, 500, 100],
      dnn_optimizer=tf.keras.optimizers.Adagrad(...))

  # To apply L1 and L2 regularization, you can set dnn_optimizer to:
  tf.compat.v1.train.ProximalAdagradOptimizer(
      learning_rate=0.1,
      l1_regularization_strength=0.001,
      l2_regularization_strength=0.001)
  # To apply learning rate decay, you can set dnn_optimizer to a callable:
  lambda: tf.keras.optimizers.Adam(
      learning_rate=tf.compat.v1.train.exponential_decay(
          learning_rate=0.1,
          global_step=tf.compat.v1.train.get_global_step(),
          decay_steps=10000,
          decay_rate=0.96)
  # It is the same for linear_optimizer.

  # Input builders
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

  * for each `column` in `dnn_feature_columns` + `linear_feature_columns`:
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss is calculated by using mean squared error.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  """
    def __init__(self, head, model_dir: Incomplete | None = None, linear_feature_columns: Incomplete | None = None, linear_optimizer: str = 'Ftrl', dnn_feature_columns: Incomplete | None = None, dnn_optimizer: str = 'Adagrad', dnn_hidden_units: Incomplete | None = None, dnn_activation_fn=..., dnn_dropout: Incomplete | None = None, config: Incomplete | None = None, batch_norm: bool = False, linear_sparse_combiner: str = 'sum') -> None:
        '''Initializes a DNNLinearCombinedEstimator instance.

    Args:
      head: A `Head` instance constructed with a method such as
        `tf.estimator.MultiLabelHead`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into an estimator to
        continue training a previously saved model.
      linear_feature_columns: An iterable containing all the feature columns
        used by linear part of the model. All items in the set must be instances
        of classes derived from `FeatureColumn`.
      linear_optimizer: An instance of `tf.keras.optimizers.*` used to apply
        gradients to the linear part of the model. Can also be a string (one of
        \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or callable. Defaults to
        FTRL optimizer.
      dnn_feature_columns: An iterable containing all the feature columns used
        by deep part of the model. All items in the set must be instances of
        classes derived from `FeatureColumn`.
      dnn_optimizer: An instance of `tf.keras.optimizers.*` used to apply
        gradients to the deep part of the model. Can also be a string (one of
        \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or callable. Defaults to
        Adagrad optimizer.
      dnn_hidden_units: List of hidden units per layer. All layers are fully
        connected.
      dnn_activation_fn: Activation function applied to each layer. If None,
        will use `tf.nn.relu`.
      dnn_dropout: When not None, the probability we will drop out a given
        coordinate.
      config: RunConfig object to configure the runtime settings.
      batch_norm: Whether to use batch normalization after each hidden layer.
      linear_sparse_combiner: A string specifying how to reduce the linear model
        if a categorical column is multivalent.  One of "mean", "sqrtn", and
        "sum" -- these are effectively different ways to do example-level
        normalization, which can be useful for bag-of-words features.  For more
        details, see `tf.feature_column.linear_model`.

    Raises:
      ValueError: If both linear_feature_columns and dnn_features_columns are
        empty at the same time.
    '''

class DNNLinearCombinedEstimator(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, head, model_dir: Incomplete | None = None, linear_feature_columns: Incomplete | None = None, linear_optimizer: str = 'Ftrl', dnn_feature_columns: Incomplete | None = None, dnn_optimizer: str = 'Adagrad', dnn_hidden_units: Incomplete | None = None, dnn_activation_fn=..., dnn_dropout: Incomplete | None = None, input_layer_partitioner: Incomplete | None = None, config: Incomplete | None = None, batch_norm: bool = False, linear_sparse_combiner: str = 'sum') -> None: ...

class DNNLinearCombinedRegressorV2(estimator.EstimatorV2):
    '''An estimator for TensorFlow Linear and DNN joined models for regression.

  Note: This estimator is also known as wide-n-deep.

  Example:

  ```python
  numeric_feature = numeric_column(...)
  categorical_column_a = categorical_column_with_hash_bucket(...)
  categorical_column_b = categorical_column_with_hash_bucket(...)

  categorical_feature_a_x_categorical_feature_b = crossed_column(...)
  categorical_feature_a_emb = embedding_column(
      categorical_column=categorical_feature_a, ...)
  categorical_feature_b_emb = embedding_column(
      categorical_column=categorical_feature_b, ...)

  estimator = tf.estimator.DNNLinearCombinedRegressor(
      # wide settings
      linear_feature_columns=[categorical_feature_a_x_categorical_feature_b],
      linear_optimizer=tf.keras.optimizers.Ftrl(...),
      # deep settings
      dnn_feature_columns=[
          categorical_feature_a_emb, categorical_feature_b_emb,
          numeric_feature],
      dnn_hidden_units=[1000, 500, 100],
      dnn_optimizer=tf.keras.optimizers.Adagrad(...),
      # warm-start settings
      warm_start_from="/path/to/checkpoint/dir")

  # To apply L1 and L2 regularization, you can set dnn_optimizer to:
  tf.compat.v1.train.ProximalAdagradOptimizer(
      learning_rate=0.1,
      l1_regularization_strength=0.001,
      l2_regularization_strength=0.001)
  # To apply learning rate decay, you can set dnn_optimizer to a callable:
  lambda: tf.keras.optimizers.Adam(
      learning_rate=tf.compat.v1.train.exponential_decay(
          learning_rate=0.1,
          global_step=tf.compat.v1.train.get_global_step(),
          decay_steps=10000,
          decay_rate=0.96)
  # It is the same for linear_optimizer.

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
  estimator.train(input_fn=input_fn_train, steps=100)
  metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

  * for each `column` in `dnn_feature_columns` + `linear_feature_columns`:
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
    def __init__(self, model_dir: Incomplete | None = None, linear_feature_columns: Incomplete | None = None, linear_optimizer: str = 'Ftrl', dnn_feature_columns: Incomplete | None = None, dnn_optimizer: str = 'Adagrad', dnn_hidden_units: Incomplete | None = None, dnn_activation_fn=..., dnn_dropout: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False, linear_sparse_combiner: str = 'sum') -> None:
        '''Initializes a DNNLinearCombinedRegressor instance.

    Args:
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      linear_feature_columns: An iterable containing all the feature columns
        used by linear part of the model. All items in the set must be instances
        of classes derived from `FeatureColumn`.
      linear_optimizer: An instance of `tf.keras.optimizers.*` used to apply
        gradients to the linear part of the model. Can also be a string (one of
        \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or callable. Defaults to
        FTRL optimizer.
      dnn_feature_columns: An iterable containing all the feature columns used
        by deep part of the model. All items in the set must be instances of
        classes derived from `FeatureColumn`.
      dnn_optimizer: An instance of `tf.keras.optimizers.*` used to apply
        gradients to the deep part of the model. Can also be a string (one of
        \'Adagrad\', \'Adam\', \'Ftrl\', \'RMSProp\', \'SGD\'), or callable. Defaults to
        Adagrad optimizer.
      dnn_hidden_units: List of hidden units per layer. All layers are fully
        connected.
      dnn_activation_fn: Activation function applied to each layer. If None,
        will use `tf.nn.relu`.
      dnn_dropout: When not None, the probability we will drop out a given
        coordinate.
      label_dimension: Number of regression targets per example. This is the
        size of the last dimension of the labels and logits `Tensor` objects
        (typically, these have shape `[batch_size, label_dimension]`).
      weight_column: A string or a `NumericColumn` created by
        `tf.feature_column.numeric_column` defining feature column representing
        weights. It is used to down weight or boost examples during training. It
        will be multiplied by the loss of the example. If it is a string, it is
        used as a key to fetch weight tensor from the `features`. If it is a
        `_NumericColumn`, raw tensor is fetched by key `weight_column.key`, then
        weight_column.normalizer_fn is applied on it to get weight tensor.
      config: RunConfig object to configure the runtime settings.
      warm_start_from: A string filepath to a checkpoint to warm-start from, or
        a `WarmStartSettings` object to fully configure warm-starting.  If the
        string filepath is provided instead of a `WarmStartSettings`, then all
        weights are warm-started, and it is assumed that vocabularies and Tensor
        names are unchanged.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
      batch_norm: Whether to use batch normalization after each hidden layer.
      linear_sparse_combiner: A string specifying how to reduce the linear model
        if a categorical column is multivalent.  One of "mean", "sqrtn", and
        "sum" -- these are effectively different ways to do example-level
        normalization, which can be useful for bag-of-words features.  For more
        details, see `tf.feature_column.linear_model`.

    Raises:
      ValueError: If both linear_feature_columns and dnn_features_columns are
        empty at the same time.
    '''

class DNNLinearCombinedRegressor(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, model_dir: Incomplete | None = None, linear_feature_columns: Incomplete | None = None, linear_optimizer: str = 'Ftrl', dnn_feature_columns: Incomplete | None = None, dnn_optimizer: str = 'Adagrad', dnn_hidden_units: Incomplete | None = None, dnn_activation_fn=..., dnn_dropout: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, input_layer_partitioner: Incomplete | None = None, config: Incomplete | None = None, warm_start_from: Incomplete | None = None, loss_reduction=..., batch_norm: bool = False, linear_sparse_combiner: str = 'sum') -> None: ...
