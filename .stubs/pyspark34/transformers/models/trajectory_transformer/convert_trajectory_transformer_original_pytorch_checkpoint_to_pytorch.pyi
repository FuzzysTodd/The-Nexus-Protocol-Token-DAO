import trajectory.utils as utils
from transformers import TrajectoryTransformerModel as TrajectoryTransformerModel

class Parser(utils.Parser):
    dataset: str
    config: str

def convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch(logbase, dataset, loadpath, epoch, device) -> None:
    """Converting Sequential blocks to ModuleList"""
