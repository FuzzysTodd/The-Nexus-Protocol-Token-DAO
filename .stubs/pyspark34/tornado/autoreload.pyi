from tornado import ioloop as ioloop, process as process
from tornado.log import gen_log as gen_log
from tornado.util import exec_in as exec_in
from typing import Callable

def start(check_time: int = 500) -> None:
    """Begins watching source files for changes.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.
    """
def wait() -> None:
    """Wait for a watched file to change, then restart the process.

    Intended to be used at the end of scripts like unit test runners,
    to run the tests again after any source file changes (but see also
    the command-line interface in `main`)
    """
def watch(filename: str) -> None:
    """Add a file to the watch list.

    All imported modules are watched by default.
    """
def add_reload_hook(fn: Callable[[], None]) -> None:
    """Add a function to be called before reloading the process.

    Note that for open file and socket handles it is generally
    preferable to set the ``FD_CLOEXEC`` flag (using `fcntl` or
    `os.set_inheritable`) instead of using a reload hook to close them.
    """
def main() -> None:
    """Command-line wrapper to re-run a script whenever its source changes.

    Scripts may be specified by filename or module name::

        python -m tornado.autoreload -m tornado.test.runtests
        python -m tornado.autoreload tornado/test/runtests.py

    Running a script with this wrapper is similar to calling
    `tornado.autoreload.wait` at the end of the script, but this wrapper
    can catch import-time problems like syntax errors that would otherwise
    prevent the script from reaching its call to `wait`.
    """
