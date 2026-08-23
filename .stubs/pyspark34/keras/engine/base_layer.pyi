import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.dtensor import lazy_variable as lazy_variable
from keras.engine import base_layer_utils as base_layer_utils, input_spec as input_spec, keras_tensor as keras_tensor
from keras.mixed_precision import autocast_variable as autocast_variable, loss_scale_optimizer as loss_scale_optimizer, policy as policy
from keras.saving import serialization_lib as serialization_lib
from keras.saving.legacy.saved_model import layer_serialization as layer_serialization
from keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, object_identity as object_identity, tf_inspect as tf_inspect, tf_utils as tf_utils, traceback_utils as traceback_utils, version_utils as version_utils
from keras.utils.generic_utils import to_snake_case as to_snake_case
from keras.utils.tf_utils import is_tensor_or_tensor_list as is_tensor_or_tensor_list

metrics_mod: Incomplete
keras_layers_gauge: Incomplete
keras_models_gauge: Incomplete
keras_api_gauge: Incomplete
keras_premade_model_gauge: Incomplete

class Layer(tf.Module, version_utils.LayerVersionSelector):
    """This is the class from which all layers inherit.

    A layer is a callable object that takes as input one or more tensors and
    that outputs one or more tensors. It involves *computation*, defined
    in the `call()` method, and a *state* (weight variables). State can be
    created in various places, at the convenience of the subclass implementer:

    * in `__init__()`;
    * in the optional `build()` method, which is invoked by the first
      `__call__()` to the layer, and supplies the shape(s) of the input(s),
      which may not have been known at initialization time;
    * in the first invocation of `call()`, with some caveats discussed
      below.

    Layers are recursively composable: If you assign a Layer instance as an
    attribute of another Layer, the outer layer will start tracking the weights
    created by the inner layer. Nested layers should be instantiated in the
    `__init__()` method.

    Users will just instantiate a layer and then treat it as a callable.

    Args:
      trainable: Boolean, whether the layer's variables should be trainable.
      name: String name of the layer.
      dtype: The dtype of the layer's computations and weights. Can also be a
        `tf.keras.mixed_precision.Policy`, which allows the computation and
        weight dtype to differ. Default of `None` means to use
        `tf.keras.mixed_precision.global_policy()`, which is a float32 policy
        unless set to different value.
      dynamic: Set this to `True` if your layer should only be run eagerly, and
        should not be used to generate a static computation graph.
        This would be the case for a Tree-RNN or a recursive network,
        for example, or generally for any layer that manipulates tensors
        using Python control flow. If `False`, we assume that the layer can
        safely be used to generate a static computation graph.

    Attributes:
      name: The name of the layer (string).
      dtype: The dtype of the layer's weights.
      variable_dtype: Alias of `dtype`.
      compute_dtype: The dtype of the layer's computations. Layers automatically
        cast inputs to this dtype which causes the computations and output to
        also be in this dtype. When mixed precision is used with a
        `tf.keras.mixed_precision.Policy`, this will be different than
        `variable_dtype`.
      dtype_policy: The layer's dtype policy. See the
        `tf.keras.mixed_precision.Policy` documentation for details.
      trainable_weights: List of variables to be included in backprop.
      non_trainable_weights: List of variables that should not be
        included in backprop.
      weights: The concatenation of the lists trainable_weights and
        non_trainable_weights (in this order).
      trainable: Whether the layer should be trained (boolean), i.e. whether
        its potentially-trainable weights should be returned as part of
        `layer.trainable_weights`.
      input_spec: Optional (list of) `InputSpec` object(s) specifying the
        constraints on inputs that can be accepted by the layer.

    We recommend that descendants of `Layer` implement the following methods:

    * `__init__()`: Defines custom layer attributes, and creates layer weights
      that do not depend on input shapes, using `add_weight()`, or other state.
    * `build(self, input_shape)`: This method can be used to create weights that
      depend on the shape(s) of the input(s), using `add_weight()`, or other
      state. `__call__()` will automatically build the layer (if it has not been
      built yet) by calling `build()`.
    * `call(self, inputs, *args, **kwargs)`: Called in `__call__` after making
      sure `build()` has been called. `call()` performs the logic of applying
      the layer to the `inputs`. The first invocation may additionally create
      state that could not be conveniently created in `build()`; see its
      docstring for details.
      Two reserved keyword arguments you can optionally use in `call()` are:
        - `training` (boolean, whether the call is in inference mode or training
          mode). See more details in [the layer/model subclassing guide](
          https://www.tensorflow.org/guide/keras/custom_layers_and_models#privileged_training_argument_in_the_call_method)
        - `mask` (boolean tensor encoding masked timesteps in the input, used
          in RNN layers). See more details in
          [the layer/model subclassing guide](
          https://www.tensorflow.org/guide/keras/custom_layers_and_models#privileged_mask_argument_in_the_call_method)
      A typical signature for this method is `call(self, inputs)`, and user
      could optionally add `training` and `mask` if the layer need them. `*args`
      and `**kwargs` is only useful for future extension when more input
      parameters are planned to be added.
    * `get_config(self)`: Returns a dictionary containing the configuration used
      to initialize this layer. If the keys differ from the arguments
      in `__init__`, then override `from_config(self)` as well.
      This method is used when saving
      the layer or a model that contains this layer.

    Examples:

    Here's a basic example: a layer with two variables, `w` and `b`,
    that returns `y = w . x + b`.
    It shows how to implement `build()` and `call()`.
    Variables set as attributes of a layer are tracked as weights
    of the layers (in `layer.weights`).

    ```python
    class SimpleDense(Layer):

      def __init__(self, units=32):
          super(SimpleDense, self).__init__()
          self.units = units

      def build(self, input_shape):  # Create the state of the layer (weights)
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_shape[-1], self.units),
                                 dtype='float32'),
            trainable=True)
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(self.units,), dtype='float32'),
            trainable=True)

      def call(self, inputs):  # Defines the computation from inputs to outputs
          return tf.matmul(inputs, self.w) + self.b

    # Instantiates the layer.
    linear_layer = SimpleDense(4)

    # This will also call `build(input_shape)` and create the weights.
    y = linear_layer(tf.ones((2, 2)))
    assert len(linear_layer.weights) == 2

    # These weights are trainable, so they're listed in `trainable_weights`:
    assert len(linear_layer.trainable_weights) == 2
    ```

    Note that the method `add_weight()` offers a shortcut to create weights:

    ```python
    class SimpleDense(Layer):

      def __init__(self, units=32):
          super(SimpleDense, self).__init__()
          self.units = units

      def build(self, input_shape):
          self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                   initializer='random_normal',
                                   trainable=True)
          self.b = self.add_weight(shape=(self.units,),
                                   initializer='random_normal',
                                   trainable=True)

      def call(self, inputs):
          return tf.matmul(inputs, self.w) + self.b
    ```

    Besides trainable weights, updated via backpropagation during training,
    layers can also have non-trainable weights. These weights are meant to
    be updated manually during `call()`. Here's a example layer that computes
    the running sum of its inputs:

    ```python
    class ComputeSum(Layer):

      def __init__(self, input_dim):
          super(ComputeSum, self).__init__()
          # Create a non-trainable weight.
          self.total = tf.Variable(initial_value=tf.zeros((input_dim,)),
                                   trainable=False)

      def call(self, inputs):
          self.total.assign_add(tf.reduce_sum(inputs, axis=0))
          return self.total

    my_sum = ComputeSum(2)
    x = tf.ones((2, 2))

    y = my_sum(x)
    print(y.numpy())  # [2. 2.]

    y = my_sum(x)
    print(y.numpy())  # [4. 4.]

    assert my_sum.weights == [my_sum.total]
    assert my_sum.non_trainable_weights == [my_sum.total]
    assert my_sum.trainable_weights == []
    ```

    For more information about creating layers, see the guide
    [Making new Layers and Models via subclassing](
      https://www.tensorflow.org/guide/keras/custom_layers_and_models)
    """
    built: bool
    def __init__(self, trainable: bool = True, name: Incomplete | None = None, dtype: Incomplete | None = None, dynamic: bool = False, **kwargs) -> None: ...
    def build(self, input_shape) -> None:
        """Creates the variables of the layer (for subclass implementers).

        This is a method that implementers of subclasses of `Layer` or `Model`
        can override if they need a state-creation step in-between
        layer instantiation and layer call. It is invoked automatically before
        the first execution of `call()`.

        This is typically used to create the weights of `Layer` subclasses
        (at the discretion of the subclass implementer).

        Args:
          input_shape: Instance of `TensorShape`, or list of instances of
            `TensorShape` if the layer expects a list of inputs
            (one instance per input).
        """
    def call(self, inputs, *args, **kwargs):
        """This is where the layer's logic lives.

        The `call()` method may not create state (except in its first
        invocation, wrapping the creation of variables or other resources in
        `tf.init_scope()`).  It is recommended to create state, including
        `tf.Variable` instances and nested `Layer` instances,
         in `__init__()`, or in the `build()` method that is
        called automatically before `call()` executes for the first time.

        Args:
          inputs: Input tensor, or dict/list/tuple of input tensors.
            The first positional `inputs` argument is subject to special rules:
            - `inputs` must be explicitly passed. A layer cannot have zero
              arguments, and `inputs` cannot be provided via the default value
              of a keyword argument.
            - NumPy array or Python scalar values in `inputs` get cast as
              tensors.
            - Keras mask metadata is only collected from `inputs`.
            - Layers are built (`build(input_shape)` method)
              using shape info from `inputs` only.
            - `input_spec` compatibility is only checked against `inputs`.
            - Mixed precision input casting is only applied to `inputs`.
              If a layer has tensor arguments in `*args` or `**kwargs`, their
              casting behavior in mixed precision should be handled manually.
            - The SavedModel input specification is generated using `inputs`
              only.
            - Integration with various ecosystem packages like TFMOT, TFLite,
              TF.js, etc is only supported for `inputs` and not for tensors in
              positional and keyword arguments.
          *args: Additional positional arguments. May contain tensors, although
            this is not recommended, for the reasons above.
          **kwargs: Additional keyword arguments. May contain tensors, although
            this is not recommended, for the reasons above.
            The following optional keyword arguments are reserved:
            - `training`: Boolean scalar tensor of Python boolean indicating
              whether the `call` is meant for training or inference.
            - `mask`: Boolean input mask. If the layer's `call()` method takes a
              `mask` argument, its default value will be set to the mask
              generated for `inputs` by the previous layer (if `input` did come
              from a layer that generated a corresponding mask, i.e. if it came
              from a Keras layer with masking support).

        Returns:
          A tensor or list/tuple of tensors.
        """
    def add_weight(self, name: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, trainable: Incomplete | None = None, constraint: Incomplete | None = None, use_resource: Incomplete | None = None, synchronization=..., aggregation=..., **kwargs):
        '''Adds a new variable to the layer.

        Args:
          name: Variable name.
          shape: Variable shape. Defaults to scalar if unspecified.
          dtype: The type of the variable. Defaults to `self.dtype`.
          initializer: Initializer instance (callable).
          regularizer: Regularizer instance (callable).
          trainable: Boolean, whether the variable should be part of the layer\'s
            "trainable_variables" (e.g. variables, biases)
            or "non_trainable_variables" (e.g. BatchNorm mean and variance).
            Note that `trainable` cannot be `True` if `synchronization`
            is set to `ON_READ`.
          constraint: Constraint instance (callable).
          use_resource: Whether to use a `ResourceVariable` or not.
            See [this guide](
            https://www.tensorflow.org/guide/migrate/tf1_vs_tf2#resourcevariables_instead_of_referencevariables)
             for more information.
          synchronization: Indicates when a distributed a variable will be
            aggregated. Accepted values are constants defined in the class
            `tf.VariableSynchronization`. By default the synchronization is set
            to `AUTO` and the current `DistributionStrategy` chooses when to
            synchronize. If `synchronization` is set to `ON_READ`, `trainable`
            must not be set to `True`.
          aggregation: Indicates how a distributed variable will be aggregated.
            Accepted values are constants defined in the class
            `tf.VariableAggregation`.
          **kwargs: Additional keyword arguments. Accepted values are `getter`,
            `collections`, `experimental_autocast` and `caching_device`.

        Returns:
          The variable created.

        Raises:
          ValueError: When giving unsupported dtype and no initializer or when
            trainable has been set to True with synchronization set as
            `ON_READ`.
        '''
    def __new__(cls, *args, **kwargs): ...
    def get_config(self):
        """Returns the config of the layer.

        A layer config is a Python dictionary (serializable)
        containing the configuration of a layer.
        The same layer can be reinstantiated later
        (without its trained weights) from this configuration.

        The config of a layer does not include connectivity
        information, nor the layer class name. These are handled
        by `Network` (one layer of abstraction above).

        Note that `get_config()` does not guarantee to return a fresh copy of
        dict every time it is called. The callers should make a copy of the
        returned dict if they want to modify it.

        Returns:
            Python dictionary.
        """
    @classmethod
    def from_config(cls, config):
        """Creates a layer from its config.

        This method is the reverse of `get_config`,
        capable of instantiating the same layer from the config
        dictionary. It does not handle layer connectivity
        (handled by Network), nor weights (handled by `set_weights`).

        Args:
            config: A Python dictionary, typically the
                output of get_config.

        Returns:
            A layer instance.
        """
    def compute_output_shape(self, input_shape):
        """Computes the output shape of the layer.

        This method will cause the layer's state to be built, if that has not
        happened before. This requires that the layer will later be used with
        inputs that match the input shape provided here.

        Args:
            input_shape: Shape tuple (tuple of integers) or `tf.TensorShape`,
                or structure of shape tuples / `tf.TensorShape` instances
                (one per output tensor of the layer).
                Shape tuples can include None for free dimensions,
                instead of an integer.

        Returns:
            A `tf.TensorShape` instance
            or structure of `tf.TensorShape` instances.
        """
    def compute_output_signature(self, input_signature):
        """Compute the output tensor signature of the layer based on the inputs.

        Unlike a TensorShape object, a TensorSpec object contains both shape
        and dtype information for a tensor. This method allows layers to provide
        output dtype information if it is different from the input dtype.
        For any layer that doesn't implement this function,
        the framework will fall back to use `compute_output_shape`, and will
        assume that the output dtype matches the input dtype.

        Args:
          input_signature: Single TensorSpec or nested structure of TensorSpec
            objects, describing a candidate input for the layer.

        Returns:
          Single TensorSpec or nested structure of TensorSpec objects,
            describing how the layer would transform the provided input.

        Raises:
          TypeError: If input_signature contains a non-TensorSpec object.
        """
    def compute_mask(self, inputs, mask: Incomplete | None = None):
        """Computes an output mask tensor.

        Args:
            inputs: Tensor or list of tensors.
            mask: Tensor or list of tensors.

        Returns:
            None or a tensor (or list of tensors,
                one per output tensor of the layer).
        """
    def __call__(self, *args, **kwargs):
        """Wraps `call`, applying pre- and post-processing steps.

        Args:
          *args: Positional arguments to be passed to `self.call`.
          **kwargs: Keyword arguments to be passed to `self.call`.

        Returns:
          Output tensor(s).

        Note:
          - The following optional keyword arguments are reserved for specific
            uses:
            * `training`: Boolean scalar tensor of Python boolean indicating
              whether the `call` is meant for training or inference.
            * `mask`: Boolean input mask.
          - If the layer's `call` method takes a `mask` argument (as some Keras
            layers do), its default value will be set to the mask generated
            for `inputs` by the previous layer (if `input` did come from
            a layer that generated a corresponding mask, i.e. if it came from
            a Keras layer with masking support.
          - If the layer is not built, the method will call `build`.

        Raises:
          ValueError: if the layer's `call` method returns None (an invalid
            value).
          RuntimeError: if `super().__init__()` was not called in the
            constructor.
        """
    @property
    def dtype(self):
        """The dtype of the layer weights.

        This is equivalent to `Layer.dtype_policy.variable_dtype`. Unless
        mixed precision is used, this is the same as `Layer.compute_dtype`, the
        dtype of the layer's computations.
        """
    @property
    def name(self):
        """Name of the layer (string), set in the constructor."""
    @property
    def supports_masking(self):
        """Whether this layer supports computing a mask using `compute_mask`."""
    @supports_masking.setter
    def supports_masking(self, value) -> None: ...
    @property
    def dynamic(self):
        """Whether the layer is dynamic (eager-only); set in the constructor."""
    @property
    def stateful(self): ...
    @stateful.setter
    def stateful(self, value) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value) -> None:
        """Sets trainable attribute for the layer and its sublayers.

        When this value is changed during training (e.g. with a
        `tf.keras.callbacks.Callback`) you need to call the parent
        `tf.keras.Model.make_train_function` with `force=True` in order to
        recompile the training graph.

        Args:
          value: Boolean with the desired state for the layer's trainable
            attribute.
        """
    @property
    def activity_regularizer(self):
        """Optional regularizer function for the output of this layer."""
    @activity_regularizer.setter
    def activity_regularizer(self, regularizer) -> None:
        """Optional regularizer function for the output of this layer."""
    @property
    def input_spec(self):
        """`InputSpec` instance(s) describing the input format for this layer.

        When you create a layer subclass, you can set `self.input_spec` to
        enable the layer to run input compatibility checks when it is called.
        Consider a `Conv2D` layer: it can only be called on a single input
        tensor of rank 4. As such, you can set, in `__init__()`:

        ```python
        self.input_spec = tf.keras.layers.InputSpec(ndim=4)
        ```

        Now, if you try to call the layer on an input that isn't rank 4
        (for instance, an input of shape `(2,)`, it will raise a
        nicely-formatted error:

        ```
        ValueError: Input 0 of layer conv2d is incompatible with the layer:
        expected ndim=4, found ndim=1. Full shape received: [2]
        ```

        Input checks that can be specified via `input_spec` include:
        - Structure (e.g. a single input, a list of 2 inputs, etc)
        - Shape
        - Rank (ndim)
        - Dtype

        For more information, see `tf.keras.layers.InputSpec`.

        Returns:
          A `tf.keras.layers.InputSpec` instance, or nested structure thereof.
        """
    @input_spec.setter
    def input_spec(self, value) -> None: ...
    @property
    def trainable_weights(self):
        """List of all trainable weights tracked by this layer.

        Trainable weights are updated via gradient descent during training.

        Returns:
          A list of trainable variables.
        """
    @property
    def non_trainable_weights(self):
        """List of all non-trainable weights tracked by this layer.

        Non-trainable weights are *not* updated during training. They are
        expected to be updated manually in `call()`.

        Returns:
          A list of non-trainable variables.
        """
    @property
    def weights(self):
        """Returns the list of all layer variables/weights.

        Returns:
          A list of variables.
        """
    @property
    def updates(self): ...
    @property
    def losses(self):
        """List of losses added using the `add_loss()` API.

        Variable regularization tensors are created when this property is
        accessed, so it is eager safe: accessing `losses` under a
        `tf.GradientTape` will propagate gradients back to the corresponding
        variables.

        Examples:

        >>> class MyLayer(tf.keras.layers.Layer):
        ...   def call(self, inputs):
        ...     self.add_loss(tf.abs(tf.reduce_mean(inputs)))
        ...     return inputs
        >>> l = MyLayer()
        >>> l(np.ones((10, 1)))
        >>> l.losses
        [1.0]

        >>> inputs = tf.keras.Input(shape=(10,))
        >>> x = tf.keras.layers.Dense(10)(inputs)
        >>> outputs = tf.keras.layers.Dense(1)(x)
        >>> model = tf.keras.Model(inputs, outputs)
        >>> # Activity regularization.
        >>> len(model.losses)
        0
        >>> model.add_loss(tf.abs(tf.reduce_mean(x)))
        >>> len(model.losses)
        1

        >>> inputs = tf.keras.Input(shape=(10,))
        >>> d = tf.keras.layers.Dense(10, kernel_initializer='ones')
        >>> x = d(inputs)
        >>> outputs = tf.keras.layers.Dense(1)(x)
        >>> model = tf.keras.Model(inputs, outputs)
        >>> # Weight regularization.
        >>> model.add_loss(lambda: tf.reduce_mean(d.kernel))
        >>> model.losses
        [<tf.Tensor: shape=(), dtype=float32, numpy=1.0>]

        Returns:
          A list of tensors.
        """
    def add_loss(self, losses, **kwargs):
        """Add loss tensor(s), potentially dependent on layer inputs.

        Some losses (for instance, activity regularization losses) may be
        dependent on the inputs passed when calling a layer. Hence, when reusing
        the same layer on different inputs `a` and `b`, some entries in
        `layer.losses` may be dependent on `a` and some on `b`. This method
        automatically keeps track of dependencies.

        This method can be used inside a subclassed layer or model's `call`
        function, in which case `losses` should be a Tensor or list of Tensors.

        Example:

        ```python
        class MyLayer(tf.keras.layers.Layer):
          def call(self, inputs):
            self.add_loss(tf.abs(tf.reduce_mean(inputs)))
            return inputs
        ```

        The same code works in distributed training: the input to `add_loss()`
        is treated like a regularization loss and averaged across replicas
        by the training loop (both built-in `Model.fit()` and compliant custom
        training loops).

        The `add_loss` method can also be called directly on a Functional Model
        during construction. In this case, any loss Tensors passed to this Model
        must be symbolic and be able to be traced back to the model's `Input`s.
        These losses become part of the model's topology and are tracked in
        `get_config`.

        Example:

        ```python
        inputs = tf.keras.Input(shape=(10,))
        x = tf.keras.layers.Dense(10)(inputs)
        outputs = tf.keras.layers.Dense(1)(x)
        model = tf.keras.Model(inputs, outputs)
        # Activity regularization.
        model.add_loss(tf.abs(tf.reduce_mean(x)))
        ```

        If this is not the case for your loss (if, for example, your loss
        references a `Variable` of one of the model's layers), you can wrap your
        loss in a zero-argument lambda. These losses are not tracked as part of
        the model's topology since they can't be serialized.

        Example:

        ```python
        inputs = tf.keras.Input(shape=(10,))
        d = tf.keras.layers.Dense(10)
        x = d(inputs)
        outputs = tf.keras.layers.Dense(1)(x)
        model = tf.keras.Model(inputs, outputs)
        # Weight regularization.
        model.add_loss(lambda: tf.reduce_mean(d.kernel))
        ```

        Args:
          losses: Loss tensor, or list/tuple of tensors. Rather than tensors,
            losses may also be zero-argument callables which create a loss
            tensor.
          **kwargs: Used for backwards compatibility only.
        """
    @property
    def metrics(self):
        """List of metrics added using the `add_metric()` API.

        Example:

        >>> input = tf.keras.layers.Input(shape=(3,))
        >>> d = tf.keras.layers.Dense(2)
        >>> output = d(input)
        >>> d.add_metric(tf.reduce_max(output), name='max')
        >>> d.add_metric(tf.reduce_min(output), name='min')
        >>> [m.name for m in d.metrics]
        ['max', 'min']

        Returns:
          A list of `Metric` objects.
        """
    def add_metric(self, value, name: Incomplete | None = None, **kwargs) -> None:
        """Adds metric tensor to the layer.

        This method can be used inside the `call()` method of a subclassed layer
        or model.

        ```python
        class MyMetricLayer(tf.keras.layers.Layer):
          def __init__(self):
            super(MyMetricLayer, self).__init__(name='my_metric_layer')
            self.mean = tf.keras.metrics.Mean(name='metric_1')

          def call(self, inputs):
            self.add_metric(self.mean(inputs))
            self.add_metric(tf.reduce_sum(inputs), name='metric_2')
            return inputs
        ```

        This method can also be called directly on a Functional Model during
        construction. In this case, any tensor passed to this Model must
        be symbolic and be able to be traced back to the model's `Input`s. These
        metrics become part of the model's topology and are tracked when you
        save the model via `save()`.

        ```python
        inputs = tf.keras.Input(shape=(10,))
        x = tf.keras.layers.Dense(10)(inputs)
        outputs = tf.keras.layers.Dense(1)(x)
        model = tf.keras.Model(inputs, outputs)
        model.add_metric(math_ops.reduce_sum(x), name='metric_1')
        ```

        Note: Calling `add_metric()` with the result of a metric object on a
        Functional Model, as shown in the example below, is not supported. This
        is because we cannot trace the metric result tensor back to the model's
        inputs.

        ```python
        inputs = tf.keras.Input(shape=(10,))
        x = tf.keras.layers.Dense(10)(inputs)
        outputs = tf.keras.layers.Dense(1)(x)
        model = tf.keras.Model(inputs, outputs)
        model.add_metric(tf.keras.metrics.Mean()(x), name='metric_1')
        ```

        Args:
          value: Metric tensor.
          name: String metric name.
          **kwargs: Additional keyword arguments for backward compatibility.
            Accepted values:
            `aggregation` - When the `value` tensor provided is not the result
            of calling a `keras.Metric` instance, it will be aggregated by
            default using a `keras.Metric.Mean`.
        """
    def add_update(self, updates) -> None:
        """Add update op(s), potentially dependent on layer inputs.

        Weight updates (for instance, the updates of the moving mean and
        variance in a BatchNormalization layer) may be dependent on the inputs
        passed when calling a layer. Hence, when reusing the same layer on
        different inputs `a` and `b`, some entries in `layer.updates` may be
        dependent on `a` and some on `b`. This method automatically keeps track
        of dependencies.

        This call is ignored when eager execution is enabled (in that case,
        variable updates are run on the fly and thus do not need to be tracked
        for later execution).

        Args:
          updates: Update op, or list/tuple of update ops, or zero-arg callable
            that returns an update op. A zero-arg callable should be passed in
            order to disable running the updates by setting `trainable=False`
            on this Layer, when executing in Eager mode.
        """
    def set_weights(self, weights) -> None:
        """Sets the weights of the layer, from NumPy arrays.

        The weights of a layer represent the state of the layer. This function
        sets the weight values from numpy arrays. The weight values should be
        passed in the order they are created by the layer. Note that the layer's
        weights must be instantiated before calling this function, by calling
        the layer.

        For example, a `Dense` layer returns a list of two values: the kernel
        matrix and the bias vector. These can be used to set the weights of
        another `Dense` layer:

        >>> layer_a = tf.keras.layers.Dense(1,
        ...   kernel_initializer=tf.constant_initializer(1.))
        >>> a_out = layer_a(tf.convert_to_tensor([[1., 2., 3.]]))
        >>> layer_a.get_weights()
        [array([[1.],
               [1.],
               [1.]], dtype=float32), array([0.], dtype=float32)]
        >>> layer_b = tf.keras.layers.Dense(1,
        ...   kernel_initializer=tf.constant_initializer(2.))
        >>> b_out = layer_b(tf.convert_to_tensor([[10., 20., 30.]]))
        >>> layer_b.get_weights()
        [array([[2.],
               [2.],
               [2.]], dtype=float32), array([0.], dtype=float32)]
        >>> layer_b.set_weights(layer_a.get_weights())
        >>> layer_b.get_weights()
        [array([[1.],
               [1.],
               [1.]], dtype=float32), array([0.], dtype=float32)]

        Args:
          weights: a list of NumPy arrays. The number
            of arrays and their shape must match
            number of the dimensions of the weights
            of the layer (i.e. it should match the
            output of `get_weights`).

        Raises:
          ValueError: If the provided weights list does not match the
            layer's specifications.
        """
    def get_weights(self):
        """Returns the current weights of the layer, as NumPy arrays.

        The weights of a layer represent the state of the layer. This function
        returns both trainable and non-trainable weight values associated with
        this layer as a list of NumPy arrays, which can in turn be used to load
        state into similarly parameterized layers.

        For example, a `Dense` layer returns a list of two values: the kernel
        matrix and the bias vector. These can be used to set the weights of
        another `Dense` layer:

        >>> layer_a = tf.keras.layers.Dense(1,
        ...   kernel_initializer=tf.constant_initializer(1.))
        >>> a_out = layer_a(tf.convert_to_tensor([[1., 2., 3.]]))
        >>> layer_a.get_weights()
        [array([[1.],
               [1.],
               [1.]], dtype=float32), array([0.], dtype=float32)]
        >>> layer_b = tf.keras.layers.Dense(1,
        ...   kernel_initializer=tf.constant_initializer(2.))
        >>> b_out = layer_b(tf.convert_to_tensor([[10., 20., 30.]]))
        >>> layer_b.get_weights()
        [array([[2.],
               [2.],
               [2.]], dtype=float32), array([0.], dtype=float32)]
        >>> layer_b.set_weights(layer_a.get_weights())
        >>> layer_b.get_weights()
        [array([[1.],
               [1.],
               [1.]], dtype=float32), array([0.], dtype=float32)]

        Returns:
            Weights values as a list of NumPy arrays.
        """
    def finalize_state(self) -> None:
        """Finalizes the layers state after updating layer weights.

        This function can be subclassed in a layer and will be called after
        updating a layer weights. It can be overridden to finalize any
        additional layer state after a weight update.

        This function will be called after weights of a layer have been restored
        from a loaded model.
        """
    def get_input_mask_at(self, node_index):
        """Retrieves the input mask tensor(s) of a layer at a given node.

        Args:
            node_index: Integer, index of the node
                from which to retrieve the attribute.
                E.g. `node_index=0` will correspond to the
                first time the layer was called.

        Returns:
            A mask tensor
            (or list of tensors if the layer has multiple inputs).
        """
    def get_output_mask_at(self, node_index):
        """Retrieves the output mask tensor(s) of a layer at a given node.

        Args:
            node_index: Integer, index of the node
                from which to retrieve the attribute.
                E.g. `node_index=0` will correspond to the
                first time the layer was called.

        Returns:
            A mask tensor
            (or list of tensors if the layer has multiple outputs).
        """
    @property
    def input_mask(self):
        """Retrieves the input mask tensor(s) of a layer.

        Only applicable if the layer has exactly one inbound node,
        i.e. if it is connected to one incoming layer.

        Returns:
            Input mask tensor (potentially None) or list of input
            mask tensors.

        Raises:
            AttributeError: if the layer is connected to
            more than one incoming layers.
        """
    @property
    def output_mask(self):
        """Retrieves the output mask tensor(s) of a layer.

        Only applicable if the layer has exactly one inbound node,
        i.e. if it is connected to one incoming layer.

        Returns:
            Output mask tensor (potentially None) or list of output
            mask tensors.

        Raises:
            AttributeError: if the layer is connected to
            more than one incoming layers.
        """
    def get_input_shape_at(self, node_index):
        """Retrieves the input shape(s) of a layer at a given node.

        Args:
            node_index: Integer, index of the node
                from which to retrieve the attribute.
                E.g. `node_index=0` will correspond to the
                first time the layer was called.

        Returns:
            A shape tuple
            (or list of shape tuples if the layer has multiple inputs).

        Raises:
          RuntimeError: If called in Eager mode.
        """
    def get_output_shape_at(self, node_index):
        """Retrieves the output shape(s) of a layer at a given node.

        Args:
            node_index: Integer, index of the node
                from which to retrieve the attribute.
                E.g. `node_index=0` will correspond to the
                first time the layer was called.

        Returns:
            A shape tuple
            (or list of shape tuples if the layer has multiple outputs).

        Raises:
          RuntimeError: If called in Eager mode.
        """
    def get_input_at(self, node_index):
        """Retrieves the input tensor(s) of a layer at a given node.

        Args:
            node_index: Integer, index of the node
                from which to retrieve the attribute.
                E.g. `node_index=0` will correspond to the
                first input node of the layer.

        Returns:
            A tensor (or list of tensors if the layer has multiple inputs).

        Raises:
          RuntimeError: If called in Eager mode.
        """
    def get_output_at(self, node_index):
        """Retrieves the output tensor(s) of a layer at a given node.

        Args:
            node_index: Integer, index of the node
                from which to retrieve the attribute.
                E.g. `node_index=0` will correspond to the
                first output node of the layer.

        Returns:
            A tensor (or list of tensors if the layer has multiple outputs).

        Raises:
          RuntimeError: If called in Eager mode.
        """
    @property
    def input(self):
        """Retrieves the input tensor(s) of a layer.

        Only applicable if the layer has exactly one input,
        i.e. if it is connected to one incoming layer.

        Returns:
            Input tensor or list of input tensors.

        Raises:
          RuntimeError: If called in Eager mode.
          AttributeError: If no inbound nodes are found.
        """
    @property
    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only applicable if the layer has exactly one output,
        i.e. if it is connected to one incoming layer.

        Returns:
          Output tensor or list of output tensors.

        Raises:
          AttributeError: if the layer is connected to more than one incoming
            layers.
          RuntimeError: if called in Eager mode.
        """
    @property
    def input_shape(self):
        """Retrieves the input shape(s) of a layer.

        Only applicable if the layer has exactly one input,
        i.e. if it is connected to one incoming layer, or if all inputs
        have the same shape.

        Returns:
            Input shape, as an integer shape tuple
            (or list of shape tuples, one tuple per input tensor).

        Raises:
            AttributeError: if the layer has no defined input_shape.
            RuntimeError: if called in Eager mode.
        """
    def count_params(self):
        """Count the total number of scalars composing the weights.

        Returns:
            An integer count.

        Raises:
            ValueError: if the layer isn't yet built
              (in which case its weights aren't yet defined).
        """
    @property
    def output_shape(self):
        """Retrieves the output shape(s) of a layer.

        Only applicable if the layer has one output,
        or if all outputs have the same shape.

        Returns:
            Output shape, as an integer shape tuple
            (or list of shape tuples, one tuple per output tensor).

        Raises:
            AttributeError: if the layer has no defined output shape.
            RuntimeError: if called in Eager mode.
        """
    @property
    def dtype_policy(self):
        """The dtype policy associated with this layer.

        This is an instance of a `tf.keras.mixed_precision.Policy`.
        """
    @property
    def compute_dtype(self):
        """The dtype of the layer's computations.

        This is equivalent to `Layer.dtype_policy.compute_dtype`. Unless
        mixed precision is used, this is the same as `Layer.dtype`, the dtype of
        the weights.

        Layers automatically cast their inputs to the compute dtype, which
        causes computations and the output to be in the compute dtype as well.
        This is done by the base Layer class in `Layer.__call__`, so you do not
        have to insert these casts if implementing your own layer.

        Layers often perform certain internal computations in higher precision
        when `compute_dtype` is float16 or bfloat16 for numeric stability. The
        output will still typically be float16 or bfloat16 in such cases.

        Returns:
          The layer's compute dtype.
        """
    @property
    def variable_dtype(self):
        """Alias of `Layer.dtype`, the dtype of the weights."""
    @property
    def inbound_nodes(self):
        """Return Functional API nodes upstream of this layer."""
    @property
    def outbound_nodes(self):
        """Return Functional API nodes downstream of this layer."""
    @property
    def variables(self):
        """Returns the list of all layer variables/weights.

        Alias of `self.weights`.

        Note: This will not track the weights of nested `tf.Modules` that are
        not themselves Keras layers.

        Returns:
          A list of variables.
        """
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    def add_variable(self, *args, **kwargs):
        """Deprecated, do NOT use! Alias for `add_weight`."""
    def get_build_config(self): ...
    def build_from_config(self, config) -> None: ...
    def __delattr__(self, name) -> None: ...
    def __setattr__(self, name, value): ...

class TensorFlowOpLayer(Layer):
    """Wraps a TensorFlow Operation in a Layer.

    This class is used internally by the Functional API. When a user
    uses a raw TensorFlow Operation on symbolic tensors originating
    from an `Input` Layer, the resultant operation will be wrapped
    with this Layer object in order to make the operation compatible
    with the Keras API.

    This Layer will create a new, identical operation (except for inputs
    and outputs) every time it is called. If `run_eagerly` is `True`,
    the op creation and calculation will happen inside an Eager function.

    Instances of this Layer are created when `autolambda` is called, which
    is whenever a Layer's `__call__` encounters symbolic inputs that do
    not have Keras metadata, or when a Network's `__init__` encounters
    outputs that do not have Keras metadata.

    Attributes:
      node_def: String, the serialized NodeDef of the Op this layer will wrap.
      name: String, the name of the Layer.
      constants: Dict of NumPy arrays, the values of any Tensors needed for this
        Operation that do not originate from a Keras `Input` Layer. Since all
        placeholders must come from Keras `Input` Layers, these Tensors must be
        treated as constant in the Functional API.
      trainable: Bool, whether this Layer is trainable. Currently Variables are
        not supported, and so this parameter has no effect.
      dtype: The default dtype of this Layer. Inherited from `Layer` and has no
        effect on this class, however is used in `get_config`.
    """
    node_def: Incomplete
    constants: Incomplete
    built: bool
    def __init__(self, node_def, name, constants: Incomplete | None = None, trainable: bool = True, dtype: Incomplete | None = None) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class AddLoss(Layer):
    """Adds its inputs as a loss.

    Attributes:
      unconditional: Whether or not the loss should be conditioned on the
        inputs.
    """
    unconditional: Incomplete
    def __init__(self, unconditional, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class AddMetric(Layer):
    """Adds its inputs as a metric.

    Attributes:
      aggregation: 'mean' or None. How the inputs should be aggregated.
      metric_name: The name to use for this metric.
    """
    aggregation: Incomplete
    metric_name: Incomplete
    def __init__(self, aggregation: Incomplete | None = None, metric_name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class BaseRandomLayer(Layer):
    """A layer handle the random number creation and savemodel behavior."""
    def __init__(self, seed: Incomplete | None = None, force_generator: bool = False, rng_type: Incomplete | None = None, **kwargs) -> None:
        '''Initialize the BaseRandomLayer.

        Note that the constructor is annotated with
        @no_automatic_dependency_tracking. This is to skip the auto
        tracking of self._random_generator instance, which is an AutoTrackable.
        The backend.RandomGenerator could contain a tf.random.Generator instance
        which will have tf.Variable as the internal state. We want to avoid
        saving that state into model.weights and checkpoints for backward
        compatibility reason. In the meantime, we still need to make them
        visible to SavedModel when it is tracing the tf.function for the
        `call()`.
        See _list_extra_dependencies_for_serialization below for more details.

        Args:
          seed: optional integer, used to create RandomGenerator.
          force_generator: boolean, default to False, whether to force the
            RandomGenerator to use the code branch of tf.random.Generator.
          rng_type: string, the rng type that will be passed to backend
            RandomGenerator. Default to `None`, which will allow RandomGenerator
            to choose types by itself. Valid values are "stateful", "stateless",
            "legacy_stateful".
          **kwargs: other keyword arguments that will be passed to the parent
            *class
        '''
    def build(self, input_shape) -> None: ...
