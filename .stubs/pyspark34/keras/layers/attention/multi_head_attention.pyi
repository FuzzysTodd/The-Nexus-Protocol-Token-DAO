from _typeshed import Incomplete
from keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine.base_layer import Layer as Layer
from keras.layers import activation as activation, core as core, regularization as regularization
from keras.utils import tf_utils as tf_utils

class MultiHeadAttention(Layer):
    '''MultiHeadAttention layer.

    This is an implementation of multi-headed attention as described in the
    paper "Attention is all you Need" (Vaswani et al., 2017).
    If `query`, `key,` `value` are the same, then
    this is self-attention. Each timestep in `query` attends to the
    corresponding sequence in `key`, and returns a fixed-width vector.

    This layer first projects `query`, `key` and `value`. These are
    (effectively) a list of tensors of length `num_attention_heads`, where the
    corresponding shapes are `(batch_size, <query dimensions>, key_dim)`,
    `(batch_size, <key/value dimensions>, key_dim)`,
    `(batch_size, <key/value dimensions>, value_dim)`.

    Then, the query and key tensors are dot-producted and scaled. These are
    softmaxed to obtain attention probabilities. The value tensors are then
    interpolated by these probabilities, then concatenated back to a single
    tensor.

    Finally, the result tensor with the last dimension as value_dim can take an
    linear projection and return.

    When using `MultiHeadAttention` inside a custom layer, the custom layer must
    implement its own `build()` method and call `MultiHeadAttention`\'s
    `_build_from_signature()` there.
    This enables weights to be restored correctly when the model is loaded.

    Examples:

    Performs 1D cross-attention over two sequence inputs with an attention mask.
    Returns the additional attention weights over heads.

    >>> layer = MultiHeadAttention(num_heads=2, key_dim=2)
    >>> target = tf.keras.Input(shape=[8, 16])
    >>> source = tf.keras.Input(shape=[4, 16])
    >>> output_tensor, weights = layer(target, source,
    ...                                return_attention_scores=True)
    >>> print(output_tensor.shape)
    (None, 8, 16)
    >>> print(weights.shape)
    (None, 2, 8, 4)

    Performs 2D self-attention over a 5D input tensor on axes 2 and 3.

    >>> layer = MultiHeadAttention(
    ...     num_heads=2, key_dim=2, attention_axes=(2, 3))
    >>> input_tensor = tf.keras.Input(shape=[5, 3, 4, 16])
    >>> output_tensor = layer(input_tensor, input_tensor)
    >>> print(output_tensor.shape)
    (None, 5, 3, 4, 16)

    Args:
        num_heads: Number of attention heads.
        key_dim: Size of each attention head for query and key.
        value_dim: Size of each attention head for value.
        dropout: Dropout probability.
        use_bias: Boolean, whether the dense layers use bias vectors/matrices.
        output_shape: The expected shape of an output tensor, besides the batch
            and sequence dims. If not specified, projects back to the key
            feature dim.
        attention_axes: axes over which the attention is applied. `None` means
            attention over all axes, but batch, heads, and features.
        kernel_initializer: Initializer for dense layer kernels.
        bias_initializer: Initializer for dense layer biases.
        kernel_regularizer: Regularizer for dense layer kernels.
        bias_regularizer: Regularizer for dense layer biases.
        activity_regularizer: Regularizer for dense layer activity.
        kernel_constraint: Constraint for dense layer kernels.
        bias_constraint: Constraint for dense layer kernels.

    Call arguments:
        query: Query `Tensor` of shape `(B, T, dim)`.
        value: Value `Tensor` of shape `(B, S, dim)`.
        key: Optional key `Tensor` of shape `(B, S, dim)`. If not given, will
            use `value` for both `key` and `value`, which is the most common
            case.
        attention_mask: a boolean mask of shape `(B, T, S)`, that prevents
            attention to certain positions. The boolean mask specifies which
            query elements can attend to which key elements, 1 indicates
            attention and 0 indicates no attention. Broadcasting can happen for
            the missing batch dimensions and the head dimension.
        return_attention_scores: A boolean to indicate whether the output should
            be `(attention_output, attention_scores)` if `True`, or
            `attention_output` if `False`. Defaults to `False`.
        training: Python boolean indicating whether the layer should behave in
            training mode (adding dropout) or in inference mode (no dropout).
            Defaults to either using the training mode of the parent
            layer/model, or False (inference) if there is no parent layer.
        use_causal_mask: A boolean to indicate whether to apply a causal mask to
            prevent tokens from attending to future tokens (e.g., used in a
            decoder Transformer).

    Returns:
        attention_output: The result of the computation, of shape `(B, T, E)`,
            where `T` is for target sequence shapes and `E` is the query input
            last dimension if `output_shape` is `None`. Otherwise, the
            multi-head outputs are projected to the shape specified by
            `output_shape`.
        attention_scores: [Optional] multi-head attention coefficients over
            attention axes.
    '''
    supports_masking: bool
    def __init__(self, num_heads, key_dim, value_dim: Incomplete | None = None, dropout: float = 0.0, use_bias: bool = True, output_shape: Incomplete | None = None, attention_axes: Incomplete | None = None, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
    def call(self, query, value, key: Incomplete | None = None, attention_mask: Incomplete | None = None, return_attention_scores: bool = False, training: Incomplete | None = None, use_causal_mask: bool = False): ...
    def compute_output_shape(self, query_shape, value_shape, key_shape: Incomplete | None = None): ...
