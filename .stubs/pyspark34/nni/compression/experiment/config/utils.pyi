from .compression import CompressionConfig as CompressionConfig
from .vessel import CompressionVessel as CompressionVessel
from nni.compression.pytorch.utils import count_flops_params as count_flops_params
from typing import Any, Dict, List, Tuple

KEY_MODULE_NAME: str
KEY_PRUNERS: str
KEY_VESSEL: str
KEY_ORIGINAL_TARGET: str
KEY_THETAS: str

def generate_compression_search_space(config: CompressionConfig, vessel: CompressionVessel) -> Dict[str, Dict]:
    """
    Using config (constraints & priori) and vessel (model-related) to generate the hpo search space.
    """
def parse_params(kwargs: Dict[str, Any]) -> Tuple[Dict[str, str], List[Dict[str, Any]], CompressionVessel, Dict[str, Any], Dict[str, Any]]:
    """
    Parse the parameters received by nni.get_next_parameter().

    Returns
    -------
    Dict[str, str], List[Dict[str, Any]], CompressionVessel, Dict[str, Any], Dict[str, Any]
        The compressor config, compressor config_list, model-related wrapper, evaluation value (flops, params, ...) for the original model,
        parameters of the hpo objective function.
    """
def parse_basic_pruner(pruner_config: Dict[str, str], config_list: List[Dict[str, Any]], vessel: CompressionVessel):
    """
    Parse basic pruner and model-related objects used by pruning scheduler.
    """
