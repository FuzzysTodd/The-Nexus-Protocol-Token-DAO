from . import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from ..utils import CacheNotFound as CacheNotFound, HFCacheInfo as HFCacheInfo, scan_cache_dir as scan_cache_dir
from ._cli_utils import ANSI as ANSI, tabulate as tabulate
from _typeshed import Incomplete
from argparse import Namespace, _SubParsersAction

class ScanCacheCommand(BaseHuggingfaceCLICommand):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    verbosity: Incomplete
    cache_dir: Incomplete
    def __init__(self, args: Namespace) -> None: ...
    def run(self) -> None: ...
