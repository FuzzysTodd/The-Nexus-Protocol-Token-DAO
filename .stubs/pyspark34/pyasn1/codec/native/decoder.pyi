from _typeshed import Incomplete

__all__ = ['decode']

class AbstractScalarPayloadDecoder:
    def __call__(self, pyObject, asn1Spec, decodeFun: Incomplete | None = None, **options): ...

class BitStringPayloadDecoder(AbstractScalarPayloadDecoder):
    def __call__(self, pyObject, asn1Spec, decodeFun: Incomplete | None = None, **options): ...

class SequenceOrSetPayloadDecoder:
    def __call__(self, pyObject, asn1Spec, decodeFun: Incomplete | None = None, **options): ...

class SequenceOfOrSetOfPayloadDecoder:
    def __call__(self, pyObject, asn1Spec, decodeFun: Incomplete | None = None, **options): ...

class ChoicePayloadDecoder:
    def __call__(self, pyObject, asn1Spec, decodeFun: Incomplete | None = None, **options): ...
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemDecoder:
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP
    def __init__(self, tagMap=..., typeMap=..., **ignored) -> None: ...
    def __call__(self, pyObject, asn1Spec, **options): ...

class Decoder:
    SINGLE_ITEM_DECODER = SingleItemDecoder
    def __init__(self, **options) -> None: ...
    def __call__(self, pyObject, asn1Spec: Incomplete | None = None, **kwargs): ...

decode: Incomplete
