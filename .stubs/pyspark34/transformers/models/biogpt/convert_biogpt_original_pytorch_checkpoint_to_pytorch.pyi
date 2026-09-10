from _typeshed import Incomplete
from transformers import BioGptConfig as BioGptConfig, BioGptForCausalLM as BioGptForCausalLM
from transformers.models.biogpt.tokenization_biogpt import VOCAB_FILES_NAMES as VOCAB_FILES_NAMES
from transformers.tokenization_utils_base import TOKENIZER_CONFIG_FILE as TOKENIZER_CONFIG_FILE
from transformers.utils import WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

json_indent: int

class Dictionary:
    """A mapping from symbols to consecutive integers"""
    symbols: Incomplete
    count: Incomplete
    indices: Incomplete
    bos_index: Incomplete
    pad_index: Incomplete
    eos_index: Incomplete
    unk_index: Incomplete
    nspecial: Incomplete
    def __init__(self, *, bos: str = '<s>', pad: str = '<pad>', eos: str = '</s>', unk: str = '<unk>', extra_special_symbols: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int:
        """Returns the number of symbols in the dictionary"""
    def __contains__(self, sym) -> bool: ...
    @classmethod
    def load(cls, f):
        """Loads the dictionary from a text file with the format:

        ```
        <symbol0> <count0>
        <symbol1> <count1>
        ...
        ```
        """
    def add_symbol(self, word, n: int = 1, overwrite: bool = False):
        """Adds a word to the dictionary"""
    def add_from_file(self, f) -> None:
        """
        Loads a pre-existing dictionary from a text file and adds its symbols to this instance.
        """

def rewrite_dict_keys(d): ...
def convert_biogpt_checkpoint_to_pytorch(biogpt_checkpoint_path, pytorch_dump_folder_path) -> None: ...
