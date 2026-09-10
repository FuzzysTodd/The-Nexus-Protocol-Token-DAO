from _typeshed import Incomplete
from tensorflow.core.protobuf.tpu import optimization_parameters_pb2 as optimization_parameters_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, partitioned_variables as partitioned_variables, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple, Optional

TRAINING: Incomplete
INFERENCE: Incomplete

class TableConfig(NamedTuple('TableConfig', [('vocabulary_size', Incomplete), ('dimension', Incomplete), ('initializer', Incomplete), ('combiner', Incomplete), ('hot_id_replication', Incomplete), ('learning_rate', Incomplete), ('learning_rate_fn', Incomplete), ('optimization_parameters', Incomplete)])):
    """Embedding table configuration."""
    def __new__(cls, vocabulary_size, dimension, initializer: Incomplete | None = None, combiner: str = 'mean', hot_id_replication: bool = False, learning_rate: Incomplete | None = None, learning_rate_fn: Incomplete | None = None, optimization_parameters: Incomplete | None = None):
        """Embedding table configuration.

    Args:
      vocabulary_size: Number of vocabulary (/rows) in the table.
      dimension: The embedding dimension.
      initializer: A variable initializer function to be used in embedding
        variable initialization. If not specified, defaults to
        `tf.compat.v1.truncated_normal_initializer` with mean `0.0` and standard
        deviation `1/sqrt(dimension)`.
      combiner: A string specifying how to reduce if there are multiple entries
        in a single row. Currently 'mean', 'sqrtn', 'sum' and None are
        supported, with 'mean' the default. 'sqrtn' often achieves good
        accuracy, in particular with bag-of-words columns. For more information,
        see `tf.nn.embedding_lookup_sparse`. None is only valid for dense rather
        than sparse tensors.
      hot_id_replication: If true, enables hot id replication, which can make
        embedding lookups faster if there are some hot rows in the table.
      learning_rate: float, static learning rate for this table. If
        learning_rate and learning_rate_fn are both `None`, static learning rate
        as specified in local `optimization_parameters` will be used. In case
        local `optimization_parameters` is `None`, global
        `optimization_parameters` in `TPUEmbedding` constructor will be used.
        `learning_rate_fn` must be `None` if `learning_rate` is not `None.
      learning_rate_fn: string, use dynamic learning rate given by the function.
        This function will be passed the current global step. If learning_rate
        and learning_rate_fn are both `None`, static learning rate as specified
        in `optimization_parameters` is used. `learning_rate` must be `None` if
        `learning_rate_fn` is not `None.
      optimization_parameters: `AdagradParameters`, `AdamParameters`,
        `Stochasticgradientdescentparameters`. Specifies table level optimizer.
        If it's `None` global optimizer in `TPUEmbedding` constructor is used.

    Returns:
      `TableConfig`.

    Raises:
      ValueError: if `vocabulary_size` is not positive integer.
      ValueError: if `dimension` is not positive integer.
      ValueError: if `initializer` is specified and is not callable.
      ValueError: if `combiner` is not supported.
      ValueError: if `learning_rate` and `learning_rate_fn` are both not
        `None`.
    """

class FeatureConfig(NamedTuple('FeatureConfig', [('table_id', Incomplete), ('max_sequence_length', Incomplete), ('weight_key', Incomplete)])):
    """Feature configuration."""
    def __new__(cls, table_id, max_sequence_length: int = 0, weight_key: Incomplete | None = None):
        """Feature configuration.

    Args:
      table_id: Which table the feature is uses for embedding lookups.
      max_sequence_length: If positive, the feature is a sequence feature with
        the corresponding maximum sequence length. If the sequence is longer
        than this, it will be truncated. If 0, the feature is not a sequence
        feature.
      weight_key: If using weights for the combiner, this key specifies which
        input feature contains the weights.

    Returns:
      `FeatureConfig`.

    Raises:
      ValueError: if `max_sequence_length` non-integer or negative.
    """

