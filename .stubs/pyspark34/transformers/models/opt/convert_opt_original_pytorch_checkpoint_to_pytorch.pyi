from _typeshed import Incomplete
from transformers import OPTConfig as OPTConfig, OPTModel as OPTModel
from transformers.utils import logging as logging

logger: Incomplete

def load_checkpoint(checkpoint_path):
    """Checkpoint path should end in model.pt"""
def convert_opt_checkpoint(checkpoint_path, pytorch_dump_folder_path, config: Incomplete | None = None) -> None:
    """
    Copy/paste/tweak model's weights to our BERT structure.
    """
