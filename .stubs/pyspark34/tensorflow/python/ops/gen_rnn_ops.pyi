from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _BlockLSTMOutput(NamedTuple):
    i: Incomplete
    cs: Incomplete
    f: Incomplete
    o: Incomplete
    ci: Incomplete
    co: Incomplete
    h: Incomplete

def block_lstm(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias: int = 1, cell_clip: int = 3, use_peephole: bool = False, name: Incomplete | None = None):
    """Computes the LSTM cell forward propagation for all the time steps.

  This is equivalent to applying LSTMBlockCell in a loop, like so:

  ```python
  for x1 in unpack(x):
    i1, cs1, f1, o1, ci1, co1, h1 = LSTMBlock(
      x1, cs_prev, h_prev, w, wci, wcf, wco, b)
    cs_prev = cs1
    h_prev = h1
    i.append(i1)
    cs.append(cs1)
    f.append(f1)
    o.append(o1)
    ci.append(ci1)
    co.append(co1)
    h.append(h1)
  return pack(i), pack(cs), pack(f), pack(o), pack(ci), pack(ch), pack(h)
  ```

  Args:
    seq_len_max: A `Tensor` of type `int64`.
      Maximum time length actually used by this input. Outputs are padded
      with zeros beyond this length.
    x: A `Tensor`. Must be one of the following types: `half`, `float32`.
      The sequence input to the LSTM, shape (timelen, batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      Value of the initial cell state.
    h_prev: A `Tensor`. Must have the same type as `x`.
      Initial output of cell (to be used for peephole).
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    forget_bias: An optional `float`. Defaults to `1`. The forget gate bias.
    cell_clip: An optional `float`. Defaults to `3`.
      Value to clip the 'cs' value to.
    use_peephole: An optional `bool`. Defaults to `False`.
      Whether to use peephole weights.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (i, cs, f, o, ci, co, h).

    i: A `Tensor`. Has the same type as `x`.
    cs: A `Tensor`. Has the same type as `x`.
    f: A `Tensor`. Has the same type as `x`.
    o: A `Tensor`. Has the same type as `x`.
    ci: A `Tensor`. Has the same type as `x`.
    co: A `Tensor`. Has the same type as `x`.
    h: A `Tensor`. Has the same type as `x`.
  """

BlockLSTM: Incomplete

def block_lstm_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias, cell_clip, use_peephole, name, ctx): ...

class _BlockLSTMGradOutput(NamedTuple):
    x_grad: Incomplete
    cs_prev_grad: Incomplete
    h_prev_grad: Incomplete
    w_grad: Incomplete
    wci_grad: Incomplete
    wcf_grad: Incomplete
    wco_grad: Incomplete
    b_grad: Incomplete

def block_lstm_grad(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name: Incomplete | None = None):
    """Computes the LSTM cell backward propagation for the entire time sequence.

  This implementation is to be used in conjunction of LSTMBlock.

  Args:
    seq_len_max: A `Tensor` of type `int64`.
      Maximum time length actually used by this input. Outputs are padded
      with zeros beyond this length.
    x: A `Tensor`. Must be one of the following types: `half`, `float32`.
      The sequence input to the LSTM, shape (timelen, batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      Value of the initial cell state.
    h_prev: A `Tensor`. Must have the same type as `x`.
      Initial output of cell (to be used for peephole).
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    i: A `Tensor`. Must have the same type as `x`.
      The input gate over the whole time sequence.
    cs: A `Tensor`. Must have the same type as `x`.
      The cell state before the tanh over the whole time sequence.
    f: A `Tensor`. Must have the same type as `x`.
      The forget gate over the whole time sequence.
    o: A `Tensor`. Must have the same type as `x`.
      The output gate over the whole time sequence.
    ci: A `Tensor`. Must have the same type as `x`.
      The cell input over the whole time sequence.
    co: A `Tensor`. Must have the same type as `x`.
      The cell after the tanh over the whole time sequence.
    h: A `Tensor`. Must have the same type as `x`.
      The output h vector over the whole time sequence.
    cs_grad: A `Tensor`. Must have the same type as `x`.
      The current gradient of cs.
    h_grad: A `Tensor`. Must have the same type as `x`.
      The gradient of h vector.
    use_peephole: A `bool`. Whether to use peephole weights.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad, b_grad).

    x_grad: A `Tensor`. Has the same type as `x`.
    cs_prev_grad: A `Tensor`. Has the same type as `x`.
    h_prev_grad: A `Tensor`. Has the same type as `x`.
    w_grad: A `Tensor`. Has the same type as `x`.
    wci_grad: A `Tensor`. Has the same type as `x`.
    wcf_grad: A `Tensor`. Has the same type as `x`.
    wco_grad: A `Tensor`. Has the same type as `x`.
    b_grad: A `Tensor`. Has the same type as `x`.
  """

