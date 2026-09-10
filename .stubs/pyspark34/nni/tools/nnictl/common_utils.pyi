import filelock
import string
from .constants import ERROR_INFO as ERROR_INFO, NORMAL_INFO as NORMAL_INFO, WARNING_INFO as WARNING_INFO

def get_yml_content(file_path):
    """Load yaml file content"""
def get_json_content(file_path):
    """Load json file content"""
def print_error(*content) -> None:
    """Print error information to screen"""
def print_green(*content) -> None:
    """Print information to screen in green"""
def print_normal(*content) -> None:
    """Print error information to screen"""
def print_warning(*content) -> None:
    """Print warning information to screen"""
def detect_process(pid):
    """Detect if a process is alive"""
def detect_port(port):
    """Detect if the port is used"""
def get_user(): ...
def generate_temp_dir():
    """generate a temp folder"""

class SimplePreemptiveLock(filelock.SoftFileLock):
    """this is a lock support check lock expiration, if you do not need check expiration, you can use SoftFileLock"""
    def __init__(self, lock_file, stale: int = -1) -> None: ...

def get_file_lock(path: string, stale: int = -1): ...
