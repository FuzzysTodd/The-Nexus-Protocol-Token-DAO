from typing import Tuple

def glibc_version_string() -> str | None:
    """Returns glibc version string, or None if not using glibc."""
def glibc_version_string_confstr() -> str | None:
    """Primary implementation of glibc_version_string using os.confstr."""
def glibc_version_string_ctypes() -> str | None:
    """Fallback implementation of glibc_version_string using ctypes."""
def libc_ver() -> Tuple[str, str]:
    """Try to determine the glibc version

    Returns a tuple of strings (lib, version) which default to empty strings
    in case the lookup fails.
    """
