from .utils import ExplicitEnum as ExplicitEnum, expand_dims as expand_dims, is_numpy_array as is_numpy_array, is_torch_tensor as is_torch_tensor, logging as logging, reshape as reshape, squeeze as squeeze, tensor_size as tensor_size
from _typeshed import Incomplete

logger: Incomplete

class TransposeType(ExplicitEnum):
    """
    Possible ...
    """
    NO: str
    SIMPLE: str
    CONV1D: str
    CONV2D: str

def convert_tf_weight_name_to_pt_weight_name(tf_name, start_prefix_to_remove: str = '', tf_weight_shape: Incomplete | None = None):
    """
    Convert a TF 2.0 model variable name in a pytorch model weight name.

    Conventions for TF2.0 scopes -> PyTorch attribute names conversions:

        - '$1___$2' is replaced by $2 (can be used to duplicate or remove layers in TF2.0 vs PyTorch)
        - '_._' is replaced by a new level separation (can be used to convert TF2.0 lists in PyTorch nn.ModulesList)

    return tuple with:

        - pytorch model weight name
        - transpose: `TransposeType` member indicating whether and how TF2.0 and PyTorch weights matrices should be
          transposed with regards to each other
    """
def apply_transpose(transpose: TransposeType, weight, match_shape: Incomplete | None = None, pt_to_tf: bool = True):
    """
    Apply a transpose to some weight then tries to reshape the weight to the same shape as a given shape, all in a
    framework agnostic way.
    """
def load_pytorch_checkpoint_in_tf2_model(tf_model, pytorch_checkpoint_path, tf_inputs: Incomplete | None = None, allow_missing_keys: bool = False, output_loading_info: bool = False):
    """Load pytorch checkpoints in a TF 2.0 model"""
def load_pytorch_model_in_tf2_model(tf_model, pt_model, tf_inputs: Incomplete | None = None, allow_missing_keys: bool = False):
    """Load pytorch checkpoints in a TF 2.0 model"""
def load_pytorch_weights_in_tf2_model(tf_model, pt_state_dict, tf_inputs: Incomplete | None = None, allow_missing_keys: bool = False, output_loading_info: bool = False):
    """Load pytorch state_dict in a TF 2.0 model."""
def load_pytorch_state_dict_in_tf2_model(tf_model, pt_state_dict, tf_inputs: Incomplete | None = None, allow_missing_keys: bool = False, output_loading_info: bool = False):
    """Load a pytorch state_dict in a TF 2.0 model."""
def load_tf2_checkpoint_in_pytorch_model(pt_model, tf_checkpoint_path, tf_inputs: Incomplete | None = None, allow_missing_keys: bool = False, output_loading_info: bool = False):
    """
    Load TF 2.0 HDF5 checkpoint in a PyTorch model We use HDF5 to easily do transfer learning (see
    https://github.com/tensorflow/tensorflow/blob/ee16fcac960ae660e0e4496658a366e2f745e1f0/tensorflow/python/keras/engine/network.py#L1352-L1357).
    """
def load_tf2_model_in_pytorch_model(pt_model, tf_model, allow_missing_keys: bool = False, output_loading_info: bool = False):
    """Load TF 2.0 model in a pytorch model"""
def load_tf2_weights_in_pytorch_model(pt_model, tf_weights, allow_missing_keys: bool = False, output_loading_info: bool = False):
    """Load TF2.0 symbolic weights in a PyTorch model"""
def load_tf2_state_dict_in_pytorch_model(pt_model, tf_state_dict, allow_missing_keys: bool = False, output_loading_info: bool = False): ...
