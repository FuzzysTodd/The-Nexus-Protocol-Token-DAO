from _typeshed import Incomplete
from transformers import FlavaConfig as FlavaConfig, FlavaForPreTraining as FlavaForPreTraining
from transformers.models.flava.convert_dalle_to_flava_codebook import convert_dalle_checkpoint as convert_dalle_checkpoint

def count_parameters(state_dict): ...
def upgrade_state_dict(state_dict, codebook_state_dict): ...
def convert_flava_checkpoint(checkpoint_path, codebook_path, pytorch_dump_folder_path, config_path: Incomplete | None = None) -> None:
    """
    Copy/paste/tweak model's weights to transformers design.
    """
