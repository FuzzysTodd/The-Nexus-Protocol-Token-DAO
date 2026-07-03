from _typeshed import Incomplete
from pip._internal.cli.spinners import open_spinner as open_spinner
from pip._internal.utils.setuptools_build import make_setuptools_bdist_wheel_args as make_setuptools_bdist_wheel_args
from pip._internal.utils.subprocess import call_subprocess as call_subprocess, format_command_args as format_command_args
from typing import List

logger: Incomplete

def format_command_result(command_args: List[str], command_output: str) -> str:
    """Format command information for logging."""
def get_legacy_build_wheel_path(names: List[str], temp_dir: str, name: str, command_args: List[str], command_output: str) -> str | None:
    """Return the path to the wheel in the temporary build directory."""
def build_wheel_legacy(name: str, setup_py_path: str, source_dir: str, global_options: List[str], build_options: List[str], tempd: str) -> str | None:
    '''Build one unpacked package using the "legacy" build process.

    Returns path to wheel if successfully built. Otherwise, returns None.
    '''