class EnqueueData(NamedTuple('EnqueueData', [('embedding_indices', Incomplete), ('sample_indices', Incomplete), ('aggregation_weights', Incomplete)])):
    """Data to be enqueued through generate_enqueue_ops()."""
    def __new__(cls, embedding_indices, sample_indices: Incomplete | None = None, aggregation_weights: Incomplete | None = None):
        """Data to be enqueued through generate_enqueue_ops().

    Args:
      embedding_indices: A rank 1 Tensor, indices into the embedding tables. It
        corresponds to sp_ids.values in embedding_lookup_sparse(). Both int32
        and int64 are allowed and will be converted to int32 internally.
      sample_indices: A rank 2 Tensor specifying the training example to which
        the corresponding embedding_indices and aggregation_weights values
        belong. It corresponds to sp_ids.indices in embedding_lookup_sparse().
        If it is None, we assume each embedding_indices belongs to a different
        sample. Both int32 and int64 are allowed and will be converted to int32
        internally.
      aggregation_weights: A rank 1 Tensor containing aggregation weights. It
        corresponds to sp_weights.values in embedding_lookup_sparse(). If it is
        None, we assume all weights are 1. Both float32 and float64 are allowed
        and will be converted to float32 internally.

    Returns:
      An EnqueueData tuple.

    """
    @staticmethod
    def from_sparse_tensor(sp_tensor, weights: Incomplete | None = None): ...

class RaggedEnqueueData(NamedTuple('RaggedEnqueueData', [('embedding_indices', Incomplete), ('row_splits', Incomplete), ('aggregation_weights', Incomplete)])):
    """RaggedTensor Data to be enqueued through generate_enqueue_ops()."""
    def __new__(cls, embedding_indices, row_splits: Incomplete | None = None, aggregation_weights: Incomplete | None = None):
        """Data to be enqueued through generate_enqueue_ops().

    Args:
      embedding_indices: A rank 1 Tensor, indices into the embedding tables. It
        corresponds to ids.values in embedding_lookup(), when ids is a
        RaggedTensor. Both int32 and int64 are allowed and will be converted to
        int32 internally.
      row_splits: A rank 1 Tensor specifying the length of  the break points for
        splitting embedding_indices and aggregation_weights. It corresponds to
        ids.row_splits in embedding_lookup(), when ids is a RaggedTensor. Both
        int32 and int64 are allowed and will be converted to int32 internally.
      aggregation_weights: A rank 1 Tensor containing per training example
        aggregation weights. It corresponds to the values field of a
        RaggedTensor with the same row_splits as ids in embedding_lookup(), when
        ids is a RaggedTensor.

    Returns:
      An RaggedEnqueueData tuple.

    """
    @staticmethod
    def from_ragged_tensor(rg_tensor, weights: Incomplete | None = None): ...

def get_enqueue_datas_list_from_sparse_tensors_list(sp_tensors_list):
    """Convenient function for generate_enqueue_ops().

  Args:
    sp_tensors_list: a list of dictionary mapping from string of feature names
      to SparseTensor. Each dictionary is for one TPU core. Dictionaries for the
      same host should be contiguous on the list.

  Returns:
    enqueue_datas_list: a list of dictionary mapping from string
      of feature names to EnqueueData. Each dictionary is for one
      TPU core. Dictionaries for the same host should be contiguous
      on the list.

  """
def get_enqueue_datas_list_from_ragged_tensors_list(rg_tensors_list):
    """Convenient function for generate_enqueue_ops().

  Args:
    rg_tensors_list: a list of dictionary mapping from string of feature names
      to RaggedTensor. Each dictionary is for one TPU core. Dictionaries for the
      same host should be contiguous on the list.

  Returns:
    enqueue_datas_list: a list of dictionary mapping from string
      of feature names to RaggedEnqueueData. Each dictionary is for one
      TPU core. Dictionaries for the same host should be contiguous
      on the list.

  """

class AdamSlotVariableNames(NamedTuple):
    m: Incomplete
    v: Incomplete

class AdagradSlotVariableNames(NamedTuple):
    accumulator: Incomplete

class MomentumSlotVariableNames(NamedTuple):
    momenta: Incomplete

class AdagradMomentumSlotVariableNames(NamedTuple):
    accumulator: Incomplete
    momenta: Incomplete

class RMSPropSlotVariableNames(NamedTuple):
    ms: Incomplete
    mom: Incomplete

class ProximalAdagradSlotVariableNames(NamedTuple):
    accumulator: Incomplete

