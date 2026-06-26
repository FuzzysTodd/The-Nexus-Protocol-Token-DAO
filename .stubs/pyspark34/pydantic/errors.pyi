from .typing import DictStrAny
from _typeshed import Incomplete
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable, Sequence, Set, Tuple, Type

__all__ = ['PydanticTypeError', 'PydanticValueError', 'ConfigError', 'MissingError', 'ExtraError', 'NoneIsNotAllowedError', 'NoneIsAllowedError', 'WrongConstantError', 'NotNoneError', 'BoolError', 'BytesError', 'DictError', 'EmailError', 'UrlError', 'UrlSchemeError', 'UrlSchemePermittedError', 'UrlUserInfoError', 'UrlHostError', 'UrlHostTldError', 'UrlPortError', 'UrlExtraError', 'EnumError', 'IntEnumError', 'EnumMemberError', 'IntegerError', 'FloatError', 'PathError', 'PathNotExistsError', 'PathNotAFileError', 'PathNotADirectoryError', 'PyObjectError', 'SequenceError', 'ListError', 'SetError', 'FrozenSetError', 'TupleError', 'TupleLengthError', 'ListMinLengthError', 'ListMaxLengthError', 'ListUniqueItemsError', 'SetMinLengthError', 'SetMaxLengthError', 'FrozenSetMinLengthError', 'FrozenSetMaxLengthError', 'AnyStrMinLengthError', 'AnyStrMaxLengthError', 'StrError', 'StrRegexError', 'NumberNotGtError', 'NumberNotGeError', 'NumberNotLtError', 'NumberNotLeError', 'NumberNotMultipleError', 'DecimalError', 'DecimalIsNotFiniteError', 'DecimalMaxDigitsError', 'DecimalMaxPlacesError', 'DecimalWholeDigitsError', 'DateTimeError', 'DateError', 'DateNotInThePastError', 'DateNotInTheFutureError', 'TimeError', 'DurationError', 'HashableError', 'UUIDError', 'UUIDVersionError', 'ArbitraryTypeError', 'ClassError', 'SubclassError', 'JsonError', 'JsonTypeError', 'PatternError', 'DataclassTypeError', 'CallableError', 'IPvAnyAddressError', 'IPvAnyInterfaceError', 'IPvAnyNetworkError', 'IPv4AddressError', 'IPv6AddressError', 'IPv4NetworkError', 'IPv6NetworkError', 'IPv4InterfaceError', 'IPv6InterfaceError', 'ColorError', 'StrictBoolError', 'NotDigitError', 'LuhnValidationError', 'InvalidLengthForBrand', 'InvalidByteSize', 'InvalidByteSizeUnit', 'MissingDiscriminator', 'InvalidDiscriminator']

class PydanticErrorMixin:
    code: str
    msg_template: str
    __dict__: Incomplete
    def __init__(self, **ctx: Any) -> None: ...
    def __reduce__(self) -> Tuple[Callable[..., 'PydanticErrorMixin'], Tuple[Type['PydanticErrorMixin'], 'DictStrAny']]: ...

class PydanticTypeError(PydanticErrorMixin, TypeError): ...
class PydanticValueError(PydanticErrorMixin, ValueError): ...
class ConfigError(RuntimeError): ...

class MissingError(PydanticValueError):
    msg_template: str

class ExtraError(PydanticValueError):
    msg_template: str

class NoneIsNotAllowedError(PydanticTypeError):
    code: str
    msg_template: str

class NoneIsAllowedError(PydanticTypeError):
    code: str
    msg_template: str

class WrongConstantError(PydanticValueError):
    code: str

class NotNoneError(PydanticTypeError):
    code: str
    msg_template: str

class BoolError(PydanticTypeError):
    msg_template: str

class BytesError(PydanticTypeError):
    msg_template: str

class DictError(PydanticTypeError):
    msg_template: str

class EmailError(PydanticValueError):
    msg_template: str

class UrlError(PydanticValueError):
    code: str

class UrlSchemeError(UrlError):
    code: str
    msg_template: str

class UrlSchemePermittedError(UrlError):
    code: str
    msg_template: str
    def __init__(self, allowed_schemes: Set[str]) -> None: ...

class UrlUserInfoError(UrlError):
    code: str
    msg_template: str

class UrlHostError(UrlError):
    code: str
    msg_template: str

class UrlHostTldError(UrlError):
    code: str
    msg_template: str

class UrlPortError(UrlError):
    code: str
    msg_template: str

class UrlExtraError(UrlError):
    code: str
    msg_template: str

class EnumMemberError(PydanticTypeError):
    code: str

class IntegerError(PydanticTypeError):
    msg_template: str

class FloatError(PydanticTypeError):
    msg_template: str

class PathError(PydanticTypeError):
    msg_template: str

class _PathValueError(PydanticValueError):
    def __init__(self, *, path: Path) -> None: ...

class PathNotExistsError(_PathValueError):
    code: str
    msg_template: str

class PathNotAFileError(_PathValueError):
    code: str
    msg_template: str

