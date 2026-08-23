from _typeshed import Incomplete
from tensorflow.python.autograph.lang import directives as directives
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import collective_all_reduce_strategy as collective_all_reduce_strategy
from tensorflow.python.distribute.coordinator import cluster_coordinator as cluster_coordinator
from tensorflow.python.eager import backprop as backprop, context as context, def_function as def_function
from tensorflow.python.framework import composite_tensor as composite_tensor, errors as errors, errors_impl as errors_impl, func_graph as func_graph, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.keras import backend as backend, optimizer_v1 as optimizer_v1, optimizers as optimizers
from tensorflow.python.keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils, compile_utils as compile_utils, data_adapter as data_adapter, training_utils as training_utils
from tensorflow.python.keras.mixed_precision import policy as policy
from tensorflow.python.keras.saving import hdf5_format as hdf5_format, save as save, saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import json_utils as json_utils, model_serialization as model_serialization
from tensorflow.python.keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, tf_utils as tf_utils, version_utils as version_utils
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite, path_to_string as path_to_string
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, sparse_ops as sparse_ops, summary_ops_v2 as summary_ops_v2, variables as variables
from tensorflow.python.profiler import trace as trace
from tensorflow.python.training import py_checkpoint_reader as py_checkpoint_reader
from tensorflow.python.util import nest as nest, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import keras_export as keras_export
from tensorflow.tools.docs import doc_controls as doc_controls

def disable_multi_worker(method):
    """Decorator that disallows multi-worker use of `method`."""
def inject_functional_model_class(cls):
    """Inject `Functional` into the hierarchy of this class if needed."""
def is_functional_model_init_params(args, kwargs): ...

