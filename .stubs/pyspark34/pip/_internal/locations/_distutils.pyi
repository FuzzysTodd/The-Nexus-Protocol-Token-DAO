from .base import get_major_minor_version as get_major_minor_version
from _typeshed import Incomplete
from pip._internal.models.scheme import Scheme as Scheme
from pip._internal.utils.compat import WINDOWS as WINDOWS
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv
from typing import Dict

logger: Incomplete

def distutils_scheme(dist_name: str, user: bool = False, home: str | None = None, root: str | None = None, isolated: bool = False, prefix: str | None = None, *, ignore_config_files: bool = False) -> Dict[str, str]:
    """
    Return a distutils install scheme
    """
def get_scheme(dist_name: str, user: bool = False, home: str | None = None, root: str | None = None, isolated: bool = False, prefix: str | None = None) -> Scheme:
    '''
    Get the "scheme" corresponding to the input parameters. The distutils
    documentation provides the context for the available schemes:
    https://docs.python.org/3/install/index.html#alternate-installation

    :param dist_name: the name of the package to retrieve the scheme for, used
        in the headers scheme path
    :param user: indicates to use the "user" scheme
    :param home: indicates to use the "home" scheme and provides the base
        directory for the same
    :param root: root under which other directories are re-based
    :param isolated: equivalent to --no-user-cfg, i.e. do not consider
        ~/.pydistutils.cfg (posix) or ~/pydistutils.cfg (non-posix) for
        scheme paths
    :param prefix: indicates to use the "prefix" scheme and provides the
        base directory for the same
    '''
def get_bin_prefix() -> str: ...
def get_purelib() -> str: ...
def get_platlib() -> str: ...
