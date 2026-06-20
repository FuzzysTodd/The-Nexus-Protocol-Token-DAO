from transformers import GPTNeoConfig as GPTNeoConfig, GPTNeoForCausalLM as GPTNeoForCausalLM, load_tf_weights_in_gpt_neo as load_tf_weights_in_gpt_neo
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, config_file, pytorch_dump_path) -> None: ...
