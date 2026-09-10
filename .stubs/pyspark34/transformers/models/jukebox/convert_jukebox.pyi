from _typeshed import Incomplete
from transformers import JukeboxConfig as JukeboxConfig, JukeboxModel as JukeboxModel
from transformers.utils import logging as logging

logger: Incomplete
PREFIX: str
MODEL_MAPPING: Incomplete

def replace_key(key): ...
def fix_jukebox_keys(state_dict, model_state_dict, key_prefix, mapping): ...
def convert_openai_checkpoint(model_name: Incomplete | None = None, pytorch_dump_folder_path: Incomplete | None = None):
    """
    Copy/paste/tweak model's weights to our Jukebox structure.
    """
