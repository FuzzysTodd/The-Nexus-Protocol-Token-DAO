from .tokenizer import WhitespaceTokenizer as WhitespaceTokenizer
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict, List

logger: Incomplete

class BoW(nn.Module):
    """Implements a Bag-of-Words (BoW) model to derive sentence embeddings.

    A weighting can be added to allow the generation of tf-idf vectors. The output vector has the size of the vocab.
    """
    config_keys: Incomplete
    vocab: Incomplete
    word_weights: Incomplete
    unknown_word_weight: Incomplete
    cumulative_term_frequency: Incomplete
    weights: Incomplete
    tokenizer: Incomplete
    sentence_embedding_dimension: Incomplete
    def __init__(self, vocab: List[str], word_weights: Dict[str, float] = {}, unknown_word_weight: float = 1, cumulative_term_frequency: bool = True) -> None: ...
    def forward(self, features: Dict[str, Tensor]): ...
    def tokenize(self, texts: List[str]) -> List[int]: ...
    def get_sentence_embedding_dimension(self): ...
    def get_sentence_features(self, tokenized_texts: List[List[int]], pad_seq_length: int = 0): ...
    def get_config_dict(self): ...
    def save(self, output_path) -> None: ...
    @staticmethod
    def load(input_path): ...
