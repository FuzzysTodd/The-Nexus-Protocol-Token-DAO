from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.exceptions import CommandError as CommandError, PipError as PipError
from pip._internal.utils import filesystem as filesystem
from pip._internal.utils.logging import getLogger as getLogger
from typing import Any, List

logger: Incomplete

class CacheCommand(Command):
    """
    Inspect and manage pip's wheel cache.

    Subcommands:

    - dir: Show the cache directory.
    - info: Show information about the cache.
    - list: List filenames of packages stored in the cache.
    - remove: Remove one or more package from the cache.
    - purge: Remove all items from the cache.

    ``<pattern>`` can be a glob expression or a package name.
    """
    ignore_require_venv: bool
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
    def get_cache_dir(self, options: Values, args: List[Any]) -> None: ...
    def get_cache_info(self, options: Values, args: List[Any]) -> None: ...
    def list_cache_items(self, options: Values, args: List[Any]) -> None: ...
    def format_for_human(self, files: List[str]) -> None: ...
    def format_for_abspath(self, files: List[str]) -> None: ...
    def remove_cache_items(self, options: Values, args: List[Any]) -> None: ...
    def purge_cache(self, options: Values, args: List[Any]) -> None: ...
