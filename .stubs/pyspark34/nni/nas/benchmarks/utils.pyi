from .constants import DATABASE_DIR as DATABASE_DIR, DB_URLS as DB_URLS
from _typeshed import Incomplete
from nni.common.blob_utils import load_or_download_file as load_or_download_file
from playhouse.sqlite_ext import SqliteExtDatabase

json_dumps: Incomplete

def load_benchmark(benchmark: str) -> SqliteExtDatabase:
    """
    Load a benchmark as a database.

    Parmaeters
    ----------
    benchmark : str
        Benchmark name like nasbench201.
    """
def download_benchmark(benchmark: str, progress: bool = True):
    """
    Download a converted benchmark.

    Parameters
    ----------
    benchmark : str
        Benchmark name like nasbench201.
    """
