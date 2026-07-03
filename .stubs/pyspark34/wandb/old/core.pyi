from _typeshed import Incomplete

__all__ = ['__stage_dir__', 'SCRIPT_PATH', 'START_TIME', 'wandb_dir', '_set_stage_dir', 'Error', 'WandbWarning', 'LOG_STRING', 'ERROR_STRING', 'termlog', 'termwarn', 'termerror']

__stage_dir__: Incomplete
SCRIPT_PATH: Incomplete

def wandb_dir(root_dir: Incomplete | None = None): ...
def _set_stage_dir(stage_dir) -> None: ...

class Error(Exception):
    """Base W&B Error"""
    message: Incomplete
    def __init__(self, message) -> None: ...
    def encode(self, encoding): ...

class WandbWarning(Warning):
    """Base W&B Warning"""

LOG_STRING: Incomplete
ERROR_STRING: Incomplete

def termlog(string: str = '', newline: bool = True, repeat: bool = True) -> None:
    """Log to standard error with formatting.

    Arguments:
        string (str, optional): The string to print
        newline (bool, optional): Print a newline at the end of the string
        repeat (bool, optional): If set to False only prints the string once per process
    """
def termwarn(string, **kwargs) -> None: ...
def termerror(string, **kwargs) -> None: ...

# Names in __all__ with no definition:
#   START_TIME
