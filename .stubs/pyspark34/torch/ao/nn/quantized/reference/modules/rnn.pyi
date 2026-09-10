import torch.nn as nn
from _typeshed import Incomplete
from torch import Tensor
from typing import Any, Dict, Tuple

__all__ = ['RNNCellBase', 'RNNCell', 'LSTMCell', 'GRUCell', 'RNNBase', 'LSTM', 'GRU', 'get_quantized_weight']

def get_quantized_weight(module, wn): ...

class RNNCellBase(nn.RNNCellBase):
    def __init__(self, input_size: int, hidden_size: int, bias: bool, num_chunks: int, device: Incomplete | None = None, dtype: Incomplete | None = None, weight_qparams_dict: Incomplete | None = None) -> None: ...
    def get_quantized_weight_ih(self): ...
    def get_quantized_weight_hh(self): ...
    def get_weight_ih(self): ...
    def get_weight_hh(self): ...

class RNNCell(RNNCellBase):
    """
    We'll store weight_qparams for all the weights (weight_ih and weight_hh),
    we need to pass in a `weight_qparams_dict` that maps from weight name,
    e.g. weight_ih, to the weight_qparams for that weight
    """
    nonlinearity: Incomplete
    def __init__(self, input_size: int, hidden_size: int, bias: bool = True, nonlinearity: str = 'tanh', device: Incomplete | None = None, dtype: Incomplete | None = None, weight_qparams_dict: Dict[str, Any] | None = None) -> None: ...
    def forward(self, input: Tensor, hx: Tensor | None = None) -> Tensor: ...
    @classmethod
    def from_float(cls, mod, weight_qparams_dict): ...

class LSTMCell(RNNCellBase):
    """
    We'll store weight_qparams for all the weights (weight_ih and weight_hh),
    we need to pass in a `weight_qparams_dict` that maps from weight name,
    e.g. weight_ih, to the weight_qparams for that weight
    """
    def __init__(self, input_size: int, hidden_size: int, bias: bool = True, device: Incomplete | None = None, dtype: Incomplete | None = None, weight_qparams_dict: Dict[str, Any] | None = None) -> None: ...
    def forward(self, input: Tensor, hx: Tuple[Tensor, Tensor] | None = None) -> Tuple[Tensor, Tensor]: ...
    @classmethod
    def from_float(cls, mod, weight_qparams_dict): ...

class GRUCell(RNNCellBase):
    """
    We'll store weight_qparams for all the weights (weight_ih and weight_hh),
    we need to pass in a `weight_qparams_dict` that maps from weight name,
    e.g. weight_ih, to the weight_qparams for that weight
    """
    def __init__(self, input_size: int, hidden_size: int, bias: bool = True, device: Incomplete | None = None, dtype: Incomplete | None = None, weight_qparams_dict: Dict[str, Any] | None = None) -> None: ...
    def forward(self, input: Tensor, hx: Tensor | None = None) -> Tensor: ...
    @classmethod
    def from_float(cls, mod, weight_qparams_dict): ...

class RNNBase(nn.RNNBase):
    def __init__(self, mode: str, input_size: int, hidden_size: int, num_layers: int = 1, bias: bool = True, batch_first: bool = False, dropout: float = 0.0, bidirectional: bool = False, proj_size: int = 0, device: Incomplete | None = None, dtype: Incomplete | None = None, weight_qparams_dict: Dict[str, Any] | None = None) -> None: ...

class LSTM(RNNBase):
    """ Reference Quantized LSTM Module
    We'll store weight_qparams for all the weights in _flat_weights, we need to pass in
    a `weight_qparams_dict` that maps from weight name, e.g. weight_ih_l0,
    to the weight_qparams for that weight
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def permute_hidden(self, hx: Tuple[Tensor, Tensor], permutation: Tensor | None) -> Tuple[Tensor, Tensor]: ...
    def get_expected_cell_size(self, input: Tensor, batch_sizes: Tensor | None) -> Tuple[int, int, int]: ...
    def check_forward_args(self, input: Tensor, hidden: Tuple[Tensor, Tensor], batch_sizes: Tensor | None): ...
    def get_quantized_weight_bias_dict(self):
        ''' dictionary from flat_weight_name to quantized weight or (unquantized) bias
        e.g.
        {
          "weight_ih_l0": quantized_weight,
          "bias_ih_l0": unquantized_bias,
          ...
        }
        '''
    def get_flat_weights(self): ...
    def forward(self, input, hx: Incomplete | None = None): ...
    @classmethod
    def from_float(cls, mod, weight_qparams_dict): ...

class GRU(RNNBase):
    """ Reference Quantized GRU Module
    We'll store weight_qparams for all the weights in _flat_weights, we need to pass in
    a `weight_qparams_dict` that maps from weight name, e.g. weight_ih_l0,
    to the weight_qparams for that weight
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def get_quantized_weight_bias_dict(self):
        ''' dictionary from flat_weight_name to quantized weight or (unquantized) bias
        e.g.
        {
          "weight_ih_l0": quantized_weight,
          "bias_ih_l0": unquantized_bias,
          ...
        }
        '''
    def get_flat_weights(self): ...
    def forward(self, input, hx: Incomplete | None = None): ...
    @classmethod
    def from_float(cls, mod, weight_qparams_dict): ...
