from .base import change_root as change_root, get_major_minor_version as get_major_minor_version, is_osx_framework as is_osx_framework
from _typeshed import Incomplete
from pip._internal.exceptions import InvalidSchemeCombination as InvalidSchemeCombination, UserInstallationInvalid as UserInstallationInvalid
from pip._internal.models.scheme import SCHEME_KEYS as SCHEME_KEYS, Scheme as Scheme
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv

logger: Incomplete

def get_scheme(dist_name: str, user: bool = False, home: str | None = None, root: str | None = None, isolated: bool = False, prefix: str | None = None) -> Scheme:
    '''
    Get the "scheme" corresponding to the input parameters.

    :param dist_name: the name of the package to retrieve the scheme for, used
        in the headers scheme path
    :param user: indicates to use the "user" scheme
    :param home: indicates to use the "home" scheme
    :param root: root under which other directories are re-based
    :param isolated: ignored, but kept for distutils compatibility (where
        this controls whether the user-site pydistutils.cfg is honored)
    :param prefix: indicates to use the "prefix" scheme and provides the
        base directory for the same
    '''
def get_bin_prefix() -> str: ...
def get_purelib() -> str: ...
def get_platlib() -> str: ...
