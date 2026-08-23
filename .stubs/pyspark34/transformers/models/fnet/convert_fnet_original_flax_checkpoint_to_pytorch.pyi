from transformers import FNetConfig as FNetConfig, FNetForPreTraining as FNetForPreTraining
from transformers.utils import logging as logging

def convert_flax_checkpoint_to_pytorch(flax_checkpoint_path, fnet_config_file, save_path) -> None: ...
