from _typeshed import Incomplete
from transformers import BloomConfig as BloomConfig, BloomModel as BloomModel
from transformers.file_utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME
from transformers.utils import logging as logging

WEIGHTS_TO_AVERAGE_ENDSWITH: Incomplete
WEIGHTS_WITH_ROW_PARALLELISM_CONTAIN: Incomplete

def layer_name_mapping(key, file):
    """Convert Megatron-DeepSpeed TP/PP weights mapping in transformers PP only"""
def get_dtype_size(dtype): ...
def convert_bloom_checkpoint_to_pytorch(bloom_checkpoint_path, bloom_config_file, pytorch_dump_folder_path, shard_model, pretraining_tp): ...
