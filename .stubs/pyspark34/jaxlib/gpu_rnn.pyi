from _typeshed import Incomplete
from jaxlib import xla_client as xla_client

compute_rnn_workspace_reserve_space_sizes: Incomplete

def cudnn_rnn_lowering(ctx, input, h_0, c_0, weights, seq_lengths, *, input_size: int, hidden_size: int, num_layers: int, dropout: bool, bidirectional: bool):
    """CuDnn RNN."""
def cudnn_rnn_bwd_lowering(ctx, dy, dhn, dcn, x, h0, c0, w, y, reserve_space, seq_lengths, *, input_size: int, hidden_size: int, num_layers: int, dropout: bool, bidirectional: bool):
    """CuDnn RNN Backward pass."""
