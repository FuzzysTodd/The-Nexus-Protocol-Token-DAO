from .config import BaseConfig
from .fields import ModelField
from .typing import AnyCallable
from .utils import Representation
from _typeshed import Incomplete
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network, _BaseAddress, _BaseNetwork
from typing import Any, Collection, Dict, Generator, List, Set, Tuple, Type
from typing_extensions import TypedDict

__all__ = ['AnyUrl', 'AnyHttpUrl', 'FileUrl', 'HttpUrl', 'stricturl', 'EmailStr', 'NameEmail', 'IPvAnyAddress', 'IPvAnyInterface', 'IPvAnyNetwork', 'PostgresDsn', 'CockroachDsn', 'AmqpDsn', 'RedisDsn', 'MongoDsn', 'KafkaDsn', 'validate_email']

CallableGenerator = Generator[AnyCallable, None, None]

class Parts(TypedDict, total=False):
    scheme: str
    user: str | None
    password: str | None
    ipv4: str | None
    ipv6: str | None
    domain: str | None
    port: str | None
    path: str | None
    query: str | None
    fragment: str | None

class HostParts(TypedDict, total=False):
    host: str
    tld: str | None
    host_type: str | None
    port: str | None
    rebuild: bool
NetworkType = str | bytes | int | Tuple[str | bytes | int, str | int]

class AnyUrl(str):
    strip_whitespace: bool
    min_length: int
    max_length: Incomplete
    allowed_schemes: Collection[str] | None
    tld_required: bool
    user_required: bool
    host_required: bool
    hidden_parts: Set[str]
    def __new__(cls, url, **kwargs): ...
    scheme: Incomplete
    user: Incomplete
    password: Incomplete
    host: Incomplete
    tld: Incomplete
    host_type: Incomplete
    port: Incomplete
    path: Incomplete
    query: Incomplete
    fragment: Incomplete
    def __init__(self, url: str, *, scheme: str, user: str | None = None, password: str | None = None, host: str | None = None, tld: str | None = None, host_type: str = 'domain', port: str | None = None, path: str | None = None, query: str | None = None, fragment: str | None = None) -> None: ...
    @classmethod
    def build(cls, *, scheme: str, user: str | None = None, password: str | None = None, host: str, port: str | None = None, path: str | None = None, query: str | None = None, fragment: str | None = None, **_kwargs: str) -> str: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: Any, field: ModelField, config: BaseConfig) -> AnyUrl: ...
    @classmethod
    def validate_parts(cls, parts: Parts, validate_port: bool = True) -> Parts:
        """
        A method used to validate parts of a URL.
        Could be overridden to set default values for parts if missing
        """
    @classmethod
    def validate_host(cls, parts: Parts) -> Tuple[str, str | None, str, bool]: ...
    @staticmethod
    def get_default_parts(parts: Parts) -> Parts: ...
    @classmethod
    def apply_default_parts(cls, parts: Parts) -> Parts: ...

class AnyHttpUrl(AnyUrl):
    allowed_schemes: Incomplete

class HttpUrl(AnyHttpUrl):
    tld_required: bool
    max_length: int
    hidden_parts: Incomplete
    @staticmethod
    def get_default_parts(parts: Parts) -> Parts: ...

class FileUrl(AnyUrl):
    allowed_schemes: Incomplete
    host_required: bool

class MultiHostDsn(AnyUrl):
    hosts: Incomplete
    def __init__(self, *args: Any, hosts: List['HostParts'] | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def validate_parts(cls, parts: Parts, validate_port: bool = True) -> Parts: ...

class PostgresDsn(MultiHostDsn):
    allowed_schemes: Incomplete
    user_required: bool

class CockroachDsn(AnyUrl):
    allowed_schemes: Incomplete
    user_required: bool

class AmqpDsn(AnyUrl):
    allowed_schemes: Incomplete
    host_required: bool

class RedisDsn(AnyUrl):
    allowed_schemes: Incomplete
    host_required: bool
    @staticmethod
    def get_default_parts(parts: Parts) -> Parts: ...

class MongoDsn(AnyUrl):
    allowed_schemes: Incomplete
    @staticmethod
    def get_default_parts(parts: Parts) -> Parts: ...

class KafkaDsn(AnyUrl):
    allowed_schemes: Incomplete
    @staticmethod
    def get_default_parts(parts: Parts) -> Parts: ...

def stricturl(*, strip_whitespace: bool = True, min_length: int = 1, max_length: int = ..., tld_required: bool = True, host_required: bool = True, allowed_schemes: Collection[str] | None = None) -> Type[AnyUrl]: ...

class EmailStr(str):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: str) -> str: ...

class NameEmail(Representation):
    name: Incomplete
    email: Incomplete
    def __init__(self, name: str, email: str) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: Any) -> NameEmail: ...

class IPvAnyAddress(_BaseAddress):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: str | bytes | int) -> IPv4Address | IPv6Address: ...

class IPvAnyInterface(_BaseAddress):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: NetworkType) -> IPv4Interface | IPv6Interface: ...

class IPvAnyNetwork(_BaseNetwork):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: NetworkType) -> IPv4Network | IPv6Network: ...

def validate_email(value: str) -> Tuple[str, str]:
    '''
    Email address validation using https://pypi.org/project/email-validator/
    Notes:
    * raw ip address (literal) domain parts are not allowed.
    * "John Doe <local_part@domain.com>" style "pretty" email addresses are processed
    * spaces are striped from the beginning and end of addresses but no error is raised
    '''