class Model(base_layer.Layer, version_utils.ModelVersionSelector):
    '''`Model` groups layers into an object with training and inference features.

  Args:
      inputs: The input(s) of the model: a `keras.Input` object or list of
          `keras.Input` objects.
      outputs: The output(s) of the model. See Functional API example below.
      name: String, the name of the model.

  There are two ways to instantiate a `Model`:

  1 - With the "Functional API", where you start from `Input`,
  you chain layer calls to specify the model\'s forward pass,
  and finally you create your model from inputs and outputs:

  ```python
  import tensorflow as tf

  inputs = tf.keras.Input(shape=(3,))
  x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)
  outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)
  model = tf.keras.Model(inputs=inputs, outputs=outputs)
  ```

  Note: Only dicts, lists, and tuples of input tensors are supported. Nested
  inputs are not supported (e.g. lists of list or dicts of dict).

  2 - By subclassing the `Model` class: in that case, you should define your
  layers in `__init__` and you should implement the model\'s forward pass
  in `call`.

  ```python
  import tensorflow as tf

  class MyModel(tf.keras.Model):

    def __init__(self):
      super(MyModel, self).__init__()
      self.dense1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
      self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.softmax)

    def call(self, inputs):
      x = self.dense1(inputs)
      return self.dense2(x)

  model = MyModel()
  ```

  If you subclass `Model`, you can optionally have
  a `training` argument (boolean) in `call`, which you can use to specify
  a different behavior in training and inference:

  ```python
  import tensorflow as tf

  class MyModel(tf.keras.Model):

    def __init__(self):
      super(MyModel, self).__init__()
      self.dense1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
      self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.softmax)
      self.dropout = tf.keras.layers.Dropout(0.5)

    def call(self, inputs, training=False):
      x = self.dense1(inputs)
      if training:
        x = self.dropout(x, training=training)
      return self.dense2(x)

  model = MyModel()
  ```

  Once the model is created, you can config the model with losses and metrics
  with `model.compile()`, train the model with `model.fit()`, or use the model
  to do prediction with `model.predict()`.
  '''
    def __new__(cls, *args, **kwargs): ...
    inputs: Incomplete
    outputs: Incomplete
    input_names: Incomplete
    output_names: Incomplete
    stop_training: bool
    history: Incomplete
    compiled_loss: Incomplete
    compiled_metrics: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def build(self, input_shape) -> None:
        """Builds the model based on input shapes received.

    This is to be used for subclassed models, which do not know at instantiation
    time what their inputs look like.

    This method only exists for users who want to call `model.build()` in a
    standalone way (as a substitute for calling the model on real data to
    build it). It will never be called by the framework (and thus it will
    never throw unexpected errors in an unrelated workflow).

    Args:
     input_shape: Single tuple, TensorShape, or list/dict of shapes, where
         shapes are tuples, integers, or TensorShapes.

    Raises:
      ValueError:
        1. In case of invalid user-provided data (not of type tuple,
           list, TensorShape, or dict).
        2. If the model requires call arguments that are agnostic
           to the input shapes (positional or kwarg in call signature).
        3. If not all layers were properly built.
        4. If float type inputs are not supported within the layers.

      In each of these cases, the user should build their model by calling it
      on real tensor data.
    """
    def call(self, inputs, training: Incomplete | None = None, mask: Incomplete | None = None) -> None:
        """Calls the model on new inputs.

    In this case `call` just reapplies
    all ops in the graph to the new inputs
    (e.g. build a new computational graph from the provided inputs).

    Note: This method should not be called directly. It is only meant to be
    overridden when subclassing `tf.keras.Model`.
    To call a model on an input, always use the `__call__` method,
    i.e. `model(inputs)`, which relies on the underlying `call` method.

    Args:
        inputs: Input tensor, or dict/list/tuple of input tensors.
        training: Boolean or boolean scalar tensor, indicating whether to run
          the `Network` in training mode or inference mode.
        mask: A mask or list of masks. A mask can be
            either a tensor or None (no mask).

    Returns:
        A tensor if there is a single output, or
        a list of tensors if there are more than one outputs.
    """
    optimizer: Incomplete
    loss: Incomplete
    def compile(self, optimizer: str = 'rmsprop', loss: Incomplete | None = None, metrics: Incomplete | None = None, loss_weights: Incomplete | None = None, weighted_metrics: Incomplete | None = None, run_eagerly: Incomplete | None = None, steps_per_execution: Incomplete | None = None, **kwargs) -> None:
        """Configures the model for training.

    Args:
        optimizer: String (name of optimizer) or optimizer instance. See
          `tf.keras.optimizers`.
        loss: String (name of objective function), objective function or
          `tf.keras.losses.Loss` instance. See `tf.keras.losses`. An objective
          function is any callable with the signature `loss = fn(y_true,
          y_pred)`, where y_true = ground truth values with shape =
          `[batch_size, d0, .. dN]`, except sparse loss functions such as sparse
          categorical crossentropy where shape = `[batch_size, d0, .. dN-1]`.
          y_pred = predicted values with shape = `[batch_size, d0, .. dN]`. It
          returns a weighted loss float tensor. If a custom `Loss` instance is
          used and reduction is set to `None`, return value has the shape
          `[batch_size, d0, .. dN-1]` i.e. per-sample or per-timestep loss
          values; otherwise, it is a scalar. If the model has multiple outputs,
          you can use a different loss on each output by passing a dictionary
          or a list of losses. The loss value that will be minimized by the
          model will then be the sum of all individual losses, unless
          `loss_weights` is specified.
        metrics: List of metrics to be evaluated by the model during training
          and testing. Each of this can be a string (name of a built-in
          function), function or a `tf.keras.metrics.Metric` instance. See
          `tf.keras.metrics`. Typically you will use `metrics=['accuracy']`. A
          function is any callable with the signature `result = fn(y_true,
          y_pred)`. To specify different metrics for different outputs of a
          multi-output model, you could also pass a dictionary, such as
          `metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}`.
          You can also pass a list to specify a metric or a list of metrics
          for each output, such as `metrics=[['accuracy'], ['accuracy', 'mse']]`
          or `metrics=['accuracy', ['accuracy', 'mse']]`. When you pass the
          strings 'accuracy' or 'acc', we convert this to one of
          `tf.keras.metrics.BinaryAccuracy`,
          `tf.keras.metrics.CategoricalAccuracy`,
          `tf.keras.metrics.SparseCategoricalAccuracy` based on the loss
          function used and the model output shape. We do a similar
          conversion for the strings 'crossentropy' and 'ce' as well.
        loss_weights: Optional list or dictionary specifying scalar coefficients
          (Python floats) to weight the loss contributions of different model
          outputs. The loss value that will be minimized by the model will then
          be the *weighted sum* of all individual losses, weighted by the
          `loss_weights` coefficients.
            If a list, it is expected to have a 1:1 mapping to the model's
              outputs. If a dict, it is expected to map output names (strings)
              to scalar coefficients.
        weighted_metrics: List of metrics to be evaluated and weighted by
          `sample_weight` or `class_weight` during training and testing.
        run_eagerly: Bool. Defaults to `False`. If `True`, this `Model`'s
          logic will not be wrapped in a `tf.function`. Recommended to leave
          this as `None` unless your `Model` cannot be run inside a
          `tf.function`. `run_eagerly=True` is not supported when using
          `tf.distribute.experimental.ParameterServerStrategy`.
        steps_per_execution: Int. Defaults to 1. The number of batches to
          run during each `tf.function` call. Running multiple batches
          inside a single `tf.function` call can greatly improve performance
          on TPUs or small models with a large Python overhead.
          At most, one full epoch will be run each
          execution. If a number larger than the size of the epoch is passed,
          the execution will be truncated to the size of the epoch.
          Note that if `steps_per_execution` is set to `N`,
          `Callback.on_batch_begin` and `Callback.on_batch_end` methods
          will only be called every `N` batches
          (i.e. before/after each `tf.function` execution).
        **kwargs: Arguments supported for backwards compatibility only.

    Raises:
        ValueError: In case of invalid arguments for
            `optimizer`, `loss` or `metrics`.
    """
    @property
    def metrics(self):
        '''Returns the model\'s metrics added using `compile`, `add_metric` APIs.

    Note: Metrics passed to `compile()` are available only after a `keras.Model`
    has been trained/evaluated on actual data.

    Examples:

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> outputs = tf.keras.layers.Dense(2)(inputs)
    >>> model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
    >>> [m.name for m in model.metrics]
    []

    >>> x = np.random.random((2, 3))
    >>> y = np.random.randint(0, 2, (2, 2))
    >>> model.fit(x, y)
    >>> [m.name for m in model.metrics]
    [\'loss\', \'mae\']

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> d = tf.keras.layers.Dense(2, name=\'out\')
    >>> output_1 = d(inputs)
    >>> output_2 = d(inputs)
    >>> model = tf.keras.models.Model(
    ...    inputs=inputs, outputs=[output_1, output_2])
    >>> model.add_metric(
    ...    tf.reduce_sum(output_2), name=\'mean\', aggregation=\'mean\')
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae", "acc"])
    >>> model.fit(x, (y, y))
    >>> [m.name for m in model.metrics]
    [\'loss\', \'out_loss\', \'out_1_loss\', \'out_mae\', \'out_acc\', \'out_1_mae\',
    \'out_1_acc\', \'mean\']

    '''
    @property
    def metrics_names(self):
        '''Returns the model\'s display labels for all outputs.

    Note: `metrics_names` are available only after a `keras.Model` has been
    trained/evaluated on actual data.

    Examples:

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> outputs = tf.keras.layers.Dense(2)(inputs)
    >>> model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
    >>> model.metrics_names
    []

    >>> x = np.random.random((2, 3))
    >>> y = np.random.randint(0, 2, (2, 2))
    >>> model.fit(x, y)
    >>> model.metrics_names
    [\'loss\', \'mae\']

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> d = tf.keras.layers.Dense(2, name=\'out\')
    >>> output_1 = d(inputs)
    >>> output_2 = d(inputs)
    >>> model = tf.keras.models.Model(
    ...    inputs=inputs, outputs=[output_1, output_2])
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae", "acc"])
    >>> model.fit(x, (y, y))
    >>> model.metrics_names
    [\'loss\', \'out_loss\', \'out_1_loss\', \'out_mae\', \'out_acc\', \'out_1_mae\',
    \'out_1_acc\']

    '''
    @property
    def distribute_strategy(self):
        """The `tf.distribute.Strategy` this model was created under."""
    @property
    def run_eagerly(self):
        """Settable attribute indicating whether the model should run eagerly.

    Running eagerly means that your model will be run step by step,
    like Python code. Your model might run slower, but it should become easier
    for you to debug it by stepping into individual layer calls.

    By default, we will attempt to compile your model to a static graph to
    deliver the best execution performance.

    Returns:
      Boolean, whether the model should run eagerly.
    """
    @run_eagerly.setter
    def run_eagerly(self, value) -> None: ...
    def train_step(self, data):
        """The logic for one training step.

    This method can be overridden to support custom training logic.
    For concrete examples of how to override this method see
    [Customizing what happends in fit](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit).
    This method is called by `Model.make_train_function`.

    This method should contain the mathematical logic for one step of training.
    This typically includes the forward pass, loss calculation, backpropagation,
    and metric updates.

    Configuration details for *how* this logic is run (e.g. `tf.function` and
    `tf.distribute.Strategy` settings), should be left to
    `Model.make_train_function`, which can also be overridden.

    Args:
      data: A nested structure of `Tensor`s.

    Returns:
      A `dict` containing values that will be passed to
      `tf.keras.callbacks.CallbackList.on_train_batch_end`. Typically, the
      values of the `Model`'s metrics are returned. Example:
      `{'loss': 0.2, 'accuracy': 0.7}`.

    """
    train_tf_function: Incomplete
    train_function: Incomplete
    def make_train_function(self):
        """Creates a function that executes one step of training.

    This method can be overridden to support custom training logic.
    This method is called by `Model.fit` and `Model.train_on_batch`.

    Typically, this method directly controls `tf.function` and
    `tf.distribute.Strategy` settings, and delegates the actual training
    logic to `Model.train_step`.

    This function is cached the first time `Model.fit` or
    `Model.train_on_batch` is called. The cache is cleared whenever
    `Model.compile` is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, and return a `dict` containing values that will
      be passed to `tf.keras.Callbacks.on_train_batch_end`, such as
      `{'loss': 0.2, 'accuracy': 0.7}`.
    """
    def fit(self, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: str = 'auto', callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_batch_size: Incomplete | None = None, validation_freq: int = 1, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False):
        '''Trains the model for a fixed number of epochs (iterations on a dataset).

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A dict mapping input names to the corresponding array/tensors,
            if the model has named inputs.
          - A `tf.data` dataset. Should return a tuple
            of either `(inputs, targets)` or
            `(inputs, targets, sample_weights)`.
          - A generator or `keras.utils.Sequence` returning `(inputs, targets)`
            or `(inputs, targets, sample_weights)`.
          - A `tf.keras.utils.experimental.DatasetCreator`, which wraps a
            callable that takes a single argument of type
            `tf.distribute.InputContext`, and returns a `tf.data.Dataset`.
            `DatasetCreator` should be used when users prefer to specify the
            per-replica batching and sharding logic for the `Dataset`.
            See `tf.keras.utils.experimental.DatasetCreator` doc for more
            information.
          A more detailed description of unpacking behavior for iterator types
          (Dataset, generator, Sequence) is given below. If using
          `tf.distribute.experimental.ParameterServerStrategy`, only
          `DatasetCreator` type is supported for `x`.
        y: Target data. Like the input data `x`,
          it could be either Numpy array(s) or TensorFlow tensor(s).
          It should be consistent with `x` (you cannot have Numpy inputs and
          tensor targets, or inversely). If `x` is a dataset, generator,
          or `keras.utils.Sequence` instance, `y` should
          not be specified (since targets will be obtained from `x`).
        batch_size: Integer or `None`.
            Number of samples per gradient update.
            If unspecified, `batch_size` will default to 32.
            Do not specify the `batch_size` if your data is in the
            form of datasets, generators, or `keras.utils.Sequence` instances
            (since they generate batches).
        epochs: Integer. Number of epochs to train the model.
            An epoch is an iteration over the entire `x` and `y`
            data provided.
            Note that in conjunction with `initial_epoch`,
            `epochs` is to be understood as "final epoch".
            The model is not trained for a number of iterations
            given by `epochs`, but merely until the epoch
            of index `epochs` is reached.
        verbose: \'auto\', 0, 1, or 2. Verbosity mode.
            0 = silent, 1 = progress bar, 2 = one line per epoch.
            \'auto\' defaults to 1 for most cases, but 2 when used with
            `ParameterServerStrategy`. Note that the progress bar is not
            particularly useful when logged to a file, so verbose=2 is
            recommended when not running interactively (eg, in a production
            environment).
        callbacks: List of `keras.callbacks.Callback` instances.
            List of callbacks to apply during training.
            See `tf.keras.callbacks`. Note `tf.keras.callbacks.ProgbarLogger`
            and `tf.keras.callbacks.History` callbacks are created automatically
            and need not be passed into `model.fit`.
            `tf.keras.callbacks.ProgbarLogger` is created or not based on
            `verbose` argument to `model.fit`.
            Callbacks with batch-level calls are currently unsupported with
            `tf.distribute.experimental.ParameterServerStrategy`, and users are
            advised to implement epoch-level calls instead with an appropriate
            `steps_per_epoch` value.
        validation_split: Float between 0 and 1.
            Fraction of the training data to be used as validation data.
            The model will set apart this fraction of the training data,
            will not train on it, and will evaluate
            the loss and any model metrics
            on this data at the end of each epoch.
            The validation data is selected from the last samples
            in the `x` and `y` data provided, before shuffling. This argument is
            not supported when `x` is a dataset, generator or
           `keras.utils.Sequence` instance.
            `validation_split` is not yet supported with
            `tf.distribute.experimental.ParameterServerStrategy`.
        validation_data: Data on which to evaluate
            the loss and any model metrics at the end of each epoch.
            The model will not be trained on this data. Thus, note the fact
            that the validation loss of data provided using `validation_split`
            or `validation_data` is not affected by regularization layers like
            noise and dropout.
            `validation_data` will override `validation_split`.
            `validation_data` could be:
              - A tuple `(x_val, y_val)` of Numpy arrays or tensors.
              - A tuple `(x_val, y_val, val_sample_weights)` of NumPy arrays.
              - A `tf.data.Dataset`.
              - A Python generator or `keras.utils.Sequence` returning
              `(inputs, targets)` or `(inputs, targets, sample_weights)`.
            `validation_data` is not yet supported with
            `tf.distribute.experimental.ParameterServerStrategy`.
        shuffle: Boolean (whether to shuffle the training data
            before each epoch) or str (for \'batch\'). This argument is ignored
            when `x` is a generator or an object of tf.data.Dataset.
            \'batch\' is a special option for dealing
            with the limitations of HDF5 data; it shuffles in batch-sized
            chunks. Has no effect when `steps_per_epoch` is not `None`.
        class_weight: Optional dictionary mapping class indices (integers)
            to a weight (float) value, used for weighting the loss function
            (during training only).
            This can be useful to tell the model to
            "pay more attention" to samples from
            an under-represented class.
        sample_weight: Optional Numpy array of weights for
            the training samples, used for weighting the loss function
            (during training only). You can either pass a flat (1D)
            Numpy array with the same length as the input samples
            (1:1 mapping between weights and samples),
            or in the case of temporal data,
            you can pass a 2D array with shape
            `(samples, sequence_length)`,
            to apply a different weight to every timestep of every sample. This
            argument is not supported when `x` is a dataset, generator, or
           `keras.utils.Sequence` instance, instead provide the sample_weights
            as the third element of `x`.
        initial_epoch: Integer.
            Epoch at which to start training
            (useful for resuming a previous training run).
        steps_per_epoch: Integer or `None`.
            Total number of steps (batches of samples)
            before declaring one epoch finished and starting the
            next epoch. When training with input tensors such as
            TensorFlow data tensors, the default `None` is equal to
            the number of samples in your dataset divided by
            the batch size, or 1 if that cannot be determined. If x is a
            `tf.data` dataset, and \'steps_per_epoch\'
            is None, the epoch will run until the input dataset is exhausted.
            When passing an infinitely repeating dataset, you must specify the
            `steps_per_epoch` argument. If `steps_per_epoch=-1` the training
            will run indefinitely with an infinitely repeating dataset.
            This argument is not supported with array inputs.
            When using `tf.distribute.experimental.ParameterServerStrategy`:
              * `steps_per_epoch=None` is not supported.
        validation_steps: Only relevant if `validation_data` is provided and
            is a `tf.data` dataset. Total number of steps (batches of
            samples) to draw before stopping when performing validation
            at the end of every epoch. If \'validation_steps\' is None, validation
            will run until the `validation_data` dataset is exhausted. In the
            case of an infinitely repeated dataset, it will run into an
            infinite loop. If \'validation_steps\' is specified and only part of
            the dataset will be consumed, the evaluation will start from the
            beginning of the dataset at each epoch. This ensures that the same
            validation samples are used every time.
        validation_batch_size: Integer or `None`.
            Number of samples per validation batch.
            If unspecified, will default to `batch_size`.
            Do not specify the `validation_batch_size` if your data is in the
            form of datasets, generators, or `keras.utils.Sequence` instances
            (since they generate batches).
        validation_freq: Only relevant if validation data is provided. Integer
            or `collections.abc.Container` instance (e.g. list, tuple, etc.).
            If an integer, specifies how many training epochs to run before a
            new validation run is performed, e.g. `validation_freq=2` runs
            validation every 2 epochs. If a Container, specifies the epochs on
            which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
            validation at the end of the 1st, 2nd, and 10th epochs.
        max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
            input only. Maximum size for the generator queue.
            If unspecified, `max_queue_size` will default to 10.
        workers: Integer. Used for generator or `keras.utils.Sequence` input
            only. Maximum number of processes to spin up
            when using process-based threading. If unspecified, `workers`
            will default to 1.
        use_multiprocessing: Boolean. Used for generator or
            `keras.utils.Sequence` input only. If `True`, use process-based
            threading. If unspecified, `use_multiprocessing` will default to
            `False`. Note that because this implementation relies on
            multiprocessing, you should not pass non-picklable arguments to
            the generator as they can\'t be passed easily to children processes.

    Unpacking behavior for iterator-like inputs:
        A common pattern is to pass a tf.data.Dataset, generator, or
      tf.keras.utils.Sequence to the `x` argument of fit, which will in fact
      yield not only features (x) but optionally targets (y) and sample weights.
      Keras requires that the output of such iterator-likes be unambiguous. The
      iterator should return a tuple of length 1, 2, or 3, where the optional
      second and third elements will be used for y and sample_weight
      respectively. Any other type provided will be wrapped in a length one
      tuple, effectively treating everything as \'x\'. When yielding dicts, they
      should still adhere to the top-level tuple structure.
      e.g. `({"x0": x0, "x1": x1}, y)`. Keras will not attempt to separate
      features, targets, and weights from the keys of a single dict.
        A notable unsupported data type is the namedtuple. The reason is that
      it behaves like both an ordered datatype (tuple) and a mapping
      datatype (dict). So given a namedtuple of the form:
          `namedtuple("example_tuple", ["y", "x"])`
      it is ambiguous whether to reverse the order of the elements when
      interpreting the value. Even worse is a tuple of the form:
          `namedtuple("other_tuple", ["x", "y", "z"])`
      where it is unclear if the tuple was intended to be unpacked into x, y,
      and sample_weight or passed through as a single element to `x`. As a
      result the data processing code will simply raise a ValueError if it
      encounters a namedtuple. (Along with instructions to remedy the issue.)

    Returns:
        A `History` object. Its `History.history` attribute is
        a record of training loss values and metrics values
        at successive epochs, as well as validation loss values
        and validation metrics values (if applicable).

    Raises:
        RuntimeError: 1. If the model was never compiled or,
        2. If `model.fit` is  wrapped in `tf.function`.

        ValueError: In case of mismatch between the provided input data
            and what the model expects or when the input data is empty.
    '''
    def test_step(self, data):
        """The logic for one evaluation step.

    This method can be overridden to support custom evaluation logic.
    This method is called by `Model.make_test_function`.

    This function should contain the mathematical logic for one step of
    evaluation.
    This typically includes the forward pass, loss calculation, and metrics
    updates.

    Configuration details for *how* this logic is run (e.g. `tf.function` and
    `tf.distribute.Strategy` settings), should be left to
    `Model.make_test_function`, which can also be overridden.

    Args:
      data: A nested structure of `Tensor`s.

    Returns:
      A `dict` containing values that will be passed to
      `tf.keras.callbacks.CallbackList.on_train_batch_end`. Typically, the
      values of the `Model`'s metrics are returned.
    """
    test_function: Incomplete
    def make_test_function(self):
        """Creates a function that executes one step of evaluation.

    This method can be overridden to support custom evaluation logic.
    This method is called by `Model.evaluate` and `Model.test_on_batch`.

    Typically, this method directly controls `tf.function` and
    `tf.distribute.Strategy` settings, and delegates the actual evaluation
    logic to `Model.test_step`.

    This function is cached the first time `Model.evaluate` or
    `Model.test_on_batch` is called. The cache is cleared whenever
    `Model.compile` is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, and return a `dict` containing values that will
      be passed to `tf.keras.Callbacks.on_test_batch_end`.
    """
    def evaluate(self, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, return_dict: bool = False, **kwargs):
        """Returns the loss value & metrics values for the model in test mode.

    Computation is done in batches (see the `batch_size` arg.)

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A dict mapping input names to the corresponding array/tensors,
            if the model has named inputs.
          - A `tf.data` dataset. Should return a tuple
            of either `(inputs, targets)` or
            `(inputs, targets, sample_weights)`.
          - A generator or `keras.utils.Sequence` returning `(inputs, targets)`
            or `(inputs, targets, sample_weights)`.
          A more detailed description of unpacking behavior for iterator types
          (Dataset, generator, Sequence) is given in the `Unpacking behavior
          for iterator-like inputs` section of `Model.fit`.
        y: Target data. Like the input data `x`, it could be either Numpy
          array(s) or TensorFlow tensor(s). It should be consistent with `x`
          (you cannot have Numpy inputs and tensor targets, or inversely). If
          `x` is a dataset, generator or `keras.utils.Sequence` instance, `y`
          should not be specified (since targets will be obtained from the
          iterator/dataset).
        batch_size: Integer or `None`. Number of samples per batch of
          computation. If unspecified, `batch_size` will default to 32. Do not
          specify the `batch_size` if your data is in the form of a dataset,
          generators, or `keras.utils.Sequence` instances (since they generate
          batches).
        verbose: 0 or 1. Verbosity mode. 0 = silent, 1 = progress bar.
        sample_weight: Optional Numpy array of weights for the test samples,
          used for weighting the loss function. You can either pass a flat (1D)
          Numpy array with the same length as the input samples
            (1:1 mapping between weights and samples), or in the case of
              temporal data, you can pass a 2D array with shape `(samples,
              sequence_length)`, to apply a different weight to every timestep
              of every sample. This argument is not supported when `x` is a
              dataset, instead pass sample weights as the third element of `x`.
        steps: Integer or `None`. Total number of steps (batches of samples)
          before declaring the evaluation round finished. Ignored with the
          default value of `None`. If x is a `tf.data` dataset and `steps` is
          None, 'evaluate' will run until the dataset is exhausted. This
          argument is not supported with array inputs.
        callbacks: List of `keras.callbacks.Callback` instances. List of
          callbacks to apply during evaluation. See
          [callbacks](/api_docs/python/tf/keras/callbacks).
        max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
          input only. Maximum size for the generator queue. If unspecified,
          `max_queue_size` will default to 10.
        workers: Integer. Used for generator or `keras.utils.Sequence` input
          only. Maximum number of processes to spin up when using process-based
          threading. If unspecified, `workers` will default to 1.
        use_multiprocessing: Boolean. Used for generator or
          `keras.utils.Sequence` input only. If `True`, use process-based
          threading. If unspecified, `use_multiprocessing` will default to
          `False`. Note that because this implementation relies on
          multiprocessing, you should not pass non-picklable arguments to the
          generator as they can't be passed easily to children processes.
        return_dict: If `True`, loss and metric results are returned as a dict,
          with each key being the name of the metric. If `False`, they are
          returned as a list.
        **kwargs: Unused at this time.

    See the discussion of `Unpacking behavior for iterator-like inputs` for
    `Model.fit`.

    `Model.evaluate` is not yet supported with
    `tf.distribute.experimental.ParameterServerStrategy`.

    Returns:
        Scalar test loss (if the model has a single output and no metrics)
        or list of scalars (if the model has multiple outputs
        and/or metrics). The attribute `model.metrics_names` will give you
        the display labels for the scalar outputs.

    Raises:
        RuntimeError: If `model.evaluate` is wrapped in `tf.function`.
        ValueError: in case of invalid arguments.
    """
    def predict_step(self, data):
        """The logic for one inference step.

    This method can be overridden to support custom inference logic.
    This method is called by `Model.make_predict_function`.

    This method should contain the mathematical logic for one step of inference.
    This typically includes the forward pass.

    Configuration details for *how* this logic is run (e.g. `tf.function` and
    `tf.distribute.Strategy` settings), should be left to
    `Model.make_predict_function`, which can also be overridden.

    Args:
      data: A nested structure of `Tensor`s.

    Returns:
      The result of one inference step, typically the output of calling the
      `Model` on data.
    """
    predict_function: Incomplete
    def make_predict_function(self):
        """Creates a function that executes one step of inference.

    This method can be overridden to support custom inference logic.
    This method is called by `Model.predict` and `Model.predict_on_batch`.

    Typically, this method directly controls `tf.function` and
    `tf.distribute.Strategy` settings, and delegates the actual evaluation
    logic to `Model.predict_step`.

    This function is cached the first time `Model.predict` or
    `Model.predict_on_batch` is called. The cache is cleared whenever
    `Model.compile` is called.

    Returns:
      Function. The function created by this method should accept a
      `tf.data.Iterator`, and return the outputs of the `Model`.
    """
    def predict(self, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False):
        """Generates output predictions for the input samples.

    Computation is done in batches. This method is designed for performance in
    large scale inputs. For small amount of inputs that fit in one batch,
    directly using `__call__` is recommended for faster execution, e.g.,
    `model(x)`, or `model(x, training=False)` if you have layers such as
    `tf.keras.layers.BatchNormalization` that behaves differently during
    inference. Also, note the fact that test loss is not affected by
    regularization layers like noise and dropout.

    Args:
        x: Input samples. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A `tf.data` dataset.
          - A generator or `keras.utils.Sequence` instance.
          A more detailed description of unpacking behavior for iterator types
          (Dataset, generator, Sequence) is given in the `Unpacking behavior
          for iterator-like inputs` section of `Model.fit`.
        batch_size: Integer or `None`.
            Number of samples per batch.
            If unspecified, `batch_size` will default to 32.
            Do not specify the `batch_size` if your data is in the
            form of dataset, generators, or `keras.utils.Sequence` instances
            (since they generate batches).
        verbose: Verbosity mode, 0 or 1.
        steps: Total number of steps (batches of samples)
            before declaring the prediction round finished.
            Ignored with the default value of `None`. If x is a `tf.data`
            dataset and `steps` is None, `predict` will
            run until the input dataset is exhausted.
        callbacks: List of `keras.callbacks.Callback` instances.
            List of callbacks to apply during prediction.
            See [callbacks](/api_docs/python/tf/keras/callbacks).
        max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
            input only. Maximum size for the generator queue.
            If unspecified, `max_queue_size` will default to 10.
        workers: Integer. Used for generator or `keras.utils.Sequence` input
            only. Maximum number of processes to spin up when using
            process-based threading. If unspecified, `workers` will default
            to 1.
        use_multiprocessing: Boolean. Used for generator or
            `keras.utils.Sequence` input only. If `True`, use process-based
            threading. If unspecified, `use_multiprocessing` will default to
            `False`. Note that because this implementation relies on
            multiprocessing, you should not pass non-picklable arguments to
            the generator as they can't be passed easily to children processes.

    See the discussion of `Unpacking behavior for iterator-like inputs` for
    `Model.fit`. Note that Model.predict uses the same interpretation rules as
    `Model.fit` and `Model.evaluate`, so inputs must be unambiguous for all
    three methods.

    Returns:
        Numpy array(s) of predictions.

    Raises:
        RuntimeError: If `model.predict` is wrapped in `tf.function`.
        ValueError: In case of mismatch between the provided
            input data and the model's expectations,
            or in case a stateful model receives a number of samples
            that is not a multiple of the batch size.
    """
    def reset_metrics(self) -> None:
        '''Resets the state of all the metrics in the model.

    Examples:

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> outputs = tf.keras.layers.Dense(2)(inputs)
    >>> model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae"])

    >>> x = np.random.random((2, 3))
    >>> y = np.random.randint(0, 2, (2, 2))
    >>> _ = model.fit(x, y, verbose=0)
    >>> assert all(float(m.result()) for m in model.metrics)

    >>> model.reset_metrics()
    >>> assert all(float(m.result()) == 0 for m in model.metrics)

    '''
    def train_on_batch(self, x, y: Incomplete | None = None, sample_weight: Incomplete | None = None, class_weight: Incomplete | None = None, reset_metrics: bool = True, return_dict: bool = False):
        '''Runs a single gradient update on a single batch of data.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays
              (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
              (in case the model has multiple inputs).
          - A dict mapping input names to the corresponding array/tensors,
              if the model has named inputs.
        y: Target data. Like the input data `x`, it could be either Numpy
          array(s) or TensorFlow tensor(s). It should be consistent with `x`
          (you cannot have Numpy inputs and tensor targets, or inversely).
        sample_weight: Optional array of the same length as x, containing
          weights to apply to the model\'s loss for each sample. In the case of
          temporal data, you can pass a 2D array with shape (samples,
          sequence_length), to apply a different weight to every timestep of
          every sample.
        class_weight: Optional dictionary mapping class indices (integers) to a
          weight (float) to apply to the model\'s loss for the samples from this
          class during training. This can be useful to tell the model to "pay
          more attention" to samples from an under-represented class.
        reset_metrics: If `True`, the metrics returned will be only for this
          batch. If `False`, the metrics will be statefully accumulated across
          batches.
        return_dict: If `True`, loss and metric results are returned as a dict,
          with each key being the name of the metric. If `False`, they are
          returned as a list.

    Returns:
        Scalar training loss
        (if the model has a single output and no metrics)
        or list of scalars (if the model has multiple outputs
        and/or metrics). The attribute `model.metrics_names` will give you
        the display labels for the scalar outputs.

    Raises:
      RuntimeError: If `model.train_on_batch` is wrapped in `tf.function`.
      ValueError: In case of invalid user-provided arguments.
    '''
    def test_on_batch(self, x, y: Incomplete | None = None, sample_weight: Incomplete | None = None, reset_metrics: bool = True, return_dict: bool = False):
        """Test the model on a single batch of samples.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays (in case the
              model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors (in case the model has
              multiple inputs).
          - A dict mapping input names to the corresponding array/tensors, if
              the model has named inputs.
        y: Target data. Like the input data `x`, it could be either Numpy
          array(s) or TensorFlow tensor(s). It should be consistent with `x`
          (you cannot have Numpy inputs and tensor targets, or inversely).
        sample_weight: Optional array of the same length as x, containing
          weights to apply to the model's loss for each sample. In the case of
          temporal data, you can pass a 2D array with shape (samples,
          sequence_length), to apply a different weight to every timestep of
          every sample.
        reset_metrics: If `True`, the metrics returned will be only for this
          batch. If `False`, the metrics will be statefully accumulated across
          batches.
        return_dict: If `True`, loss and metric results are returned as a dict,
          with each key being the name of the metric. If `False`, they are
          returned as a list.

    Returns:
        Scalar test loss (if the model has a single output and no metrics)
        or list of scalars (if the model has multiple outputs
        and/or metrics). The attribute `model.metrics_names` will give you
        the display labels for the scalar outputs.

    Raises:
        RuntimeError: If `model.test_on_batch` is wrapped in `tf.function`.
        ValueError: In case of invalid user-provided arguments.
    """
    def predict_on_batch(self, x):
        """Returns predictions for a single batch of samples.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays (in case the
              model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors (in case the model has
              multiple inputs).

    Returns:
        Numpy array(s) of predictions.

    Raises:
        RuntimeError: If `model.predict_on_batch` is wrapped in `tf.function`.
        ValueError: In case of mismatch between given number of inputs and
          expectations of the model.
    """
    def fit_generator(self, generator, steps_per_epoch: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_data: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, class_weight: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, shuffle: bool = True, initial_epoch: int = 0):
        """Fits the model on data yielded batch-by-batch by a Python generator.

    DEPRECATED:
      `Model.fit` now supports generators, so there is no longer any need to use
      this endpoint.
    """
    def evaluate_generator(self, generator, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, verbose: int = 0):
        """Evaluates the model on a data generator.

    DEPRECATED:
      `Model.evaluate` now supports generators, so there is no longer any need
      to use this endpoint.
    """
    def predict_generator(self, generator, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, verbose: int = 0):
        """Generates predictions for the input samples from a data generator.

    DEPRECATED:
      `Model.predict` now supports generators, so there is no longer any need
      to use this endpoint.
    """
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    def get_weights(self):
        """Retrieves the weights of the model.

    Returns:
        A flat list of Numpy arrays.
    """
    def save(self, filepath, overwrite: bool = True, include_optimizer: bool = True, save_format: Incomplete | None = None, signatures: Incomplete | None = None, options: Incomplete | None = None, save_traces: bool = True) -> None:
        """Saves the model to Tensorflow SavedModel or a single HDF5 file.

    Please see `tf.keras.models.save_model` or the
    [Serialization and Saving guide](https://keras.io/guides/serialization_and_saving/)
    for details.

    Args:
        filepath: String, PathLike, path to SavedModel or H5 file to save the
            model.
        overwrite: Whether to silently overwrite any existing file at the
            target location, or provide the user with a manual prompt.
        include_optimizer: If True, save optimizer's state together.
        save_format: Either `'tf'` or `'h5'`, indicating whether to save the
            model to Tensorflow SavedModel or HDF5. Defaults to 'tf' in TF 2.X,
            and 'h5' in TF 1.X.
        signatures: Signatures to save with the SavedModel. Applicable to the
            'tf' format only. Please see the `signatures` argument in
            `tf.saved_model.save` for details.
        options: (only applies to SavedModel format)
            `tf.saved_model.SaveOptions` object that specifies options for
            saving to SavedModel.
        save_traces: (only applies to SavedModel format) When enabled, the
            SavedModel will store the function traces for each layer. This
            can be disabled, so that only the configs of each layer are stored.
            Defaults to `True`. Disabling this will decrease serialization time
            and reduce file size, but it requires that all custom layers/models
            implement a `get_config()` method.

    Example:

    ```python
    from keras.models import load_model

    model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
    del model  # deletes the existing model

    # returns a compiled model
    # identical to the previous one
    model = load_model('my_model.h5')
    ```
    """
    def save_weights(self, filepath, overwrite: bool = True, save_format: Incomplete | None = None, options: Incomplete | None = None) -> None:
        """Saves all layer weights.

    Either saves in HDF5 or in TensorFlow format based on the `save_format`
    argument.

    When saving in HDF5 format, the weight file has:
      - `layer_names` (attribute), a list of strings
          (ordered names of model layers).
      - For every layer, a `group` named `layer.name`
          - For every such layer group, a group attribute `weight_names`,
              a list of strings
              (ordered names of weights tensor of the layer).
          - For every weight in the layer, a dataset
              storing the weight value, named after the weight tensor.

    When saving in TensorFlow format, all objects referenced by the network are
    saved in the same format as `tf.train.Checkpoint`, including any `Layer`
    instances or `Optimizer` instances assigned to object attributes. For
    networks constructed from inputs and outputs using `tf.keras.Model(inputs,
    outputs)`, `Layer` instances used by the network are tracked/saved
    automatically. For user-defined classes which inherit from `tf.keras.Model`,
    `Layer` instances must be assigned to object attributes, typically in the
    constructor. See the documentation of `tf.train.Checkpoint` and
    `tf.keras.Model` for details.

    While the formats are the same, do not mix `save_weights` and
    `tf.train.Checkpoint`. Checkpoints saved by `Model.save_weights` should be
    loaded using `Model.load_weights`. Checkpoints saved using
    `tf.train.Checkpoint.save` should be restored using the corresponding
    `tf.train.Checkpoint.restore`. Prefer `tf.train.Checkpoint` over
    `save_weights` for training checkpoints.

    The TensorFlow format matches objects and variables by starting at a root
    object, `self` for `save_weights`, and greedily matching attribute
    names. For `Model.save` this is the `Model`, and for `Checkpoint.save` this
    is the `Checkpoint` even if the `Checkpoint` has a model attached. This
    means saving a `tf.keras.Model` using `save_weights` and loading into a
    `tf.train.Checkpoint` with a `Model` attached (or vice versa) will not match
    the `Model`'s variables. See the [guide to training
    checkpoints](https://www.tensorflow.org/guide/checkpoint) for details
    on the TensorFlow format.

    Args:
        filepath: String or PathLike, path to the file to save the weights to.
            When saving in TensorFlow format, this is the prefix used for
            checkpoint files (multiple files are generated). Note that the '.h5'
            suffix causes weights to be saved in HDF5 format.
        overwrite: Whether to silently overwrite any existing file at the
            target location, or provide the user with a manual prompt.
        save_format: Either 'tf' or 'h5'. A `filepath` ending in '.h5' or
            '.keras' will default to HDF5 if `save_format` is `None`. Otherwise
            `None` defaults to 'tf'.
        options: Optional `tf.train.CheckpointOptions` object that specifies
            options for saving weights.

    Raises:
        ImportError: If h5py is not available when attempting to save in HDF5
            format.
        ValueError: For invalid/unknown format arguments.
    """
    def load_weights(self, filepath, by_name: bool = False, skip_mismatch: bool = False, options: Incomplete | None = None):
        """Loads all layer weights, either from a TensorFlow or an HDF5 weight file.

    If `by_name` is False weights are loaded based on the network's
    topology. This means the architecture should be the same as when the weights
    were saved.  Note that layers that don't have weights are not taken into
    account in the topological ordering, so adding or removing layers is fine as
    long as they don't have weights.

    If `by_name` is True, weights are loaded into layers only if they share the
    same name. This is useful for fine-tuning or transfer-learning models where
    some of the layers have changed.

    Only topological loading (`by_name=False`) is supported when loading weights
    from the TensorFlow format. Note that topological loading differs slightly
    between TensorFlow and HDF5 formats for user-defined classes inheriting from
    `tf.keras.Model`: HDF5 loads based on a flattened list of weights, while the
    TensorFlow format loads based on the object-local names of attributes to
    which layers are assigned in the `Model`'s constructor.

    Args:
        filepath: String, path to the weights file to load. For weight files in
            TensorFlow format, this is the file prefix (the same as was passed
            to `save_weights`). This can also be a path to a SavedModel
            saved from `model.save`.
        by_name: Boolean, whether to load weights by name or by topological
            order. Only topological loading is supported for weight files in
            TensorFlow format.
        skip_mismatch: Boolean, whether to skip loading of layers where there is
            a mismatch in the number of weights, or a mismatch in the shape of
            the weight (only valid when `by_name=True`).
        options: Optional `tf.train.CheckpointOptions` object that specifies
            options for loading weights.

    Returns:
        When loading a weight file in TensorFlow format, returns the same status
        object as `tf.train.Checkpoint.restore`. When graph building, restore
        ops are run automatically as soon as the network is built (on first call
        for user-defined classes inheriting from `Model`, immediately if it is
        already built).

        When loading weights in HDF5 format, returns `None`.

    Raises:
        ImportError: If h5py is not available and the weight file is in HDF5
            format.
        ValueError: If `skip_mismatch` is set to `True` when `by_name` is
          `False`.
    """
    def get_config(self) -> None: ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
    def to_json(self, **kwargs):
        """Returns a JSON string containing the network configuration.

    To load a network from a JSON save file, use
    `keras.models.model_from_json(json_string, custom_objects={})`.

    Args:
        **kwargs: Additional keyword arguments
            to be passed to `json.dumps()`.

    Returns:
        A JSON string.
    """
    def to_yaml(self, **kwargs) -> None:
        """Returns a yaml string containing the network configuration.

    Note: Since TF 2.6, this method is no longer supported and will raise a
    RuntimeError.

    To load a network from a yaml save file, use
    `keras.models.model_from_yaml(yaml_string, custom_objects={})`.

    `custom_objects` should be a dictionary mapping
    the names of custom losses / layers / etc to the corresponding
    functions / classes.

    Args:
        **kwargs: Additional keyword arguments
            to be passed to `yaml.dump()`.

    Returns:
        A YAML string.

    Raises:
        RuntimeError: announces that the method poses a security risk
    """
    def reset_states(self) -> None: ...
    @property
    def state_updates(self):
        """Deprecated, do NOT use!

    Returns the `updates` from all layers that are stateful.

    This is useful for separating training updates and
    state updates, e.g. when we need to update a layer's internal state
    during prediction.

    Returns:
        A list of update ops.
    """
    @property
    def weights(self):
        """Returns the list of all layer variables/weights.

    Note: This will not track the weights of nested `tf.Modules` that are not
    themselves Keras layers.

    Returns:
      A list of variables.
    """
    def summary(self, line_length: Incomplete | None = None, positions: Incomplete | None = None, print_fn: Incomplete | None = None) -> None:
        """Prints a string summary of the network.

    Args:
        line_length: Total length of printed lines
            (e.g. set this to adapt the display to different
            terminal window sizes).
        positions: Relative or absolute positions of log elements
            in each line. If not provided,
            defaults to `[.33, .55, .67, 1.]`.
        print_fn: Print function to use. Defaults to `print`.
            It will be called on each line of the summary.
            You can set it to a custom function
            in order to capture the string summary.

    Raises:
        ValueError: if `summary()` is called before the model is built.
    """
    @property
    def layers(self): ...
    def get_layer(self, name: Incomplete | None = None, index: Incomplete | None = None):
        """Retrieves a layer based on either its name (unique) or index.

    If `name` and `index` are both provided, `index` will take precedence.
    Indices are based on order of horizontal graph traversal (bottom-up).

    Args:
        name: String, name of layer.
        index: Integer, index of layer.

    Returns:
        A layer instance.

    Raises:
        ValueError: In case of invalid layer name or index.
    """

def reduce_per_replica(values, strategy, reduction: str = 'first'):
    """Reduce PerReplica objects.

  Args:
    values: Structure of `PerReplica` objects or `Tensor`s. `Tensor`s are
      returned as-is.
    strategy: `tf.distribute.Strategy` object.
    reduction: One of 'first', 'concat'.

  Returns:
    Structure of `Tensor`s.
  """
def concat(tensors, axis: int = 0):
    """Concats `tensor`s along `axis`."""
def write_scalar_summaries(logs, step) -> None: ...
def flatten_metrics_in_order(logs, metrics_names):
    """Turns the `logs` dict into a list as per key order of `metrics_names`."""