BlockLSTMGrad: Incomplete

def block_lstm_grad_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name, ctx): ...

class _BlockLSTMGradV2Output(NamedTuple):
    x_grad: Incomplete
    cs_prev_grad: Incomplete
    h_prev_grad: Incomplete
    w_grad: Incomplete
    wci_grad: Incomplete
    wcf_grad: Incomplete
    wco_grad: Incomplete
    b_grad: Incomplete

def block_lstm_grad_v2(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name: Incomplete | None = None):
    """Computes the LSTM cell backward propagation for the entire time sequence.

  This implementation is to be used in conjunction of BlockLSTMV2.

  Args:
    seq_len_max: A `Tensor` of type `int64`.
      Maximum time length actually used by this input. Outputs are padded
      with zeros beyond this length.
    x: A `Tensor`. Must be one of the following types: `half`, `float32`.
      The sequence input to the LSTM, shape (timelen, batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      Value of the initial cell state.
    h_prev: A `Tensor`. Must have the same type as `x`.
      Initial output of cell (to be used for peephole).
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    i: A `Tensor`. Must have the same type as `x`.
      The input gate over the whole time sequence.
    cs: A `Tensor`. Must have the same type as `x`.
      The cell state before the tanh over the whole time sequence.
    f: A `Tensor`. Must have the same type as `x`.
      The forget gate over the whole time sequence.
    o: A `Tensor`. Must have the same type as `x`.
      The output gate over the whole time sequence.
    ci: A `Tensor`. Must have the same type as `x`.
      The cell input over the whole time sequence.
    co: A `Tensor`. Must have the same type as `x`.
      The cell after the tanh over the whole time sequence.
    h: A `Tensor`. Must have the same type as `x`.
      The output h vector over the whole time sequence.
    cs_grad: A `Tensor`. Must have the same type as `x`.
      The current gradient of cs.
    h_grad: A `Tensor`. Must have the same type as `x`.
      The gradient of h vector.
    use_peephole: A `bool`. Whether to use peephole weights.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad, b_grad).

    x_grad: A `Tensor`. Has the same type as `x`.
    cs_prev_grad: A `Tensor`. Has the same type as `x`.
    h_prev_grad: A `Tensor`. Has the same type as `x`.
    w_grad: A `Tensor`. Has the same type as `x`.
    wci_grad: A `Tensor`. Has the same type as `x`.
    wcf_grad: A `Tensor`. Has the same type as `x`.
    wco_grad: A `Tensor`. Has the same type as `x`.
    b_grad: A `Tensor`. Has the same type as `x`.
  """

BlockLSTMGradV2: Incomplete

def block_lstm_grad_v2_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, h, cs_grad, h_grad, use_peephole, name, ctx): ...

class _BlockLSTMV2Output(NamedTuple):
    i: Incomplete
    cs: Incomplete
    f: Incomplete
    o: Incomplete
    ci: Incomplete
    co: Incomplete
    h: Incomplete

