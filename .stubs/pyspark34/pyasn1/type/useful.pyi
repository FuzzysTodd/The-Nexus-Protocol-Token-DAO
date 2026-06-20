import datetime
from _typeshed import Incomplete
from pyasn1.type import char

__all__ = ['ObjectDescriptor', 'GeneralizedTime', 'UTCTime']

class ObjectDescriptor(char.GraphicString):
    __doc__: Incomplete
    tagSet: Incomplete
    typeId: Incomplete

class TimeMixIn:
    class FixedOffset(datetime.tzinfo):
        """Fixed offset in minutes east from UTC."""
        def __init__(self, offset: int = 0, name: str = 'UTC') -> None: ...
        def utcoffset(self, dt): ...
        def tzname(self, dt): ...
        def dst(self, dt): ...
    UTC: Incomplete
    @property
    def asDateTime(self):
        """Create :py:class:`datetime.datetime` object from a |ASN.1| object.

        Returns
        -------
        :
            new instance of :py:class:`datetime.datetime` object
        """
    @classmethod
    def fromDateTime(cls, dt):
        """Create |ASN.1| object from a :py:class:`datetime.datetime` object.

        Parameters
        ----------
        dt: :py:class:`datetime.datetime` object
            The `datetime.datetime` object to initialize the |ASN.1| object
            from

        Returns
        -------
        :
            new instance of |ASN.1| value
        """

class GeneralizedTime(char.VisibleString, TimeMixIn):
    __doc__: Incomplete
    tagSet: Incomplete
    typeId: Incomplete

class UTCTime(char.VisibleString, TimeMixIn):
    __doc__: Incomplete
    tagSet: Incomplete
    typeId: Incomplete
