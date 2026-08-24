from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict

class WeightedLayerPooling(nn.Module):
    """
    Token embeddings are weighted mean of their different hidden layer representations
    """
    config_keys: Incomplete
    word_embedding_dimension: Incomplete
    layer_start: Incomplete
    num_hidden_layers: Incomplete
    layer_weights: Incomplete
    def __init__(self, word_embedding_dimension, num_hidden_layers: int = 12, layer_start: int = 4, layer_weights: Incomplete | None = None) -> None: ...
    def forward(self, features: Dict[str, Tensor]): ...
    def get_word_embedding_dimension(self): ...
    def get_config_dict(self): ...
    def save(self, output_path) -> None: ...
    @staticmethod
    def load(input_path): ...
