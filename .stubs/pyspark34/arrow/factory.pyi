from arrow import parser as parser
from arrow.arrow import Arrow as Arrow, TZ_EXPR as TZ_EXPR
from arrow.constants import DEFAULT_LOCALE as DEFAULT_LOCALE
from arrow.util import is_timestamp as is_timestamp, iso_to_gregorian as iso_to_gregorian
from datetime import date, datetime, tzinfo as dt_tzinfo
from time import struct_time
from typing import List, Tuple, Type, overload

class ArrowFactory:
    """A factory for generating :class:`Arrow <arrow.arrow.Arrow>` objects.

    :param type: (optional) the :class:`Arrow <arrow.arrow.Arrow>`-based class to construct from.
        Defaults to :class:`Arrow <arrow.arrow.Arrow>`.

    """
    type: Type[Arrow]
    def __init__(self, type: Type[Arrow] = ...) -> None: ...
    @overload
    def get(self, *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
    @overload
    def get(self, __obj: Arrow | datetime | date | struct_time | dt_tzinfo | int | float | str | Tuple[int, int, int], *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
    @overload
    def get(self, __arg1: datetime | date, __arg2: TZ_EXPR, *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
    @overload
    def get(self, __arg1: str, __arg2: str | List[str], *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
    def utcnow(self) -> Arrow:
        '''Returns an :class:`Arrow <arrow.arrow.Arrow>` object, representing "now" in UTC time.

        Usage::

            >>> import arrow
            >>> arrow.utcnow()
            <Arrow [2013-05-08T05:19:07.018993+00:00]>
        '''
    def now(self, tz: TZ_EXPR | None = None) -> Arrow:
        '''Returns an :class:`Arrow <arrow.arrow.Arrow>` object, representing "now" in the given
        timezone.

        :param tz: (optional) A :ref:`timezone expression <tz-expr>`.  Defaults to local time.

        Usage::

            >>> import arrow
            >>> arrow.now()
            <Arrow [2013-05-07T22:19:11.363410-07:00]>

            >>> arrow.now(\'US/Pacific\')
            <Arrow [2013-05-07T22:19:15.251821-07:00]>

            >>> arrow.now(\'+02:00\')
            <Arrow [2013-05-08T07:19:25.618646+02:00]>

            >>> arrow.now(\'local\')
            <Arrow [2013-05-07T22:19:39.130059-07:00]>
        '''
