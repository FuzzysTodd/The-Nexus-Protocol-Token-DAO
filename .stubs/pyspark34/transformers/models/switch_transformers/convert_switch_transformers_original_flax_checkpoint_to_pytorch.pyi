from _typeshed import Incomplete
from transformers import SwitchTransformersConfig as SwitchTransformersConfig, SwitchTransformersForConditionalGeneration as SwitchTransformersForConditionalGeneration
from transformers.modeling_flax_pytorch_utils import load_flax_weights_in_pytorch_model as load_flax_weights_in_pytorch_model
from transformers.utils import logging as logging

MOE_LAYER_NAME_MAPPING: Incomplete

def rename_keys(s_dict): ...

GIN_TO_CONFIG_MAPPING: Incomplete

def convert_gin_to_config(gin_file, num_experts): ...
def convert_flax_checkpoint_to_pytorch(flax_checkpoint_path, config_file, gin_file: Incomplete | None = None, pytorch_dump_path: str = './', num_experts: int = 8) -> None: ...
