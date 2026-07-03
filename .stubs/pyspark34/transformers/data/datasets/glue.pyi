from ...tokenization_utils_base import PreTrainedTokenizerBase as PreTrainedTokenizerBase
from ...utils import logging as logging
from ..processors.glue import glue_convert_examples_to_features as glue_convert_examples_to_features, glue_output_modes as glue_output_modes, glue_processors as glue_processors
from ..processors.utils import InputFeatures as InputFeatures
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from torch.utils.data import Dataset
from typing import List, Optional, Union

logger: Incomplete

@dataclass
class GlueDataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.

    Using `HfArgumentParser` we can turn this class into argparse arguments to be able to specify them on the command
    line.
    """
    task_name: str = ...
    data_dir: str = ...
    max_seq_length: int = ...
    overwrite_cache: bool = ...
    def __post_init__(self) -> None: ...
    def __init__(self, task_name, data_dir, max_seq_length, overwrite_cache) -> None: ...

class Split(Enum):
    train: str
    dev: str
    test: str

class GlueDataset(Dataset):
    """
    This will be superseded by a framework-agnostic approach soon.
    """
    args: GlueDataTrainingArguments
    output_mode: str
    features: List[InputFeatures]
    processor: Incomplete
    label_list: Incomplete
    def __init__(self, args: GlueDataTrainingArguments, tokenizer: PreTrainedTokenizerBase, limit_length: Optional[int] = None, mode: Union[str, Split] = ..., cache_dir: Optional[str] = None) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i) -> InputFeatures: ...
    def get_labels(self): ...
