from . import StdoutProgressIndicator as StdoutProgressIndicator, appdata_dir as appdata_dir, resource_dirs as resource_dirs, urlopen as urlopen
from _typeshed import Incomplete

class InternetNotAllowedError(IOError):
    """Plugins that need resources can just use get_remote_file(), but
    should catch this error and silently ignore it.
    """
class NeedDownloadError(IOError):
    """Is raised when a remote file is requested that is not locally
    available, but which needs to be explicitly downloaded by the user.
    """

def get_remote_file(fname, directory: Incomplete | None = None, force_download: bool = False, auto: bool = True):
    """Get a the filename for the local version of a file from the web

    Parameters
    ----------
    fname : str
        The relative filename on the remote data repository to download.
        These correspond to paths on
        ``https://github.com/imageio/imageio-binaries/``.
    directory : str | None
        The directory where the file will be cached if a download was
        required to obtain the file. By default, the appdata directory
        is used. This is also the first directory that is checked for
        a local version of the file. If the directory does not exist,
        it will be created.
    force_download : bool | str
        If True, the file will be downloaded even if a local copy exists
        (and this copy will be overwritten). Can also be a YYYY-MM-DD date
        to ensure a file is up-to-date (modified date of a file on disk,
        if present, is checked).
    auto : bool
        Whether to auto-download the file if its not present locally. Default
        True. If False and a download is needed, raises NeedDownloadError.

    Returns
    -------
    fname : str
        The path to the file on the local system.
    """
