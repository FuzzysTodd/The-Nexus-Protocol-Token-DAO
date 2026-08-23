from .common_utils import print_error as print_error, print_warning as print_warning
from _typeshed import Incomplete

def check_output_command(file_path, head: Incomplete | None = None, tail: Incomplete | None = None):
    """call check_output command to read content from a file"""
def kill_command(pid, timeout: int = 60) -> None:
    """Kill the process of pid (with a terminate signal).
    Waiting up to 60 seconds until the process is killed.
    """
def install_package_command(package_name) -> None:
    """
    Install python package from pip.

    Parameters
    ----------
    package_name: str
        The name of package to be installed.
    """
def install_requirements_command(requirements_path):
    """
    Install packages from `requirements.txt` in `requirements_path`.

    Parameters
    ----------
    requirements_path: str
        Path to the directory that contains `requirements.txt`.
    """
def call_pip_install(source): ...
def call_pip_uninstall(module_name): ...
