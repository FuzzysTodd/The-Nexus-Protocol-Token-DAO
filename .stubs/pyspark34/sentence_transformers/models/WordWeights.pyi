from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict, List

logger: Incomplete

class WordWeights(nn.Module):
    """This model can weight word embeddings, for example, with idf-values."""
    config_keys: Incomplete
    vocab: Incomplete
    word_weights: Incomplete
    unknown_word_weight: Incomplete
    emb_layer: Incomplete
    def __init__(self, vocab: List[str], word_weights: Dict[str, float], unknown_word_weight: float = 1) -> None:
        """

        :param vocab:
            Vocabulary of the tokenizer
        :param word_weights:
            Mapping of tokens to a float weight value. Words embeddings are multiplied by  this float value. Tokens in word_weights must not be equal to the vocab (can contain more or less values)
        :param unknown_word_weight:
            Weight for words in vocab, that do not appear in the word_weights lookup. These can be for example rare words in the vocab, where no weight exists.
        """
    def forward(self, features: Dict[str, Tensor]): ...
    def get_config_dict(self): ...
    def save(self, output_path) -> None: ...
    @staticmethod
    def load(input_path): ...
