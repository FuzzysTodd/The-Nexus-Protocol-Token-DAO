from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from ..utils import logging as logging
from argparse import ArgumentParser, Namespace

def convert_command_factory(args: Namespace):
    """
    Factory function used to convert a model TF 1.0 checkpoint in a PyTorch checkpoint.

    Returns: ServeCommand
    """

IMPORT_ERROR_MESSAGE: str

class ConvertCommand(BaseTransformersCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        """
        Register this command to argparse so it's available for the transformer-cli

        Args:
            parser: Root parser to register command-specific arguments
        """
    def __init__(self, model_type: str, tf_checkpoint: str, pytorch_dump_output: str, config: str, finetuning_task_name: str, *args) -> None: ...
    def run(self) -> None: ...
