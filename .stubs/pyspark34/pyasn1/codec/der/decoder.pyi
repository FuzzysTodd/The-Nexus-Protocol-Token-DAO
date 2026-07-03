from _typeshed import Incomplete
from pyasn1.codec.cer import decoder

__all__ = ['decode', 'StreamingDecoder']

class BitStringPayloadDecoder(decoder.BitStringPayloadDecoder):
    supportConstructedForm: bool

class OctetStringPayloadDecoder(decoder.OctetStringPayloadDecoder):
    supportConstructedForm: bool
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemDecoder(decoder.SingleItemDecoder):
    __doc__: Incomplete
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP
    supportIndefLength: bool

class StreamingDecoder(decoder.StreamingDecoder):
    __doc__: Incomplete
    SINGLE_ITEM_DECODER = SingleItemDecoder

class Decoder(decoder.Decoder):
    __doc__: Incomplete
    STREAMING_DECODER = StreamingDecoder

decode: Incomplete
