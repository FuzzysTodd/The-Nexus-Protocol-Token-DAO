from .builder import DatasetBuilder as DatasetBuilder
from .download.download_config import DownloadConfig as DownloadConfig
from .download.streaming_download_manager import xPath as xPath, xbasename as xbasename, xdirname as xdirname, xet_parse as xet_parse, xexists as xexists, xgetsize as xgetsize, xglob as xglob, xgzip_open as xgzip_open, xisdir as xisdir, xisfile as xisfile, xjoin as xjoin, xlistdir as xlistdir, xnumpy_load as xnumpy_load, xopen as xopen, xpandas_read_csv as xpandas_read_csv, xpandas_read_excel as xpandas_read_excel, xrelpath as xrelpath, xsio_loadmat as xsio_loadmat, xsplit as xsplit, xsplitext as xsplitext, xwalk as xwalk, xxml_dom_minidom_parse as xxml_dom_minidom_parse
from .utils.logging import get_logger as get_logger
from .utils.patching import patch_submodule as patch_submodule
from .utils.py_utils import get_imports as get_imports
from _typeshed import Incomplete

logger: Incomplete

def extend_module_for_streaming(module_path, download_config: DownloadConfig | None = None):
    '''Extend the module to support streaming.

    We patch some functions in the module to use `fsspec` to support data streaming:
    - We use `fsspec.open` to open and read remote files. We patch the module function:
      - `open`
    - We use the "::" hop separator to join paths and navigate remote compressed/archive files. We patch the module
      functions:
      - `os.path.join`
      - `pathlib.Path.joinpath` and `pathlib.Path.__truediv__` (called when using the "/" operator)

    The patched functions are replaced with custom functions defined to work with the
    :class:`~download.streaming_download_manager.StreamingDownloadManager`.

    Args:
        module_path: Path to the module to be extended.
        download_config : mainly use use_auth_token or storage_options to support different platforms and auth types.
    '''
def extend_dataset_builder_for_streaming(builder: DatasetBuilder):
    """Extend the dataset builder module and the modules imported by it to support streaming.

    Args:
        builder (:class:`DatasetBuilder`): Dataset builder instance.
    """
