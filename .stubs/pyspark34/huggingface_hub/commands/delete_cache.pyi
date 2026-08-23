from . import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from ..utils import CachedRepoInfo as CachedRepoInfo, CachedRevisionInfo as CachedRevisionInfo, HFCacheInfo as HFCacheInfo, scan_cache_dir as scan_cache_dir
from ._cli_utils import ANSI as ANSI
from _typeshed import Incomplete
from argparse import Namespace, _SubParsersAction
from typing import Callable

def require_inquirer_py(fn: Callable) -> Callable:
    """Decorator to flag methods that require `InquirerPy`."""

class DeleteCacheCommand(BaseHuggingfaceCLICommand):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    cache_dir: Incomplete
    disable_tui: Incomplete
    def __init__(self, args: Namespace) -> None: ...
    def run(self) -> None:
        """Run `delete-cache` command with or without TUI."""
