from transformers import RemBertConfig as RemBertConfig, RemBertModel as RemBertModel, load_tf_weights_in_rembert as load_tf_weights_in_rembert
from transformers.utils import logging as logging

def convert_rembert_tf_checkpoint_to_pytorch(tf_checkpoint_path, bert_config_file, pytorch_dump_path) -> None: ...
