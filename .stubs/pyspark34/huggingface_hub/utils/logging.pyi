import logging
from _typeshed import Incomplete
from logging import CRITICAL as CRITICAL, FATAL as FATAL, NOTSET as NOTSET, WARN as WARN

log_levels: Incomplete

def get_logger(name: str | None = None) -> logging.Logger:
    """
        Returns a logger with the specified name. This function is not supposed
        to be directly accessed by library users.

        Args:
            name (`str`, *optional*):
                The name of the logger to get, usually the filename

        Example:

    ```python
    >>> from huggingface_hub import get_logger

    >>> logger = get_logger(__file__)
    >>> logger.set_verbosity_info()
    ```
    """
def get_verbosity() -> int:
    """Return the current level for the HuggingFace Hub's root logger.

    Returns:
        Logging level, e.g., `huggingface_hub.logging.DEBUG` and
        `huggingface_hub.logging.INFO`.

    <Tip>

    HuggingFace Hub has following logging levels:

    - `huggingface_hub.logging.CRITICAL`, `huggingface_hub.logging.FATAL`
    - `huggingface_hub.logging.ERROR`
    - `huggingface_hub.logging.WARNING`, `huggingface_hub.logging.WARN`
    - `huggingface_hub.logging.INFO`
    - `huggingface_hub.logging.DEBUG`

    </Tip>
    """
def set_verbosity(verbosity: int) -> None:
    """
    Sets the level for the HuggingFace Hub's root logger.

    Args:
        verbosity (`int`):
            Logging level, e.g., `huggingface_hub.logging.DEBUG` and
            `huggingface_hub.logging.INFO`.
    """
def set_verbosity_info():
    """
    Sets the verbosity to `logging.INFO`.
    """
def set_verbosity_warning():
    """
    Sets the verbosity to `logging.WARNING`.
    """
def set_verbosity_debug():
    """
    Sets the verbosity to `logging.DEBUG`.
    """
def set_verbosity_error():
    """
    Sets the verbosity to `logging.ERROR`.
    """
def disable_propagation() -> None:
    """
    Disable propagation of the library log outputs. Note that log propagation is
    disabled by default.
    """
def enable_propagation() -> None:
    """
    Enable propagation of the library log outputs. Please disable the
    HuggingFace Hub's default handler to prevent double logging if the root
    logger has been configured.
    """