class PathNotADirectoryError(_PathValueError):
    code: str
    msg_template: str

class PyObjectError(PydanticTypeError):
    msg_template: str

class SequenceError(PydanticTypeError):
    msg_template: str

class IterableError(PydanticTypeError):
    msg_template: str

class ListError(PydanticTypeError):
    msg_template: str

class SetError(PydanticTypeError):
    msg_template: str

class FrozenSetError(PydanticTypeError):
    msg_template: str

class DequeError(PydanticTypeError):
    msg_template: str

class TupleError(PydanticTypeError):
    msg_template: str

class TupleLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, actual_length: int, expected_length: int) -> None: ...

class ListMinLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class ListMaxLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class ListUniqueItemsError(PydanticValueError):
    code: str
    msg_template: str

class SetMinLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class SetMaxLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class FrozenSetMinLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class FrozenSetMaxLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class AnyStrMinLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class AnyStrMaxLengthError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, limit_value: int) -> None: ...

class StrError(PydanticTypeError):
    msg_template: str

class StrRegexError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, pattern: str) -> None: ...

class _NumberBoundError(PydanticValueError):
    def __init__(self, *, limit_value: int | float | Decimal) -> None: ...

class NumberNotGtError(_NumberBoundError):
    code: str
    msg_template: str

class NumberNotGeError(_NumberBoundError):
    code: str
    msg_template: str

class NumberNotLtError(_NumberBoundError):
    code: str
    msg_template: str

class NumberNotLeError(_NumberBoundError):
    code: str
    msg_template: str

class NumberNotFiniteError(PydanticValueError):
    code: str
    msg_template: str

class NumberNotMultipleError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, multiple_of: int | float | Decimal) -> None: ...

class DecimalError(PydanticTypeError):
    msg_template: str

class DecimalIsNotFiniteError(PydanticValueError):
    code: str
    msg_template: str

class DecimalMaxDigitsError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, max_digits: int) -> None: ...

class DecimalMaxPlacesError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, decimal_places: int) -> None: ...

class DecimalWholeDigitsError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, whole_digits: int) -> None: ...

class DateTimeError(PydanticValueError):
    msg_template: str

class DateError(PydanticValueError):
    msg_template: str

class DateNotInThePastError(PydanticValueError):
    code: str
    msg_template: str

class DateNotInTheFutureError(PydanticValueError):
    code: str
    msg_template: str

class TimeError(PydanticValueError):
    msg_template: str

class DurationError(PydanticValueError):
    msg_template: str

class HashableError(PydanticTypeError):
    msg_template: str

class UUIDError(PydanticTypeError):
    msg_template: str

class UUIDVersionError(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, required_version: int) -> None: ...

class ArbitraryTypeError(PydanticTypeError):
    code: str
    msg_template: str
    def __init__(self, *, expected_arbitrary_type: Type[Any]) -> None: ...

class ClassError(PydanticTypeError):
    code: str
    msg_template: str

class SubclassError(PydanticTypeError):
    code: str
    msg_template: str
    def __init__(self, *, expected_class: Type[Any]) -> None: ...

class JsonError(PydanticValueError):
    msg_template: str

class JsonTypeError(PydanticTypeError):
    code: str
    msg_template: str

class PatternError(PydanticValueError):
    code: str
    msg_template: str

class DataclassTypeError(PydanticTypeError):
    code: str
    msg_template: str

class CallableError(PydanticTypeError):
    msg_template: str

class EnumError(PydanticTypeError):
    code: str
    msg_template: str

class IntEnumError(PydanticTypeError):
    code: str
    msg_template: str

class IPvAnyAddressError(PydanticValueError):
    msg_template: str

class IPvAnyInterfaceError(PydanticValueError):
    msg_template: str

class IPvAnyNetworkError(PydanticValueError):
    msg_template: str

class IPv4AddressError(PydanticValueError):
    msg_template: str

class IPv6AddressError(PydanticValueError):
    msg_template: str

class IPv4NetworkError(PydanticValueError):
    msg_template: str

class IPv6NetworkError(PydanticValueError):
    msg_template: str

class IPv4InterfaceError(PydanticValueError):
    msg_template: str

class IPv6InterfaceError(PydanticValueError):
    msg_template: str

class ColorError(PydanticValueError):
    msg_template: str

class StrictBoolError(PydanticValueError):
    msg_template: str

class NotDigitError(PydanticValueError):
    code: str
    msg_template: str

class LuhnValidationError(PydanticValueError):
    code: str
    msg_template: str

class InvalidLengthForBrand(PydanticValueError):
    code: str
    msg_template: str

class InvalidByteSize(PydanticValueError):
    msg_template: str

class InvalidByteSizeUnit(PydanticValueError):
    msg_template: str

class MissingDiscriminator(PydanticValueError):
    code: str
    msg_template: str

class InvalidDiscriminator(PydanticValueError):
    code: str
    msg_template: str
    def __init__(self, *, discriminator_key: str, discriminator_value: Any, allowed_values: Sequence[Any]) -> None: ...
