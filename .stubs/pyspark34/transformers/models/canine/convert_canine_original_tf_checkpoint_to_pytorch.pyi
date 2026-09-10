from transformers import CanineConfig as CanineConfig, CanineModel as CanineModel, CanineTokenizer as CanineTokenizer, load_tf_weights_in_canine as load_tf_weights_in_canine
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, pytorch_dump_path) -> None: ...
