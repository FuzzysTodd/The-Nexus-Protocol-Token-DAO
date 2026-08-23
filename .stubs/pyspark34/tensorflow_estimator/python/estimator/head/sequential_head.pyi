import abc
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.head import base_head as base_head, multi_head as multi_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class _SequentialHead(base_head.Head, metaclass=abc.ABCMeta):
    """Interface for the head of a sequential model.

  A sequential head handles input sequences of different lengths to compute the
  output of a model. It requires a sequence mask tensor, to indicate which steps
  of the sequences are padded and ensure proper aggregation for loss and metrics
  computation. It has a `input_sequence_mask_key` property that specifies which
  tensor of the feature dictionary to use as the sequence mask tensor.

  Such a head can for instance be used with `RNNEstimator` for sequential
  predictions.

  Example of usage:
    ```python
    def _my_model_fn(features, labels, mode, params, config=None):
      feature_layer = tf.feature_column.SequenceFeatureLayer(columns)
      input_layer, sequence_length = feature_layer(features)
      sequence_length_mask = tf.sequence_mask(sequence_length)
      rnn_layer = tf.keras.layers.RNN(cell=tf.keras.layers.SimpleRNNCell(units),
                                      return_sequences=True)
      logits = rnn_layer(input_layer, mask=sequence_length_mask)
      features[sequential_head.input_sequence_mask_key] = sequence_length_mask
      return sequential_head.create_estimator_spec(
          features=features,
          labels=labels,
          mode=mode,
          logits=logits,
          optimizer=optimizer)
    ```
  """
    __metaclass__ = abc.ABCMeta
    @property
    @abc.abstractmethod
    def input_sequence_mask_key(self):
        """Key of the sequence mask tensor in the feature dictionary.

    Returns:
      A string.
    """

