from _typeshed import Incomplete
from collections.abc import Generator
from sklearn._min_dependencies import PYTEST_MIN_VERSION as PYTEST_MIN_VERSION
from sklearn.datasets import fetch_20newsgroups as fetch_20newsgroups, fetch_20newsgroups_vectorized as fetch_20newsgroups_vectorized, fetch_california_housing as fetch_california_housing, fetch_covtype as fetch_covtype, fetch_kddcup99 as fetch_kddcup99, fetch_olivetti_faces as fetch_olivetti_faces, fetch_rcv1 as fetch_rcv1
from sklearn.tests import random_seed as random_seed
from sklearn.utils.fixes import parse_version as parse_version, sp_version as sp_version

scipy_datasets_require_network: Incomplete

def raccoon_face_or_skip(): ...

dataset_fetchers: Incomplete

def global_dtype(request) -> Generator[Incomplete, None, None]: ...

fetch_20newsgroups_fxt: Incomplete
fetch_20newsgroups_vectorized_fxt: Incomplete
fetch_california_housing_fxt: Incomplete
fetch_covtype_fxt: Incomplete
fetch_kddcup99_fxt: Incomplete
fetch_olivetti_faces_fxt: Incomplete
fetch_rcv1_fxt: Incomplete
raccoon_face_fxt: Incomplete

def pytest_collection_modifyitems(config, items) -> None:
    """Called after collect is completed.

    Parameters
    ----------
    config : pytest config
    items : list of collected items
    """
def pyplot() -> Generator[Incomplete, None, None]:
    """Setup and teardown fixture for matplotlib.

    This fixture checks if we can import matplotlib. If not, the tests will be
    skipped. Otherwise, we close the figures before and after running the
    functions.

    Returns
    -------
    pyplot : module
        The ``matplotlib.pyplot`` module.
    """
def pytest_configure(config) -> None: ...
