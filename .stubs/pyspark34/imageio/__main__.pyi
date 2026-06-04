from . import plugins as plugins
from .core import util as util
from _typeshed import Incomplete

PLUGINS_WITH_BINARIES: Incomplete

def download_bin(plugin_names=['all'], package_dir: bool = False) -> None:
    '''Download binary dependencies of plugins

    This is a convenience method for downloading the binaries
    (e.g. for freeimage) from the imageio-binaries
    repository.

    Parameters
    ----------
    plugin_names: list
        A list of imageio plugin names. If it contains "all", all
        binary dependencies are downloaded.
    package_dir: bool
        If set to `True`, the binaries will be downloaded to the
        `resources` directory of the imageio package instead of
        to the users application data directory. Note that this
        might require administrative rights if imageio is installed
        in a system directory.
    '''
def download_bin_main() -> None:
    """Argument-parsing wrapper for `download_bin`"""
def remove_bin(plugin_names=['all']) -> None:
    """Remove binary dependencies of plugins

    This is a convenience method that removes all binaries
    dependencies for plugins downloaded by imageio.

    Notes
    -----
    It only makes sense to use this method if the binaries
    are corrupt.
    """
def remove_bin_main() -> None:
    """Argument-parsing wrapper for `remove_bin`"""
