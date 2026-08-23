from ._process_common import get_output_error_code as get_output_error_code, getoutputerror as getoutputerror, process_handler as process_handler
from ._process_posix import arg_split as arg_split, check_pid as check_pid, getoutput as getoutput, system as system

class FindCmdError(Exception): ...

def find_cmd(cmd):
    """Find absolute path to executable cmd in a cross platform manner.

    This function tries to determine the full path to a command line program
    using `which` on Unix/Linux/OS X and `win32api` on Windows.  Most of the
    time it will use the version that is first on the users `PATH`.

    Warning, don't use this to find IPython command line programs as there
    is a risk you will find the wrong one.  Instead find those using the
    following code and looking for the application itself::

        import sys
        argv = [sys.executable, '-m', 'IPython']

    Parameters
    ----------
    cmd : str
        The command line program to look for.
    """
def abbrev_cwd():
    """ Return abbreviated version of cwd, e.g. d:mydir """
