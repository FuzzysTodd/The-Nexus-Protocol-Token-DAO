from _typeshed import Incomplete
from keras import backend as backend, losses as losses, optimizers as optimizers
from keras.distribute import distributed_training_utils as distributed_training_utils, distributed_training_utils_v1 as distributed_training_utils_v1
from keras.engine import base_layer as base_layer, training as training_lib, training_arrays_v1 as training_arrays_v1, training_distributed_v1 as training_distributed_v1, training_eager_v1 as training_eager_v1, training_generator_v1 as training_generator_v1, training_utils as training_utils, training_utils_v1 as training_utils_v1
from keras.mixed_precision import loss_scale_optimizer as loss_scale_optimizer
from keras.optimizers import optimizer_v1 as optimizer_v1
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2
from keras.saving.legacy import saving_utils as saving_utils
from keras.saving.legacy.saved_model import model_serialization as model_serialization
from keras.utils import data_utils as data_utils, layer_utils as layer_utils, losses_utils as losses_utils, tf_inspect as tf_inspect, tf_utils as tf_utils
from keras.utils.mode_keys import ModeKeys as ModeKeys

class Model(training_lib.Model):
    '''A model groups layers into an object with training & inference features.

    There are two ways to instantiate a `Model`:

    1 - With the "functional API", where you start from `Input`,
    you chain layer calls to specify the model\'s forward pass,
    and finally you create your model from inputs and outputs:

    ```python
    import tensorflow as tf

    inputs = tf.keras.Input(shape=(3,))
    x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)
    outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    ```

    2 - By subclassing the `Model` class: in that case, you should define your
    layers in `__init__` and you should implement the model\'s forward pass
    in `call`.

    ```python
    import tensorflow as tf

    class MyModel(tf.keras.Model):

      def __init__(self):
        super().__init__()
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
        super().__init__()
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
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def get_weights(self):
        """Retrieves the weights of the model.

        Returns:
            A flat list of Numpy arrays.
        """
    def load_weights(self, filepath, by_name: bool = False, skip_mismatch: bool = False):
        """Loads all layer weights, either from a TensorFlow or an HDF5 file.

        If `by_name` is False weights are loaded based on the network's
        topology. This means the architecture should be the same as when the
        weights were saved.  Note that layers that don't have weights are not
        taken into account in the topological ordering, so adding or removing
        layers is fine as long as they don't have weights.

        If `by_name` is True, weights are loaded into layers only if they share
        the same name. This is useful for fine-tuning or transfer-learning
        models where some of the layers have changed.

        Only topological loading (`by_name=False`) is supported when loading
        weights from the TensorFlow format. Note that topological loading
        differs slightly between TensorFlow and HDF5 formats for user-defined
        classes inheriting from `tf.keras.Model`: HDF5 loads based on a
        flattened list of weights, while the TensorFlow format loads based on
        the object-local names of attributes to which layers are assigned in the
        `Model`'s constructor.

        Args:
            filepath: String, path to the weights file to load. For weight files
                in TensorFlow format, this is the file prefix (the same as was
                passed to `save_weights`).
            by_name: Boolean, whether to load weights by name or by topological
                order. Only topological loading is supported for weight files in
                TensorFlow format.
            skip_mismatch: Boolean, whether to skip loading of layers where
                there is a mismatch in the number of weights, or a mismatch in
                the shape of the weight (only valid when `by_name=True`).

        Returns:
            When loading a weight file in TensorFlow format, returns the same
            status object as `tf.train.Checkpoint.restore`. When graph building,
            restore ops are run automatically as soon as the network is built
            (on first call for user-defined classes inheriting from `Model`,
            immediately if it is already built).

            When loading weights in HDF5 format, returns `None`.

        Raises:
            ImportError: If h5py is not available and the weight file is in HDF5
                format.
            ValueError: If `skip_mismatch` is set to `True` when `by_name` is
              `False`.
        """
    loss: Incomplete
    loss_weights: Incomplete
    sample_weight_mode: Incomplete
    loss_functions: Incomplete
    train_function: Incomplete
    test_function: Incomplete
    predict_function: Incomplete
    def compile(self, optimizer: str = 'rmsprop', loss: Incomplete | None = None, metrics: Incomplete | None = None, loss_weights: Incomplete | None = None, sample_weight_mode: Incomplete | None = None, weighted_metrics: Incomplete | None = None, target_tensors: Incomplete | None = None, distribute: Incomplete | None = None, **kwargs) -> None:
        '''Configures the model for training.

        Args:
            optimizer: String (name of optimizer) or optimizer instance.
                See `tf.keras.optimizers`.
            loss: String (name of objective function), objective function or
                `tf.keras.losses.Loss` instance. See `tf.keras.losses`. An
                objective function is any callable with the signature
                `scalar_loss = fn(y_true, y_pred)`. If the model has multiple
                outputs, you can use a different loss on each output by passing
                a dictionary or a list of losses. The loss value that will be
                minimized by the model will then be the sum of all individual
                losses.
            metrics: List of metrics to be evaluated by the model during
                training and testing. Typically you will use
                `metrics=[\'accuracy\']`.  To specify different metrics for
                different outputs of a multi-output model, you could also pass a
                dictionary, such as `metrics={\'output_a\': \'accuracy\',
                \'output_b\': [\'accuracy\', \'mse\']}`.  You can also pass a list
                (len = len(outputs)) of lists of metrics such as
                `metrics=[[\'accuracy\'], [\'accuracy\', \'mse\']]` or
                `metrics=[\'accuracy\', [\'accuracy\', \'mse\']]`.
            loss_weights: Optional list or dictionary specifying scalar
                coefficients (Python floats) to weight the loss contributions
                of different model outputs.
                The loss value that will be minimized by the model
                will then be the *weighted sum* of all individual losses,
                weighted by the `loss_weights` coefficients.
                If a list, it is expected to have a 1:1 mapping
                to the model\'s outputs. If a tensor, it is expected to map
                output names (strings) to scalar coefficients.
            sample_weight_mode: If you need to do timestep-wise
                sample weighting (2D weights), set this to `"temporal"`.
                `None` defaults to sample-wise weights (1D).
                If the model has multiple outputs, you can use a different
                `sample_weight_mode` on each output by passing a
                dictionary or a list of modes.
            weighted_metrics: List of metrics to be evaluated and weighted
                by sample_weight or class_weight during training and testing.
            target_tensors: By default, Keras will create placeholders for the
                model\'s target, which will be fed with the target data during
                training. If instead you would like to use your own
                target tensors (in turn, Keras will not expect external
                Numpy data for these targets at training time), you
                can specify them via the `target_tensors` argument. It can be
                a single tensor (for a single-output model), a list of tensors,
                or a dict mapping output names to target tensors.
            distribute: NOT SUPPORTED IN TF 2.0, please create and compile the
                model under distribution strategy scope instead of passing it to
                compile.
            **kwargs: Any additional arguments.

        Raises:
            ValueError: In case of invalid arguments for
                `optimizer`, `loss`, `metrics` or `sample_weight_mode`.
        '''
    @property
    def metrics(self):
        """Returns the model's metrics added using `compile`, `add_metric`
        APIs."""
    @property
    def metrics_names(self):
        """Returns the model's display labels for all outputs."""
    @property
    def run_eagerly(self):
        """Settable attribute indicating whether the model should run eagerly.

        Running eagerly means that your model will be run step by step,
        like Python code. Your model might run slower, but it should become
        easier for you to debug it by stepping into individual layer calls.

        By default, we will attempt to compile your model to a static graph to
        deliver the best execution performance.

        Returns:
          Boolean, whether the model should run eagerly.
        """
    @run_eagerly.setter
    def run_eagerly(self, value) -> None: ...
    def fit(self, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, **kwargs):
        '''Trains the model for a fixed number of epochs (dataset iterations).

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
              - A generator or `keras.utils.Sequence` returning `(inputs,
                targets)` or `(inputs, targets, sample weights)`.
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
                form of symbolic tensors, datasets,
                generators, or `keras.utils.Sequence` instances (since they
                generate batches).
            epochs: Integer. Number of epochs to train the model.
                An epoch is an iteration over the entire `x` and `y`
                data provided.
                Note that in conjunction with `initial_epoch`,
                `epochs` is to be understood as "final epoch".
                The model is not trained for a number of iterations
                given by `epochs`, but merely until the epoch
                of index `epochs` is reached.
            verbose: 0, 1, or 2. Verbosity mode.
                0 = silent, 1 = progress bar, 2 = one line per epoch.
                Note that the progress bar is not particularly useful when
                logged to a file, so verbose=2 is recommended when not running
                interactively (eg, in a production environment).
            callbacks: List of `keras.callbacks.Callback` instances.
                List of callbacks to apply during training.
                See `tf.keras.callbacks`.
            validation_split: Float between 0 and 1.
                Fraction of the training data to be used as validation data.
                The model will set apart this fraction of the training data,
                will not train on it, and will evaluate
                the loss and any model metrics
                on this data at the end of each epoch.
                The validation data is selected from the last samples
                in the `x` and `y` data provided, before shuffling. This
                argument is not supported when `x` is a dataset, generator or
               `keras.utils.Sequence` instance.
            validation_data: Data on which to evaluate
                the loss and any model metrics at the end of each epoch.
                The model will not be trained on this data.
                `validation_data` will override `validation_split`.
                `validation_data` could be:
                  - tuple `(x_val, y_val)` of Numpy arrays or tensors
                  - tuple `(x_val, y_val, val_sample_weights)` of Numpy arrays
                  - dataset
                For the first two cases, `batch_size` must be provided.
                For the last case, `validation_steps` could be provided.
            shuffle: Boolean (whether to shuffle the training data
                before each epoch) or str (for \'batch\').
                \'batch\' is a special option for dealing with the
                limitations of HDF5 data; it shuffles in batch-sized chunks.
                Has no effect when `steps_per_epoch` is not `None`.
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
                to apply a different weight to every timestep of every sample.
                In this case you should make sure to specify
                `sample_weight_mode="temporal"` in `compile()`. This argument is
                not supported when `x` is a dataset, generator, or
                `keras.utils.Sequence` instance, instead provide the
                sample_weights as the third element of `x`.
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
                is None, the epoch will run until the input dataset is
                exhausted.  This argument is not supported with array inputs.
            validation_steps: Only relevant if `validation_data` is provided and
                is a `tf.data` dataset. Total number of steps (batches of
                samples) to draw before stopping when performing validation at
                the end of every epoch. If \'validation_steps\' is None,
                validation will run until the `validation_data` dataset is
                exhausted. In the case of a infinite dataset, it will run into a
                infinite loop.  If \'validation_steps\' is specified and only part
                of the dataset will be consumed, the evaluation will start from
                the beginning of the dataset at each epoch. This ensures that
                the same validation samples are used every time.
            validation_freq: Only relevant if validation data is provided.
                Integer or `collections.abc.Container` instance (e.g. list,
                tuple, etc.).  If an integer, specifies how many training epochs
                to run before a new validation run is performed, e.g.
                `validation_freq=2` runs validation every 2 epochs. If a
                Container, specifies the epochs on which to run validation, e.g.
                `validation_freq=[1, 2, 10]` runs validation at the end of the
                1st, 2nd, and 10th epochs.
            max_queue_size: Integer. Used for generator or
                `keras.utils.Sequence` input only. Maximum size for the
                generator queue.  If unspecified, `max_queue_size` will default
                to 10.
            workers: Integer. Used for generator or `keras.utils.Sequence` input
                only. Maximum number of processes to spin up
                when using process-based threading. If unspecified, `workers`
                will default to 1. If 0, will execute the generator on the main
                thread.
            use_multiprocessing: Boolean. Used for generator or
                `keras.utils.Sequence` input only. If `True`, use process-based
                threading. If unspecified, `use_multiprocessing` will default to
                `False`. Note that because this implementation relies on
                multiprocessing, you should not pass non-picklable arguments to
                the generator as they can\'t be passed easily to children
                processes.
            **kwargs: Used for backwards compatibility.

        Returns:
            A `History` object. Its `History.history` attribute is
            a record of training loss values and metrics values
            at successive epochs, as well as validation loss values
            and validation metrics values (if applicable).

        Raises:
            RuntimeError: If the model was never compiled.
            ValueError: In case of mismatch between the provided input data
                and what the model expects.
        '''
    def evaluate(self, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False):
        '''Returns the loss value & metrics values for the model in test mode.

        Computation is done in batches (see the `batch_size` arg.)

        Args:
            x: Input data. It could be:
              - A Numpy array (or array-like), or a list of arrays
                (in case the model has multiple inputs).
              - A TensorFlow tensor, or a list of tensors
                (in case the model has multiple inputs).
              - A dict mapping input names to the corresponding array/tensors,
                if the model has named inputs.
              - A `tf.data` dataset.
              - A generator or `keras.utils.Sequence` instance.
            y: Target data. Like the input data `x`,
              it could be either Numpy array(s) or TensorFlow tensor(s).
              It should be consistent with `x` (you cannot have Numpy inputs and
              tensor targets, or inversely).
              If `x` is a dataset, generator or
              `keras.utils.Sequence` instance, `y` should not be specified
              (since targets will be obtained from the iterator/dataset).
            batch_size: Integer or `None`.
                Number of samples per batch of computation.
                If unspecified, `batch_size` will default to 32.
                Do not specify the `batch_size` if your data is in the
                form of symbolic tensors, dataset,
                generators, or `keras.utils.Sequence` instances (since they
                generate batches).
            verbose: 0 or 1. Verbosity mode.
                0 = silent, 1 = progress bar.
            sample_weight: Optional Numpy array of weights for
                the test samples, used for weighting the loss function.
                You can either pass a flat (1D)
                Numpy array with the same length as the input samples
                (1:1 mapping between weights and samples),
                or in the case of temporal data,
                you can pass a 2D array with shape
                `(samples, sequence_length)`,
                to apply a different weight to every timestep of every sample.
                In this case you should make sure to specify
                `sample_weight_mode="temporal"` in `compile()`. This argument is
                not supported when `x` is a dataset, instead pass sample weights
                as the third element of `x`.
            steps: Integer or `None`.
                Total number of steps (batches of samples)
                before declaring the evaluation round finished.
                Ignored with the default value of `None`.
                If x is a `tf.data` dataset and `steps` is
                None, \'evaluate\' will run until the dataset is exhausted.
                This argument is not supported with array inputs.
            callbacks: List of `keras.callbacks.Callback` instances.
                List of callbacks to apply during evaluation.
                See [callbacks](/api_docs/python/tf/keras/callbacks).
            max_queue_size: Integer. Used for generator or
                `keras.utils.Sequence` input only. Maximum size for the
                generator queue.  If unspecified, `max_queue_size` will default
                to 10.
            workers: Integer. Used for generator or `keras.utils.Sequence` input
                only. Maximum number of processes to spin up when using
                process-based threading. If unspecified, `workers` will default
                to 1. If 0, will execute the generator on the main thread.
            use_multiprocessing: Boolean. Used for generator or
                `keras.utils.Sequence` input only. If `True`, use process-based
                threading. If unspecified, `use_multiprocessing` will default to
                `False`. Note that because this implementation relies on
                multiprocessing, you should not pass non-picklable arguments to
                the generator as they can\'t be passed easily to children
                processes.

        Returns:
            Scalar test loss (if the model has a single output and no metrics)
            or list of scalars (if the model has multiple outputs
            and/or metrics). The attribute `model.metrics_names` will give you
            the display labels for the scalar outputs.

        Raises:
            ValueError: in case of invalid arguments.
        '''
    def predict(self, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False):
        """Generates output predictions for the input samples.

        Computation is done in batches (see the `batch_size` arg.)

        Args:
            x: Input samples. It could be:
              - A Numpy array (or array-like), or a list of arrays
                (in case the model has multiple inputs).
              - A TensorFlow tensor, or a list of tensors
                (in case the model has multiple inputs).
              - A `tf.data` dataset.
              - A generator or `keras.utils.Sequence` instance.
            batch_size: Integer or `None`.
                Number of samples per batch of computation.
                If unspecified, `batch_size` will default to 32.
                Do not specify the `batch_size` if your data is in the
                form of symbolic tensors, dataset,
                generators, or `keras.utils.Sequence` instances (since they
                generate batches).
            verbose: Verbosity mode, 0 or 1.
            steps: Total number of steps (batches of samples)
                before declaring the prediction round finished.
                Ignored with the default value of `None`. If x is a `tf.data`
                dataset and `steps` is None, `predict` will
                run until the input dataset is exhausted.
            callbacks: List of `keras.callbacks.Callback` instances.
                List of callbacks to apply during prediction.
                See [callbacks](/api_docs/python/tf/keras/callbacks).
            max_queue_size: Integer. Used for generator or
                `keras.utils.Sequence` input only. Maximum size for the
                generator queue. If unspecified, `max_queue_size` will default
                to 10.
            workers: Integer. Used for generator or `keras.utils.Sequence` input
                only. Maximum number of processes to spin up when using
                process-based threading. If unspecified, `workers` will default
                to 1. If 0, will execute the generator on the main thread.
            use_multiprocessing: Boolean. Used for generator or
                `keras.utils.Sequence` input only. If `True`, use process-based
                threading. If unspecified, `use_multiprocessing` will default to
                `False`. Note that because this implementation relies on
                multiprocessing, you should not pass non-picklable arguments to
                the generator as they can't be passed easily to children
                processes.


        Returns:
            Numpy array(s) of predictions.

        Raises:
            ValueError: In case of mismatch between the provided
                input data and the model's expectations,
                or in case a stateful model receives a number of samples
                that is not a multiple of the batch size.
        """
    def reset_metrics(self) -> None:
        """Resets the state of metrics."""
    def train_on_batch(self, x, y: Incomplete | None = None, sample_weight: Incomplete | None = None, class_weight: Incomplete | None = None, reset_metrics: bool = True):
        '''Runs a single gradient update on a single batch of data.

        Args:
            x: Input data. It could be:
              - A Numpy array (or array-like), or a list of arrays
                  (in case the model has multiple inputs).
              - A TensorFlow tensor, or a list of tensors
                  (in case the model has multiple inputs).
              - A dict mapping input names to the corresponding array/tensors,
                  if the model has named inputs.
              - A `tf.data` dataset.
            y: Target data. Like the input data `x`, it could be either Numpy
              array(s) or TensorFlow tensor(s). It should be consistent with `x`
              (you cannot have Numpy inputs and tensor targets, or inversely).
              If `x` is a dataset, `y` should not be specified
              (since targets will be obtained from the iterator).
            sample_weight: Optional array of the same length as x, containing
              weights to apply to the model\'s loss for each sample. In the case
              of temporal data, you can pass a 2D array with shape (samples,
              sequence_length), to apply a different weight to every timestep of
              every sample. In this case you should make sure to specify
              sample_weight_mode="temporal" in compile(). This argument is not
              supported when `x` is a dataset.
            class_weight: Optional dictionary mapping class indices (integers)
              to a weight (float) to apply to the model\'s loss for the samples
              from this class during training. This can be useful to tell the
              model to "pay more attention" to samples from an under-represented
              class.
            reset_metrics: If `True`, the metrics returned will be only for this
              batch. If `False`, the metrics will be statefully accumulated
              across batches.

        Returns:
            Scalar training loss
            (if the model has a single output and no metrics)
            or list of scalars (if the model has multiple outputs
            and/or metrics). The attribute `model.metrics_names` will give you
            the display labels for the scalar outputs.

        Raises:
          ValueError: In case of invalid user-provided arguments.
        '''
    def test_on_batch(self, x, y: Incomplete | None = None, sample_weight: Incomplete | None = None, reset_metrics: bool = True):
        '''Test the model on a single batch of samples.

        Args:
            x: Input data. It could be:
              - A Numpy array (or array-like), or a list of arrays
                (in case the model has multiple inputs).
              - A TensorFlow tensor, or a list of tensors
                (in case the model has multiple inputs).
              - A dict mapping input names to the corresponding array/tensors,
                if the model has named inputs.
              - A `tf.data` dataset.
            y: Target data. Like the input data `x`,
              it could be either Numpy array(s) or TensorFlow tensor(s).
              It should be consistent with `x` (you cannot have Numpy inputs and
              tensor targets, or inversely). If `x` is a dataset `y` should
              not be specified (since targets will be obtained from the
              iterator).
            sample_weight: Optional array of the same length as x, containing
                weights to apply to the model\'s loss for each sample.
                In the case of temporal data, you can pass a 2D array
                with shape (samples, sequence_length),
                to apply a different weight to every timestep of every sample.
                In this case you should make sure to specify
                sample_weight_mode="temporal" in compile(). This argument is not
                supported when `x` is a dataset.
            reset_metrics: If `True`, the metrics returned will be only for this
              batch. If `False`, the metrics will be statefully accumulated
              across batches.

        Returns:
            Scalar test loss (if the model has a single output and no metrics)
            or list of scalars (if the model has multiple outputs
            and/or metrics). The attribute `model.metrics_names` will give you
            the display labels for the scalar outputs.

        Raises:
            ValueError: In case of invalid user-provided arguments.
        '''
    def predict_on_batch(self, x):
        """Returns predictions for a single batch of samples.

        Args:
            x: Input data. It could be:
              - A Numpy array (or array-like), or a list of arrays
                (in case the model has multiple inputs).
              - A TensorFlow tensor, or a list of tensors
                (in case the model has multiple inputs).
              - A `tf.data` dataset.

        Returns:
            Numpy array(s) of predictions.

        Raises:
            ValueError: In case of mismatch between given number of inputs and
              expectations of the model.
        """
    def fit_generator(self, generator, steps_per_epoch: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_data: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, class_weight: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, shuffle: bool = True, initial_epoch: int = 0):
        """Fits the model on data yielded batch-by-batch by a Python generator.

        DEPRECATED:
          `Model.fit` now supports generators, so there is no longer any need to
          use this endpoint.
        """
    def evaluate_generator(self, generator, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, verbose: int = 0):
        """Evaluates the model on a data generator.

        DEPRECATED:
          `Model.evaluate` now supports generators, so there is no longer any
          need to use this endpoint.
        """
    def predict_generator(self, generator, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, verbose: int = 0):
        """Generates predictions for the input samples from a data generator.

        DEPRECATED:
          `Model.predict` now supports generators, so there is no longer any
          need to use this endpoint.
        """
    @property
    def sample_weights(self): ...

class DistributedCallbackModel(Model):
    """Model that is used for callbacks with tf.distribute.Strategy."""
    optimizer: Incomplete
    def __init__(self, model) -> None: ...
    def set_original_model(self, orig_model) -> None: ...
    def save_weights(self, filepath, overwrite: bool = True, save_format: Incomplete | None = None) -> None: ...
    def save(self, filepath, overwrite: bool = True, include_optimizer: bool = True) -> None: ...
    def load_weights(self, filepath, by_name: bool = False) -> None: ...
    def __getattr__(self, item): ...

class _TrainingEndpoint:
    """A container for the training output/target and related entities.

    In the case of model with multiple outputs, there is a one-to-one mapping
    between model output (y_pred), model target (y_true), loss, metrics etc.
    By unifying these entities into one class, different entity can access
    information between each other, rather than currently access different list
    of attributes of the model.
    """
    def __init__(self, output, output_name, loss_fn, loss_weight: Incomplete | None = None, training_target: Incomplete | None = None, output_loss_metric: Incomplete | None = None, sample_weight: Incomplete | None = None, sample_weight_mode: Incomplete | None = None) -> None:
        """Initialize the _TrainingEndpoint.

        Note that the output and output_name should be stable as long as the
        model structure doesn't change. The training_target suppose to be
        mutable since the information is provided via `compile()`

        Args:
          output: the output tensor of the model.
          output_name: the unique name of the output tensor.
          loss_fn: the loss function for the output tensor.
          loss_weight: float, the weights for the loss.
          training_target: the _TrainingTarget for the model.
          output_loss_metric: the metric object for the loss function.
          sample_weight: the weights for how a sample is weighted during metric
            and loss calculation. Could be None.
          sample_weight_mode: string, 'temporal', 'samplewise' or None. The mode
            for how the sample_weight is populated.
        """
    @property
    def output(self): ...
    @property
    def output_name(self): ...
    @property
    def shape(self): ...
    @property
    def loss_fn(self): ...
    @property
    def loss_weight(self): ...
    @loss_weight.setter
    def loss_weight(self, value) -> None: ...
    @property
    def training_target(self): ...
    @training_target.setter
    def training_target(self, value) -> None: ...
    def create_training_target(self, target, run_eagerly: bool = False) -> None:
        """Create training_target instance and update the self.training_target.

        Note that the input target should just be a tensor or None, and
        corresponding training target will be created based on the output and
        loss_fn.

        Args:
          target: the target tensor for the current output. Could be None.
          run_eagerly: boolean, whether the model is in run_eagerly mode.

        Raises:
          ValueError if the training_target field for the current instance has
          already been populated.
        """
    @property
    def output_loss_metric(self): ...
    @output_loss_metric.setter
    def output_loss_metric(self, value) -> None: ...
    @property
    def sample_weight(self): ...
    @sample_weight.setter
    def sample_weight(self, value) -> None: ...
    @property
    def sample_weight_mode(self): ...
    @sample_weight_mode.setter
    def sample_weight_mode(self, value) -> None: ...
    def should_skip_target(self): ...
    def should_skip_target_weights(self): ...
    def has_training_target(self): ...
    def has_feedable_training_target(self): ...
    def loss_name(self): ...
    @property
    def feed_output_shape(self):
        """The output shape for the feedable target."""
    def sample_weights_mismatch(self):
        """Check if the sample weight and the mode match or not."""
    def populate_sample_weight(self, sample_weight, sample_weight_mode) -> None:
        """Populate the sample weight and based on the sample weight mode."""

class _TrainingTarget:
    """Container for a target tensor (y_true) and its metadata (shape, loss...).

    Args:
      target: A target tensor for the model. It may be `None` if the
        output is excluded from loss computation. It is still kept as None
        since each output of the model should have a corresponding target. If
        the target is None, the rest of the attributes will be None as well.
      feedable: Boolean, whether the target is feedable (requires data to be
        passed in `fit` or `train_on_batch`), or not (model compiled with
        `target_tensors` argument).
      skip_target_weights: Boolean, whether the target should be skipped during
        weights calculation.
    """
    def __init__(self, target, feedable: bool = False, skip_target_weights: bool = True) -> None: ...
    @property
    def target(self): ...
    @property
    def feedable(self): ...
    @property
    def skip_target_weights(self): ...
