from transformers import RoFormerConfig as RoFormerConfig, RoFormerForMaskedLM as RoFormerForMaskedLM, load_tf_weights_in_roformer as load_tf_weights_in_roformer
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, bert_config_file, pytorch_dump_path) -> None: ...
