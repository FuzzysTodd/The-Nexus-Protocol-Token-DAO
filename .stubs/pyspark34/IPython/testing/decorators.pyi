from .ipunittest import ipdocstring as ipdocstring, ipdoctest as ipdoctest
from _typeshed import Incomplete
from decorator import decorator as decorator

def as_unittest(func):
    """Decorator to make a simple function into a normal test via unittest."""
def skipif(skip_condition, msg: Incomplete | None = None):
    """Make function raise SkipTest exception if skip_condition is true

    Parameters
    ----------

    skip_condition : bool or callable
      Flag to determine whether to skip test. If the condition is a
      callable, it is used at runtime to dynamically make the decision. This
      is useful for tests that may require costly imports, to delay the cost
      until the test suite is actually executed.
    msg : string
      Message to give on raising a SkipTest exception.

    Returns
    -------
    decorator : function
      Decorator, which, when applied to a function, causes SkipTest
      to be raised when the skip_condition was True, and the function
      to be called normally otherwise.
    """
def skip(msg: Incomplete | None = None):
    """Decorator factory - mark a test function for skipping from test suite.

    Parameters
    ----------
      msg : string
        Optional message to be added.

    Returns
    -------
       decorator : function
         Decorator, which, when applied to a function, causes SkipTest
         to be raised, with the optional message added.
      """
def onlyif(condition, msg):
    """The reverse from skipif, see skipif for details."""
def module_not_available(module):
    """Can module be imported?  Returns true if module does NOT import.

    This is used to make a decorator to skip tests that require module to be
    available, but delay the 'import numpy' to test execution time.
    """

skip_win32: Incomplete
skip_linux: Incomplete
skip_osx: Incomplete
skip_if_not_win32: Incomplete
skip_if_not_linux: Incomplete
skip_if_no_x11: Incomplete
skip_without: Incomplete
skipif_not_numpy: Incomplete
skipif_not_matplotlib: Incomplete
null_deco: Incomplete
f: Incomplete
unicode_paths: bool
onlyif_unicode_paths: Incomplete

def onlyif_cmds_exist(*commands):
    """
    Decorator to skip test when at least one of `commands` is not found.
    """
