from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict

class Dropout(nn.Module):
    """Dropout layer.

    :param dropout: Sets a dropout value for dense layer.
    """
    dropout: Incomplete
    dropout_layer: Incomplete
    def __init__(self, dropout: float = 0.2) -> None: ...
    def forward(self, features: Dict[str, Tensor]): ...
    def save(self, output_path) -> None: ...
    @staticmethod
    def load(input_path): ...
