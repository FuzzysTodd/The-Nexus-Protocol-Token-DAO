from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_output as export_output
from tensorflow_estimator.python.estimator.head import base_head as base_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class MultiHead(base_head.Head):
    """Creates a `Head` for multi-objective learning.

  This class merges the output of multiple `Head` objects. Specifically:

  * For training, sums losses of each head, calls `train_op_fn` with this
    final loss.
  * For eval, merges metrics by adding `head.name` suffix to the keys in eval
    metrics, such as `precision/head1.name`, `precision/head2.name`.
  * For prediction, merges predictions and updates keys in prediction dict to a
    2-tuple, `(head.name, prediction_key)`. Merges `export_outputs` such that
    by default the first head is served.

  Usage:

  >>> head1 = tf.estimator.MultiLabelHead(n_classes=2, name='head1')
  >>> head2 = tf.estimator.MultiLabelHead(n_classes=3, name='head2')
  >>> multi_head = tf.estimator.MultiHead([head1, head2])
  >>> logits = {
  ...    'head1': np.array([[-10., 10.], [-15., 10.]], dtype=np.float32),
  ...    'head2': np.array([[20., -20., 20.], [-30., 20., -20.]],
  ...    dtype=np.float32),}
  >>> labels = {
  ...    'head1': np.array([[1, 0], [1, 1]], dtype=np.int64),
  ...    'head2': np.array([[0, 1, 0], [1, 1, 0]], dtype=np.int64),}
  >>> features = {'x': np.array(((42,),), dtype=np.float32)}
  >>> # For large logits, sigmoid cross entropy loss is approximated as:
  >>> # loss = labels * (logits < 0) * (-logits) +
  >>> #        (1 - labels) * (logits > 0) * logits =>
  >>> # head1: expected_unweighted_loss = [[10., 10.], [15., 0.]]
  >>> # loss1 = ((10 + 10) / 2 + (15 + 0) / 2) / 2 = 8.75
  >>> # head2: expected_unweighted_loss = [[20., 20., 20.], [30., 0., 0]]
  >>> # loss2 = ((20 + 20 + 20) / 3 + (30 + 0 + 0) / 3) / 2 = 15.00
  >>> # loss = loss1 + loss2 = 8.75 + 15.00 = 23.75
  >>> loss = multi_head.loss(labels, logits, features=features)
  >>> print('{:.2f}'.format(loss.numpy()))
  23.75
  >>> eval_metrics = multi_head.metrics()
  >>> updated_metrics = multi_head.update_metrics(
  ...   eval_metrics, features, logits, labels)
  >>> for k in sorted(updated_metrics):
  ...  print('{} : {:.2f}'.format(k, updated_metrics[k].result().numpy()))
  auc/head1 : 0.17
  auc/head2 : 0.33
  auc_precision_recall/head1 : 0.60
  auc_precision_recall/head2 : 0.40
  average_loss/head1 : 8.75
  average_loss/head2 : 15.00
  loss/head1 : 8.75
  loss/head2 : 15.00
  >>> preds = multi_head.predictions(logits)
  >>> print(preds[('head1', 'logits')])
  tf.Tensor(
    [[-10.  10.]
     [-15.  10.]], shape=(2, 2), dtype=float32)

  Usage with a canned estimator:

  ```python
  # In `input_fn`, specify labels as a dict keyed by head name:
  def input_fn():
    features = ...
    labels1 = ...
    labels2 = ...
    return features, {'head1.name': labels1, 'head2.name': labels2}

  # In `model_fn`, specify logits as a dict keyed by head name:
  def model_fn(features, labels, mode):
    # Create simple heads and specify head name.
    head1 = tf.estimator.MultiClassHead(n_classes=3, name='head1')
    head2 = tf.estimator.BinaryClassHead(name='head2')
    # Create MultiHead from two simple heads.
    head = tf.estimator.MultiHead([head1, head2])
    # Create logits for each head, and combine them into a dict.
    logits1, logits2 = logit_fn()
    logits = {'head1.name': logits1, 'head2.name': logits2}
    # Return the merged EstimatorSpec
    return head.create_estimator_spec(..., logits=logits, ...)

  # Create an estimator with this model_fn.
  estimator = tf.estimator.Estimator(model_fn=model_fn)
  estimator.train(input_fn=input_fn)
  ```

  Also supports `logits` as a `Tensor` of shape
  `[D0, D1, ... DN, logits_dimension]`. It will split the `Tensor` along the
  last dimension and distribute it appropriately among the heads. E.g.:

  ```python
  # Input logits.
  logits = np.array([[-1., 1., 2., -2., 2.], [-1.5, 1., -3., 2., -2.]],
                    dtype=np.float32)
  # Suppose head1 and head2 have the following logits dimension.
  head1.logits_dimension = 2
  head2.logits_dimension = 3
  # After splitting, the result will be:
  logits_dict = {'head1_name': [[-1., 1.], [-1.5, 1.]],
                 'head2_name':  [[2., -2., 2.], [-3., 2., -2.]]}
  ```

  Usage:

  ```python
  def model_fn(features, labels, mode):
    # Create simple heads and specify head name.
    head1 = tf.estimator.MultiClassHead(n_classes=3, name='head1')
    head2 = tf.estimator.BinaryClassHead(name='head2')
    # Create multi-head from two simple heads.
    head = tf.estimator.MultiHead([head1, head2])
    # Create logits for the multihead. The result of logits is a `Tensor`.
    logits = logit_fn(logits_dimension=head.logits_dimension)
    # Return the merged EstimatorSpec
    return head.create_estimator_spec(..., logits=logits, ...)
  ```

  Args:
    heads: List or tuple of `Head` instances. All heads must have `name`
      specified. The first head in the list is the default used at serving time.
    head_weights: Optional list of weights, same length as `heads`. Used when
      merging losses to calculate the weighted sum of losses from each head. If
      `None`, all losses are weighted equally.
  """
    def __init__(self, heads, head_weights: Incomplete | None = None) -> None: ...
    @property
    def name(self):
        """See `base_head.Head` for details."""
    @property
    def logits_dimension(self):
        """See `base_head.Head` for details."""
    @property
    def loss_reduction(self):
        """See `base_head.Head` for details."""
    def loss(self, labels, logits, features: Incomplete | None = None, mode: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns regularized training loss. See `base_head.Head` for details."""
    def predictions(self, logits, keys: Incomplete | None = None):
        """Create predictions. See `base_head.Head` for details."""
    def metrics(self, regularization_losses: Incomplete | None = None):
        """Creates metrics. See `base_head.Head` for details."""
    def update_metrics(self, eval_metrics, features, logits, labels, regularization_losses: Incomplete | None = None):
        """Updates eval metrics. See `base_head.Head` for details."""
    def create_estimator_spec(self, features, mode, logits, labels: Incomplete | None = None, optimizer: Incomplete | None = None, trainable_variables: Incomplete | None = None, train_op_fn: Incomplete | None = None, update_ops: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns a `model_fn.EstimatorSpec`.

    Args:
      features: Input `dict` of `Tensor` or `SparseTensor` objects.
      mode: Estimator's `ModeKeys`.
      logits: Input `dict` keyed by head name, or logits `Tensor` with shape
        `[D0, D1, ... DN, logits_dimension]`. For many applications, the
        `Tensor` shape is `[batch_size, logits_dimension]`. If logits is a
        `Tensor`, it  will split the `Tensor` along the last dimension and
        distribute it appropriately among the heads. Check `MultiHead` for
        examples.
      labels: Input `dict` keyed by head name. For each head, the label value
        can be integer or string `Tensor` with shape matching its corresponding
        `logits`.`labels` is a required argument when `mode` equals `TRAIN` or
        `EVAL`.
      optimizer: An `tf.keras.optimizers.Optimizer` instance to optimize the
        loss in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
        trainable_variables)`, which updates variables to minimize `loss`.
      trainable_variables: A list or tuple of `Variable` objects to update to
        minimize `loss`. In Tensorflow 1.x, by default these are the list of
        variables collected in the graph under the key
        `GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
        collections and GraphKeys, trainable_variables need to be passed
        explicitly here.
      train_op_fn: Function that takes a scalar loss `Tensor` and returns
        `train_op`. Used if `optimizer` is `None`.
      update_ops: A list or tuple of update ops to be run at training time. For
        example, layers such as BatchNormalization create mean and variance
        update ops that need to be run at training time. In Tensorflow 1.x,
        these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
        doesn't have collections, update_ops need to be passed explicitly here.
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses. These losses are
        usually expressed as a batch average, so for best results, in each head,
        users need to use the default `loss_reduction=SUM_OVER_BATCH_SIZE` to
        avoid scaling errors.  Compared to the regularization losses for each
        head, this loss is to regularize the merged loss of all heads in multi
        head, and will be added to the overall training loss of multi head.

    Returns:
      A `model_fn.EstimatorSpec` instance.

    Raises:
      ValueError: If both `train_op_fn` and `optimizer` are `None` in TRAIN
      mode, or if both are set.
      If `mode` is not in Estimator's `ModeKeys`.
    """
