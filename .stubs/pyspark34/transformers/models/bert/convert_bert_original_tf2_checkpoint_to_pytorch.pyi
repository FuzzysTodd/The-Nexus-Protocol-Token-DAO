from _typeshed import Incomplete
from transformers import BertConfig as BertConfig, BertModel as BertModel
from transformers.utils import logging as logging

logger: Incomplete

def load_tf2_weights_in_bert(model, tf_checkpoint_path, config): ...
def convert_tf2_checkpoint_to_pytorch(tf_checkpoint_path, config_path, pytorch_dump_path) -> None: ...
