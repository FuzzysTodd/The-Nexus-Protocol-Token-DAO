from _typeshed import Incomplete
from pip._internal.cli.base_command import Command as Command
from typing import Any, Dict, NamedTuple

class CommandInfo(NamedTuple):
    module_path: Incomplete
    class_name: Incomplete
    summary: Incomplete

commands_dict: Dict[str, CommandInfo]

def create_command(name: str, **kwargs: Any) -> Command:
    """
    Create an instance of the Command class with the given name.
    """
def get_similar_commands(name: str) -> str | None:
    """Command name auto-correct."""
