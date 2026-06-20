from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.command_context import CommandContextMixIn
from typing import List, Tuple

__all__ = ['Command']

class Command(CommandContextMixIn):
    usage: str
    ignore_require_venv: bool
    name: Incomplete
    summary: Incomplete
    parser: Incomplete
    tempdir_registry: Incomplete
    cmd_opts: Incomplete
    def __init__(self, name: str, summary: str, isolated: bool = False) -> None: ...
    def add_options(self) -> None: ...
    def handle_pip_version_check(self, options: Values) -> None:
        """
        This is a no-op so that commands by default do not do the pip version
        check.
        """
    def run(self, options: Values, args: List[str]) -> int: ...
    def parse_args(self, args: List[str]) -> Tuple[Values, List[str]]: ...
    def main(self, args: List[str]) -> int: ...
