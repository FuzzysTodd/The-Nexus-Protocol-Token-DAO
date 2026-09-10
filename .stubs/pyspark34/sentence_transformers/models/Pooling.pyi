from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict

class Pooling(nn.Module):
    """Performs pooling (max or mean) on the token embeddings.

    Using pooling, it generates from a variable sized sentence a fixed sized sentence embedding. This layer also allows to use the CLS token if it is returned by the underlying word embedding model.
    You can concatenate multiple poolings together.

    :param word_embedding_dimension: Dimensions for the word embeddings
    :param pooling_mode: Can be a string: mean/max/cls. If set, overwrites the other pooling_mode_* settings
    :param pooling_mode_cls_token: Use the first token (CLS token) as text representations
    :param pooling_mode_max_tokens: Use max in each dimension over all tokens.
    :param pooling_mode_mean_tokens: Perform mean-pooling
    :param pooling_mode_mean_sqrt_len_tokens: Perform mean-pooling, but devide by sqrt(input_length).
    """
    config_keys: Incomplete
    word_embedding_dimension: Incomplete
    pooling_mode_cls_token: Incomplete
    pooling_mode_mean_tokens: Incomplete
    pooling_mode_max_tokens: Incomplete
    pooling_mode_mean_sqrt_len_tokens: Incomplete
    pooling_output_dimension: Incomplete
    def __init__(self, word_embedding_dimension: int, pooling_mode: str = None, pooling_mode_cls_token: bool = False, pooling_mode_max_tokens: bool = False, pooling_mode_mean_tokens: bool = True, pooling_mode_mean_sqrt_len_tokens: bool = False) -> None: ...
    def get_pooling_mode_str(self) -> str:
        """
        Returns the pooling mode as string
        """
    def forward(self, features: Dict[str, Tensor]): ...
    def get_sentence_embedding_dimension(self): ...
    def get_config_dict(self): ...
    def save(self, output_path) -> None: ...
    @staticmethod
    def load(input_path): ...
