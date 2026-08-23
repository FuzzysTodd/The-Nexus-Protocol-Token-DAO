from _typeshed import Incomplete
from collections import OrderedDict

__all__ = ['encode']

class AbstractItemEncoder:
    def encode(self, value, encodeFun, **options) -> None: ...

class BooleanEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class IntegerEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class BitStringEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class OctetStringEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class TextStringEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class NullEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options) -> None: ...

class ObjectIdentifierEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class RealEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class SetEncoder(AbstractItemEncoder):
    protoDict = dict
    def encode(self, value, encodeFun, **options): ...

class SequenceEncoder(SetEncoder):
    protoDict = OrderedDict

class SequenceOfEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class ChoiceEncoder(SequenceEncoder): ...

class AnyEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemEncoder:
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP
    def __init__(self, tagMap=..., typeMap=..., **ignored) -> None: ...
    def __call__(self, value, **options): ...

class Encoder:
    SINGLE_ITEM_ENCODER = SingleItemEncoder
    def __init__(self, **options) -> None: ...
    def __call__(self, pyObject, asn1Spec: Incomplete | None = None, **options): ...

encode: Incomplete
