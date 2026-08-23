import colorlog.formatter
from _typeshed import Incomplete
from logging import CRITICAL as CRITICAL, DEBUG as DEBUG, ERROR as ERROR, FATAL as FATAL, INFO as INFO, NOTSET as NOTSET, StreamHandler as StreamHandler, WARN as WARN, WARNING as WARNING, getLogger as getLogger, root as root

__all__ = ['CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'INFO', 'NOTSET', 'WARN', 'WARNING', 'StreamHandler', 'basicConfig', 'critical', 'debug', 'error', 'exception', 'getLogger', 'info', 'log', 'root', 'warning']

def basicConfig(style: colorlog.formatter._FormatStyle = '%', log_colors: colorlog.formatter.LogColors | None = None, reset: bool = True, secondary_log_colors: colorlog.formatter.SecondaryLogColors | None = None, format: str = '%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s', datefmt: str | None = None, **kwargs) -> None:
    """Call ``logging.basicConfig`` and override the formatter it creates."""

debug: Incomplete
info: Incomplete
warning: Incomplete
error: Incomplete
critical: Incomplete
log: Incomplete
exception: Incomplete
