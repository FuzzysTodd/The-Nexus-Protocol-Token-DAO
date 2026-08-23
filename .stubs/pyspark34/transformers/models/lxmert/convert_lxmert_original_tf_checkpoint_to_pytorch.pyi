from transformers import LxmertConfig as LxmertConfig, LxmertForPreTraining as LxmertForPreTraining, load_tf_weights_in_lxmert as load_tf_weights_in_lxmert
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, config_file, pytorch_dump_path) -> None: ...
