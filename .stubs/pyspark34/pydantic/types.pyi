import abc
from .dataclasses import Dataclass
from .main import BaseModel
from .typing import CallableGenerator
from datetime import date
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any, Callable, ClassVar, Dict, FrozenSet, List, Pattern, Set, Tuple, Type, TypeVar
from typing_extensions import Annotated
from uuid import UUID

__all__ = ['NoneStr', 'NoneBytes', 'StrBytes', 'NoneStrBytes', 'StrictStr', 'ConstrainedBytes', 'conbytes', 'ConstrainedList', 'conlist', 'ConstrainedSet', 'conset', 'ConstrainedFrozenSet', 'confrozenset', 'ConstrainedStr', 'constr', 'PyObject', 'ConstrainedInt', 'conint', 'PositiveInt', 'NegativeInt', 'NonNegativeInt', 'NonPositiveInt', 'ConstrainedFloat', 'confloat', 'PositiveFloat', 'NegativeFloat', 'NonNegativeFloat', 'NonPositiveFloat', 'FiniteFloat', 'ConstrainedDecimal', 'condecimal', 'UUID1', 'UUID3', 'UUID4', 'UUID5', 'FilePath', 'DirectoryPath', 'Json', 'JsonWrapper', 'SecretField', 'SecretStr', 'SecretBytes', 'StrictBool', 'StrictBytes', 'StrictInt', 'StrictFloat', 'PaymentCardNumber', 'ByteSize', 'PastDate', 'FutureDate', 'ConstrainedDate', 'condate']

NoneStr = str | None
NoneBytes = bytes | None
StrBytes = str | bytes
NoneStrBytes = StrBytes | None
OptionalInt = int | None
OptionalIntFloat = OptionalInt | float
OptionalIntFloatDecimal = OptionalIntFloat | Decimal
OptionalDate = date | None
StrIntFloat = str | int | float
ModelOrDc = Type[BaseModel | Dataclass]
T = TypeVar('T')

class ConstrainedNumberMeta(type):
    def __new__(cls, name: str, bases: Any, dct: Dict[str, Any]) -> ConstrainedInt: ...
StrictBool = bool

class ConstrainedInt(int, metaclass=ConstrainedNumberMeta):
    strict: bool
    gt: OptionalInt
    ge: OptionalInt
    lt: OptionalInt
    le: OptionalInt
    multiple_of: OptionalInt
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...

def conint(*, strict: bool = False, gt: int | None = None, ge: int | None = None, lt: int | None = None, le: int | None = None, multiple_of: int | None = None) -> Type[int]: ...
PositiveInt = int
NegativeInt = int
NonPositiveInt = int
NonNegativeInt = int
StrictInt = int

class ConstrainedFloat(float, metaclass=ConstrainedNumberMeta):
    strict: bool
    gt: OptionalIntFloat
    ge: OptionalIntFloat
    lt: OptionalIntFloat
    le: OptionalIntFloat
    multiple_of: OptionalIntFloat
    allow_inf_nan: bool | None
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...

def confloat(*, strict: bool = False, gt: float = None, ge: float = None, lt: float = None, le: float = None, multiple_of: float = None, allow_inf_nan: bool | None = None) -> Type[float]: ...
PositiveFloat = float
NegativeFloat = float
NonPositiveFloat = float
NonNegativeFloat = float
StrictFloat = float
FiniteFloat = float

class ConstrainedBytes(bytes):
    strip_whitespace: bool
    to_upper: bool
    to_lower: bool
    min_length: OptionalInt
    max_length: OptionalInt
    strict: bool
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...

def conbytes(*, strip_whitespace: bool = False, to_upper: bool = False, to_lower: bool = False, min_length: int | None = None, max_length: int | None = None, strict: bool = False) -> Type[bytes]: ...
StrictBytes = bytes

class ConstrainedStr(str):
    strip_whitespace: bool
    to_upper: bool
    to_lower: bool
    min_length: OptionalInt
    max_length: OptionalInt
    curtail_length: OptionalInt
    regex: str | Pattern[str] | None
    strict: bool
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: str) -> str: ...

def constr(*, strip_whitespace: bool = False, to_upper: bool = False, to_lower: bool = False, strict: bool = False, min_length: int | None = None, max_length: int | None = None, curtail_length: int | None = None, regex: str | None = None) -> Type[str]: ...
StrictStr = str

class ConstrainedSet(set):
    __origin__ = set
    __args__: Set[Type[T]]
    min_items: int | None
    max_items: int | None
    item_type: Type[T]
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def set_length_validator(cls, v: Set[T] | None) -> Set[T] | None: ...

def conset(item_type: Type[T], *, min_items: int | None = None, max_items: int | None = None) -> Type[Set[T]]: ...

