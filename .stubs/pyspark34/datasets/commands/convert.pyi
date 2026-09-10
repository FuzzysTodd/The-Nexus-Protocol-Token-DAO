from _typeshed import Incomplete
from argparse import ArgumentParser, Namespace
from datasets.commands import BaseDatasetsCLICommand as BaseDatasetsCLICommand
from datasets.utils.logging import get_logger as get_logger

HIGHLIGHT_MESSAGE_PRE: str
HIGHLIGHT_MESSAGE_POST: str
TO_HIGHLIGHT: Incomplete
TO_CONVERT: Incomplete

def convert_command_factory(args: Namespace):
    """
    Factory function used to convert a model TF 1.0 checkpoint in a PyTorch checkpoint.

    Returns: ConvertCommand
    """

class ConvertCommand(BaseDatasetsCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        """
        Register this command to argparse so it's available for the datasets-cli

        Args:
            parser: Root parser to register command-specific arguments
        """
    def __init__(self, tfds_path: str, datasets_directory: str, *args) -> None: ...
    def run(self): ...
