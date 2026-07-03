import jax
from _typeshed import Incomplete
from jax._src import core as core
from jax._src.custom_derivatives import custom_vjp as custom_vjp
from jax._src.lax import lax as lax
from jax._src.lib import gpu_rnn as gpu_rnn
from jax._src.typing import Array as Array, Shape as Shape
from jax.interpreters import mlir as mlir, xla as xla
from typing import Any

PRNGKeyArray = Any
sigmoid: Incomplete
tanh = jax.nn.tanh

def get_num_params_in_lstm(input_size: int, hidden_size: int, num_layers: int, bidirectional: bool) -> int:
    """Get param count in LSTM."""
def init_lstm_weight(rng: PRNGKeyArray, input_size: int, hidden_size: int, num_layers: int, bidirectional: bool):
    """Random initialize LSTM weights from U(-k, k), k=sqrt(1/hidden_size)."""
def unpack_lstm_weights(weights: Array, input_size: int, hidden_size: int, num_layers: int, bidirectional: bool) -> tuple[dict[int, Array], dict[int, Array], dict[int, Array], dict[int, Array]]:
    """Unpack cudnn LSTM weights into individual weights.

  CUDNN LSTM weight layout: (num_layers, num_directions, W_ih, W_hh, b_ih, b_hh)
  Returns W_ih, W_hh, b_ih, b_hh. e.g. W_ih[2][1] is the concat weights of
  4 weights (W_ii, W_if, W_ig, W_io), each of shape (hidden_size, input_size)
  at 2nd layer for the reverse direction. See notations from
  https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html#torch.nn.LSTM.
  """
def lstm(x: Array, h_0: Array, c_0: Array, weights: Array, seq_lengths: Array, input_size: int, hidden_size: int, num_layers: int, dropout: float, bidirectional: bool, precision: lax.PrecisionLike = None) -> tuple[Array, Array, Array]:
    """LSTM via CuDNN or HIPDNN (not-yet-supported).

  Assume batch-first inputs.

  Arguments:
    x: (batch_size, max_seq_length, input_size)
    h_0: (num_directions * num_layers, batch_size, hidden_size)
    c_0: (num_directions * num_layers, batch_size, hidden_size)
    weights: (num_params,) where num_params = get_num_params_in_lstm(...)
    seq_lengths: (batch_size,)
  Returns: (y, h_n, c_n, reserve_space).
    y: (batch_size, max_seq_length, hidden_size * num_directions)
    h_n: (num_directions * num_layers, batch_size, hidden_size)
    c_n: (num_directions * num_layers, batch_size, hidden_size)
  """
def lstm_ref(x: Array, h_0: Array, c_0: Array, W_ih: dict[int, Array], W_hh: dict[int, Array], b_ih: dict[int, Array], b_hh: dict[int, Array], seq_lengths: Array, input_size: int, hidden_size: int, num_layers: int, dropout: float, bidirectional: bool) -> tuple[Array, Array, Array]:
    """Reference implementation of LSTM.

  See https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html#lstm
  https://docs.nvidia.com/deeplearning/cudnn/api/index.html#cudnnRNNMode_t
  """
def lstm_fwd(x: Array, h_0: Array, c_0: Array, w: Array, seq_lengths: Array, input_size: int, hidden_size: int, num_layers: int, dropout: float, bidirectional: bool, precision: lax.PrecisionLike): ...
def rnn_abstract_eval(x_aval, h_0_aval, c_0_aval, w_aval, seq_lengths_aval, input_size: int, hidden_size: int, num_layers: int, dropout: float, bidirectional: bool, cudnn_allow_tf32: bool): ...

rnn_fwd_p: Incomplete

def lstm_bwd(input_size: int, hidden_size: int, num_layers: int, dropout: float, bidirectional: bool, precision: lax.PrecisionLike, residuals, gradients): ...
def rnn_bwd_abstract_eval(dy_aval, dhn_aval, dcn_aval, x_aval, h0_aval, c0_aval, w_aval, y_aval, reserve_space_aval, seq_lengths_aval, input_size: int, hidden_size: int, num_layers: int, dropout: float, bidirectional: bool, cudnn_allow_tf32: bool): ...

rnn_bwd_p: Incomplete
