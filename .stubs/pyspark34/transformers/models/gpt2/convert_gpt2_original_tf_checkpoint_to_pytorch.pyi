from transformers import GPT2Config as GPT2Config, GPT2Model as GPT2Model, load_tf_weights_in_gpt2 as load_tf_weights_in_gpt2
from transformers.utils import CONFIG_NAME as CONFIG_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging

def convert_gpt2_checkpoint_to_pytorch(gpt2_checkpoint_path, gpt2_config_file, pytorch_dump_folder_path) -> None: ...
