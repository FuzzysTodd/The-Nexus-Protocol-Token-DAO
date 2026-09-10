import torch.nn as nn
from _typeshed import Incomplete

class StackedLSTMCell(nn.Module):
    lstm_num_layers: Incomplete
    lstm_modules: Incomplete
    def __init__(self, layers, size, bias) -> None: ...
    def forward(self, inputs, hidden): ...

class ReinforceField:
    """
    A field with ``name``, with ``total`` choices. ``choose_one`` is true if one and only one is meant to be
    selected. Otherwise, any number of choices can be chosen.
    """
    name: Incomplete
    total: Incomplete
    choose_one: Incomplete
    def __init__(self, name, total, choose_one) -> None: ...

class ReinforceController(nn.Module):
    """
    A controller that mutates the graph with RL.

    Parameters
    ----------
    fields : list of ReinforceField
        List of fields to choose.
    lstm_size : int
        Controller LSTM hidden units.
    lstm_num_layers : int
        Number of layers for stacked LSTM.
    tanh_constant : float
        Logits will be equal to ``tanh_constant * tanh(logits)``. Don't use ``tanh`` if this value is ``None``.
    skip_target : float
        Target probability that skipconnect (chosen by InputChoice) will appear.
        If the chosen number of inputs is away from the ``skip_connect``, there will be
        a sample skip penalty which is a KL divergence added.
    temperature : float
        Temperature constant that divides the logits.
    entropy_reduction : str
        Can be one of ``sum`` and ``mean``. How the entropy of multi-input-choice is reduced.
    """
    fields: Incomplete
    lstm_size: Incomplete
    lstm_num_layers: Incomplete
    tanh_constant: Incomplete
    temperature: Incomplete
    skip_target: Incomplete
    lstm: Incomplete
    attn_anchor: Incomplete
    attn_query: Incomplete
    v_attn: Incomplete
    g_emb: Incomplete
    skip_targets: Incomplete
    entropy_reduction: Incomplete
    cross_entropy_loss: Incomplete
    soft: Incomplete
    embedding: Incomplete
    def __init__(self, fields, lstm_size: int = 64, lstm_num_layers: int = 1, tanh_constant: float = 1.5, skip_target: float = 0.4, temperature: Incomplete | None = None, entropy_reduction: str = 'sum') -> None: ...
    def resample(self, return_prob: bool = False): ...
