from transformers import BertConfig as BertConfig, BertForPreTraining as BertForPreTraining, load_tf_weights_in_bert as load_tf_weights_in_bert
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, bert_config_file, pytorch_dump_path) -> None: ...
