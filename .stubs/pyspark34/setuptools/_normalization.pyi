from .extern import packaging as packaging
from .warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning

def safe_identifier(name: str) -> str:
    '''Make a string safe to be used as Python identifier.
    >>> safe_identifier("12abc")
    \'_12abc\'
    >>> safe_identifier("__editable__.myns.pkg-78.9.3_local")
    \'__editable___myns_pkg_78_9_3_local\'
    '''
def safe_name(component: str) -> str:
    '''Escape a component used as a project name according to Core Metadata.
    >>> safe_name("hello world")
    \'hello-world\'
    >>> safe_name("hello?world")
    \'hello-world\'
    '''
def safe_version(version: str) -> str:
    '''Convert an arbitrary string into a valid version string.
    >>> safe_version("1988 12 25")
    \'1988.12.25\'
    >>> safe_version("v0.2.1")
    \'0.2.1\'
    >>> safe_version("v0.2?beta")
    \'0.2b0\'
    >>> safe_version("v0.2 beta")
    \'0.2b0\'
    >>> safe_version("ubuntu lts")
    Traceback (most recent call last):
    ...
    setuptools.extern.packaging.version.InvalidVersion: Invalid version: \'ubuntu.lts\'
    '''
def best_effort_version(version: str) -> str:
    '''Convert an arbitrary string into a version-like string.
    >>> best_effort_version("v0.2 beta")
    \'0.2b0\'

    >>> import warnings
    >>> warnings.simplefilter("ignore", category=SetuptoolsDeprecationWarning)
    >>> best_effort_version("ubuntu lts")
    \'ubuntu.lts\'
    '''
def safe_extra(extra: str) -> str:
    '''Normalize extra name according to PEP 685
    >>> safe_extra("_FrIeNdLy-._.-bArD")
    \'friendly-bard\'
    >>> safe_extra("FrIeNdLy-._.-bArD__._-")
    \'friendly-bard\'
    '''
def filename_component(value: str) -> str:
    '''Normalize each component of a filename (e.g. distribution/version part of wheel)
    Note: ``value`` needs to be already normalized.
    >>> filename_component("my-pkg")
    \'my_pkg\'
    '''
def safer_name(value: str) -> str:
    """Like ``safe_name`` but can be used as filename component for wheel"""
def safer_best_effort_version(value: str) -> str:
    """Like ``best_effort_version`` but can be used as filename component for wheel"""