class FtrlSlotVariableNames(NamedTuple):
    accumulator: Incomplete
    linear: Incomplete

class ProximalYogiSlotVariableNames(NamedTuple):
    v: Incomplete
    m: Incomplete

class FrequencyEstimatorSlotVariableNames(NamedTuple):
    last_hit_step: Incomplete

class AdamSlotVariables(NamedTuple):
    m: Incomplete
    v: Incomplete

class MomentumSlotVariables(NamedTuple):
    momenta: Incomplete

class AdagradMomentumSlotVariables(NamedTuple):
    accumulator: Incomplete
    momenta: Incomplete

class RMSPropSlotVariables(NamedTuple):
    ms: Incomplete
    mom: Incomplete

class AdagradSlotVariables(NamedTuple):
    accumulator: Incomplete

class ProximalAdagradSlotVariables(NamedTuple):
    accumulator: Incomplete

class FtrlSlotVariable(NamedTuple):
    accumulator: Incomplete
    linear: Incomplete

class ProximalYogiSlotVariables(NamedTuple):
    v: Incomplete
    m: Incomplete

class FrequencyEstimatorSlotVariables(NamedTuple):
    last_hit_step: Incomplete

class VariablesAndOps(NamedTuple):
    embedding_variables_by_table: Incomplete
    slot_variables_by_table: Incomplete
    load_ops: Incomplete
    retrieve_ops: Incomplete