def block_lstmv2(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, cell_clip: int = 0, use_peephole: bool = False, name: Incomplete | None = None):
    """Computes the LSTM cell forward propagation for all the time steps.

  This is equivalent to applying LSTMBlockCell in a loop, like so:

  ```python
  for x1 in unpack(x):
    i1, cs1, f1, o1, ci1, co1, h1 = LSTMBlock(
      x1, cs_prev, h_prev, w, wci, wcf, wco, b)
    cs_prev = cs1
    h_prev = h1
    i.append(i1)
    cs.append(cs1)
    f.append(f1)
    o.append(o1)
    ci.append(ci1)
    co.append(co1)
    h.append(h1)
  return pack(i), pack(cs), pack(f), pack(o), pack(ci), pack(ch), pack(h)

  Note that unlike LSTMBlockCell (and BlockLSTM) which uses ICFO gate layout,
  this op uses IFCO. So in order for the following snippet to be equivalent
  all gate-related outputs should be reordered.
  ```

  Args:
    seq_len_max: A `Tensor` of type `int64`.
      Maximum time length actually used by this input. Outputs are padded
      with zeros beyond this length.
    x: A `Tensor`. Must be one of the following types: `half`, `float32`.
      The sequence input to the LSTM, shape (timelen, batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      Value of the initial cell state.
    h_prev: A `Tensor`. Must have the same type as `x`.
      Initial output of cell (to be used for peephole).
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    cell_clip: An optional `float`. Defaults to `0`.
      Value to clip the 'cs' value to.
    use_peephole: An optional `bool`. Defaults to `False`.
      Whether to use peephole weights.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (i, cs, f, o, ci, co, h).

    i: A `Tensor`. Has the same type as `x`.
    cs: A `Tensor`. Has the same type as `x`.
    f: A `Tensor`. Has the same type as `x`.
    o: A `Tensor`. Has the same type as `x`.
    ci: A `Tensor`. Has the same type as `x`.
    co: A `Tensor`. Has the same type as `x`.
    h: A `Tensor`. Has the same type as `x`.
  """

BlockLSTMV2: Incomplete

def block_lstmv2_eager_fallback(seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b, cell_clip, use_peephole, name, ctx): ...

class _GRUBlockCellOutput(NamedTuple):
    r: Incomplete
    u: Incomplete
    c: Incomplete
    h: Incomplete

def gru_block_cell(x, h_prev, w_ru, w_c, b_ru, b_c, name: Incomplete | None = None):
    """Computes the GRU cell forward propagation for 1 time step.

  Args
      x: Input to the GRU cell.
      h_prev: State input from the previous GRU cell.
      w_ru: Weight matrix for the reset and update gate.
      w_c: Weight matrix for the cell connection gate.
      b_ru: Bias vector for the reset and update gate.
      b_c: Bias vector for the cell connection gate.

  Returns
      r: Output of the reset gate.
      u: Output of the update gate.
      c: Output of the cell connection gate.
      h: Current state of the GRU cell.

  Note on notation of the variables:

  Concatenation of a and b is represented by a_b
  Element-wise dot product of a and b is represented by ab
  Element-wise dot product is represented by \\circ
  Matrix multiplication is represented by *

  Biases are initialized with :
  `b_ru` - constant_initializer(1.0)
  `b_c` - constant_initializer(0.0)

  This kernel op implements the following mathematical equations:

  ```
  x_h_prev = [x, h_prev]

  [r_bar u_bar] = x_h_prev * w_ru + b_ru

  r = sigmoid(r_bar)
  u = sigmoid(u_bar)

  h_prevr = h_prev \\circ r

  x_h_prevr = [x h_prevr]

  c_bar = x_h_prevr * w_c + b_c
  c = tanh(c_bar)

  h = (1-u) \\circ c + u \\circ h_prev
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`.
    h_prev: A `Tensor`. Must have the same type as `x`.
    w_ru: A `Tensor`. Must have the same type as `x`.
    w_c: A `Tensor`. Must have the same type as `x`.
    b_ru: A `Tensor`. Must have the same type as `x`.
    b_c: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (r, u, c, h).

    r: A `Tensor`. Has the same type as `x`.
    u: A `Tensor`. Has the same type as `x`.
    c: A `Tensor`. Has the same type as `x`.
    h: A `Tensor`. Has the same type as `x`.
  """

GRUBlockCell: Incomplete

def gru_block_cell_eager_fallback(x, h_prev, w_ru, w_c, b_ru, b_c, name, ctx): ...

class _GRUBlockCellGradOutput(NamedTuple):
    d_x: Incomplete
    d_h_prev: Incomplete
    d_c_bar: Incomplete
    d_r_bar_u_bar: Incomplete

