import logging
from typing import Any

def get_logger() -> logging.Logger | logging.LoggerAdapter[Any]:
    """Grab the global logger instance.

    If a global Application is instantiated, grab its logger.
    Otherwise, grab the root logger.
    """
