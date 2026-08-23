from IPython.terminal.interactiveshell import InteractiveShell as InteractiveShell
from _typeshed import Incomplete

def count_failures(runner):
    """Count number of failures in a doctest runner.

    Code modeled after the summarize() method in doctest.
    """

class IPython2PythonConverter:
    """Convert IPython 'syntax' to valid Python.

    Eventually this code may grow to be the full IPython syntax conversion
    implementation, but for now it only does prompt conversion."""
    rps1: Incomplete
    rps2: Incomplete
    rout: Incomplete
    pyps1: str
    pyps2: str
    rpyps1: Incomplete
    rpyps2: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, ds):
        """Convert IPython prompts to python ones in a string."""

class Doc2UnitTester:
    """Class whose instances act as a decorator for docstring testing.

    In practice we're only likely to need one instance ever, made below (though
    no attempt is made at turning it into a singleton, there is no need for
    that).
    """
    verbose: Incomplete
    finder: Incomplete
    def __init__(self, verbose: bool = False) -> None:
        """New decorator.

        Parameters
        ----------

        verbose : boolean, optional (False)
          Passed to the doctest finder and runner to control verbosity.
        """
    def __call__(self, func):
        """Use as a decorator: doctest a function's docstring as a unittest.
        
        This version runs normal doctests, but the idea is to make it later run
        ipython syntax instead."""

def ipdocstring(func):
    """Change the function docstring via ip2py.
    """

ipdoctest: Incomplete
ip2py: Incomplete
