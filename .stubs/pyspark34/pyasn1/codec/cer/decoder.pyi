from _typeshed import Incomplete
from collections.abc import Generator
from pyasn1 import error
from pyasn1.codec.ber import decoder

__all__ = ['decode', 'StreamingDecoder']

SubstrateUnderrunError = error.SubstrateUnderrunError

class BooleanPayloadDecoder(decoder.AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemDecoder(decoder.SingleItemDecoder):
    __doc__: Incomplete
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP

class StreamingDecoder(decoder.StreamingDecoder):
    __doc__: Incomplete
    SINGLE_ITEM_DECODER = SingleItemDecoder

class Decoder(decoder.Decoder):
    __doc__: Incomplete
    STREAMING_DECODER = StreamingDecoder

decode: Incomplete
