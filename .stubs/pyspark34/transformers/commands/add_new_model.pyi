from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from ..utils import logging as logging
from _typeshed import Incomplete
from argparse import ArgumentParser, Namespace

logger: Incomplete

def add_new_model_command_factory(args: Namespace): ...

class AddNewModelCommand(BaseTransformersCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser): ...
    def __init__(self, testing: bool, testing_file: str, path: Incomplete | None = None, *args) -> None: ...
    def run(self): ...
