from datasets.commands.convert import ConvertCommand as ConvertCommand
from datasets.commands.dummy_data import DummyDataCommand as DummyDataCommand
from datasets.commands.env import EnvironmentCommand as EnvironmentCommand
from datasets.commands.run_beam import RunBeamCommand as RunBeamCommand
from datasets.commands.test import TestCommand as TestCommand
from datasets.utils.logging import set_verbosity_info as set_verbosity_info

def parse_unknown_args(unknown_args): ...
def main() -> None: ...
