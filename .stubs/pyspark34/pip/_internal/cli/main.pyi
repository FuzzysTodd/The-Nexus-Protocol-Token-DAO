from _typeshed import Incomplete
from pip._internal.cli.autocompletion import autocomplete as autocomplete
from pip._internal.cli.main_parser import parse_command as parse_command
from pip._internal.commands import create_command as create_command
from pip._internal.exceptions import PipError as PipError
from pip._internal.utils import deprecation as deprecation
from typing import List

logger: Incomplete

def main(args: List[str] | None = None) -> int: ...
