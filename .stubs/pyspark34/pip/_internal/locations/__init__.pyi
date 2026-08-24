from .base import USER_CACHE_DIR as USER_CACHE_DIR, get_major_minor_version as get_major_minor_version, get_src_prefix as get_src_prefix, site_packages as site_packages, user_site as user_site
from pip._internal.models.scheme import Scheme

__all__ = ['USER_CACHE_DIR', 'get_bin_prefix', 'get_bin_user', 'get_major_minor_version', 'get_platlib', 'get_purelib', 'get_scheme', 'get_src_prefix', 'site_packages', 'user_site']

def get_scheme(dist_name: str, user: bool = False, home: str | None = None, root: str | None = None, isolated: bool = False, prefix: str | None = None) -> Scheme: ...
def get_bin_prefix() -> str: ...
def get_bin_user() -> str: ...
def get_purelib() -> str:
    """Return the default pure-Python lib location."""
def get_platlib() -> str:
    """Return the default platform-shared lib location."""
