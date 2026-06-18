from _typeshed import Incomplete
from transformers import BigBirdPegasusConfig as BigBirdPegasusConfig, BigBirdPegasusForConditionalGeneration as BigBirdPegasusForConditionalGeneration
from typing import Dict

INIT_COMMON: Incomplete
END_COMMON: Incomplete
DECODER_PATTERNS: Incomplete
REMAINING_PATTERNS: Incomplete
KEYS_TO_IGNORE: Incomplete

def rename_state_dict_key(k, patterns): ...
def convert_bigbird_pegasus(tf_weights: dict, config_update: dict) -> BigBirdPegasusForConditionalGeneration: ...
def get_tf_weights_as_numpy(path) -> Dict: ...
def convert_bigbird_pegasus_ckpt_to_pytorch(ckpt_path: str, save_dir: str, config_update: dict): ...