def gru_block_cell_grad(x, h_prev, w_ru, w_c, b_ru, b_c, r, u, c, d_h, name: Incomplete | None = None):
    """Computes the GRU cell back-propagation for 1 time step.

  Args
      x: Input to the GRU cell.
      h_prev: State input from the previous GRU cell.
      w_ru: Weight matrix for the reset and update gate.
      w_c: Weight matrix for the cell connection gate.
      b_ru: Bias vector for the reset and update gate.
      b_c: Bias vector for the cell connection gate.
      r: Output of the reset gate.
      u: Output of the update gate.
      c: Output of the cell connection gate.
      d_h: Gradients of the h_new wrt to objective function.

  Returns
      d_x: Gradients of the x wrt to objective function.
      d_h_prev: Gradients of the h wrt to objective function.
      d_c_bar Gradients of the c_bar wrt to objective function.
      d_r_bar_u_bar Gradients of the r_bar & u_bar wrt to objective function.

  This kernel op implements the following mathematical equations:

  Note on notation of the variables:

  Concatenation of a and b is represented by a_b
  Element-wise dot product of a and b is represented by ab
  Element-wise dot product is represented by \\circ
  Matrix multiplication is represented by *

  Additional notes for clarity:

  `w_ru` can be segmented into 4 different matrices.
  ```
  w_ru = [w_r_x w_u_x
          w_r_h_prev w_u_h_prev]
  ```
  Similarly, `w_c` can be segmented into 2 different matrices.
  ```
  w_c = [w_c_x w_c_h_prevr]
  ```
  Same goes for biases.
  ```
  b_ru = [b_ru_x b_ru_h]
  b_c = [b_c_x b_c_h]
  ```
  Another note on notation:
  ```
  d_x = d_x_component_1 + d_x_component_2

  where d_x_component_1 = d_r_bar * w_r_x^T + d_u_bar * w_r_x^T
  and d_x_component_2 = d_c_bar * w_c_x^T

  d_h_prev = d_h_prev_component_1 + d_h_prevr \\circ r + d_h \\circ u
  where d_h_prev_componenet_1 = d_r_bar * w_r_h_prev^T + d_u_bar * w_r_h_prev^T
  ```

  Mathematics behind the Gradients below:
  ```
  d_c_bar = d_h \\circ (1-u) \\circ (1-c \\circ c)
  d_u_bar = d_h \\circ (h-c) \\circ u \\circ (1-u)

  d_r_bar_u_bar = [d_r_bar d_u_bar]

  [d_x_component_1 d_h_prev_component_1] = d_r_bar_u_bar * w_ru^T

  [d_x_component_2 d_h_prevr] = d_c_bar * w_c^T

  d_x = d_x_component_1 + d_x_component_2

  d_h_prev = d_h_prev_component_1 + d_h_prevr \\circ r + u
  ```
  Below calculation is performed in the python wrapper for the Gradients
  (not in the gradient kernel.)
  ```
  d_w_ru = x_h_prevr^T * d_c_bar

  d_w_c = x_h_prev^T * d_r_bar_u_bar

  d_b_ru = sum of d_r_bar_u_bar along axis = 0

  d_b_c = sum of d_c_bar along axis = 0
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`.
    h_prev: A `Tensor`. Must have the same type as `x`.
    w_ru: A `Tensor`. Must have the same type as `x`.
    w_c: A `Tensor`. Must have the same type as `x`.
    b_ru: A `Tensor`. Must have the same type as `x`.
    b_c: A `Tensor`. Must have the same type as `x`.
    r: A `Tensor`. Must have the same type as `x`.
    u: A `Tensor`. Must have the same type as `x`.
    c: A `Tensor`. Must have the same type as `x`.
    d_h: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d_x, d_h_prev, d_c_bar, d_r_bar_u_bar).

    d_x: A `Tensor`. Has the same type as `x`.
    d_h_prev: A `Tensor`. Has the same type as `x`.
    d_c_bar: A `Tensor`. Has the same type as `x`.
    d_r_bar_u_bar: A `Tensor`. Has the same type as `x`.
  """

GRUBlockCellGrad: Incomplete

def gru_block_cell_grad_eager_fallback(x, h_prev, w_ru, w_c, b_ru, b_c, r, u, c, d_h, name, ctx): ...

class _LSTMBlockCellOutput(NamedTuple):
    i: Incomplete
    cs: Incomplete
    f: Incomplete
    o: Incomplete
    ci: Incomplete
    co: Incomplete
    h: Incomplete

