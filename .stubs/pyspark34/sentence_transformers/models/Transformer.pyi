from _typeshed import Incomplete
from torch import nn
from typing import Dict, List, Tuple

class Transformer(nn.Module):
    """Huggingface AutoModel to generate token embeddings.
    Loads the correct class, e.g. BERT / RoBERTa etc.

    :param model_name_or_path: Huggingface models name (https://huggingface.co/models)
    :param max_seq_length: Truncate any inputs longer than max_seq_length
    :param model_args: Arguments (key, value pairs) passed to the Huggingface Transformers model
    :param cache_dir: Cache dir for Huggingface Transformers to store/load models
    :param tokenizer_args: Arguments (key, value pairs) passed to the Huggingface Tokenizer model
    :param do_lower_case: If true, lowercases the input (independent if the model is cased or not)
    :param tokenizer_name_or_path: Name or path of the tokenizer. When None, then model_name_or_path is used
    """
    config_keys: Incomplete
    do_lower_case: Incomplete
    auto_model: Incomplete
    tokenizer: Incomplete
    max_seq_length: Incomplete
    def __init__(self, model_name_or_path: str, max_seq_length: int | None = None, model_args: Dict = {}, cache_dir: str | None = None, tokenizer_args: Dict = {}, do_lower_case: bool = False, tokenizer_name_or_path: str = None) -> None: ...
    def forward(self, features):
        """Returns token_embeddings, cls_token"""
    def get_word_embedding_dimension(self) -> int: ...
    def tokenize(self, texts: List[str] | List[Dict] | List[Tuple[str, str]]):
        """
        Tokenizes a text and maps tokens to token-ids
        """
    def get_config_dict(self): ...
    def save(self, output_path: str): ...
    @staticmethod
    def load(input_path: str): ...
