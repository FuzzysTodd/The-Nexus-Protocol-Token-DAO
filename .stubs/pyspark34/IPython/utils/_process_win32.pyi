from . import py3compat as py3compat
from ._process_common import arg_split as py_arg_split, process_handler as process_handler, read_no_interrupt as read_no_interrupt
from .encoding import DEFAULT_ENCODING as DEFAULT_ENCODING
from _typeshed import Incomplete
from subprocess import TimeoutExpired as TimeoutExpired

class AvoidUNCPath:
    '''A context manager to protect command execution from UNC paths.

    In the Win32 API, commands can\'t be invoked with the cwd being a UNC path.
    This context manager temporarily changes directory to the \'C:\' drive on
    entering, and restores the original working directory on exit.

    The context manager returns the starting working directory *if* it made a
    change and None otherwise, so that users can apply the necessary adjustment
    to their system calls in the event of a change.

    Examples
    --------
    ::
        cmd = \'dir\'
        with AvoidUNCPath() as path:
            if path is not None:
                cmd = \'"pushd %s &&"%s\' % (path, cmd)
            os.system(cmd)
    '''
    path: Incomplete
    is_unc_path: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def system(cmd):
    """Win32 version of os.system() that works with network shares.

    Note that this implementation returns None, as meant for use in IPython.

    Parameters
    ----------
    cmd : str or list
        A command to be executed in the system shell.

    Returns
    -------
    int : child process' exit code.
    """
def getoutput(cmd):
    """Return standard output of executing cmd in a shell.

    Accepts the same arguments as os.system().

    Parameters
    ----------
    cmd : str or list
        A command to be executed in the system shell.

    Returns
    -------
    stdout : str
    """

CommandLineToArgvW: Incomplete
LocalFree: Incomplete

def arg_split(commandline, posix: bool = False, strict: bool = True):
    """Split a command line's arguments in a shell-like manner.

        This is a special version for windows that use a ctypes call to CommandLineToArgvW
        to do the argv splitting. The posix parameter is ignored.

        If strict=False, process_common.arg_split(...strict=False) is used instead.
        """
arg_split = py_arg_split

def check_pid(pid): ...
