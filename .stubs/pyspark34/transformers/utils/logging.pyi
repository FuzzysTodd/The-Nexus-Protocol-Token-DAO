import logging
from _typeshed import Incomplete
from logging import CRITICAL as CRITICAL, FATAL as FATAL, NOTSET as NOTSET, WARN as WARN
from typing import Optional

log_levels: Incomplete

def get_log_levels_dict(): ...
def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Return a logger with the specified name.

    This function is not supposed to be directly accessed unless you are writing a custom transformers module.
    """
def get_verbosity() -> int:
    """
    Return the current level for the 🤗 Transformers's root logger as an int.

    Returns:
        `int`: The logging level.

    <Tip>

    🤗 Transformers has following logging levels:

    - 50: `transformers.logging.CRITICAL` or `transformers.logging.FATAL`
    - 40: `transformers.logging.ERROR`
    - 30: `transformers.logging.WARNING` or `transformers.logging.WARN`
    - 20: `transformers.logging.INFO`
    - 10: `transformers.logging.DEBUG`

    </Tip>"""
def set_verbosity(verbosity: int) -> None:
    """
    Set the verbosity level for the 🤗 Transformers's root logger.

    Args:
        verbosity (`int`):
            Logging level, e.g., one of:

            - `transformers.logging.CRITICAL` or `transformers.logging.FATAL`
            - `transformers.logging.ERROR`
            - `transformers.logging.WARNING` or `transformers.logging.WARN`
            - `transformers.logging.INFO`
            - `transformers.logging.DEBUG`
    """
def set_verbosity_info():
    """Set the verbosity to the `INFO` level."""
def set_verbosity_warning():
    """Set the verbosity to the `WARNING` level."""
def set_verbosity_debug():
    """Set the verbosity to the `DEBUG` level."""
def set_verbosity_error():
    """Set the verbosity to the `ERROR` level."""
def disable_default_handler() -> None:
    """Disable the default handler of the HuggingFace Transformers's root logger."""
def enable_default_handler() -> None:
    """Enable the default handler of the HuggingFace Transformers's root logger."""
def add_handler(handler: logging.Handler) -> None:
    """adds a handler to the HuggingFace Transformers's root logger."""
def remove_handler(handler: logging.Handler) -> None:
    """removes given handler from the HuggingFace Transformers's root logger."""
def disable_propagation() -> None:
    """
    Disable propagation of the library log outputs. Note that log propagation is disabled by default.
    """
def enable_propagation() -> None:
    """
    Enable propagation of the library log outputs. Please disable the HuggingFace Transformers's default handler to
    prevent double logging if the root logger has been configured.
    """
def enable_explicit_format() -> None:
    """
    Enable explicit formatting for every HuggingFace Transformers's logger. The explicit formatter is as follows:
    ```
        [LEVELNAME|FILENAME|LINE NUMBER] TIME >> MESSAGE
    ```
    All handlers currently bound to the root logger are affected by this method.
    """
def reset_format() -> None:
    """
    Resets the formatting for HuggingFace Transformers's loggers.

    All handlers currently bound to the root logger are affected by this method.
    """
def warning_advice(self, *args, **kwargs) -> None:
    """
    This method is identical to `logger.warning()`, but if env var TRANSFORMERS_NO_ADVISORY_WARNINGS=1 is set, this
    warning will not be printed
    """

class EmptyTqdm:
    """Dummy tqdm which doesn't do anything."""
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self): ...
    def __getattr__(self, _):
        """Return empty function."""
    def __enter__(self): ...
    def __exit__(self, type_: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class _tqdm_cls:
    def __call__(self, *args, **kwargs): ...
    def set_lock(self, *args, **kwargs): ...
    def get_lock(self): ...

tqdm: Incomplete

def is_progress_bar_enabled() -> bool:
    """Return a boolean indicating whether tqdm progress bars are enabled."""
def enable_progress_bar() -> None:
    """Enable tqdm progress bar."""
def disable_progress_bar() -> None:
    """Disable tqdm progress bar."""
