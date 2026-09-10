import email.message
from ._compat import pypy_partial as pypy_partial
from ._text import FoldedCase as FoldedCase
from _typeshed import Incomplete

class Message(email.message.Message):
    multiple_use_keys: Incomplete
    def __new__(cls, orig: email.message.Message): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, item):
        """
        Warn users that a ``KeyError`` can be expected when a
        mising key is supplied. Ref python/importlib_metadata#371.
        """
    @property
    def json(self):
        """
        Convert PackageMetadata to a JSON-compatible format
        per PEP 0566.
        """
