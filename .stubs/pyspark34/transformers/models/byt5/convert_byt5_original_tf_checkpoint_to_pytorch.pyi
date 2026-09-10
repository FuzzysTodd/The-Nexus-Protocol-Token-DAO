from transformers import T5Config as T5Config, T5ForConditionalGeneration as T5ForConditionalGeneration, load_tf_weights_in_t5 as load_tf_weights_in_t5
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, config_file, pytorch_dump_path) -> None: ...
