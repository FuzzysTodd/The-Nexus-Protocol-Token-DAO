from _typeshed import Incomplete
from transformers import BlenderbotConfig as BlenderbotConfig, BlenderbotForConditionalGeneration as BlenderbotForConditionalGeneration
from transformers.utils import logging as logging

logger: Incomplete
PATTERNS: Incomplete

def rename_state_dict_key(k): ...
def rename_layernorm_keys(sd) -> None: ...

IGNORE_KEYS: Incomplete

def convert_parlai_checkpoint(checkpoint_path, pytorch_dump_folder_path, config_json_path) -> None:
    """
    Copy/paste/tweak model's weights to our BERT structure.
    """
