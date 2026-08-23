from .. import AutoFeatureExtractor as AutoFeatureExtractor, AutoProcessor as AutoProcessor, AutoTokenizer as AutoTokenizer
from ..utils import logging as logging
from ..utils.import_utils import is_optimum_available as is_optimum_available
from .convert import export as export, validate_model_outputs as validate_model_outputs
from .features import FeaturesManager as FeaturesManager
from .utils import get_preprocessor as get_preprocessor
from _typeshed import Incomplete

MIN_OPTIMUM_VERSION: str
ENCODER_DECODER_MODELS: Incomplete

def export_with_optimum(args) -> None: ...
def export_with_transformers(args) -> None: ...
def main() -> None: ...
