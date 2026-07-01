from transformers import ConvBertConfig as ConvBertConfig, ConvBertModel as ConvBertModel, TFConvBertModel as TFConvBertModel, load_tf_weights_in_convbert as load_tf_weights_in_convbert
from transformers.utils import logging as logging

def convert_orig_tf1_checkpoint_to_pytorch(tf_checkpoint_path, convbert_config_file, pytorch_dump_path) -> None: ...
