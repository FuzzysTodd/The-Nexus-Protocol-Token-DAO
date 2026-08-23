from _typeshed import Incomplete
from transformers import FlavaImageCodebook as FlavaImageCodebook, FlavaImageCodebookConfig as FlavaImageCodebookConfig

def rreplace(s, old, new, occurrence): ...
def count_parameters(state_dict): ...
def upgrade_state_dict(state_dict): ...
def convert_dalle_checkpoint(checkpoint_path, pytorch_dump_folder_path, config_path: Incomplete | None = None, save_checkpoint: bool = True):
    """
    Copy/paste/tweak model's weights to transformers design.
    """
