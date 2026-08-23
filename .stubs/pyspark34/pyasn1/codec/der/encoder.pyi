from _typeshed import Incomplete
from pyasn1.codec.cer import encoder

__all__ = ['Encoder', 'encode']

class SetEncoder(encoder.SetEncoder): ...
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemEncoder(encoder.SingleItemEncoder):
    fixedDefLengthMode: bool
    fixedChunkSize: int
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP

class Encoder(encoder.Encoder):
    SINGLE_ITEM_ENCODER = SingleItemEncoder

encode: Incomplete
