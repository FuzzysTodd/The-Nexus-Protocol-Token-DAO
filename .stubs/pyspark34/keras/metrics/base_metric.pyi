import abc
from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils, keras_tensor as keras_tensor
from keras.saving.legacy.saved_model import metric_serialization as metric_serialization
from keras.utils import generic_utils as generic_utils, losses_utils as losses_utils, metrics_utils as metrics_utils, tf_utils as tf_utils

class Metric(base_layer.Layer, metaclass=abc.ABCMeta):
    """Encapsulates metric logic and state.

    Args:
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      **kwargs: Additional layer keywords arguments.

    Standalone usage:

    ```python
    m = SomeMetric(...)
    for input in ...:
      m.update_state(input)
    print('Final result: ', m.result().numpy())
    ```

    Usage with `compile()` API:

    ```python
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.RMSprop(0.01),
                  loss=tf.keras.losses.CategoricalCrossentropy(),
                  metrics=[tf.keras.metrics.CategoricalAccuracy()])

    data = np.random.random((1000, 32))
    labels = np.random.random((1000, 10))

    dataset = tf.data.Dataset.from_tensor_slices((data, labels))
    dataset = dataset.batch(32)

    model.fit(dataset, epochs=10)
    ```

    To be implemented by subclasses:
    * `__init__()`: All state variables should be created in this method by
      calling `self.add_weight()` like: `self.var = self.add_weight(...)`
    * `update_state()`: Has all updates to the state variables like:
      self.var.assign_add(...).
    * `result()`: Computes and returns a scalar value or a dict of scalar values
      for the metric from the state variables.

    Example subclass implementation:

    ```python
    class BinaryTruePositives(tf.keras.metrics.Metric):

      def __init__(self, name='binary_true_positives', **kwargs):
        super(BinaryTruePositives, self).__init__(name=name, **kwargs)
        self.true_positives = self.add_weight(name='tp', initializer='zeros')

      def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = tf.cast(y_true, tf.bool)
        y_pred = tf.cast(y_pred, tf.bool)

        values = tf.logical_and(tf.equal(y_true, True), tf.equal(y_pred, True))
        values = tf.cast(values, self.dtype)
        if sample_weight is not None:
          sample_weight = tf.cast(sample_weight, self.dtype)
          sample_weight = tf.broadcast_to(sample_weight, values.shape)
          values = tf.multiply(values, sample_weight)
        self.true_positives.assign_add(tf.reduce_sum(values))

      def result(self):
        return self.true_positives
    ```
    """
    stateful: bool
    built: bool
    def __init__(self, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    def __new__(cls, *args, **kwargs): ...
    def __call__(self, *args, **kwargs):
        """Accumulates statistics and then computes metric result value.

        Args:
          *args:
          **kwargs: A mini-batch of inputs to the Metric,
            passed on to `update_state()`.

        Returns:
          The metric value tensor.
        """
    def __deepcopy__(self, memo: Incomplete | None = None): ...
    @property
    def dtype(self): ...
    def get_config(self):
        """Returns the serializable config of the metric."""
    def reset_state(self):
        """Resets all of the metric state variables.

        This function is called between epochs/steps,
        when a metric is evaluated during training.
        """
    @abc.abstractmethod
    def update_state(self, *args, **kwargs):
        """Accumulates statistics for the metric.

        Note: This function is executed as a graph function in graph mode.
        This means:
          a) Operations on the same resource are executed in textual order.
             This should make it easier to do things like add the updated
             value of a variable to another, for example.
          b) You don't need to worry about collecting the update ops to execute.
             All update ops added to the graph by this function will be
             executed.
          As a result, code should generally work the same way with graph or
          eager execution.

        Args:
          *args:
          **kwargs: A mini-batch of inputs to the Metric.
        """
    def merge_state(self, metrics):
        """Merges the state from one or more metrics.

        This method can be used by distributed systems to merge the state
        computed by different metric instances. Typically the state will be
        stored in the form of the metric's weights. For example, a
        tf.keras.metrics.Mean metric contains a list of two weight values: a
        total and a count. If there were two instances of a
        tf.keras.metrics.Accuracy that each independently aggregated partial
        state for an overall accuracy calculation, these two metric's states
        could be combined as follows:

        >>> m1 = tf.keras.metrics.Accuracy()
        >>> _ = m1.update_state([[1], [2]], [[0], [2]])

        >>> m2 = tf.keras.metrics.Accuracy()
        >>> _ = m2.update_state([[3], [4]], [[3], [4]])

        >>> m2.merge_state([m1])
        >>> m2.result().numpy()
        0.75

        Args:
          metrics: an iterable of metrics. The metrics must have compatible
            state.

        Raises:
          ValueError: If the provided iterable does not contain metrics matching
            the metric's required specifications.
        """
    @abc.abstractmethod
    def result(self):
        """Computes and returns the scalar metric value tensor or a dict of
        scalars.

        Result computation is an idempotent operation that simply calculates the
        metric value using the state variables.

        Returns:
          A scalar tensor, or a dictionary of scalar tensors.
        """
    def add_weight(self, name, shape=(), aggregation=..., synchronization=..., initializer: Incomplete | None = None, dtype: Incomplete | None = None):
        """Adds state variable. Only for use by subclasses."""
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    def reset_states(self): ...

class Reduce(Metric):
    """Encapsulates metrics that perform a reduce operation on the values.

    Args:
      reduction: a `tf.keras.metrics.Reduction` enum value.
      name: string name of the metric instance.
      dtype: (Optional) data type of the metric result.
    """
    reduction: Incomplete
    total: Incomplete
    count: Incomplete
    def __init__(self, reduction, name, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, values, sample_weight: Incomplete | None = None):
        """Accumulates statistics for computing the metric.

        Args:
          values: Per-example value.
          sample_weight: Optional weighting of each example. Defaults to 1.

        Returns:
          Update op.
        """
    def result(self): ...

class Sum(Reduce):
    """Computes the (weighted) sum of the given values.

    For example, if values is [1, 3, 5, 7] then the sum is 16.
    If the weights were specified as [1, 1, 0, 0] then the sum would be 4.

    This metric creates one variable, `total`, that is used to compute the sum
    of `values`. This is ultimately returned as `sum`.

    If `sample_weight` is `None`, weights default to 1.  Use `sample_weight` of
    0 to mask values.

    Args:
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.

    Standalone usage:

    >>> m = tf.keras.metrics.Sum()
    >>> m.update_state([1, 3, 5, 7])
    >>> m.result().numpy()
    16.0

    Usage with `compile()` API:

    ```python
    model.add_metric(tf.keras.metrics.Sum(name='sum_1')(outputs))
    model.compile(optimizer='sgd', loss='mse')
    ```
    """
    def __init__(self, name: str = 'sum', dtype: Incomplete | None = None) -> None: ...

class Mean(Reduce):
    """Computes the (weighted) mean of the given values.

    For example, if values is [1, 3, 5, 7] then the mean is 4.
    If the weights were specified as [1, 1, 0, 0] then the mean would be 2.

    This metric creates two variables, `total` and `count` that are used to
    compute the average of `values`. This average is ultimately returned as
    `mean` which is an idempotent operation that simply divides `total` by
    `count`.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    Args:
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.

    Standalone usage:

    >>> m = tf.keras.metrics.Mean()
    >>> m.update_state([1, 3, 5, 7])
    >>> m.result().numpy()
    4.0
    >>> m.reset_state()
    >>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0])
    >>> m.result().numpy()
    2.0

    Usage with `compile()` API:

    ```python
    model.add_metric(tf.keras.metrics.Mean(name='mean_1')(outputs))
    model.compile(optimizer='sgd', loss='mse')
    ```
    """
    def __init__(self, name: str = 'mean', dtype: Incomplete | None = None) -> None: ...

class MeanMetricWrapper(Mean):
    """Wraps a stateless metric function with the Mean metric.

    You could use this class to quickly build a mean metric from a function. The
    function needs to have the signature `fn(y_true, y_pred)` and return a
    per-sample loss array. `MeanMetricWrapper.result()` will return
    the average metric value across all samples seen so far.

    For example:

    ```python
    def accuracy(y_true, y_pred):
      return tf.cast(tf.math.equal(y_true, y_pred), tf.float32)

    accuracy_metric = tf.keras.metrics.MeanMetricWrapper(fn=accuracy)

    keras_model.compile(..., metrics=accuracy_metric)
    ```

    Args:
      fn: The metric function to wrap, with signature `fn(y_true, y_pred,
        **kwargs)`.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      **kwargs: Keyword arguments to pass on to `fn`.
    """
    def __init__(self, fn, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates metric statistics.

        `y_true` and `y_pred` should have the same shape.

        Args:
          y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
          y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
          sample_weight: Optional `sample_weight` acts as a
            coefficient for the metric. If a scalar is provided, then the metric
            is simply scaled by the given value. If `sample_weight` is a tensor
            of size `[batch_size]`, then the metric for each sample of the batch
            is rescaled by the corresponding element in the `sample_weight`
            vector. If the shape of `sample_weight` is `[batch_size, d0, ..
            dN-1]` (or can be broadcasted to this shape), then each metric
            element of `y_pred` is scaled by the corresponding value of
            `sample_weight`. (Note on `dN-1`: all metric functions reduce by 1
            dimension, usually the last axis (-1)).

        Returns:
          Update op.
        """
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class MeanTensor(Metric):
    """Computes the element-wise (weighted) mean of the given tensors.

    `MeanTensor` returns a tensor with the same shape of the input tensors. The
    mean value is updated by keeping local variables `total` and `count`. The
    `total` tracks the sum of the weighted values, and `count` stores the sum of
    the weighted counts.

    Args:
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      shape: (Optional) A list of integers, a tuple of integers, or a 1-D Tensor
        of type int32. If not specified, the shape is inferred from the values
        at the first call of update_state.

    Standalone usage:

    >>> m = tf.keras.metrics.MeanTensor()
    >>> m.update_state([0, 1, 2, 3])
    >>> m.update_state([4, 5, 6, 7])
    >>> m.result().numpy()
    array([2., 3., 4., 5.], dtype=float32)

    >>> m.update_state([12, 10, 8, 6], sample_weight= [0, 0.2, 0.5, 1])
    >>> m.result().numpy()
    array([2.       , 3.6363635, 4.8      , 5.3333335], dtype=float32)

    >>> m = tf.keras.metrics.MeanTensor(dtype=tf.float64, shape=(1, 4))
    >>> m.result().numpy()
    array([[0., 0., 0., 0.]])
    >>> m.update_state([[0, 1, 2, 3]])
    >>> m.update_state([[4, 5, 6, 7]])
    >>> m.result().numpy()
    array([[2., 3., 4., 5.]])
    """
    def __init__(self, name: str = 'mean_tensor', dtype: Incomplete | None = None, shape: Incomplete | None = None) -> None: ...
    @property
    def total(self): ...
    @property
    def count(self): ...
    def update_state(self, values, sample_weight: Incomplete | None = None):
        """Accumulates statistics for computing the element-wise mean.

        Args:
          values: Per-example value.
          sample_weight: Optional weighting of each example. Defaults to 1.

        Returns:
          Update op.
        """
    def result(self): ...
    def reset_state(self) -> None: ...

class SumOverBatchSize(Reduce):
    """Computes the weighted sum over batch size of the given values.

    For example, if values is [1, 3, 5, 7] then the metric value is 4.
    If the weights were specified as [1, 1, 0, 0] then the value would be 1.

    This metric creates two variables, `total` and `count` that are used to
    compute the average of `values`. This average is ultimately returned as sum
    over batch size which is an idempotent operation that simply divides `total`
    by `count`.

    If `sample_weight` is `None`, weights default to 1.  Use `sample_weight` of
    0 to mask values.
    """
    def __init__(self, name: str = 'sum_over_batch_size', dtype: Incomplete | None = None) -> None: ...

class SumOverBatchSizeMetricWrapper(SumOverBatchSize):
    """Wraps a function with the `SumOverBatchSizeMetricWrapper` metric."""
    def __init__(self, fn, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None:
        """Creates a `SumOverBatchSizeMetricWrapper` instance.

        Args:
          fn: The metric function to wrap, with signature `fn(y_true, y_pred,
            **kwargs)`.
          name: (Optional) string name of the metric instance.
          dtype: (Optional) data type of the metric result.
          **kwargs: The keyword arguments that are passed on to `fn`.
        """
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None): ...
    def get_config(self): ...

def clone_metric(metric):
    """Returns a clone of the metric if stateful, otherwise returns it as is."""
def clone_metrics(metrics):
    """Clones the given metric list/dict."""
def is_built_in(cls): ...
