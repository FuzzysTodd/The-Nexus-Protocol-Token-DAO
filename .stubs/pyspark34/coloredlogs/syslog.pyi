from _typeshed import Incomplete
from coloredlogs import DEFAULT_LOG_LEVEL as DEFAULT_LOG_LEVEL, ProgramNameFilter as ProgramNameFilter, adjust_level as adjust_level, find_program_name as find_program_name, level_to_number as level_to_number, replace_handler as replace_handler

LOG_DEVICE_MACOSX: str
LOG_DEVICE_UNIX: str
DEFAULT_LOG_FORMAT: str
logger: Incomplete

class SystemLogging:
    """Context manager to enable system logging."""
    args: Incomplete
    kw: Incomplete
    handler: Incomplete
    def __init__(self, *args, **kw) -> None:
        """
        Initialize a :class:`SystemLogging` object.

        :param args: Positional arguments to :func:`enable_system_logging()`.
        :param kw: Keyword arguments to :func:`enable_system_logging()`.
        """
    def __enter__(self):
        """Enable system logging when entering the context."""
    def __exit__(self, exc_type: Incomplete | None = None, exc_value: Incomplete | None = None, traceback: Incomplete | None = None) -> None:
        """
        Disable system logging when leaving the context.

        .. note:: If an exception is being handled when we leave the context a
                  warning message including traceback is logged *before* system
                  logging is disabled.
        """

def enable_system_logging(programname: Incomplete | None = None, fmt: Incomplete | None = None, logger: Incomplete | None = None, reconfigure: bool = True, **kw):
    """
    Redirect :mod:`logging` messages to the system log (e.g. ``/var/log/syslog``).

    :param programname: The program name to embed in log messages (a string, defaults
                         to the result of :func:`~coloredlogs.find_program_name()`).
    :param fmt: The log format for system log messages (a string, defaults to
                :data:`DEFAULT_LOG_FORMAT`).
    :param logger: The logger to which the :class:`~logging.handlers.SysLogHandler`
                   should be connected (defaults to the root logger).
    :param level: The logging level for the :class:`~logging.handlers.SysLogHandler`
                  (defaults to :data:`.DEFAULT_LOG_LEVEL`). This value is coerced
                  using :func:`~coloredlogs.level_to_number()`.
    :param reconfigure: If :data:`True` (the default) multiple calls to
                        :func:`enable_system_logging()` will each override
                        the previous configuration.
    :param kw: Refer to :func:`connect_to_syslog()`.
    :returns: A :class:`~logging.handlers.SysLogHandler` object or
              :data:`None`. If an existing handler is found and `reconfigure`
              is :data:`False` the existing handler object is returned. If the
              connection to the system logging daemon fails :data:`None` is
              returned.

    As of release 15.0 this function uses :func:`is_syslog_supported()` to
    check whether system logging is supported and appropriate before it's
    enabled.

    .. note:: When the logger's effective level is too restrictive it is
              relaxed (refer to `notes about log levels`_ for details).
    """
def connect_to_syslog(address: Incomplete | None = None, facility: Incomplete | None = None, level: Incomplete | None = None):
    """
    Create a :class:`~logging.handlers.SysLogHandler`.

    :param address: The device file or network address of the system logging
                    daemon (a string or tuple, defaults to the result of
                    :func:`find_syslog_address()`).
    :param facility: Refer to :class:`~logging.handlers.SysLogHandler`.
                     Defaults to ``LOG_USER``.
    :param level: The logging level for the :class:`~logging.handlers.SysLogHandler`
                  (defaults to :data:`.DEFAULT_LOG_LEVEL`). This value is coerced
                  using :func:`~coloredlogs.level_to_number()`.
    :returns: A :class:`~logging.handlers.SysLogHandler` object or :data:`None` (if the
              system logging daemon is unavailable).

    The process of connecting to the system logging daemon goes as follows:

    - The following two socket types are tried (in decreasing preference):

       1. :data:`~socket.SOCK_RAW` avoids truncation of log messages but may
          not be supported.
       2. :data:`~socket.SOCK_STREAM` (TCP) supports longer messages than the
          default (which is UDP).
    """
def find_syslog_address():
    """
    Find the most suitable destination for system log messages.

    :returns: The pathname of a log device (a string) or an address/port tuple as
              supported by :class:`~logging.handlers.SysLogHandler`.

    On Mac OS X this prefers :data:`LOG_DEVICE_MACOSX`, after that :data:`LOG_DEVICE_UNIX`
    is checked for existence. If both of these device files don't exist the default used
    by :class:`~logging.handlers.SysLogHandler` is returned.
    """
def is_syslog_supported():
    '''
    Determine whether system logging is supported.

    :returns:

        :data:`True` if system logging is supported and can be enabled,
        :data:`False` if system logging is not supported or there are good
        reasons for not enabling it.

    The decision making process here is as follows:

    Override
     If the environment variable ``$COLOREDLOGS_SYSLOG`` is set it is evaluated
     using :func:`~humanfriendly.coerce_boolean()` and the resulting value
     overrides the platform detection discussed below, this allows users to
     override the decision making process if they disagree / know better.

    Linux / UNIX
     On systems that are not Windows or MacOS (see below) we assume UNIX which
     means either syslog is available or sending a bunch of UDP packets to
     nowhere won\'t hurt anyone...

    Microsoft Windows
     Over the years I\'ve had multiple reports of :pypi:`coloredlogs` spewing
     extremely verbose errno 10057 warning messages to the console (once for
     each log message I suppose) so I now assume it a default that
     "syslog-style system logging" is not generally available on Windows.

    Apple MacOS
     There\'s cPython issue `#38780`_ which seems to result in a fatal exception
     when the Python interpreter shuts down. This is (way) worse than not
     having system logging enabled. The error message mentioned in `#38780`_
     has actually been following me around for years now, see for example:

     - https://github.com/xolox/python-rotate-backups/issues/9 mentions Docker
       images implying Linux, so not strictly the same as `#38780`_.

     - https://github.com/xolox/python-npm-accel/issues/4 is definitely related
       to `#38780`_ and is what eventually prompted me to add the
       :func:`is_syslog_supported()` logic.

    .. _#38780: https://bugs.python.org/issue38780
    '''
def match_syslog_handler(handler):
    """
    Identify system logging handlers.

    :param handler: The :class:`~logging.Handler` class to check.
    :returns: :data:`True` if the handler is a
              :class:`~logging.handlers.SysLogHandler`,
              :data:`False` otherwise.

    This function can be used as a callback for :func:`.find_handler()`.
    """
