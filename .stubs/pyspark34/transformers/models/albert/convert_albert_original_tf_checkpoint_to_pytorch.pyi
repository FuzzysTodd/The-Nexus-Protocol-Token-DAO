from transformers import AlbertConfig as AlbertConfig, AlbertForPreTraining as AlbertForPreTraining, load_tf_weights_in_albert as load_tf_weights_in_albert
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, albert_config_file, pytorch_dump_path) -> None: ...