class _OptimizationParameters:
    """Parameters common to all optimizations."""
    learning_rate: Incomplete
    use_gradient_accumulation: Incomplete
    clip_weight_min: Incomplete
    clip_weight_max: Incomplete
    weight_decay_factor: Incomplete
    multiply_weight_decay_factor_by_learning_rate: Incomplete
    clip_gradient_min: Incomplete
    clip_gradient_max: Incomplete
    def __init__(self, learning_rate: float, use_gradient_accumulation: bool, clip_weight_min: Optional[float], clip_weight_max: Optional[float], weight_decay_factor: Optional[float], multiply_weight_decay_factor_by_learning_rate: Optional[bool], clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None: ...

class AdagradParameters(_OptimizationParameters):
    """Optimization parameters for Adagrad with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=tf.tpu.experimental.AdagradParameters(0.1),
          ...))
  ```

  """
    initial_accumulator: Incomplete
    def __init__(self, learning_rate: float, initial_accumulator: float = 0.1, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for Adagrad.

    Args:
      learning_rate: used for updating embedding table.
      initial_accumulator: initial accumulator for Adagrad.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class AdagradMomentumParameters(_OptimizationParameters):
    """Optimization parameters for Adagrad + Momentum with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=tf.tpu.experimental.AdagradMomentumParameters(0.1),
          ...))
  ```

  """
    momentum: Incomplete
    use_nesterov: Incomplete
    exponent: Incomplete
    beta2: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float, momentum: float, use_nesterov: bool = False, exponent: float = 2, beta2: float = 1, epsilon: float = 1e-10, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for Adagrad.

    Args:
      learning_rate: used for updating embedding table.
      momentum: Moving average parameter for the momentum accumulator.
      use_nesterov: Whether to use the Nesterov variant of momentum. See
        Sutskever et al., 2013.
      exponent: Exponent for the Adagrad accumulator.
      beta2: Moving average parameter for the Adagrad accumulator.
      epsilon: initial accumulator for Adagrad accumulator.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class ProximalAdagradParameters(_OptimizationParameters):
    """Optimization parameters for ProximalAdagrad with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.
  """
    initial_accumulator: Incomplete
    l1_regularization_strength: Incomplete
    l2_regularization_strength: Incomplete
    def __init__(self, learning_rate: float, initial_accumulator: float = 0.1, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for Adagrad.

    Args:
      learning_rate: used for updating embedding table.
      initial_accumulator: initial accumulator for Adagrad.
      l1_regularization_strength: A float value, must be greater than or equal
        to zero.
      l2_regularization_strength: A float value, must be greater than or equal
        to zero.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details. for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class AdamParameters(_OptimizationParameters):
    """Optimization parameters for Adam with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=tf.tpu.experimental.AdamParameters(0.1),
          ...))
  ```

  """
    beta1: Incomplete
    beta2: Incomplete
    epsilon: Incomplete
    lazy_adam: Incomplete
    sum_inside_sqrt: Incomplete
    def __init__(self, learning_rate: float, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, lazy_adam: bool = True, sum_inside_sqrt: bool = True, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for Adam.

    Args:
      learning_rate: a floating point value. The learning rate.
      beta1: A float value. The exponential decay rate for the 1st moment
        estimates.
      beta2: A float value. The exponential decay rate for the 2nd moment
        estimates.
      epsilon: A small constant for numerical stability.
      lazy_adam: Use lazy Adam instead of Adam. Lazy Adam trains faster. See
        `optimization_parameters.proto` for details.
      sum_inside_sqrt: This improves training speed. Please see
        `optimization_parameters.proto` for details.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class FtrlParameters(_OptimizationParameters):
    """Optimization parameters for Ftrl with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=tf.tpu.experimental.FtrlParameters(0.1),
          ...))
  ```

  """
    learning_rate_power: Incomplete
    initial_accumulator_value: Incomplete
    initial_linear_value: float
    l1_regularization_strength: Incomplete
    l2_regularization_strength: Incomplete
    multiply_linear_by_learning_rate: Incomplete
    beta: Incomplete
    allow_zero_accumulator: Incomplete
    def __init__(self, learning_rate: float, learning_rate_power: float = -0.5, initial_accumulator_value: float = 0.1, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, multiply_linear_by_learning_rate: bool = False, beta: float = 0, allow_zero_accumulator: bool = False, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for Ftrl.

    Implements FTRL as described in the following [paper](
    https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41159.pdf)

    Args:
      learning_rate: a floating point value. The learning rate.
      learning_rate_power: A float value, must be less or equal to zero.
        Controls how the learning rate decreases during training. Use zero for a
        fixed learning rate. See section 3.1 in the
        [paper](https://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf).
      initial_accumulator_value: The starting value for accumulators. Only zero
        or positive values are allowed.
      l1_regularization_strength: A float value, must be greater than or equal
        to zero.
      l2_regularization_strength: A float value, must be greater than or equal
        to zero.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details. for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      multiply_linear_by_learning_rate: When true, multiplies the usages of the
        linear slot in the weight update by the learning rate. This is useful
        when ramping up learning rate from 0 (which would normally produce
        NaNs).
      beta: The beta parameter for FTRL.
      allow_zero_accumulator: Changes the implementation of the square root to
        allow for the case of initial_accumulator_value being zero. This will
        cause a slight performance drop.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class ProximalYogiParameters(_OptimizationParameters):
    """Optimization parameters for Proximal Yogi with TPU embeddings.

  Implements the Yogi optimizer as described in
  [Adaptive Methods for Nonconvex
  Optimization](https://papers.nips.cc/paper/8186-adaptive-methods-for-nonconvex-optimization).

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.
  """
    beta1: Incomplete
    beta2: Incomplete
    epsilon: Incomplete
    l1_regularization_strength: Incomplete
    l2_regularization_strength: Incomplete
    initial_accumulator_value: Incomplete
    def __init__(self, learning_rate: float = 0.01, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 0.001, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, initial_accumulator_value: float = 1e-06, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for Proximal Yogi.

    Args:
      learning_rate: a floating point value. The learning rate.
      beta1: A float value. The exponential decay rate for the 1st moment
        estimates.
      beta2: A float value. The exponential decay rate for the 2nd moment
        estimates.
      epsilon: A small constant for numerical stability.
      l1_regularization_strength: A float value, must be greater than or equal
        to zero.
      l2_regularization_strength: A float value, must be greater than or equal
        to zero.
      initial_accumulator_value: The starting value for accumulators. Only zero
        or positive values are allowed.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details. for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class MomentumParameters(_OptimizationParameters):
    """Optimization parameters for Momentum with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=tf.tpu.experimental.MomentumParameters(0.1),
          ...))
  ```

  """
    momentum: Incomplete
    use_nesterov: Incomplete
    def __init__(self, learning_rate: float, momentum: float, use_nesterov: bool = False, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        '''Optimization parameters for momentum.

    Args:
      learning_rate: a floating point value. The learning rate.
      momentum: a floating point value.  The momentum.
      use_nesterov: If `True` use Nesterov Momentum. See (Sutskever et al.,
        2013). This implementation always computes gradients at the value of the
        variable(s) passed to the optimizer. Using Nesterov Momentum makes the
        variable(s) track the values called `theta_t + mu*v_t` in the paper.
        This implementation is an approximation of the original formula, valid
        for high values of momentum. It will compute the "adjusted gradient" in
        NAG by assuming that the new gradient will be estimated by the current
        average gradient plus the product of momentum and the change in the
        average gradient.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    '''

class RMSPropParameters(_OptimizationParameters):
    """Optimization parameters for RMSProp with TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=tf.tpu.experimental.MomentumParameters(0.1),
          ...))
  ```

  """
    rho: Incomplete
    momentum: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float, rho: float, momentum: float, epsilon: float, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for RMS prop.

    Args:
      learning_rate: a floating point value. The learning rate.
      rho: Discounting factor for the history/coming gradient
      momentum: A scalar tensor.
      epsilon: Small value to avoid zero denominator.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details. for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
        Gradient accumulation must be set to true if this is set.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
        Gradient accumulation must be set to true if this is set.
    """

class StochasticGradientDescentParameters(_OptimizationParameters):
    """Optimization parameters for stochastic gradient descent for TPU embeddings.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=(
              tf.tpu.experimental.StochasticGradientDescentParameters(0.1))))
  ```

  """
    def __init__(self, learning_rate: float, use_gradient_accumulation: bool = True, clip_weight_min: Optional[float] = None, clip_weight_max: Optional[float] = None, weight_decay_factor: Optional[float] = None, multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None, clip_gradient_min: Optional[float] = None, clip_gradient_max: Optional[float] = None) -> None:
        """Optimization parameters for stochastic gradient descent.

    Args:
      learning_rate: a floating point value. The learning rate.
      use_gradient_accumulation: setting this to `False` makes embedding
        gradients calculation less accurate but faster. Please see
        `optimization_parameters.proto` for details.
      clip_weight_min: the minimum value to clip by; None means -infinity.
      clip_weight_max: the maximum value to clip by; None means +infinity.
      weight_decay_factor: amount of weight decay to apply; None means that the
        weights are not decayed.
      multiply_weight_decay_factor_by_learning_rate: if true,
        `weight_decay_factor` is multiplied by the current learning rate.
      clip_gradient_min: the minimum value to clip by; None means -infinity.
      clip_gradient_max: the maximum value to clip by; None means +infinity.
    """

class FrequencyEstimatorParameters(_OptimizationParameters):
    """Optimization parameters for Frequency Estimator TPU embeddings.

  This is a non-standard optimizer, which returns the estimated frequency of
  lookup for the feature passed to it. It should only be used on a table of
  width 1. The gradient fed back to the TPU embedding should always be zero.
  This can be acomplished via using `tf.stop_gradients` on the feature before
  using it.

  You must use the dynamic learning rate mechanism to set the 'learning rate'
  for this table to be the a float32 cast of the global training step counter.

  See `tensorflow/core/protobuf/tpu/optimization_parameters.proto` for more
  details on this optimizer.

  Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
  `optimization_parameters` argument to set the optimizer and its parameters.
  See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
  for more details.

  ```
  estimator = tf.estimator.tpu.TPUEstimator(
      ...
      embedding_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          ...
          optimization_parameters=FrequencyEstimatorParameters(0.1),
          ...))
  ```

  """
    tau: Incomplete
    max_delta: Incomplete
    outlier_threshold: Incomplete
    weight_exponent: Incomplete
    def __init__(self, tau: float, max_delta: float, outlier_threshold: float, weight_exponent: float) -> None:
        """Optimization parameters for frequency estimator.

    Args:
      tau: Learning rate between (0, 1) that is used to update the array.
      max_delta: Maximum value of delta, the difference between the current
        global step and the last global step at which the row was sampled.
      outlier_threshold: Threshold used to determine whether the current update
        is an outlier.
      weight_exponent: The weight exponent used to transform the estimated delta
        into weights.
    """

class DeviceConfig(NamedTuple):
    num_hosts: Incomplete
    num_cores: Incomplete
    job_name: Incomplete

class TPUEmbedding:
    """API for using TPU for embedding.

    Example:
    ```
    table_config_user = tpu_embedding.TableConfig(
        vocabulary_size=4, dimension=2,
        initializer=initializer, combiner='mean')
    table_to_config_dict = {'video': table_config_video,
                          'user': table_config_user}
    feature_to_config_dict = {'watched': tpu_embedding.FeatureConfig('video'),
                              'favorited': tpu_embedding.FeatureConfig('video'),
                              'friends': tpu_embedding.FeatureConfig('user')}
    batch_size = 4
    num_hosts = 1
    optimization_parameters = tpu_embedding.AdagradParameters(1., 1.)
    mode = tpu_embedding.TRAINING
    embedding = tpu_embedding.TPUEmbedding(
        table_to_config_dict, feature_to_config_dict,
        batch_size, num_hosts, mode, optimization_parameters)

    batch_size_per_core = embedding.batch_size_per_core
    sparse_features_list = []
    for host in hosts:
      with ops.device(host):
        for _ in range(embedding.num_cores_per_host):
          sparse_features = {}
          sparse_features['watched'] = sparse_tensor.SparseTensor(...)
          sparse_features['favorited'] = sparse_tensor.SparseTensor(...)
          sparse_features['friends'] = sparse_tensor.SparseTensor(...)
          sparse_features_list.append(sparse_features)

    enqueue_ops = embedding.generate_enqueue_ops(sparse_features_list)
    embedding_variables_and_ops = embedding.create_variables_and_ops()

    def computation():
      activations = embedding.get_activations()
      loss = compute_loss(activations)

      base_optimizer = gradient_descent.GradientDescentOptimizer(
          learning_rate=1)
      cross_shard_optimizer = tpu_optimizer.CrossShardOptimizer(
          base_optimizer)

      train_op = cross_shard_optimizer.minimize(loss)
      gradients = (
          tpu_embedding_gradient.get_gradients_through_compute_gradients(
              cross_shard_optimizer, loss, activations)
      send_gradients_op = embedding.generate_send_gradients_op(gradients)
      with ops.control_dependencies([train_op, send_gradients_op]):
        loss = array_ops.identity(loss)

    loss = tpu.shard(computation,
                     num_shards=embedding.num_cores)

    with self.test_session() as sess:
      sess.run(tpu.initialize_system(embedding_config=
                                     embedding.config_proto))
      sess.run(variables.global_variables_initializer())
      sess.run(embedding_variables_and_ops.load_ops())
      sess.run(enqueue_ops)
      loss_val = sess.run(loss)
    ```

  Example with weight decay:

  >>> def learning_rate_fn(global_step):
  ...   return tf.compat.v1.train.polynomial_decay(
  ...     learning_rate=5e-5,
  ...     global_step=global_step,
  ...     decay_steps=100000,
  ...     end_learning_rate=0.0)
  >>> wordpiece_table_config = TableConfig(
  ...   vocabulary_size=119547,
  ...   dimension=256,
  ...   learning_rate_fn=learning_rate_fn)
  >>> wordpiece_feature_config = FeatureConfig(
  ...   table_id='bert/embeddings/word_embeddings',
  ...   max_sequence_length=512)
  >>> optimization_parameters = AdamParameters(
  ...   learning_rate=5e-5,
  ...   epsilon=1e-6,
  ...   weight_decay_factor=0.01,
  ...   multiply_weight_decay_factor_by_learning_rate=True)
  >>> tpu_embedding = TPUEmbedding(
  ...  table_to_config_dict={
  ...    'bert/embeddings/word_embeddings': wordpiece_table_config,
  ...  },
  ...  feature_to_config_dict={'input_ids': wordpiece_feature_config},
  ...  batch_size=128,
  ...  mode=TRAINING,
  ...  optimization_parameters=optimization_parameters,
  ...  master='')
  >>> with tf.Graph().as_default():
  ...   init_tpu_op = tf.compat.v1.tpu.initialize_system(
  ...     embedding_config=tpu_embedding.config_proto)
  ...   tf.compat.v1.Session().run(init_tpu_op)
  """
    def __init__(self, table_to_config_dict, feature_to_config_dict, batch_size, mode, master: Incomplete | None = None, optimization_parameters: Incomplete | None = None, cluster_def: Incomplete | None = None, pipeline_execution_with_tensor_core: bool = False, partition_strategy: str = 'div', profile_data_directory: Incomplete | None = None, device_config: Incomplete | None = None, master_job_name: Incomplete | None = None) -> None:
        """API for using TPU for embedding lookups.

    Args:
      table_to_config_dict: A dictionary mapping from string of table name to
        `TableConfig`. Table refers to an embedding table, e.g. `params`
        argument to `tf.nn.embedding_lookup_sparse()`.
      feature_to_config_dict: A dictionary mapping from string of feature name
        to `FeatureConfig`. Feature refers to ids to lookup in embedding table,
        e.g. `sp_ids` argument to `tf.nn.embedding_lookup_sparse()`.
      batch_size: An `int` representing the global batch size.
      mode: `TRAINING` or `INFERENCE`.
      master: A `string` representing the TensorFlow master to use.
      optimization_parameters: `AdagradParameters`, `AdamParameters`,
        `Stochasticgradientdescentparameters`. Must be set in training unless
        all tables specify their own optimizers. And it must be `None` in
        inference.
      cluster_def: A ClusterDef object describing the TPU cluster.
      pipeline_execution_with_tensor_core: setting this to `True` makes training
        faster, but trained model will be different if step N and step N+1
        involve the same set of embedding IDs. Please see
        `tpu_embedding_configuration.proto` for details.
      partition_strategy: A string, either 'mod' or 'div', specifying how to map
        the lookup id to the embedding tensor. For more information see
        `tf.nn.embedding_lookup_sparse`.
      profile_data_directory: Directory where embedding lookup statistics are
        stored. These statistics summarize information about the inputs to the
        embedding lookup operation, in particular, the average number of
        embedding IDs per example and how well the embedding IDs are load
        balanced across the system. The lookup statistics are used during TPU
        initialization for embedding table partitioning. Collection of lookup
        statistics is done at runtime by  profiling the embedding inputs, only a
        small fraction of input samples are profiled to minimize host CPU
        overhead. Once a suitable number of samples are profiled, the lookup
        statistics are saved to table-specific files in the profile data
        directory generally at the end of a TPU training loop. The filename
        corresponding to each table is obtained by hashing table specific
        parameters (e.g., table name and number of features) and global
        configuration parameters (e.g., sharding strategy and task count). The
        same profile data directory can be shared among several models to reuse
        embedding lookup statistics.
      device_config: A DeviceConfig instance, used when `master` and
        `cluster_def` are both `None`.
      master_job_name: if set, overrides the master job name used to schedule
        embedding ops.

    Raises:
      ValueError: if any input is invalid.
    """
    @property
    def hosts(self):
        """A list of device names for CPU hosts.

    Returns:
      A list of device names for CPU hosts.
    """
    @property
    def num_cores_per_host(self):
        """Number of TPU cores on a CPU host.

    Returns:
      Number of TPU cores on a CPU host.
    """
    @property
    def num_cores(self):
        """Total number of TPU cores on all hosts.

    Returns:
      Total number of TPU cores on all hosts.
    """
    @property
    def batch_size_per_core(self):
        """Batch size for each TPU core.

    The sparse tensors in `sparse_features_list` to `generate_enqueue_ops`
       must have batch dimension equal to this.

    Returns:
      Batch size for each TPU core.
    """
    @property
    def config_proto(self):
        """Create embedding config proto for `tpu.initialize_system()`.

    Returns:
      an `TPUEmbeddingConfiguration` proto describing the desired
         configuration of the hardware embedding lookup tables, which
         is passed to `tpu.initialize_system()`.
    """
    @property
    def table_to_config_dict(self): ...
    @property
    def feature_to_config_dict(self): ...
    @property
    def table_to_features_dict(self): ...
    @property
    def optimization_parameters(self): ...
    def create_variables_and_ops(self, embedding_variable_name_by_table: Incomplete | None = None, slot_variable_names_by_table: Incomplete | None = None):
        """Create embedding and slot variables, with ops to load and retrieve them.

    N.B.: the retrieve embedding variables (including slot variables) ops are
    returned as lambda fn, as the call side might want to impose control
    dependencies between the TPU computation and retrieving actions. For
    example, the following code snippet ensures the TPU computation finishes
    first, and then we pull the variables back from TPU to CPU.

    ```
    updates_ops = []
    with ops.control_dependencies([loss]):
      for op_fn in retrieve_parameters_op_fns:
        update_ops.append(op_fn())
    ```

    Args:
      embedding_variable_name_by_table: A dictionary mapping from string of
        table name to string of embedding variable name. If `None`, defaults
        from `get_default_slot_variable_names()` will be used.
      slot_variable_names_by_table: A dictionary mapping from string of table
        name to `AdamSlotVariableNames`, `AdagradSlotVariableNames` etc. If
        `None`, defaults from `get_default_slot_variable_names()` will be used.

    Returns:
      `tpu_embedding.VariablesAndOps` with:
        A dictionary mapping from string of table name to embedding variables,
        A dictionary mapping from string of table name to AdagradSlotVariables,
         AdamSlotVariables etc with slot variables,
        A function which returns a list of ops to load embedding and slot
         variables from CPU to TPU.
        A function which returns a list of ops to retrieve embedding and slot
         variables from TPU to CPU.
    """
    def generate_enqueue_ops(self, enqueue_datas_list, mode_override: Incomplete | None = None, ragged: bool = False):
        """Generate enqueue ops.

    Args:
      enqueue_datas_list: a list of dictionary mapping from string of feature
        names to EnqueueData. Each dictionary is for one TPU core. Dictionaries
        for the same host should be contiguous in the list.
      mode_override: A string input that overrides the mode specified in the
        TPUEmbeddingConfiguration. Supported values are {'unspecified',
        'inference', 'training', 'backward_pass_only'}. When set to
        'unspecified', the mode set in TPUEmbeddingConfiguration is used,
        otherwise mode_override is used (optional).
      ragged: If True, creates RaggedTensor enqueue ops rather than
        SparseTensor.

    Returns:
      Ops to enqueue to TPU for embedding.
    """
    def get_activations(self):
        """Get activations for features.

    This should be called within `computation` that is passed to
      `tpu.replicate` and friends.

    Returns:
      A dictionary mapping from `String` of feature name to `Tensor`
        of activation.
    """
    def generate_send_gradients_op(self, feature_to_gradient_dict, step: Incomplete | None = None):
        """Send gradient to TPU embedding.

    Args:
      feature_to_gradient_dict: dict mapping feature names to gradient wrt
        activations.
      step: the current global step, used for dynamic learning rate.

    Returns:
      SendTPUEmbeddingGradients Op.

    Raises:
      RuntimeError: If `mode` is not `TRAINING`.
    """

class _OptimizerHandler:
    """Interface class for handling optimizer specific logic."""
    def __init__(self, optimization_parameters) -> None: ...
    def get_optimization_parameters(self): ...
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table) -> None: ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto) -> None: ...

class _AdagradHandler(_OptimizerHandler):
    """Handles Adagrad specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _AdagradMomentumHandler(_OptimizerHandler):
    """Handles Adagrad with Momentum specific logic.

  Creates slot variables and defines their initializers. Defines load/retrieve
  operations to be used for loading variables into TPU memory (from host memory)
  and retrieving variables from TPU memory (into host memory).
  """
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _ProximalAdagradHandler(_OptimizerHandler):
    """Handles ProximalAdagrad specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _AdamHandler(_OptimizerHandler):
    """Handles Adam specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _FtrlHandler(_OptimizerHandler):
    """Handles Ftrl specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _ProximalYogiHandler(_OptimizerHandler):
    """Handles Proximal Yogi specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _MomentumHandler(_OptimizerHandler):
    """Handles Momentum specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _RMSPropHandler(_OptimizerHandler):
    """Handles RMS prop specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _FrequencyEstimatorHandler(_OptimizerHandler):
    """Handles frequency estimator specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _StochasticGradientDescentHandler(_OptimizerHandler):
    """Handles stochastic gradient descent specific logic."""
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table) -> None: ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...
