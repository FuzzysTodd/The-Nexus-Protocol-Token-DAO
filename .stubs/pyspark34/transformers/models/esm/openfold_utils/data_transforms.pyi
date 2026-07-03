import numpy as np
import torch
from .tensor_utils import tensor_tree_map as tensor_tree_map, tree_map as tree_map
from typing import Dict

def make_atom14_masks(protein: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
    """Construct denser atom positions (14 dimensions instead of 37)."""
def make_atom14_masks_np(batch: Dict[str, torch.Tensor]) -> Dict[str, np.ndarray]: ...
