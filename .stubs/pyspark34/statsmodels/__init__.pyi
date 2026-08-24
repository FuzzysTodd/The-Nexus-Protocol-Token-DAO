from _typeshed import Incomplete
from statsmodels._version import __version__ as __version__, __version_tuple__ as __version_tuple__

__all__ = ['__version__', '__version_info__', '__version_tuple__', 'test']

__version_info__ = __version_tuple__

def test(extra_args: Incomplete | None = None, exit: bool = False):
    """
    Run the test suite

    Parameters
    ----------
    extra_args : list[str]
        List of argument to pass to pytest when running the test suite. The
        default is ['--tb=short', '--disable-pytest-warnings'].
    exit : bool
        Flag indicating whether the test runner should exist when finished.

    Returns
    -------
    int
        The status code from the test run if exit is False.
    """
