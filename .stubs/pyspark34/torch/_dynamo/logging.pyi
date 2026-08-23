from _typeshed import Incomplete
from torch.hub import tqdm as tqdm

disable_progress: bool

def get_loggers(): ...
def set_loggers_level(level) -> None:
    """Write current log level"""
def get_loggers_level():
    """Read current log level"""

LOGGING_CONFIG: Incomplete

def init_logging(log_level, log_file_name: Incomplete | None = None) -> None: ...

num_steps: int
pbar: Incomplete

def get_step_logger(logger): ...
