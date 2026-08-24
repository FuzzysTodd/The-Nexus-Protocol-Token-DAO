from arrow.arrow import Arrow, TZ_EXPR
from arrow.factory import ArrowFactory
from datetime import date, datetime, tzinfo as dt_tzinfo
from time import struct_time
from typing import List, Tuple, Type, overload

__all__ = ['get', 'utcnow', 'now', 'factory']

@overload
def get(*, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
@overload
def get(*args: int, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
@overload
def get(__obj: Arrow | datetime | date | struct_time | dt_tzinfo | int | float | str | Tuple[int, int, int], *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
@overload
def get(__arg1: datetime | date, __arg2: TZ_EXPR, *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
@overload
def get(__arg1: str, __arg2: str | List[str], *, locale: str = ..., tzinfo: TZ_EXPR | None = None, normalize_whitespace: bool = False) -> Arrow: ...
def utcnow() -> Arrow:
    """Calls the default :class:`ArrowFactory <arrow.factory.ArrowFactory>` ``utcnow`` method."""
def now(tz: TZ_EXPR | None = None) -> Arrow:
    """Calls the default :class:`ArrowFactory <arrow.factory.ArrowFactory>` ``now`` method."""
def factory(type: Type[Arrow]) -> ArrowFactory:
    """Returns an :class:`.ArrowFactory` for the specified :class:`Arrow <arrow.arrow.Arrow>`
    or derived type.

    :param type: the type, :class:`Arrow <arrow.arrow.Arrow>` or derived.

    """
