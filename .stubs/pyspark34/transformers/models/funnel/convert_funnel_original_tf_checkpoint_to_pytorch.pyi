from transformers import FunnelBaseModel as FunnelBaseModel, FunnelConfig as FunnelConfig, FunnelModel as FunnelModel, load_tf_weights_in_funnel as load_tf_weights_in_funnel
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, config_file, pytorch_dump_path, base_model) -> None: ...
