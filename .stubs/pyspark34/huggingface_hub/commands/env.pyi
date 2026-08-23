from . import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from ..utils import dump_environment_info as dump_environment_info
from _typeshed import Incomplete
from argparse import _SubParsersAction

class EnvironmentCommand(BaseHuggingfaceCLICommand):
    args: Incomplete
    def __init__(self, args) -> None: ...
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    def run(self) -> None: ...
