from _typeshed import Incomplete
from transformers import GLPNConfig as GLPNConfig, GLPNFeatureExtractor as GLPNFeatureExtractor, GLPNForDepthEstimation as GLPNForDepthEstimation
from transformers.utils import logging as logging

logger: Incomplete

def rename_keys(state_dict): ...
def read_in_k_v(state_dict, config) -> None: ...
def prepare_img(): ...
def convert_glpn_checkpoint(checkpoint_path, pytorch_dump_folder_path, push_to_hub: bool = False, model_name: Incomplete | None = None) -> None:
    """
    Copy/paste/tweak model's weights to our GLPN structure.
    """
