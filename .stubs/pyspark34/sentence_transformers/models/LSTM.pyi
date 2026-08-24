from _typeshed import Incomplete
from torch import nn
from typing import List

class LSTM(nn.Module):
    """
    Bidirectional LSTM running over word embeddings.
    """
    config_keys: Incomplete
    word_embedding_dimension: Incomplete
    hidden_dim: Incomplete
    num_layers: Incomplete
    dropout: Incomplete
    bidirectional: Incomplete
    embeddings_dimension: Incomplete
    encoder: Incomplete
    def __init__(self, word_embedding_dimension: int, hidden_dim: int, num_layers: int = 1, dropout: float = 0, bidirectional: bool = True) -> None: ...
    def forward(self, features): ...
    def get_word_embedding_dimension(self) -> int: ...
    def tokenize(self, text: str) -> List[int]: ...
    def save(self, output_path: str): ...
    def get_config_dict(self): ...
    @staticmethod
    def load(input_path: str): ...
