import typing
from cryptography import utils as utils
from cryptography.x509.oid import NameOID as NameOID, ObjectIdentifier as ObjectIdentifier

class _ASN1Type(utils.Enum):
    BitString: int
    OctetString: int
    UTF8String: int
    NumericString: int
    PrintableString: int
    T61String: int
    IA5String: int
    UTCTime: int
    GeneralizedTime: int
    VisibleString: int
    UniversalString: int
    BMPString: int

class NameAttribute:
    def __init__(self, oid: ObjectIdentifier, value: str | bytes, _type: _ASN1Type | None = None, *, _validate: bool = True) -> None: ...
    @property
    def oid(self) -> ObjectIdentifier: ...
    @property
    def value(self) -> str | bytes: ...
    @property
    def rfc4514_attribute_name(self) -> str:
        '''
        The short attribute name (for example "CN") if available,
        otherwise the OID dotted string.
        '''
    def rfc4514_string(self, attr_name_overrides: _OidNameMap | None = None) -> str:
        """
        Format as RFC4514 Distinguished Name string.

        Use short attribute name if available, otherwise fall back to OID
        dotted string.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class RelativeDistinguishedName:
    def __init__(self, attributes: typing.Iterable[NameAttribute]) -> None: ...
    def get_attributes_for_oid(self, oid: ObjectIdentifier) -> typing.List[NameAttribute]: ...
    def rfc4514_string(self, attr_name_overrides: _OidNameMap | None = None) -> str:
        """
        Format as RFC4514 Distinguished Name string.

        Within each RDN, attributes are joined by '+', although that is rarely
        used in certificates.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> typing.Iterator[NameAttribute]: ...
    def __len__(self) -> int: ...

class Name:
    @typing.overload
    def __init__(self, attributes: typing.Iterable[NameAttribute]) -> None: ...
    @typing.overload
    def __init__(self, attributes: typing.Iterable[RelativeDistinguishedName]) -> None: ...
    @classmethod
    def from_rfc4514_string(cls, data: str, attr_name_overrides: _NameOidMap | None = None) -> Name: ...
    def rfc4514_string(self, attr_name_overrides: _OidNameMap | None = None) -> str:
        """
        Format as RFC4514 Distinguished Name string.
        For example 'CN=foobar.com,O=Foo Corp,C=US'

        An X.509 name is a two-level structure: a list of sets of attributes.
        Each list element is separated by ',' and within each list element, set
        elements are separated by '+'. The latter is almost never used in
        real world certificates. According to RFC4514 section 2.1 the
        RDNSequence must be reversed when converting to string representation.
        """
    def get_attributes_for_oid(self, oid: ObjectIdentifier) -> typing.List[NameAttribute]: ...
    @property
    def rdns(self) -> typing.List[RelativeDistinguishedName]: ...
    def public_bytes(self, backend: typing.Any = None) -> bytes: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> typing.Iterator[NameAttribute]: ...
    def __len__(self) -> int: ...

class _RFC4514NameParser:
    def __init__(self, data: str, attr_name_overrides: _NameOidMap) -> None: ...
    def parse(self) -> Name:
        """
        Parses the `data` string and converts it to a Name.

        According to RFC4514 section 2.1 the RDNSequence must be
        reversed when converting to string representation. So, when
        we parse it, we need to reverse again to get the RDNs on the
        correct order.
        """