def lstm_block_cell(x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias: int = 1, cell_clip: int = 3, use_peephole: bool = False, name: Incomplete | None = None):
    """Computes the LSTM cell forward propagation for 1 time step.

  This implementation uses 1 weight matrix and 1 bias vector, and there's an
  optional peephole connection.

  This kernel op implements the following mathematical equations:

  ```python
  xh = [x, h_prev]
  [i, f, ci, o] = xh * w + b
  f = f + forget_bias

  if not use_peephole:
    wci = wcf = wco = 0

  i = sigmoid(cs_prev * wci + i)
  f = sigmoid(cs_prev * wcf + f)
  ci = tanh(ci)

  cs = ci .* i + cs_prev .* f
  cs = clip(cs, cell_clip)

  o = sigmoid(cs * wco + o)
  co = tanh(cs)
  h = co .* o
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `half`, `float32`.
      The input to the LSTM cell, shape (batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      Value of the cell state at previous time step.
    h_prev: A `Tensor`. Must have the same type as `x`.
      Output of the previous cell at previous time step.
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    forget_bias: An optional `float`. Defaults to `1`. The forget gate bias.
    cell_clip: An optional `float`. Defaults to `3`.
      Value to clip the 'cs' value to.
    use_peephole: An optional `bool`. Defaults to `False`.
      Whether to use peephole weights.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (i, cs, f, o, ci, co, h).

    i: A `Tensor`. Has the same type as `x`.
    cs: A `Tensor`. Has the same type as `x`.
    f: A `Tensor`. Has the same type as `x`.
    o: A `Tensor`. Has the same type as `x`.
    ci: A `Tensor`. Has the same type as `x`.
    co: A `Tensor`. Has the same type as `x`.
    h: A `Tensor`. Has the same type as `x`.
  """

LSTMBlockCell: Incomplete

def lstm_block_cell_eager_fallback(x, cs_prev, h_prev, w, wci, wcf, wco, b, forget_bias, cell_clip, use_peephole, name, ctx): ...

class _LSTMBlockCellGradOutput(NamedTuple):
    cs_prev_grad: Incomplete
    dicfo: Incomplete
    wci_grad: Incomplete
    wcf_grad: Incomplete
    wco_grad: Incomplete

def lstm_block_cell_grad(x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, cs_grad, h_grad, use_peephole, name: Incomplete | None = None):
    """Computes the LSTM cell backward propagation for 1 timestep.

  This implementation is to be used in conjunction of LSTMBlockCell.

  Args:
    x: A `Tensor`. Must be one of the following types: `half`, `float32`.
      The input to the LSTM cell, shape (batch_size, num_inputs).
    cs_prev: A `Tensor`. Must have the same type as `x`.
      The previous cell state.
    h_prev: A `Tensor`. Must have the same type as `x`. The previous h state.
    w: A `Tensor`. Must have the same type as `x`. The weight matrix.
    wci: A `Tensor`. Must have the same type as `x`.
      The weight matrix for input gate peephole connection.
    wcf: A `Tensor`. Must have the same type as `x`.
      The weight matrix for forget gate peephole connection.
    wco: A `Tensor`. Must have the same type as `x`.
      The weight matrix for output gate peephole connection.
    b: A `Tensor`. Must have the same type as `x`. The bias vector.
    i: A `Tensor`. Must have the same type as `x`. The input gate.
    cs: A `Tensor`. Must have the same type as `x`.
      The cell state before the tanh.
    f: A `Tensor`. Must have the same type as `x`. The forget gate.
    o: A `Tensor`. Must have the same type as `x`. The output gate.
    ci: A `Tensor`. Must have the same type as `x`. The cell input.
    co: A `Tensor`. Must have the same type as `x`. The cell after the tanh.
    cs_grad: A `Tensor`. Must have the same type as `x`.
      The current gradient of cs.
    h_grad: A `Tensor`. Must have the same type as `x`.
      The gradient of h vector.
    use_peephole: A `bool`. Whether the cell uses peephole connections.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (cs_prev_grad, dicfo, wci_grad, wcf_grad, wco_grad).

    cs_prev_grad: A `Tensor`. Has the same type as `x`.
    dicfo: A `Tensor`. Has the same type as `x`.
    wci_grad: A `Tensor`. Has the same type as `x`.
    wcf_grad: A `Tensor`. Has the same type as `x`.
    wco_grad: A `Tensor`. Has the same type as `x`.
  """

LSTMBlockCellGrad: Incomplete

def lstm_block_cell_grad_eager_fallback(x, cs_prev, h_prev, w, wci, wcf, wco, b, i, cs, f, o, ci, co, cs_grad, h_grad, use_peephole, name, ctx): ...
