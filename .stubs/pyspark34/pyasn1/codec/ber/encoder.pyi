from _typeshed import Incomplete

__all__ = ['Encoder', 'encode']

class AbstractItemEncoder:
    supportIndefLenMode: bool
    eooIntegerSubstrate: Incomplete
    eooOctetsSubstrate: Incomplete
    def encodeTag(self, singleTag, isConstructed): ...
    def encodeLength(self, length, defMode): ...
    def encodeValue(self, value, asn1Spec, encodeFun, **options) -> None: ...
    def encode(self, value, asn1Spec: Incomplete | None = None, encodeFun: Incomplete | None = None, **options): ...

class EndOfOctetsEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class BooleanEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class IntegerEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    supportCompactZero: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class BitStringEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class OctetStringEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class NullEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class ObjectIdentifierEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class RealEncoder(AbstractItemEncoder):
    supportIndefLenMode: bool
    binEncBase: int
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceEncoder(AbstractItemEncoder):
    omitEmptyOptionals: bool
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceOfEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class ChoiceEncoder(AbstractItemEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class AnyEncoder(OctetStringEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemEncoder:
    fixedDefLengthMode: Incomplete
    fixedChunkSize: Incomplete
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP
    def __init__(self, tagMap=..., typeMap=..., **ignored) -> None: ...
    def __call__(self, value, asn1Spec: Incomplete | None = None, **options): ...

class Encoder:
    SINGLE_ITEM_ENCODER = SingleItemEncoder
    def __init__(self, tagMap=..., typeMap=..., **options) -> None: ...
    def __call__(self, pyObject, asn1Spec: Incomplete | None = None, **options): ...

encode: Incomplete
