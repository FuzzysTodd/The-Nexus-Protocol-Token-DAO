from _typeshed import Incomplete
from torch import nn
from typing import Dict, List

logger: Incomplete

class T5(nn.Module):
    """DEPRECATED: Please use models.Transformer instead.

    T5 model to generate token embeddings.

    Each token is mapped to an output vector from BERT.
    """
    config_keys: Incomplete
    do_lower_case: Incomplete
    max_seq_length: Incomplete
    t5model: Incomplete
    tokenizer: Incomplete
    task_identifier: Incomplete
    def __init__(self, model_name_or_path: str, max_seq_length: int = 128, do_lower_case: bool | None = None, task_identifier: str = 'stsb sentence1: ', model_args: Dict = {}, tokenizer_args: Dict = {}) -> None: ...
    def forward(self, features):
        """Returns token_embeddings, cls_token"""
    def get_word_embedding_dimension(self) -> int: ...
    def tokenize(self, text: str) -> List[int]:
        """
        Tokenizes a text and maps tokens to token-ids
        """
    def get_sentence_features(self, tokens: List[int], pad_seq_length: int):
        """
        Convert tokenized sentence in its embedding ids, segment ids and mask

        :param tokens:
            a tokenized sentence
        :param pad_seq_length:
            the maximal length of the sequence. Cannot be greater than self.sentence_transformer_config.max_seq_length
        :return: embedding ids, segment ids and mask for the sentence
        """
    def get_config_dict(self): ...
    def save(self, output_path: str): ...
    @staticmethod
    def load(input_path: str): ...
