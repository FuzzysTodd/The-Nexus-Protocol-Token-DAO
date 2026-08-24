from . import tools as tools
from IPython.core import page as page
from IPython.terminal.interactiveshell import TerminalInteractiveShell as TerminalInteractiveShell
from IPython.utils import io as io

def get_ipython(): ...
def xsys(self, cmd) -> None:
    """Replace the default system call with a capturing one for doctest.
    """
def start_ipython():
    """Start a global IPython shell, which we need for IPython-specific syntax.
    """
