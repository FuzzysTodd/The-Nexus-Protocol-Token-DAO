from .core import Pooch as Pooch, create as create, retrieve as retrieve
from .downloaders import DOIDownloader as DOIDownloader, FTPDownloader as FTPDownloader, HTTPDownloader as HTTPDownloader, SFTPDownloader as SFTPDownloader
from .hashes import file_hash as file_hash, make_registry as make_registry
from .processors import Decompress as Decompress, Untar as Untar, Unzip as Unzip
from .utils import check_version as check_version, get_logger as get_logger, os_cache as os_cache
from _typeshed import Incomplete

__version__: Incomplete

def test(doctest: bool = True, verbose: bool = True, coverage: bool = False) -> None:
    """
    Run the test suite.

    Uses `py.test <http://pytest.org/>`__ to discover and run the tests.

    Parameters
    ----------

    doctest : bool
        If ``True``, will run the doctests as well (code examples that start
        with a ``>>>`` in the docs).
    verbose : bool
        If ``True``, will print extra information during the test run.
    coverage : bool
        If ``True``, will run test coverage analysis on the code as well.
        Requires ``pytest-cov``.

    Raises
    ------

    AssertionError
        If pytest returns a non-zero error code indicating that some tests have
        failed.

    """