class SequentialHeadWrapper(_SequentialHead):
    """Sequential head wrapping a Head object.

  Wraps a `Head` object and applies a sequential mask to:
    - Loss aggregation: To only account for masked steps. Used for
      `create_estimator_spec` and `loss` methods.
    - Metrics: The sequence mask is used to only account for mask steps in
      metrics computation with the `update_metrics` method.
    - Predictions: To add a sequence length mask tensor to the predictions
      dictionary.
  """
    def __init__(self, static_head, sequence_length_mask: str = 'sequence_length_mask', feature_columns: Incomplete | None = None) -> None:
        """Initializes a `SequentialHeadWrapper` instance.

    Example of usage:
      ```python
      # Define a sequential head.
      static_head = tf.estimator.BinaryClassHead(weight_column='weights')
      sequential_head = head_lib.SequentialHeadWrapper(
          static_head=static_head, sequence_length_mask='mask',
          feature_columns='weights')

      # Define feature columns and parsing spec.
      feature_columns = [
        tf.feature_column.sequence_numeric_column('sequential-feature')
      ]
      label_column = tf.feature_column.sequence_numeric_column(
          'label', dtype=tf.int32),
      weight_column = tf.feature_column.sequence_numeric_column('weights')
      parsing_spec = tf.feature_column.make_parse_example_spec(
          feature_columns + [label_column, weight_column])

      # Use the head in a model function.
      def _my_model_fn(features, labels, mode, params, config=None):
        feature_layer = tf.feature_column.SequenceFeatureLayer(feature_columns)
        input_layer, sequence_length = feature_layer(features)
        sequence_length_mask = tf.sequence_mask(sequence_length)
        rnn_layer = tf.keras.layers.RNN(
            cell=tf.keras.layers.SimpleRNNCell(units),
            return_sequences=True)
        logits = rnn_layer(input_layer, mask=sequence_length_mask)
        features['mask'] = sequence_length_mask
        return sequential_head.create_estimator_spec(
            features=features,
            labels=labels,
            mode=mode,
            logits=logits,
            optimizer=optimizer)
      ```

    Args:
      static_head: `Head` object, static head to wrap.
      sequence_length_mask: `str`, name of sequence length mask tensor in
        features dictionary. Tensor must be a dense tensor of shape [batch_size,
        seq_length].
      feature_columns: `str` or list of the former. Specifies the features of
        the features dictionary to which the sequence length mask must be
        applied, and which are passed to the static head's methods when calling
        `create_estimator_spec`, `loss` or `update_metrics`. This is typically a
        weight tensor.

    Raises:
      TypeError: If `sequence_length_mask` is not of string type.
      TypeError: If provided features columns are not of string type.
    """
    def loss(self, logits, labels, features: Incomplete | None = None, mode: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Flattens input and returns regularized training loss.

    Flattens `logits`, `labels`, and `features` tensors that are specified by
    the head's `feature_columns` before calling the static head's `loss` method.

    Args:
      logits: Logits `Tensor` of rank >= 2 and shape [batch_size, seq_length,
        D2, ... DN].
      labels: Labels `Tensor` or `SparseTensor` or rank >= 2 and shape
        [batch_size, seq_length, D2, ... DN].
      features: Input `dict` mapping string feature names to `Tensor` or
        `SparseTensor` objects containing the values for that feature in a
        minibatch. Must contain the sequence length mask tensor. Features
        corresponding to the sequential's head `feature_columns` are flattened
        and passed to the static head's `loss` method.
      mode: Estimator's `ModeKeys`. To be used in case loss calculation is
        different in Train and Eval mode.
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses.

    Returns:
      A scalar `Tensor` representing regularized training loss used in train and
      eval.
    """
    def create_estimator_spec(self, features, mode, logits, labels: Incomplete | None = None, optimizer: Incomplete | None = None, trainable_variables: Incomplete | None = None, train_op_fn: Incomplete | None = None, update_ops: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns `EstimatorSpec` that a model_fn can return.

    If in TRAIN or EVAL mode, `logits`, `labels`, and `features` tensors
    corresponding to the head's `feature_columns` are flattened before calling
    the static head's `create_estimator_spec` method.
    If in PREDICT mode, no flattening is done. The `EstimatatorSpec` is computed
    using the static head's `create_estimator_spec` method. The sequence length
    mask tensor is added to the predictions dictionary.

    Args:
      features: Input `dict` mapping string feature names to `Tensor` or
        `SparseTensor` objects containing the values for that feature in a
        minibatch. If in TRAIN or EVAL mode, only specified features are
        flattened and passed to the static head's method.
      mode: Estimator's `ModeKeys`.
      logits: Logits `Tensor` of rank >= 2 and shape [batch_size, seq_length,
        D2, ... DN].
      labels: Labels `Tensor` or `SparseTensor` or rank >= 2 and shape
        [batch_size, seq_length, D2, ... DN].
      optimizer: An `tf.keras.optimizers.Optimizer` instance to optimize the
        loss in TRAIN mode. Namely, sets
        `train_op = optimizer.get_updates(loss, trainable_variables)`, which
        updates variables to minimize `loss`.
      trainable_variables: A list or tuple of `Variable` objects to update to
        minimize `loss`. In Tensorflow 1.x, by default these are the list of
        variables collected in the graph under the key
        `GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
        collections and GraphKeys, trainable_variables need to be passed
        explicitly here.
      train_op_fn: Function that takes a scalar loss `Tensor` and returns an op
        to optimize the model with the loss in TRAIN mode. Used if `optimizer`
        is `None`. Exactly one of `train_op_fn` and `optimizer` must be set in
        TRAIN mode. By default, it is `None` in other modes. If you want to
        optimize loss yourself, you can pass `lambda _: tf.no_op()` and then use
          `EstimatorSpec.loss` to compute and apply gradients.
      update_ops: A list or tuple of update ops to be run at training time. For
        example, layers such as BatchNormalization create mean and variance
        update ops that need to be run at training time. In Tensorflow 1.x,
        these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
        doesn't have collections, update_ops need to be passed explicitly here.
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses.

    Returns:
      `EstimatorSpec`.
    """
    def update_metrics(self, eval_metrics, features, logits, labels, regularization_losses: Incomplete | None = None):
        """Updates metric objects and returns a `dict` of the updated metrics.

    Flattens `logits`, `labels`, and `features` tensors that are specified by
    the head's feature_columns` before calling the static head's
    `update_metrics` method.

    Args:
      eval_metrics: A `dict` of metrics to be updated.
      features: Input `dict` mapping string feature names to `Tensor` or
        `SparseTensor` objects containing the values for that feature in a
        minibatch. Only specified features are flattened and passed to the
        static head's method.
      logits: Logits `Tensor` of rank >= 2 and shape [batch_size, seq_length,
        D2, ... DN].
      labels: Labels `Tensor` or `SparseTensor` or rank >= 2 and shape
        [batch_size, seq_length, D2, ... DN].
      regularization_losses: A list of additional scalar losses to be added to
        the training and evaluation loss, such as regularization losses.

    Returns:
       A `dict` of updated metrics keyed by name. The value is an instance of
       `Metric` class.
    """
    def predictions(self, logits, keys: Incomplete | None = None):
        """Calls the static head's `predictions` method."""
    def metrics(self, regularization_losses: Incomplete | None = None):
        """Calls the static head's `metrics` method."""
    @property
    def input_sequence_mask_key(self):
        """Returns the key for the sequence mask feature."""
    @property
    def logits_dimension(self):
        """Returns the logits dimension of the static head."""
    @property
    def loss_reduction(self):
        """Returns the loss reduction of the static head."""
    @property
    def name(self):
        """Returns the name of the static head."""
    @property
    def static_head(self):
        """Returns the wrapped static head."""
