from _typeshed import Incomplete
from transformers import DeformableDetrConfig as DeformableDetrConfig, DeformableDetrFeatureExtractor as DeformableDetrFeatureExtractor, DeformableDetrForObjectDetection as DeformableDetrForObjectDetection
from transformers.utils import logging as logging

logger: Incomplete

def rename_key(orig_key): ...
def read_in_q_k_v(state_dict) -> None: ...
def prepare_img(): ...
def convert_deformable_detr_checkpoint(checkpoint_path, single_scale, dilation, with_box_refine, two_stage, pytorch_dump_folder_path, push_to_hub) -> None:
    """
    Copy/paste/tweak model's weights to our Deformable DETR structure.
    """
