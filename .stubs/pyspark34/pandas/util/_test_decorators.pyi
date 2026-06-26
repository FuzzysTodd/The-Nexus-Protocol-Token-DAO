from _typeshed import Incomplete
from pandas._config import get_option as get_option
from pandas._typing import F as F
from pandas.compat import IS64 as IS64, is_platform_windows as is_platform_windows
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.computation.expressions import NUMEXPR_INSTALLED as NUMEXPR_INSTALLED, USE_NUMEXPR as USE_NUMEXPR
from pandas.util.version import Version as Version
from typing import Callable

def safe_import(mod_name: str, min_version: str | None = None):
    """
    Parameters
    ----------
    mod_name : str
        Name of the module to be imported
    min_version : str, default None
        Minimum required version of the specified mod_name

    Returns
    -------
    object
        The imported module if successful, or False
    """
def skip_if_installed(package: str):
    """
    Skip a test if a package is installed.

    Parameters
    ----------
    package : str
        The name of the package.
    """
def skip_if_no(package: str, min_version: str | None = None):
    """
    Generic function to help skip tests when required packages are not
    present on the testing system.

    This function returns a pytest mark with a skip condition that will be
    evaluated during test collection. An attempt will be made to import the
    specified ``package`` and optionally ensure it meets the ``min_version``

    The mark can be used as either a decorator for a test function or to be
    applied to parameters in pytest.mark.parametrize calls or parametrized
    fixtures.

    If the import and version check are unsuccessful, then the test function
    (or test case when used in conjunction with parametrization) will be
    skipped.

    Parameters
    ----------
    package: str
        The name of the required package.
    min_version: str or None, default None
        Optional minimum version of the package.

    Returns
    -------
    _pytest.mark.structures.MarkDecorator
        a pytest.mark.skipif to use as either a test decorator or a
        parametrization mark.
    """

skip_if_no_mpl: Incomplete
skip_if_mpl: Incomplete
skip_if_32bit: Incomplete
skip_if_windows: Incomplete
skip_if_not_us_locale: Incomplete
skip_if_no_scipy: Incomplete
skip_if_no_ne: Incomplete

def skip_if_np_lt(ver_str: str, *args, reason: str | None = None): ...
def parametrize_fixture_doc(*args) -> Callable[[F], F]:
    """
    Intended for use as a decorator for parametrized fixture,
    this function will wrap the decorated function with a pytest
    ``parametrize_fixture_doc`` mark. That mark will format
    initial fixture docstring by replacing placeholders {0}, {1} etc
    with parameters passed as arguments.

    Parameters
    ----------
    args: iterable
        Positional arguments for docstring.

    Returns
    -------
    function
        The decorated function wrapped within a pytest
        ``parametrize_fixture_doc`` mark
    """
def async_mark(): ...
def mark_array_manager_not_yet_implemented(request) -> None: ...

skip_array_manager_not_yet_implemented: Incomplete
skip_array_manager_invalid_test: Incomplete
skip_copy_on_write_not_yet_implemented: Incomplete
skip_copy_on_write_invalid_test: Incomplete
