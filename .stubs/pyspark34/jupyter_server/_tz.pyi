import abc
from _typeshed import Incomplete
from datetime import tzinfo

ZERO: Incomplete

class tzUTC(tzinfo, metaclass=abc.ABCMeta):
    """tzinfo object for UTC (zero offset)"""
    def utcoffset(self, d):
        """Compute utcoffset."""
    def dst(self, d):
        """Compute dst."""

UTC: Incomplete

def utc_aware(unaware):
    """decorator for adding UTC tzinfo to datetime's utcfoo methods"""

utcfromtimestamp: Incomplete
utcnow: Incomplete

def isoformat(dt):
    """Return iso-formatted timestamp

    Like .isoformat(), but uses Z for UTC instead of +00:00
    """
