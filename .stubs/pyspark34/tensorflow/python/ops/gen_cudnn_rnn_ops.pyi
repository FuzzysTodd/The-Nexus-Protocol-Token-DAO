from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _CudnnRNNOutput(NamedTuple):
    output: Incomplete
    output_h: Incomplete
    output_c: Incomplete
    reserve_space: Incomplete

def cudnn_rnn(input, input_h, input_c, params, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, is_training: bool = True, name: Incomplete | None = None):
    '''A RNN backed by cuDNN.

  Computes the RNN from the input and initial states, with respect to the params
  buffer.

  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
    the actual computation before the first layer. \'skip_input\' is only allowed
    when input_size == num_units; \'auto_select\' implies \'skip_input\' when
    input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used. Should be
    "unidirectional" or "bidirectional".
  dropout: Dropout probability. When set to 0., dropout is disabled.
  seed: The 1st part of a seed to initialize dropout.
  seed2: The 2nd part of a seed to initialize dropout.
  input: A 3-D tensor with the shape of [seq_length, batch_size, input_size].
  input_h: A 3-D tensor with the shape of [num_layer * dir, batch_size,
      num_units].
  input_c: For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
  params: A 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
  output: A 3-D tensor with the shape of [seq_length, batch_size,
      dir * num_units].
  output_h: The same shape has input_h.
  output_c: The same shape as input_c for LSTM. An empty tensor for other models.
  is_training: Indicates whether this operation is used for inference or
    training.
  reserve_space: An opaque tensor that can be used in backprop calculation. It
    is only produced if is_training is false.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    input_h: A `Tensor`. Must have the same type as `input`.
    input_c: A `Tensor`. Must have the same type as `input`.
    params: A `Tensor`. Must have the same type as `input`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    is_training: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_h, output_c, reserve_space).

    output: A `Tensor`. Has the same type as `input`.
    output_h: A `Tensor`. Has the same type as `input`.
    output_c: A `Tensor`. Has the same type as `input`.
    reserve_space: A `Tensor`. Has the same type as `input`.
  '''

CudnnRNN: Incomplete

def cudnn_rnn_eager_fallback(input, input_h, input_c, params, rnn_mode, input_mode, direction, dropout, seed, seed2, is_training, name, ctx): ...

class _CudnnRNNBackpropOutput(NamedTuple):
    input_backprop: Incomplete
    input_h_backprop: Incomplete
    input_c_backprop: Incomplete
    params_backprop: Incomplete

