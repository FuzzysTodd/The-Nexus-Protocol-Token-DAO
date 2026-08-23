from typing import NamedTuple, Sequence

class Version(NamedTuple):
    major: int
    minor: int
    micro: int

def split_lines(string: str, keepends: bool = False) -> Sequence[str]:
    '''
    Intended for Python code. In contrast to Python\'s :py:meth:`str.splitlines`,
    looks at form feeds and other special characters as normal text. Just
    splits ``\\n`` and ``\\r\\n``.
    Also different: Returns ``[""]`` for an empty string input.

    In Python 2.7 form feeds are used as normal characters when using
    str.splitlines. However in Python 3 somewhere there was a decision to split
    also on form feeds.
    '''
def python_bytes_to_unicode(source: str | bytes, encoding: str = 'utf-8', errors: str = 'strict') -> str:
    """
    Checks for unicode BOMs and PEP 263 encoding declarations. Then returns a
    unicode object like in :py:meth:`bytes.decode`.

    :param encoding: See :py:meth:`bytes.decode` documentation.
    :param errors: See :py:meth:`bytes.decode` documentation. ``errors`` can be
        ``'strict'``, ``'replace'`` or ``'ignore'``.
    """
def version_info() -> Version:
    """
    Returns a namedtuple of parso's version, similar to Python's
    ``sys.version_info``.
    """

class _PythonVersionInfo(NamedTuple):
    major: int
    minor: int

class PythonVersionInfo(_PythonVersionInfo):
    def __gt__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

def parse_version_string(version: str = None) -> PythonVersionInfo:
    """
    Checks for a valid version number (e.g. `3.8` or `3.10.1` or `3`) and
    returns a corresponding version info that is always two characters long in
    decimal.
    """
