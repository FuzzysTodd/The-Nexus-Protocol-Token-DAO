from ._process_common import arg_split as arg_split, getoutput as getoutput
from IPython.utils.encoding import DEFAULT_ENCODING as DEFAULT_ENCODING
from _typeshed import Incomplete

class ProcessHandler:
    """Execute subprocesses under the control of pexpect.
    """
    read_timeout: float
    terminate_timeout: float
    logfile: Incomplete
    @property
    def sh(self): ...
    def __init__(self, logfile: Incomplete | None = None, read_timeout: Incomplete | None = None, terminate_timeout: Incomplete | None = None) -> None:
        """Arguments are used for pexpect calls."""
    def getoutput(self, cmd):
        """Run a command and return its stdout/stderr as a string.

        Parameters
        ----------
        cmd : str
            A command to be executed in the system shell.

        Returns
        -------
        output : str
            A string containing the combination of stdout and stderr from the
        subprocess, in whatever order the subprocess originally wrote to its
        file descriptors (so the order of the information in this string is the
        correct order as would be seen if running the command in a terminal).
        """
    def getoutput_pexpect(self, cmd):
        """Run a command and return its stdout/stderr as a string.

        Parameters
        ----------
        cmd : str
            A command to be executed in the system shell.

        Returns
        -------
        output : str
            A string containing the combination of stdout and stderr from the
        subprocess, in whatever order the subprocess originally wrote to its
        file descriptors (so the order of the information in this string is the
        correct order as would be seen if running the command in a terminal).
        """
    def system(self, cmd):
        """Execute a command in a subshell.

        Parameters
        ----------
        cmd : str
            A command to be executed in the system shell.

        Returns
        -------
        int : child's exitstatus
        """

system: Incomplete

def check_pid(pid): ...
