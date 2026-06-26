from transformers import MobileBertConfig as MobileBertConfig, MobileBertForPreTraining as MobileBertForPreTraining, load_tf_weights_in_mobilebert as load_tf_weights_in_mobilebert
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, mobilebert_config_file, pytorch_dump_path) -> None: ...
