from _typeshed import Incomplete
from pyasn1.codec.ber import encoder

__all__ = ['Encoder', 'encode']

class BooleanEncoder(encoder.IntegerEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class RealEncoder(encoder.RealEncoder): ...

class TimeEncoderMixIn:
    Z_CHAR: Incomplete
    PLUS_CHAR: Incomplete
    MINUS_CHAR: Incomplete
    COMMA_CHAR: Incomplete
    DOT_CHAR: Incomplete
    ZERO_CHAR: Incomplete
    MIN_LENGTH: int
    MAX_LENGTH: int
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class GeneralizedTimeEncoder(TimeEncoderMixIn, encoder.OctetStringEncoder):
    MIN_LENGTH: int
    MAX_LENGTH: int

class UTCTimeEncoder(TimeEncoderMixIn, encoder.OctetStringEncoder):
    MIN_LENGTH: int
    MAX_LENGTH: int

class SetOfEncoder(encoder.SequenceOfEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceOfEncoder(encoder.SequenceOfEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SetEncoder(encoder.SequenceEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceEncoder(encoder.SequenceEncoder):
    omitEmptyOptionals: bool
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
