import jax.numpy as jnp
import numpy as np
from .utils import logging as logging
from _typeshed import Incomplete
from typing import Dict, Tuple

logger: Incomplete

def load_pytorch_checkpoint_in_flax_state_dict(flax_model, pytorch_checkpoint_path, is_sharded, allow_missing_keys: bool = False):
    """Load pytorch checkpoints in a flax model"""
def rename_key_and_reshape_tensor(pt_tuple_key: Tuple[str], pt_tensor: np.ndarray, random_flax_state_dict: Dict[str, jnp.ndarray], model_prefix: str) -> tuple[Tuple[str], np.ndarray]:
    """Rename PT weight names to corresponding Flax weight names and reshape tensor if necessary"""
def convert_pytorch_state_dict_to_flax(pt_state_dict, flax_model): ...
def convert_pytorch_sharded_state_dict_to_flax(shard_filenames, flax_model): ...
def load_flax_checkpoint_in_pytorch_model(model, flax_checkpoint_path):
    """Load flax checkpoints in a PyTorch model"""
def load_flax_weights_in_pytorch_model(pt_model, flax_state):
    """Load flax checkpoints in a PyTorch model"""
