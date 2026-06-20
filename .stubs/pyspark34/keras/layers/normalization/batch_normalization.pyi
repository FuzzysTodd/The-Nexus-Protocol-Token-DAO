from _typeshed import Incomplete
from keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.dtensor import utils as utils
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import control_flow_util as control_flow_util, tf_utils as tf_utils

class BatchNormalizationBase(Layer):
    '''Layer that normalizes its inputs.

    Batch normalization applies a transformation that maintains the mean output
    close to 0 and the output standard deviation close to 1.

    Importantly, batch normalization works differently during training and
    during inference.

    **During training** (i.e. when using `fit()` or when calling the layer/model
    with the argument `training=True`), the layer normalizes its output using
    the mean and standard deviation of the current batch of inputs. That is to
    say, for each channel being normalized, the layer returns
    `gamma * (batch - mean(batch)) / sqrt(var(batch) + epsilon) + beta`, where:

    - `epsilon` is small constant (configurable as part of the constructor
    arguments)
    - `gamma` is a learned scaling factor (initialized as 1), which
    can be disabled by passing `scale=False` to the constructor.
    - `beta` is a learned offset factor (initialized as 0), which
    can be disabled by passing `center=False` to the constructor.

    **During inference** (i.e. when using `evaluate()` or `predict()`) or when
    calling the layer/model with the argument `training=False` (which is the
    default), the layer normalizes its output using a moving average of the
    mean and standard deviation of the batches it has seen during training. That
    is to say, it returns
    `gamma * (batch - self.moving_mean) / sqrt(self.moving_var+epsilon) + beta`.

    `self.moving_mean` and `self.moving_var` are non-trainable variables that
    are updated each time the layer in called in training mode, as such:

    - `moving_mean = moving_mean * momentum + mean(batch) * (1 - momentum)`
    - `moving_var = moving_var * momentum + var(batch) * (1 - momentum)`

    As such, the layer will only normalize its inputs during inference
    *after having been trained on data that has similar statistics as the
    inference data*.

    Args:
      axis: Integer or a list of integers, the axis that should be normalized
        (typically the features axis). For instance, after a `Conv2D` layer with
        `data_format="channels_first"`, set `axis=1` in `BatchNormalization`.
      momentum: Momentum for the moving average.
      epsilon: Small float added to variance to avoid dividing by zero.
      center: If True, add offset of `beta` to normalized tensor. If False,
        `beta` is ignored.
      scale: If True, multiply by `gamma`. If False, `gamma` is not used. When
        the next layer is linear (also e.g. `nn.relu`), this can be disabled
        since the scaling will be done by the next layer.
      beta_initializer: Initializer for the beta weight.
      gamma_initializer: Initializer for the gamma weight.
      moving_mean_initializer: Initializer for the moving mean.
      moving_variance_initializer: Initializer for the moving variance.
      beta_regularizer: Optional regularizer for the beta weight.
      gamma_regularizer: Optional regularizer for the gamma weight.
      beta_constraint: Optional constraint for the beta weight.
      gamma_constraint: Optional constraint for the gamma weight.
      renorm: Whether to use [Batch Renormalization](
        https://arxiv.org/abs/1702.03275). This adds extra variables during
          training. The inference is the same for either value of this
          parameter.
      renorm_clipping: A dictionary that may map keys \'rmax\', \'rmin\', \'dmax\' to
        scalar `Tensors` used to clip the renorm correction. The correction `(r,
        d)` is used as `corrected_value = normalized_value * r + d`, with `r`
        clipped to [rmin, rmax], and `d` to [-dmax, dmax]. Missing rmax, rmin,
        dmax are set to inf, 0, inf, respectively.
      renorm_momentum: Momentum used to update the moving means and standard
        deviations with renorm. Unlike `momentum`, this affects training and
        should be neither too small (which would add noise) nor too large (which
        would give stale estimates). Note that `momentum` is still applied to
        get the means and variances for inference.
      fused: if `True`, use a faster, fused implementation, or raise a
        ValueError if the fused implementation cannot be used. If `None`, use
        the faster implementation if possible. If False, do not used the fused
        implementation. Note that in TensorFlow 1.x, the meaning of
        `fused=True` is different: if `False`, the layer uses the
        system-recommended implementation. You cannot use `fused=True` if a
        mask is passed in the `call()` method.
      trainable: Boolean, if `True` the variables will be marked as trainable.
      virtual_batch_size: An `int`. By default, `virtual_batch_size` is `None`,
        which means batch normalization is performed across the whole batch.
        When `virtual_batch_size` is not `None`, instead perform "Ghost Batch
        Normalization", which creates virtual sub-batches which are each
        normalized separately (with shared gamma, beta, and moving statistics).
        Must divide the actual batch size during execution.
      adjustment: A function taking the `Tensor` containing the (dynamic) shape
        of the input tensor and returning a pair (scale, bias) to apply to the
        normalized values (before gamma and beta), only during training. For
        example, if `axis=-1`,
          `adjustment = lambda shape: (
            tf.random.uniform(shape[-1:], 0.93, 1.07),
            tf.random.uniform(shape[-1:], -0.1, 0.1))` will scale the normalized
              value by up to 7% up or down, then shift the result by up to 0.1
              (with independent scaling and bias for each feature but shared
              across all examples), and finally apply gamma and/or beta. If
              `None`, no adjustment is applied. Cannot be specified if
              virtual_batch_size is specified.
      synchronized: If True, synchronizes the global batch statistics (mean and
        variance) for the layer across all devices at each training step in a
        distributed training strategy. If False, each replica uses its own
        local batch statistics. Only relevant when used inside a
        `tf.distribute` strategy.

    Call arguments:
      inputs: Input tensor (of any rank).
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode.
        - `training=True`: The layer will normalize its inputs using the mean
          and variance of the current batch of inputs.
        - `training=False`: The layer will normalize its inputs using the mean
          and variance of its moving statistics, learned during training.
      mask: Binary tensor of shape broadcastable to `inputs` tensor, indicating
        the positions for which the mean and variance should be computed.

    Input shape: Arbitrary. Use the keyword argument `input_shape` (tuple of
      integers, does not include the samples axis) when using this layer as the
      first layer in a model.

    Output shape: Same shape as input.

    Reference:
      - [Ioffe and Szegedy, 2015](https://arxiv.org/abs/1502.03167).
    '''
    axis: Incomplete
    synchronized: Incomplete
    momentum: Incomplete
    epsilon: Incomplete
    center: Incomplete
    scale: Incomplete
    beta_initializer: Incomplete
    gamma_initializer: Incomplete
    moving_mean_initializer: Incomplete
    moving_variance_initializer: Incomplete
    beta_regularizer: Incomplete
    gamma_regularizer: Incomplete
    beta_constraint: Incomplete
    gamma_constraint: Incomplete
    renorm: Incomplete
    virtual_batch_size: Incomplete
    adjustment: Incomplete
    supports_masking: bool
    fused: Incomplete
    renorm_clipping: Incomplete
    renorm_momentum: Incomplete
    def __init__(self, axis: int = -1, momentum: float = 0.99, epsilon: float = 0.001, center: bool = True, scale: bool = True, beta_initializer: str = 'zeros', gamma_initializer: str = 'ones', moving_mean_initializer: str = 'zeros', moving_variance_initializer: str = 'ones', beta_regularizer: Incomplete | None = None, gamma_regularizer: Incomplete | None = None, beta_constraint: Incomplete | None = None, gamma_constraint: Incomplete | None = None, renorm: bool = False, renorm_clipping: Incomplete | None = None, renorm_momentum: float = 0.99, fused: Incomplete | None = None, trainable: bool = True, virtual_batch_size: Incomplete | None = None, adjustment: Incomplete | None = None, name: Incomplete | None = None, synchronized: bool = False, **kwargs) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value) -> None: ...
    input_spec: Incomplete
    gamma: Incomplete
    beta: Incomplete
    moving_mean: Incomplete
    moving_variance: Incomplete
    moving_stddev: Incomplete
    renorm_mean: Incomplete
    renorm_stddev: Incomplete
    built: bool
    def build(self, input_shape): ...
    def call(self, inputs, training: Incomplete | None = None, mask: Incomplete | None = None): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class BatchNormalization(BatchNormalizationBase):
    '''Layer that normalizes its inputs.

    Batch normalization applies a transformation that maintains the mean output
    close to 0 and the output standard deviation close to 1.

    Importantly, batch normalization works differently during training and
    during inference.

    **During training** (i.e. when using `fit()` or when calling the layer/model
    with the argument `training=True`), the layer normalizes its output using
    the mean and standard deviation of the current batch of inputs. That is to
    say, for each channel being normalized, the layer returns
    `gamma * (batch - mean(batch)) / sqrt(var(batch) + epsilon) + beta`, where:

    - `epsilon` is small constant (configurable as part of the constructor
    arguments)
    - `gamma` is a learned scaling factor (initialized as 1), which
    can be disabled by passing `scale=False` to the constructor.
    - `beta` is a learned offset factor (initialized as 0), which
    can be disabled by passing `center=False` to the constructor.

    **During inference** (i.e. when using `evaluate()` or `predict()` or when
    calling the layer/model with the argument `training=False` (which is the
    default), the layer normalizes its output using a moving average of the
    mean and standard deviation of the batches it has seen during training. That
    is to say, it returns
    `gamma * (batch - self.moving_mean) / sqrt(self.moving_var+epsilon) + beta`.

    `self.moving_mean` and `self.moving_var` are non-trainable variables that
    are updated each time the layer in called in training mode, as such:

    - `moving_mean = moving_mean * momentum + mean(batch) * (1 - momentum)`
    - `moving_var = moving_var * momentum + var(batch) * (1 - momentum)`

    As such, the layer will only normalize its inputs during inference
    *after having been trained on data that has similar statistics as the
    inference data*.

    When `synchronized=True` is set and if this layer is used within a
    `tf.distribute` strategy, there will be an `allreduce` call
    to aggregate batch statistics across all replicas at every
    training step. Setting `synchronized` has no impact when the model is
    trained without specifying any distribution strategy.

    Example usage:

    ```python
    strategy = tf.distribute.MirroredStrategy()

    with strategy.scope():
      model = tf.keras.Sequential()
      model.add(tf.keras.layers.Dense(16))
      model.add(tf.keras.layers.BatchNormalization(synchronized=True))
    ```

    Args:
      axis: Integer, the axis that should be normalized (typically the features
        axis). For instance, after a `Conv2D` layer with
        `data_format="channels_first"`, set `axis=1` in `BatchNormalization`.
      momentum: Momentum for the moving average.
      epsilon: Small float added to variance to avoid dividing by zero.
      center: If True, add offset of `beta` to normalized tensor. If False,
        `beta` is ignored.
      scale: If True, multiply by `gamma`. If False, `gamma` is not used. When
        the next layer is linear (also e.g. `nn.relu`), this can be disabled
        since the scaling will be done by the next layer.
      beta_initializer: Initializer for the beta weight.
      gamma_initializer: Initializer for the gamma weight.
      moving_mean_initializer: Initializer for the moving mean.
      moving_variance_initializer: Initializer for the moving variance.
      beta_regularizer: Optional regularizer for the beta weight.
      gamma_regularizer: Optional regularizer for the gamma weight.
      beta_constraint: Optional constraint for the beta weight.
      gamma_constraint: Optional constraint for the gamma weight.
      synchronized: If True, synchronizes the global batch statistics (mean and
        variance) for the layer across all devices at each training step in a
        distributed training strategy. If False, each replica uses its own
        local batch statistics. Only relevant when used inside a
        `tf.distribute` strategy.

    Call arguments:
      inputs: Input tensor (of any rank).
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode.
        - `training=True`: The layer will normalize its inputs using the mean
          and variance of the current batch of inputs.
        - `training=False`: The layer will normalize its inputs using the mean
          and variance of its moving statistics, learned during training.

    Input shape:
      Arbitrary. Use the keyword argument `input_shape` (tuple of
      integers, does not include the samples axis) when using this layer as the
      first layer in a model.

    Output shape:
      Same shape as input.

    Reference:
      - [Ioffe and Szegedy, 2015](https://arxiv.org/abs/1502.03167).

    **About setting `layer.trainable = False` on a `BatchNormalization` layer:**

    The meaning of setting `layer.trainable = False` is to freeze the layer,
    i.e. its internal state will not change during training:
    its trainable weights will not be updated
    during `fit()` or `train_on_batch()`, and its state updates will not be run.

    Usually, this does not necessarily mean that the layer is run in inference
    mode (which is normally controlled by the `training` argument that can
    be passed when calling a layer). "Frozen state" and "inference mode"
    are two separate concepts.

    However, in the case of the `BatchNormalization` layer, **setting
    `trainable = False` on the layer means that the layer will be
    subsequently run in inference mode** (meaning that it will use
    the moving mean and the moving variance to normalize the current batch,
    rather than using the mean and variance of the current batch).

    This behavior has been introduced in TensorFlow 2.0, in order
    to enable `layer.trainable = False` to produce the most commonly
    expected behavior in the convnet fine-tuning use case.

    Note that:
      - Setting `trainable` on an model containing other layers will
        recursively set the `trainable` value of all inner layers.
      - If the value of the `trainable`
        attribute is changed after calling `compile()` on a model,
        the new value doesn\'t take effect for this model
        until `compile()` is called again.
    '''
    def __init__(self, axis: int = -1, momentum: float = 0.99, epsilon: float = 0.001, center: bool = True, scale: bool = True, beta_initializer: str = 'zeros', gamma_initializer: str = 'ones', moving_mean_initializer: str = 'zeros', moving_variance_initializer: str = 'ones', beta_regularizer: Incomplete | None = None, gamma_regularizer: Incomplete | None = None, beta_constraint: Incomplete | None = None, gamma_constraint: Incomplete | None = None, synchronized: bool = False, **kwargs) -> None: ...

class SyncBatchNormalization(BatchNormalizationBase):
    """Deprecated. Please use `tf.keras.layers.BatchNormalization` instead.

    Caution: `tf.keras.layers.experimental.SyncBatchNormalization` endpoint is
      deprecated and will be removed in a future release. Please use
      `tf.keras.layers.BatchNormalization` with parameter `synchronized`
      set to True
    """
    def __init__(self, axis: int = -1, momentum: float = 0.99, epsilon: float = 0.001, center: bool = True, scale: bool = True, beta_initializer: str = 'zeros', gamma_initializer: str = 'ones', moving_mean_initializer: str = 'zeros', moving_variance_initializer: str = 'ones', beta_regularizer: Incomplete | None = None, gamma_regularizer: Incomplete | None = None, beta_constraint: Incomplete | None = None, gamma_constraint: Incomplete | None = None, **kwargs) -> None: ...