def cudnn_rnn_backprop(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Backprop step of CudnnRNN.

  Compute the backprop of both data and weights in a RNN.

  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
      the actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used. Should be
    "unidirectional" or "bidirectional".
  dropout: Dropout probability. When set to 0., dropout is disabled.
  seed: The 1st part of a seed to initialize dropout.
  seed2: The 2nd part of a seed to initialize dropout.
  input: A 3-D tensor with the shape of [seq_length, batch_size, input_size].
  input_h: A 3-D tensor with the shape of [num_layer * dir, batch_size,
      num_units].
  input_c: For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
  params: A 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
  output: A 3-D tensor with the shape of [seq_length, batch_size,
      dir * num_units].
  output_h: The same shape has input_h.
  output_c: The same shape as input_c for LSTM. An empty tensor for other models.
  output_backprop: A 3-D tensor with the same shape as output in the forward pass.
  output_h_backprop: A 3-D tensor with the same shape as output_h in the forward
      pass.
  output_c_backprop: A 3-D tensor with the same shape as output_c in the forward
      pass.
  reserve_space: The same reserve_space produced in for forward operation.
  input_backprop: The backprop to input in the forward pass. Has the same shape
      as input.
  input_h_backprop: The backprop to input_h in the forward pass. Has the same
      shape as input_h.
  input_c_backprop: The backprop to input_c in the forward pass. Has the same
      shape as input_c.
  params_backprop: The backprop to the params buffer in the forward pass. Has the
      same shape as params.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    input_h: A `Tensor`. Must have the same type as `input`.
    input_c: A `Tensor`. Must have the same type as `input`.
    params: A `Tensor`. Must have the same type as `input`.
    output: A `Tensor`. Must have the same type as `input`.
    output_h: A `Tensor`. Must have the same type as `input`.
    output_c: A `Tensor`. Must have the same type as `input`.
    output_backprop: A `Tensor`. Must have the same type as `input`.
    output_h_backprop: A `Tensor`. Must have the same type as `input`.
    output_c_backprop: A `Tensor`. Must have the same type as `input`.
    reserve_space: A `Tensor`. Must have the same type as `input`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (input_backprop, input_h_backprop, input_c_backprop, params_backprop).

    input_backprop: A `Tensor`. Has the same type as `input`.
    input_h_backprop: A `Tensor`. Has the same type as `input`.
    input_c_backprop: A `Tensor`. Has the same type as `input`.
    params_backprop: A `Tensor`. Has the same type as `input`.
  '''

CudnnRNNBackprop: Incomplete

def cudnn_rnn_backprop_eager_fallback(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...

class _CudnnRNNBackpropV2Output(NamedTuple):
    input_backprop: Incomplete
    input_h_backprop: Incomplete
    input_c_backprop: Incomplete
    params_backprop: Incomplete

def cudnn_rnn_backprop_v2(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Backprop step of CudnnRNN.

  Compute the backprop of both data and weights in a RNN. Takes an extra
      "host_reserved" inupt than CudnnRNNBackprop, which is used to determine RNN
      cudnnRNNAlgo_t and cudnnMathType_t.

  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicates whether there is a linear projection between the input and
      the actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used. Should be
    "unidirectional" or "bidirectional".
  dropout: Dropout probability. When set to 0., dropout is disabled.
  seed: The 1st part of a seed to initialize dropout.
  seed2: The 2nd part of a seed to initialize dropout.
  input: A 3-D tensor with the shape of [seq_length, batch_size, input_size].
  input_h: A 3-D tensor with the shape of [num_layer * dir, batch_size,
      num_units].
  input_c: For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
  params: A 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
  output: A 3-D tensor with the shape of [seq_length, batch_size,
      dir * num_units].
  output_h: The same shape has input_h.
  output_c: The same shape as input_c for LSTM. An empty tensor for other models.
  output_backprop: A 3-D tensor with the same shape as output in the forward pass.
  output_h_backprop: A 3-D tensor with the same shape as output_h in the forward
      pass.
  output_c_backprop: A 3-D tensor with the same shape as output_c in the forward
      pass.
  reserve_space: The same reserve_space produced in the forward operation.
  host_reserved: The same host_reserved produced in the forward operation.
  input_backprop: The backprop to input in the forward pass. Has the same shape
      as input.
  input_h_backprop: The backprop to input_h in the forward pass. Has the same
      shape as input_h.
  input_c_backprop: The backprop to input_c in the forward pass. Has the same
      shape as input_c.
  params_backprop: The backprop to the params buffer in the forward pass. Has the
      same shape as params.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    input_h: A `Tensor`. Must have the same type as `input`.
    input_c: A `Tensor`. Must have the same type as `input`.
    params: A `Tensor`. Must have the same type as `input`.
    output: A `Tensor`. Must have the same type as `input`.
    output_h: A `Tensor`. Must have the same type as `input`.
    output_c: A `Tensor`. Must have the same type as `input`.
    output_backprop: A `Tensor`. Must have the same type as `input`.
    output_h_backprop: A `Tensor`. Must have the same type as `input`.
    output_c_backprop: A `Tensor`. Must have the same type as `input`.
    reserve_space: A `Tensor`. Must have the same type as `input`.
    host_reserved: A `Tensor` of type `int8`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (input_backprop, input_h_backprop, input_c_backprop, params_backprop).

    input_backprop: A `Tensor`. Has the same type as `input`.
    input_h_backprop: A `Tensor`. Has the same type as `input`.
    input_c_backprop: A `Tensor`. Has the same type as `input`.
    params_backprop: A `Tensor`. Has the same type as `input`.
  '''

CudnnRNNBackpropV2: Incomplete

def cudnn_rnn_backprop_v2_eager_fallback(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...

class _CudnnRNNBackpropV3Output(NamedTuple):
    input_backprop: Incomplete
    input_h_backprop: Incomplete
    input_c_backprop: Incomplete
    params_backprop: Incomplete

def cudnn_rnn_backprop_v3(input, input_h, input_c, params, sequence_lengths, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, num_proj: int = 0, time_major: bool = True, name: Incomplete | None = None):
    '''Backprop step of CudnnRNNV3.

  Compute the backprop of both data and weights in a RNN. Takes an extra
      "sequence_lengths" input than CudnnRNNBackprop.

  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicates whether there is a linear projection between the input and
      the actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used. Should be
    "unidirectional" or "bidirectional".
  dropout: Dropout probability. When set to 0., dropout is disabled.
  seed: The 1st part of a seed to initialize dropout.
  seed2: The 2nd part of a seed to initialize dropout.
  input: If time_major is true, this is a 3-D tensor with the shape of
      [seq_length, batch_size, input_size]. If time_major is false, the shape is
      [batch_size, seq_length, input_size].
  input_h: If time_major is true, this is a 3-D tensor with the shape of
      [num_layer * dir, batch_size, num_units]. If time_major is false, the shape
      is [batch_size, num_layer * dir, num_units].
  input_c: For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
  params: A 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
  sequence_lengths: a vector of lengths of each input sequence.
  output: If time_major is true, this is a 3-D tensor with the shape of
      [seq_length, batch_size, dir * num_units]. If time_major is false, the
      shape is [batch_size, seq_length, dir * num_units].
  output_h: The same shape has input_h.
  output_c: The same shape as input_c for LSTM. An empty tensor for other models.
  output_backprop: A 3-D tensor with the same shape as output in the forward pass.
  output_h_backprop: A 3-D tensor with the same shape as output_h in the forward
      pass.
  output_c_backprop: A 3-D tensor with the same shape as output_c in the forward
      pass.
  time_major: Indicates whether the input/output format is time major or batch
      major.
  reserve_space: The same reserve_space produced in the forward operation.
  input_backprop: The backprop to input in the forward pass. Has the same shape
      as input.
  input_h_backprop: The backprop to input_h in the forward pass. Has the same
      shape as input_h.
  input_c_backprop: The backprop to input_c in the forward pass. Has the same
      shape as input_c.
  params_backprop: The backprop to the params buffer in the forward pass. Has the
      same shape as params.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    input_h: A `Tensor`. Must have the same type as `input`.
    input_c: A `Tensor`. Must have the same type as `input`.
    params: A `Tensor`. Must have the same type as `input`.
    sequence_lengths: A `Tensor` of type `int32`.
    output: A `Tensor`. Must have the same type as `input`.
    output_h: A `Tensor`. Must have the same type as `input`.
    output_c: A `Tensor`. Must have the same type as `input`.
    output_backprop: A `Tensor`. Must have the same type as `input`.
    output_h_backprop: A `Tensor`. Must have the same type as `input`.
    output_c_backprop: A `Tensor`. Must have the same type as `input`.
    reserve_space: A `Tensor`. Must have the same type as `input`.
    host_reserved: A `Tensor` of type `int8`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    num_proj: An optional `int`. Defaults to `0`.
    time_major: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (input_backprop, input_h_backprop, input_c_backprop, params_backprop).

    input_backprop: A `Tensor`. Has the same type as `input`.
    input_h_backprop: A `Tensor`. Has the same type as `input`.
    input_c_backprop: A `Tensor`. Has the same type as `input`.
    params_backprop: A `Tensor`. Has the same type as `input`.
  '''

CudnnRNNBackpropV3: Incomplete

def cudnn_rnn_backprop_v3_eager_fallback(input, input_h, input_c, params, sequence_lengths, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, time_major, name, ctx): ...
def cudnn_rnn_canonical_to_params(num_layers, num_units, input_size, weights, biases, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Converts CudnnRNN params from canonical form to usable form.

  Writes a set of weights into the opaque params buffer so they can be used in
  upcoming training or inferences.

  Note that the params buffer may not be compatible across different GPUs. So any
  save and restoration should be converted to and from the canonical weights and
  biases.

  num_layers: Specifies the number of layers in the RNN model.
  num_units: Specifies the size of the hidden state.
  input_size: Specifies the size of the input state.
  weights: the canonical form of weights that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  biases: the canonical form of biases that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  num_params: number of parameter sets for all layers.
      Each layer may contain multiple parameter sets, with each set consisting of
      a weight matrix and a bias vector.
  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
  dropout: dropout probability. When set to 0., dropout is disabled.
  seed: the 1st part of a seed to initialize dropout.
  seed2: the 2nd part of a seed to initialize dropout.

  Args:
    num_layers: A `Tensor` of type `int32`.
    num_units: A `Tensor` of type `int32`.
    input_size: A `Tensor` of type `int32`.
    weights: A list of at least 1 `Tensor` objects with the same type in: `half`, `float32`, `float64`.
    biases: A list with the same length as `weights` of `Tensor` objects with the same type as `weights`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  '''

CudnnRNNCanonicalToParams: Incomplete

def cudnn_rnn_canonical_to_params_eager_fallback(num_layers, num_units, input_size, weights, biases, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...
def cudnn_rnn_canonical_to_params_v2(num_layers, num_units, input_size, weights, biases, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, num_proj: int = 0, name: Incomplete | None = None):
    '''Converts CudnnRNN params from canonical form to usable form. It supports the projection in LSTM.

  Writes a set of weights into the opaque params buffer so they can be used in
  upcoming training or inferences.

  Note that the params buffer may not be compatible across different GPUs. So any
  save and restoration should be converted to and from the canonical weights and
  biases.

  num_layers: Specifies the number of layers in the RNN model.
  num_units: Specifies the size of the hidden state.
  input_size: Specifies the size of the input state.
  weights: the canonical form of weights that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  biases: the canonical form of biases that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  num_params_weights: number of weight parameter matrix for all layers.
  num_params_biases: number of bias parameter vector for all layers.
  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
  dropout: dropout probability. When set to 0., dropout is disabled.
  seed: the 1st part of a seed to initialize dropout.
  seed2: the 2nd part of a seed to initialize dropout.
  num_proj: The output dimensionality for the projection matrices. If None or 0,
      no projection is performed.

  Args:
    num_layers: A `Tensor` of type `int32`.
    num_units: A `Tensor` of type `int32`.
    input_size: A `Tensor` of type `int32`.
    weights: A list of at least 1 `Tensor` objects with the same type in: `half`, `float32`, `float64`.
    biases: A list of at least 1 `Tensor` objects with the same type as `weights`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    num_proj: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  '''

CudnnRNNCanonicalToParamsV2: Incomplete

def cudnn_rnn_canonical_to_params_v2_eager_fallback(num_layers, num_units, input_size, weights, biases, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, name, ctx): ...
def cudnn_rnn_params_size(num_layers, num_units, input_size, T, S, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, num_proj: int = 0, name: Incomplete | None = None):
    '''Computes size of weights that can be used by a Cudnn RNN model.

  Return the params size that can be used by the Cudnn RNN model. Subsequent
  weight allocation and initialization should use this size.

  num_layers: Specifies the number of layers in the RNN model.
  num_units: Specifies the size of the hidden state.
  input_size: Specifies the size of the input state.
  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
    The actual computation before the first layer. \'skip_input\' is only allowed
    when input_size == num_units; \'auto_select\' implies \'skip_input\' when
    input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used.
    dir = (direction == bidirectional) ? 2 : 1
  dropout: dropout probability. When set to 0., dropout is disabled.
  seed: the 1st part of a seed to initialize dropout.
  seed2: the 2nd part of a seed to initialize dropout.
  params_size: The size of the params buffer that should be allocated and
    initialized for this RNN model. Note that this params buffer may not be
    compatible across GPUs. Please use CudnnRNNParamsWeights and
    CudnnRNNParamsBiases to save and restore them in a way that is compatible
    across different runs.

  Args:
    num_layers: A `Tensor` of type `int32`.
    num_units: A `Tensor` of type `int32`.
    input_size: A `Tensor` of type `int32`.
    T: A `tf.DType` from: `tf.half, tf.float32, tf.float64`.
    S: A `tf.DType` from: `tf.int32, tf.int64`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    num_proj: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `S`.
  '''

CudnnRNNParamsSize: Incomplete

def cudnn_rnn_params_size_eager_fallback(num_layers, num_units, input_size, T, S, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, name, ctx): ...

class _CudnnRNNParamsToCanonicalOutput(NamedTuple):
    weights: Incomplete
    biases: Incomplete

def cudnn_rnn_params_to_canonical(num_layers, num_units, input_size, params, num_params, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Retrieves CudnnRNN params in canonical form.

  Retrieves a set of weights from the opaque params buffer that can be saved and
  restored in a way compatible with future runs.

  Note that the params buffer may not be compatible across different GPUs. So any
  save and restoration should be converted to and from the canonical weights and
  biases.

  num_layers: Specifies the number of layers in the RNN model.
  num_units: Specifies the size of the hidden state.
  input_size: Specifies the size of the input state.
  num_params: number of parameter sets for all layers.
      Each layer may contain multiple parameter sets, with each set consisting of
      a weight matrix and a bias vector.
  weights: the canonical form of weights that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  biases: the canonical form of biases that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
  dropout: dropout probability. When set to 0., dropout is disabled.
  seed: the 1st part of a seed to initialize dropout.
  seed2: the 2nd part of a seed to initialize dropout.

  Args:
    num_layers: A `Tensor` of type `int32`.
    num_units: A `Tensor` of type `int32`.
    input_size: A `Tensor` of type `int32`.
    params: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    num_params: An `int` that is `>= 1`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (weights, biases).

    weights: A list of `num_params` `Tensor` objects with the same type as `params`.
    biases: A list of `num_params` `Tensor` objects with the same type as `params`.
  '''

CudnnRNNParamsToCanonical: Incomplete

def cudnn_rnn_params_to_canonical_eager_fallback(num_layers, num_units, input_size, params, num_params, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...

class _CudnnRNNParamsToCanonicalV2Output(NamedTuple):
    weights: Incomplete
    biases: Incomplete

def cudnn_rnn_params_to_canonical_v2(num_layers, num_units, input_size, params, num_params_weights, num_params_biases, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, num_proj: int = 0, name: Incomplete | None = None):
    '''Retrieves CudnnRNN params in canonical form. It supports the projection in LSTM.

  Retrieves a set of weights from the opaque params buffer that can be saved and
  restored in a way compatible with future runs.

  Note that the params buffer may not be compatible across different GPUs. So any
  save and restoration should be converted to and from the canonical weights and
  biases.

  num_layers: Specifies the number of layers in the RNN model.
  num_units: Specifies the size of the hidden state.
  input_size: Specifies the size of the input state.
  num_params_weights: number of weight parameter matrix for all layers.
  num_params_biases: number of bias parameter vector for all layers.
  weights: the canonical form of weights that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  biases: the canonical form of biases that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. \'skip_input\' is only allowed
      when input_size == num_units; \'auto_select\' implies \'skip_input\' when
      input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
  dropout: dropout probability. When set to 0., dropout is disabled.
  seed: the 1st part of a seed to initialize dropout.
  seed2: the 2nd part of a seed to initialize dropout.
  num_proj: The output dimensionality for the projection matrices. If None or 0,
      no projection is performed.

  Args:
    num_layers: A `Tensor` of type `int32`.
    num_units: A `Tensor` of type `int32`.
    input_size: A `Tensor` of type `int32`.
    params: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    num_params_weights: An `int` that is `>= 1`.
    num_params_biases: An `int` that is `>= 1`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    num_proj: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (weights, biases).

    weights: A list of `num_params_weights` `Tensor` objects with the same type as `params`.
    biases: A list of `num_params_biases` `Tensor` objects with the same type as `params`.
  '''

CudnnRNNParamsToCanonicalV2: Incomplete

def cudnn_rnn_params_to_canonical_v2_eager_fallback(num_layers, num_units, input_size, params, num_params_weights, num_params_biases, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, name, ctx): ...

class _CudnnRNNV2Output(NamedTuple):
    output: Incomplete
    output_h: Incomplete
    output_c: Incomplete
    reserve_space: Incomplete
    host_reserved: Incomplete

def cudnn_rnnv2(input, input_h, input_c, params, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, is_training: bool = True, name: Incomplete | None = None):
    '''A RNN backed by cuDNN.

  Computes the RNN from the input and initial states, with respect to the params
  buffer. Produces one extra output "host_reserved" than CudnnRNN.

  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicates whether there is a linear projection between the input and
    the actual computation before the first layer. \'skip_input\' is only allowed
    when input_size == num_units; \'auto_select\' implies \'skip_input\' when
    input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used. Should be
    "unidirectional" or "bidirectional".
  dropout: Dropout probability. When set to 0., dropout is disabled.
  seed: The 1st part of a seed to initialize dropout.
  seed2: The 2nd part of a seed to initialize dropout.
  input: A 3-D tensor with the shape of [seq_length, batch_size, input_size].
  input_h: A 3-D tensor with the shape of [num_layer * dir, batch_size,
      num_units].
  input_c: For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
  params: A 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
  output: A 3-D tensor with the shape of [seq_length, batch_size,
      dir * num_units].
  output_h: The same shape has input_h.
  output_c: The same shape as input_c for LSTM. An empty tensor for other models.
  is_training: Indicates whether this operation is used for inference or
    training.
  reserve_space: An opaque tensor that can be used in backprop calculation. It
    is only produced if is_training is true.
  host_reserved: An opaque tensor that can be used in backprop calculation. It is
    only produced if is_training is true. It is output on host memory rather than
    device memory.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    input_h: A `Tensor`. Must have the same type as `input`.
    input_c: A `Tensor`. Must have the same type as `input`.
    params: A `Tensor`. Must have the same type as `input`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    is_training: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_h, output_c, reserve_space, host_reserved).

    output: A `Tensor`. Has the same type as `input`.
    output_h: A `Tensor`. Has the same type as `input`.
    output_c: A `Tensor`. Has the same type as `input`.
    reserve_space: A `Tensor`. Has the same type as `input`.
    host_reserved: A `Tensor` of type `int8`.
  '''

CudnnRNNV2: Incomplete

def cudnn_rnnv2_eager_fallback(input, input_h, input_c, params, rnn_mode, input_mode, direction, dropout, seed, seed2, is_training, name, ctx): ...

class _CudnnRNNV3Output(NamedTuple):
    output: Incomplete
    output_h: Incomplete
    output_c: Incomplete
    reserve_space: Incomplete
    host_reserved: Incomplete

def cudnn_rnnv3(input, input_h, input_c, params, sequence_lengths, rnn_mode: str = 'lstm', input_mode: str = 'linear_input', direction: str = 'unidirectional', dropout: int = 0, seed: int = 0, seed2: int = 0, num_proj: int = 0, is_training: bool = True, time_major: bool = True, name: Incomplete | None = None):
    '''A RNN backed by cuDNN.

  Computes the RNN from the input and initial states, with respect to the params
  buffer. Accepts one extra input "sequence_lengths" than CudnnRNN.

  rnn_mode: Indicates the type of the RNN model.
  input_mode: Indicates whether there is a linear projection between the input and
    the actual computation before the first layer. \'skip_input\' is only allowed
    when input_size == num_units; \'auto_select\' implies \'skip_input\' when
    input_size == num_units; otherwise, it implies \'linear_input\'.
  direction: Indicates whether a bidirectional model will be used. Should be
    "unidirectional" or "bidirectional".
  dropout: Dropout probability. When set to 0., dropout is disabled.
  seed: The 1st part of a seed to initialize dropout.
  seed2: The 2nd part of a seed to initialize dropout.
  input: If time_major is true, this is a 3-D tensor with the shape of
      [seq_length, batch_size, input_size]. If time_major is false, the shape is
      [batch_size, seq_length, input_size].
  input_h: If time_major is true, this is a 3-D tensor with the shape of
      [num_layer * dir, batch_size, num_units]. If time_major is false, the shape
      is [batch_size, num_layer * dir, num_units].
  input_c: For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
  params: A 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
  sequence_lengths: a vector of lengths of each input sequence.
  output: If time_major is true, this is a 3-D tensor with the shape of
      [seq_length, batch_size, dir * num_units]. If time_major is false, the
      shape is [batch_size, seq_length, dir * num_units].
  output_h: The same shape has input_h.
  output_c: The same shape as input_c for LSTM. An empty tensor for other models.
  is_training: Indicates whether this operation is used for inference or
    training.
  time_major: Indicates whether the input/output format is time major or batch
      major.
  reserve_space: An opaque tensor that can be used in backprop calculation. It
    is only produced if is_training is true.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    input_h: A `Tensor`. Must have the same type as `input`.
    input_c: A `Tensor`. Must have the same type as `input`.
    params: A `Tensor`. Must have the same type as `input`.
    sequence_lengths: A `Tensor` of type `int32`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
    dropout: An optional `float`. Defaults to `0`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    num_proj: An optional `int`. Defaults to `0`.
    is_training: An optional `bool`. Defaults to `True`.
    time_major: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_h, output_c, reserve_space, host_reserved).

    output: A `Tensor`. Has the same type as `input`.
    output_h: A `Tensor`. Has the same type as `input`.
    output_c: A `Tensor`. Has the same type as `input`.
    reserve_space: A `Tensor`. Has the same type as `input`.
    host_reserved: A `Tensor` of type `int8`.
  '''

CudnnRNNV3: Incomplete

def cudnn_rnnv3_eager_fallback(input, input_h, input_c, params, sequence_lengths, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, is_training, time_major, name, ctx): ...
