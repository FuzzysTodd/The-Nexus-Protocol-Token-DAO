import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator, model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import optimizers as optimizers
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export

USE_DEFAULT: Incomplete

class RNNModel(tf.keras.models.Model):
    """A Keras RNN model.

  Composition of layers to compute logits from RNN model, along with training
  and inference features. See `tf.keras.models.Model` for more details on Keras
  models.

  Example of usage:

  ```python
  rating = tf.feature_column.embedding_column(
      tf.feature_column.sequence_categorical_column_with_identity('rating', 5),
      10)
  rnn_layer = tf.keras.layers.SimpleRNN(20)
  rnn_model = RNNModel(rnn_layer, units=1, sequence_feature_columns=[rating])

  rnn_model.compile(
      tf.keras.optimizers.Adam(), loss=tf.keras.losses.MeanSquaredError())
  rnn_model.fit(generator(), epochs=10, steps_per_epoch=100)
  rnn_model.predict({'rating': np.array([[0, 1], [2, 3]])}, steps=1)
  ```
  """
    def __init__(self, rnn_layer, units, sequence_feature_columns, context_feature_columns: Incomplete | None = None, activation: Incomplete | None = None, return_sequences: bool = False, **kwargs) -> None:
        """Initializes a RNNModel instance.

    Args:
      rnn_layer: A Keras RNN layer.
      units: An int indicating the dimension of the logit layer, and of the
        model output.
      sequence_feature_columns: An iterable containing the `FeatureColumn`s that
        represent sequential input. All items in the set should either be
        sequence columns (e.g. `sequence_numeric_column`) or constructed from
        one (e.g. `embedding_column` with `sequence_categorical_column_*` as
        input).
      context_feature_columns: An iterable containing the `FeatureColumn`s for
        contextual input. The data represented by these columns will be
        replicated and given to the RNN at each timestep. These columns must be
        instances of classes derived from `DenseColumn` such as
        `numeric_column`, not the sequential variants.
      activation: Activation function to apply to the logit layer (for instance
        `tf.keras.activations.sigmoid`). If you don't specify anything, no
        activation is applied.
      return_sequences: A boolean indicating whether to return the last output
        in the output sequence, or the full sequence.
      **kwargs: Additional arguments.

    Raises:
      ValueError: If `units` is not an int.
    """
    def call(self, inputs, training: Incomplete | None = None):
        """Computes the RNN output.

    By default no activation is applied and the logits are returned. To output
    probabilites an activation needs to be specified such as sigmoid or softmax.

    Args:
      inputs: A dict mapping keys to input tensors.
      training: Python boolean indicating whether the layers should behave in
        training mode or in inference mode. This argument is passed to the
        model's layers. This is for instance used with cells that use dropout.

    Returns:
      A `Tensor` with logits from RNN model. It has shape
      (batch_size, time_step, logits_size) if `return_sequence` is `True`,
      (batch_size, logits_size) otherwise.
    """
    def get_config(self):
        """Returns a dictionary with the config of the model."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None):
        """Creates a RNNModel from its config.

    Args:
      config: A Python dictionary, typically the output of `get_config`.
      custom_objects: Optional dictionary mapping names (strings) to custom
        classes or functions to be considered during deserialization.

    Returns:
      A RNNModel.
    """

class RNNEstimator(estimator.Estimator):
    """An Estimator for TensorFlow RNN models with user-specified head.

  Example:

  ```python
  token_sequence = sequence_categorical_column_with_hash_bucket(...)
  token_emb = embedding_column(categorical_column=token_sequence, ...)

  estimator = RNNEstimator(
      head=tf.estimator.RegressionHead(),
      sequence_feature_columns=[token_emb],
      units=[32, 16], cell_type='lstm')

  # Or with custom RNN cell:
  def rnn_cell_fn(_):
    cells = [ tf.keras.layers.LSTMCell(size) for size in [32, 16] ]
    return tf.keras.layers.StackedRNNCells(cells)

  estimator = RNNEstimator(
      head=tf.estimator.RegressionHead(),
      sequence_feature_columns=[token_emb],
      rnn_cell_fn=rnn_cell_fn)

  # Input builders
  def input_fn_train: # returns x, y
    pass
  estimator.train(input_fn=input_fn_train, steps=100)

  def input_fn_eval: # returns x, y
    pass
  metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
  def input_fn_predict: # returns x, None
    pass
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

  * if the head's `weight_column` is not `None`, a feature with
    `key=weight_column` whose value is a `Tensor`.
  * for each `column` in `sequence_feature_columns`:
    - a feature with `key=column.name` whose `value` is a `SparseTensor`.
  * for each `column` in `context_feature_columns`:
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss and predicted output are determined by the specified head.

  @compatibility(eager)
  Estimators are not compatible with eager execution.
  @end_compatibility
  """
    def __init__(self, head, sequence_feature_columns, context_feature_columns: Incomplete | None = None, units: Incomplete | None = None, cell_type=..., rnn_cell_fn: Incomplete | None = None, return_sequences: bool = False, model_dir: Incomplete | None = None, optimizer: str = 'Adagrad', config: Incomplete | None = None) -> None:
        """Initializes a `RNNEstimator` instance.

    Args:
      head: A `Head` instance. This specifies the model's output and loss
        function to be optimized.
      sequence_feature_columns: An iterable containing the `FeatureColumn`s that
        represent sequential input. All items in the set should either be
        sequence columns (e.g. `sequence_numeric_column`) or constructed from
        one (e.g. `embedding_column` with `sequence_categorical_column_*` as
        input).
      context_feature_columns: An iterable containing the `FeatureColumn`s for
        contextual input. The data represented by these columns will be
        replicated and given to the RNN at each timestep. These columns must be
        instances of classes derived from `DenseColumn` such as
        `numeric_column`, not the sequential variants.
      units: Iterable of integer number of hidden units per RNN layer. If set,
        `cell_type` must also be specified and `rnn_cell_fn` must be `None`.
      cell_type: A class producing a RNN cell or a string specifying the cell
        type. Supported strings are: `'simple_rnn'`, `'lstm'`, and `'gru'`. If
          set, `units` must also be specified and `rnn_cell_fn` must be `None`.
      rnn_cell_fn: A function that returns a RNN cell instance that will be used
        to construct the RNN. If set, `units` and `cell_type` cannot be set.
        This is for advanced users who need additional customization beyond
        `units` and `cell_type`. Note that `tf.keras.layers.StackedRNNCells` is
        needed for stacked RNNs.
      return_sequences: A boolean indicating whether to return the last output
        in the output sequence, or the full sequence.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      optimizer: An instance of `tf.Optimizer` or string specifying optimizer
        type. Defaults to Adagrad optimizer.
      config: `RunConfig` object to configure the runtime settings.

    Note that a RNN cell has:
      - a `call` method.
      - a `state_size` attribute.
      - a `output_size` attribute.
      - a `get_initial_state` method.

    See the documentation on `tf.keras.layers.RNN` for more details.

    Raises:
      ValueError: If `units`, `cell_type`, and `rnn_cell_fn` are not
        compatible.
    """

class RNNClassifier(RNNEstimator):
    """A classifier for TensorFlow RNN models.

  Trains a recurrent neural network model to classify instances into one of
  multiple classes.

  Example:

  ```python
  token_sequence = sequence_categorical_column_with_hash_bucket(...)
  token_emb = embedding_column(categorical_column=token_sequence, ...)

  estimator = RNNClassifier(
      sequence_feature_columns=[token_emb],
      units=[32, 16], cell_type='lstm')

  # Input builders
  def input_fn_train: # returns x, y
    pass
  estimator.train(input_fn=input_fn_train, steps=100)

  def input_fn_eval: # returns x, y
    pass
  metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
  def input_fn_predict: # returns x, None
    pass
  predictions = estimator.predict(input_fn=input_fn_predict)
  ```

  Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

  * if `weight_column` is not `None`, a feature with
    `key=weight_column` whose value is a `Tensor`.
  * for each `column` in `sequence_feature_columns`:
    - a feature with `key=column.name` whose `value` is a `SparseTensor`.
  * for each `column` in `context_feature_columns`:
    - if `column` is a `CategoricalColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedCategoricalColumn`, two features: the first
      with `key` the id column name, the second with `key` the weight column
      name. Both features' `value` must be a `SparseTensor`.
    - if `column` is a `DenseColumn`, a feature with `key=column.name`
      whose `value` is a `Tensor`.

  Loss is calculated by using softmax cross entropy.

  @compatibility(eager)
  Estimators are not compatible with eager execution.
  @end_compatibility
  """
    def __init__(self, sequence_feature_columns, context_feature_columns: Incomplete | None = None, units: Incomplete | None = None, cell_type=..., rnn_cell_fn: Incomplete | None = None, return_sequences: bool = False, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Adagrad', loss_reduction=..., sequence_mask: str = 'sequence_mask', config: Incomplete | None = None) -> None:
        """Initializes a `RNNClassifier` instance.

    Args:
      sequence_feature_columns: An iterable containing the `FeatureColumn`s that
        represent sequential input. All items in the set should either be
        sequence columns (e.g. `sequence_numeric_column`) or constructed from
        one (e.g. `embedding_column` with `sequence_categorical_column_*` as
        input).
      context_feature_columns: An iterable containing the `FeatureColumn`s for
        contextual input. The data represented by these columns will be
        replicated and given to the RNN at each timestep. These columns must be
        instances of classes derived from `DenseColumn` such as
        `numeric_column`, not the sequential variants.
      units: Iterable of integer number of hidden units per RNN layer. If set,
        `cell_type` must also be specified and `rnn_cell_fn` must be `None`.
      cell_type: A class producing a RNN cell or a string specifying the cell
        type. Supported strings are: `'simple_rnn'`, `'lstm'`, and `'gru'`. If
          set, `units` must also be specified and `rnn_cell_fn` must be `None`.
      rnn_cell_fn: A function that returns a RNN cell instance that will be used
        to construct the RNN. If set, `units` and `cell_type` cannot be set.
        This is for advanced users who need additional customization beyond
        `units` and `cell_type`. Note that `tf.keras.layers.StackedRNNCells` is
        needed for stacked RNNs.
      return_sequences: A boolean indicating whether to return the last output
        in the output sequence, or the full sequence. Note that if True,
        `weight_column` must be None or a string.
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
        `NumericColumn`, raw tensor is fetched by key `weight_column.key`, then
        weight_column.normalizer_fn is applied on it to get weight tensor.
      label_vocabulary: A list of strings represents possible label values. If
        given, labels must be string type and have any value in
        `label_vocabulary`. If it is not given, that means labels are already
        encoded as integer or float within [0, 1] for `n_classes=2` and encoded
        as integer values in {0, 1,..., n_classes-1} for `n_classes`>2 . Also
        there will be errors if vocabulary is not provided and labels are
        string.
      optimizer: An instance of `tf.Optimizer` or string specifying optimizer
        type. Defaults to Adagrad optimizer.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
      sequence_mask: A string with the name of the sequence mask tensor. If
        `sequence_mask` is in the features dictionary, the provided tensor is
        used, otherwise the sequence mask is computed from the length of
        sequential features. The sequence mask is used in evaluation and
        training mode to aggregate loss and metrics computation while excluding
        padding steps. It is also added to the predictions dictionary in
        prediction mode to indicate which steps are padding.
      config: `RunConfig` object to configure the runtime settings.

    Note that a RNN cell has:
      - a `call` method.
      - a `state_size` attribute.
      - a `output_size` attribute.
      - a `get_initial_state` method.

    See the documentation on `tf.keras.layers.RNN` for more details.

    Raises:
      ValueError: If `units`, `cell_type`, and `rnn_cell_fn` are not
        compatible.
    """
