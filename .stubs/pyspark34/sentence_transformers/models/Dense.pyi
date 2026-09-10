from ..util import fullname as fullname, import_from_string as import_from_string
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict

class Dense(nn.Module):
    """Feed-forward function with  activiation function.

    This layer takes a fixed-sized sentence embedding and passes it through a feed-forward layer. Can be used to generate deep averaging networs (DAN).

    :param in_features: Size of the input dimension
    :param out_features: Output size
    :param bias: Add a bias vector
    :param activation_function: Pytorch activation function applied on output
    :param init_weight: Initial value for the matrix of the linear layer
    :param init_bias: Initial value for the bias of the linear layer
    """
    in_features: Incomplete
    out_features: Incomplete
    bias: Incomplete
    activation_function: Incomplete
    linear: Incomplete
    def __init__(self, in_features: int, out_features: int, bias: bool = True, activation_function=..., init_weight: Tensor = None, init_bias: Tensor = None) -> None: ...
    def forward(self, features: Dict[str, Tensor]): ...
    def get_sentence_embedding_dimension(self) -> int: ...
    def get_config_dict(self): ...
    def save(self, output_path) -> None: ...
    @staticmethod
    def load(input_path): ...
