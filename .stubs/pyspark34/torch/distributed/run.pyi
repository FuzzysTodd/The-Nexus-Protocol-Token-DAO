from _typeshed import Incomplete
from argparse import ArgumentParser
from torch.distributed.argparse_util import check_env as check_env, env as env
from torch.distributed.elastic.multiprocessing import Std as Std
from torch.distributed.elastic.multiprocessing.errors import record as record
from torch.distributed.elastic.utils import macros as macros
from torch.distributed.elastic.utils.logging import get_logger as get_logger
from torch.distributed.launcher.api import LaunchConfig as LaunchConfig, elastic_launch as elastic_launch
from typing import Callable, List, Tuple

log: Incomplete

def get_args_parser() -> ArgumentParser:
    """Helper function parsing the command line options."""
def parse_args(args): ...
def parse_min_max_nnodes(nnodes: str): ...
def determine_local_world_size(nproc_per_node: str): ...
def get_rdzv_endpoint(args): ...
def get_use_env(args) -> bool:
    """
    Retrieves ``use_env`` from the args.
    ``use_env`` is a legacy argument, if ``use_env`` is False, the
    ``--node-rank`` argument will be transferred to all worker processes.
    ``use_env`` is only used by the ``torch.distributed.launch`` and will
    be deprecated in future releases.
    """
def config_from_args(args) -> Tuple[LaunchConfig, Callable | str, List[str]]: ...
def run_script_path(training_script: str, *training_script_args: str):
    '''
    Runs the provided `training_script` from within this interpreter.
    Usage: `script_as_function("/abs/path/to/script.py", "--arg1", "val1")`
    '''
def run(args) -> None: ...
def main(args: Incomplete | None = None) -> None: ...
