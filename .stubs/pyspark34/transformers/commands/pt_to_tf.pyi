from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from .. import AutoConfig as AutoConfig, AutoFeatureExtractor as AutoFeatureExtractor, AutoImageProcessor as AutoImageProcessor, AutoProcessor as AutoProcessor, AutoTokenizer as AutoTokenizer, FEATURE_EXTRACTOR_MAPPING as FEATURE_EXTRACTOR_MAPPING, IMAGE_PROCESSOR_MAPPING as IMAGE_PROCESSOR_MAPPING, PROCESSOR_MAPPING as PROCESSOR_MAPPING, TOKENIZER_MAPPING as TOKENIZER_MAPPING, is_datasets_available as is_datasets_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available
from ..utils import TF2_WEIGHTS_INDEX_NAME as TF2_WEIGHTS_INDEX_NAME, TF2_WEIGHTS_NAME as TF2_WEIGHTS_NAME, logging as logging
from argparse import ArgumentParser, Namespace

MAX_ERROR: float

def convert_command_factory(args: Namespace):
    """
    Factory function used to convert a model PyTorch checkpoint in a TensorFlow 2 checkpoint.

    Returns: ServeCommand
    """

class PTtoTFCommand(BaseTransformersCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        """
        Register this command to argparse so it's available for the transformer-cli

        Args:
            parser: Root parser to register command-specific arguments
        """
    @staticmethod
    def find_pt_tf_differences(pt_outputs, tf_outputs):
        """
        Compares the TensorFlow and PyTorch outputs, returning a dictionary with all tensor differences.
        """
    def __init__(self, model_name: str, local_dir: str, max_error: float, new_weights: bool, no_pr: bool, push: bool, extra_commit_description: str, *args) -> None: ...
    def get_inputs(self, pt_model, config):
        """
        Returns the right inputs for the model, based on its signature.
        """
    def run(self) -> None: ...
