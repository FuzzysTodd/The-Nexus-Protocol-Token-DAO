import logging
from _typeshed import Incomplete
from logging import CRITICAL as CRITICAL, FATAL as FATAL, NOTSET as NOTSET, WARN as WARN

log_levels: Incomplete

def get_logger(name: str | None = None) -> logging.Logger:
    """Return a logger with the specified name.
    This function can be used in dataset scripts.
    """
def get_verbosity() -> int:
    """Return the current level for the HuggingFace datasets library's root logger.
    Returns:
        Logging level, e.g., `datasets.logging.DEBUG` and `datasets.logging.INFO`.

    <Tip>

        HuggingFace datasets library has following logging levels:
        - `datasets.logging.CRITICAL`, `datasets.logging.FATAL`
        - `datasets.logging.ERROR`
        - `datasets.logging.WARNING`, `datasets.logging.WARN`
        - `datasets.logging.INFO`
        - `datasets.logging.DEBUG`

    </Tip>
    """
def set_verbosity(verbosity: int) -> None:
    """Set the level for the Hugging Face Datasets library's root logger.
    Args:
        verbosity:
            Logging level, e.g., `datasets.logging.DEBUG` and `datasets.logging.INFO`.
    """
def set_verbosity_info():
    """Set the level for the Hugging Face datasets library's root logger to `INFO`.

    This will display most of the logging information and tqdm bars.

    Shortcut to `datasets.logging.set_verbosity(datasets.logging.INFO)`.
    """
def set_verbosity_warning():
    """Set the level for the Hugging Face datasets library's root logger to `WARNING`.

    This will display only the warning and errors logging information and tqdm bars.

    Shortcut to `datasets.logging.set_verbosity(datasets.logging.WARNING)`.
    """
def set_verbosity_debug():
    """Set the level for the Hugging Face datasets library's root logger to `DEBUG`.

    This will display all the logging information and tqdm bars.

    Shortcut to `datasets.logging.set_verbosity(datasets.logging.DEBUG)`.
    """
def set_verbosity_error():
    """Set the level for the Hugging Face datasets library's root logger to `ERROR`.

    This will display only the errors logging information and tqdm bars.

    Shortcut to `datasets.logging.set_verbosity(datasets.logging.ERROR)`.
    """
def disable_propagation() -> None:
    """Disable propagation of the library log outputs.
    Note that log propagation is disabled by default.
    """
def enable_propagation() -> None:
    """Enable propagation of the library log outputs.
    Please disable the Hugging Face datasets library's default handler to prevent double logging if the root logger has
    been configured.
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
    def __call__(self, *args, disable: bool = False, **kwargs): ...
    def set_lock(self, *args, **kwargs): ...
    def get_lock(self): ...
    def __delattr__(self, attr) -> None:
        """fix for https://github.com/huggingface/datasets/issues/6066"""

tqdm: Incomplete

def is_progress_bar_enabled() -> bool:
    """Return a boolean indicating whether tqdm progress bars are enabled."""
def enable_progress_bar() -> None:
    """Enable tqdm progress bar."""
def disable_progress_bar() -> None:
    """Disable tqdm progress bar."""
