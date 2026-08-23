import torch
from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from torch.utils.data import Dataset
from typing import Dict, List, Optional

logger: Incomplete
DEPRECATION_WARNING: str

class TextDataset(Dataset):
    """
    This will be superseded by a framework-agnostic approach soon.
    """
    examples: Incomplete
    def __init__(self, tokenizer: PreTrainedTokenizer, file_path: str, block_size: int, overwrite_cache: bool = False, cache_dir: Optional[str] = None) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i) -> torch.Tensor: ...

class LineByLineTextDataset(Dataset):
    """
    This will be superseded by a framework-agnostic approach soon.
    """
    examples: Incomplete
    def __init__(self, tokenizer: PreTrainedTokenizer, file_path: str, block_size: int) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i) -> Dict[str, torch.tensor]: ...

class LineByLineWithRefDataset(Dataset):
    """
    This will be superseded by a framework-agnostic approach soon.
    """
    examples: Incomplete
    def __init__(self, tokenizer: PreTrainedTokenizer, file_path: str, block_size: int, ref_path: str) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i) -> Dict[str, torch.tensor]: ...

class LineByLineWithSOPTextDataset(Dataset):
    """
    Dataset for sentence order prediction task, prepare sentence pairs for SOP task
    """
    examples: Incomplete
    def __init__(self, tokenizer: PreTrainedTokenizer, file_dir: str, block_size: int) -> None: ...
    def create_examples_from_document(self, document, block_size, tokenizer, short_seq_prob: float = 0.1):
        """Creates examples for a single document."""
    def __len__(self) -> int: ...
    def __getitem__(self, i) -> Dict[str, torch.tensor]: ...

class TextDatasetForNextSentencePrediction(Dataset):
    """
    This will be superseded by a framework-agnostic approach soon.
    """
    short_seq_probability: Incomplete
    nsp_probability: Incomplete
    tokenizer: Incomplete
    examples: Incomplete
    documents: Incomplete
    def __init__(self, tokenizer: PreTrainedTokenizer, file_path: str, block_size: int, overwrite_cache: bool = False, short_seq_probability: float = 0.1, nsp_probability: float = 0.5) -> None: ...
    def create_examples_from_document(self, document: List[List[int]], doc_index: int, block_size: int):
        """Creates examples for a single document."""
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
