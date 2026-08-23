from pip._internal.cli.main_parser import create_main_parser as create_main_parser
from pip._internal.commands import commands_dict as commands_dict, create_command as create_command
from pip._internal.metadata import get_default_environment as get_default_environment
from typing import Any, Iterable, List

def autocomplete() -> None:
    """Entry Point for completion of main and subcommand options."""
def get_path_completion_type(cwords: List[str], cword: int, opts: Iterable[Any]) -> str | None:
    """Get the type of path completion (``file``, ``dir``, ``path`` or None)

    :param cwords: same as the environmental variable ``COMP_WORDS``
    :param cword: same as the environmental variable ``COMP_CWORD``
    :param opts: The available options to check
    :return: path completion type (``file``, ``dir``, ``path`` or None)
    """
def auto_complete_paths(current: str, completion_type: str) -> Iterable[str]:
    """If ``completion_type`` is ``file`` or ``path``, list all regular files
    and directories starting with ``current``; otherwise only list directories
    starting with ``current``.

    :param current: The word to be completed
    :param completion_type: path completion type(``file``, ``path`` or ``dir``)
    :return: A generator of regular files and/or directories
    """
