import abc
from _typeshed import Incomplete
from datetime import tzinfo

ZERO: Incomplete

class tzUTC(tzinfo, metaclass=abc.ABCMeta):
    """tzinfo object for UTC (zero offset)"""
    def utcoffset(self, d): ...
    def dst(self, d): ...

UTC: Incomplete

def utc_aware(unaware):
    """decorator for adding UTC tzinfo to datetime's utcfoo methods"""

utcfromtimestamp: Incomplete
utcnow: Incomplete