class ConstrainedFrozenSet(frozenset):
    __origin__ = frozenset
    __args__: FrozenSet[Type[T]]
    min_items: int | None
    max_items: int | None
    item_type: Type[T]
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def frozenset_length_validator(cls, v: FrozenSet[T] | None) -> FrozenSet[T] | None: ...

def confrozenset(item_type: Type[T], *, min_items: int | None = None, max_items: int | None = None) -> Type[FrozenSet[T]]: ...

class ConstrainedList(list):
    __origin__ = list
    __args__: Tuple[Type[T], ...]
    min_items: int | None
    max_items: int | None
    unique_items: bool | None
    item_type: Type[T]
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def list_length_validator(cls, v: List[T] | None) -> List[T] | None: ...
    @classmethod
    def unique_items_validator(cls, v: List[T] | None) -> List[T] | None: ...

def conlist(item_type: Type[T], *, min_items: int | None = None, max_items: int | None = None, unique_items: bool = None) -> Type[List[T]]: ...
PyObject = Callable[..., Any]

class ConstrainedDecimal(Decimal, metaclass=ConstrainedNumberMeta):
    gt: OptionalIntFloatDecimal
    ge: OptionalIntFloatDecimal
    lt: OptionalIntFloatDecimal
    le: OptionalIntFloatDecimal
    max_digits: OptionalInt
    decimal_places: OptionalInt
    multiple_of: OptionalIntFloatDecimal
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: Decimal) -> Decimal: ...

def condecimal(*, gt: Decimal = None, ge: Decimal = None, lt: Decimal = None, le: Decimal = None, max_digits: int | None = None, decimal_places: int | None = None, multiple_of: Decimal = None) -> Type[Decimal]: ...
UUID1 = UUID
UUID3 = UUID
UUID4 = UUID
UUID5 = UUID
FilePath = Path
DirectoryPath = Path

class JsonWrapper: ...

class JsonMeta(type):
    def __getitem__(self, t: Type[Any]) -> Type[JsonWrapper]: ...
Json = Annotated[T, ...]

class SecretField(abc.ABC, metaclass=abc.ABCMeta):
    """
    Note: this should be implemented as a generic like `SecretField(ABC, Generic[T])`,
          the `__init__()` should be part of the abstract class and the
          `get_secret_value()` method should use the generic `T` type.

          However Cython doesn't support very well generics at the moment and
          the generated code fails to be imported (see
          https://github.com/cython/cython/issues/2753).
    """
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @abc.abstractmethod
    def get_secret_value(self) -> Any: ...

class SecretStr(SecretField):
    min_length: OptionalInt
    max_length: OptionalInt
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: Any) -> SecretStr: ...
    def __init__(self, value: str) -> None: ...
    def __len__(self) -> int: ...
    def display(self) -> str: ...
    def get_secret_value(self) -> str: ...

class SecretBytes(SecretField):
    min_length: OptionalInt
    max_length: OptionalInt
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: Any) -> SecretBytes: ...
    def __init__(self, value: bytes) -> None: ...
    def __len__(self) -> int: ...
    def display(self) -> str: ...
    def get_secret_value(self) -> bytes: ...

class PaymentCardBrand(str, Enum):
    amex: str
    mastercard: str
    visa: str
    other: str

class PaymentCardNumber(str):
    """
    Based on: https://en.wikipedia.org/wiki/Payment_card_number
    """
    strip_whitespace: ClassVar[bool]
    min_length: ClassVar[int]
    max_length: ClassVar[int]
    bin: str
    last4: str
    brand: PaymentCardBrand
    def __init__(self, card_number: str) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @property
    def masked(self) -> str: ...
    @classmethod
    def validate_digits(cls, card_number: str) -> str: ...
    @classmethod
    def validate_luhn_check_digit(cls, card_number: str) -> str:
        """
        Based on: https://en.wikipedia.org/wiki/Luhn_algorithm
        """
    @classmethod
    def validate_length_for_brand(cls, card_number: PaymentCardNumber) -> PaymentCardNumber:
        """
        Validate length based on BIN for major brands:
        https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
        """

class ByteSize(int):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, v: StrIntFloat) -> ByteSize: ...
    def human_readable(self, decimal: bool = False) -> str: ...
    def to(self, unit: str) -> float: ...
PastDate = date
FutureDate = date

class ConstrainedDate(date, metaclass=ConstrainedNumberMeta):
    gt: OptionalDate
    ge: OptionalDate
    lt: OptionalDate
    le: OptionalDate
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...

def condate(*, gt: date = None, ge: date = None, lt: date = None, le: date = None) -> Type[date]: ...
