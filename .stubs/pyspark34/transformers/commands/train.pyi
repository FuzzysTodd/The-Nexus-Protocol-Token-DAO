from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from ..pipelines import TextClassificationPipeline as TextClassificationPipeline
from ..utils import is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from _typeshed import Incomplete
from argparse import ArgumentParser, Namespace

USE_XLA: bool
USE_AMP: bool

def train_command_factory(args: Namespace):
    """
    Factory function used to instantiate training command from provided command line arguments.

    Returns: TrainCommand
    """

class TrainCommand(BaseTransformersCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        """
        Register this command to argparse so it's available for the transformer-cli

        Args:
            parser: Root parser to register command-specific arguments
        """
    logger: Incomplete
    framework: Incomplete
    output: Incomplete
    column_label: Incomplete
    column_text: Incomplete
    column_id: Incomplete
    pipeline: Incomplete
    train_dataset: Incomplete
    valid_dataset: Incomplete
    validation_split: Incomplete
    train_batch_size: Incomplete
    valid_batch_size: Incomplete
    learning_rate: Incomplete
    adam_epsilon: Incomplete
    def __init__(self, args: Namespace) -> None: ...
    def run(self): ...
    def run_torch(self) -> None: ...
    def run_tf(self) -> None: ...
