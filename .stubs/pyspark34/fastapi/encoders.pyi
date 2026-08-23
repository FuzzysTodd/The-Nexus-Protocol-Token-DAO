import datetime
from ._compat import PYDANTIC_V2 as PYDANTIC_V2, Url as Url
from _typeshed import Incomplete
from decimal import Decimal
from fastapi.types import IncEx as IncEx
from typing import Any, Callable, Dict, Tuple, Type

def isoformat(o: datetime.date | datetime.time) -> str: ...
def decimal_encoder(dec_value: Decimal) -> int | float:
    '''
    Encodes a Decimal as int of there\'s no exponent, otherwise float

    This is useful when we use ConstrainedDecimal to represent Numeric(x,0)
    where a integer (but not int typed) is used. Encoding this as a float
    results in failed round-tripping between encode and parse.
    Our Id type is a prime example of this.

    >>> decimal_encoder(Decimal("1.0"))
    1.0

    >>> decimal_encoder(Decimal("1"))
    1
    '''

ENCODERS_BY_TYPE: Dict[Type[Any], Callable[[Any], Any]]

def generate_encoders_by_class_tuples(type_encoder_map: Dict[Any, Callable[[Any], Any]]) -> Dict[Callable[[Any], Any], Tuple[Any, ...]]: ...

encoders_by_class_tuples: Incomplete

def jsonable_encoder(obj: Any, include: IncEx | None = None, exclude: IncEx | None = None, by_alias: bool = True, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False, custom_encoder: Dict[Any, Callable[[Any], Any]] | None = None, sqlalchemy_safe: bool = True) -> Any: ...
