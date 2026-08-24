import abc
from _typeshed import Incomplete
from datetime import datetime, tzinfo

__all__ = ['tzname_in_python2', 'enfold']

def tzname_in_python2(namefunc):
    """Change unicode output into bytestrings in Python 2

    tzname() API changed in Python 3. It used to return bytes, but was changed
    to unicode strings
    """
def enfold(dt, fold: int = 1):
    """
        Provides a unified interface for assigning the ``fold`` attribute to
        datetimes both before and after the implementation of PEP-495.

        :param fold:
            The value for the ``fold`` attribute in the returned datetime. This
            should be either 0 or 1.

        :return:
            Returns an object for which ``getattr(dt, 'fold', 0)`` returns
            ``fold`` for all versions of Python. In versions prior to
            Python 3.6, this is a ``_DatetimeWithFold`` object, which is a
            subclass of :py:class:`datetime.datetime` with the ``fold``
            attribute added, if ``fold`` is 1.

        .. versionadded:: 2.6.0
        """

class _DatetimeWithFold(datetime):
    """
        This is a class designed to provide a PEP 495-compliant interface for
        Python versions before 3.6. It is used only for dates in a fold, so
        the ``fold`` attribute is fixed at ``1``.

        .. versionadded:: 2.6.0
        """
    def replace(self, *args, **kwargs):
        """
            Return a datetime with the same attributes, except for those
            attributes given new values by whichever keyword arguments are
            specified. Note that tzinfo=None can be specified to create a naive
            datetime from an aware datetime with no conversion of date and time
            data.

            This is reimplemented in ``_DatetimeWithFold`` because pypy3 will
            return a ``datetime.datetime`` even if ``fold`` is unchanged.
            """
    @property
    def fold(self): ...

class _tzinfo(tzinfo, metaclass=abc.ABCMeta):
    """
    Base class for all ``dateutil`` ``tzinfo`` objects.
    """
    def is_ambiguous(self, dt):
        '''
        Whether or not the "wall time" of a given datetime is ambiguous in this
        zone.

        :param dt:
            A :py:class:`datetime.datetime`, naive or time zone aware.


        :return:
            Returns ``True`` if ambiguous, ``False`` otherwise.

        .. versionadded:: 2.6.0
        '''
    def fromutc(self, dt):
        '''
        Given a timezone-aware datetime in a given timezone, calculates a
        timezone-aware datetime in a new timezone.

        Since this is the one time that we *know* we have an unambiguous
        datetime object, we take this opportunity to determine whether the
        datetime is ambiguous and in a "fold" state (e.g. if it\'s the first
        occurrence, chronologically, of the ambiguous datetime).

        :param dt:
            A timezone-aware :class:`datetime.datetime` object.
        '''

class tzrangebase(_tzinfo):
    """
    This is an abstract base class for time zones represented by an annual
    transition into and out of DST. Child classes should implement the following
    methods:

        * ``__init__(self, *args, **kwargs)``
        * ``transitions(self, year)`` - this is expected to return a tuple of
          datetimes representing the DST on and off transitions in standard
          time.

    A fully initialized ``tzrangebase`` subclass should also provide the
    following attributes:
        * ``hasdst``: Boolean whether or not the zone uses DST.
        * ``_dst_offset`` / ``_std_offset``: :class:`datetime.timedelta` objects
          representing the respective UTC offsets.
        * ``_dst_abbr`` / ``_std_abbr``: Strings representing the timezone short
          abbreviations in DST and STD, respectively.
        * ``_hasdst``: Whether or not the zone has DST.

    .. versionadded:: 2.6.0
    """
    def __init__(self) -> None: ...
    def utcoffset(self, dt): ...
    def dst(self, dt): ...
    def tzname(self, dt): ...
    def fromutc(self, dt):
        """ Given a datetime in UTC, return local time """
    def is_ambiguous(self, dt):
        '''
        Whether or not the "wall time" of a given datetime is ambiguous in this
        zone.

        :param dt:
            A :py:class:`datetime.datetime`, naive or time zone aware.


        :return:
            Returns ``True`` if ambiguous, ``False`` otherwise.

        .. versionadded:: 2.6.0
        '''
    __hash__: Incomplete
    def __ne__(self, other): ...
    __reduce__: Incomplete
