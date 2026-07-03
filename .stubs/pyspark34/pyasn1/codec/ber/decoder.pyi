from _typeshed import Incomplete
from collections.abc import Generator
from pyasn1 import error

__all__ = ['StreamingDecoder', 'Decoder', 'decode']

SubstrateUnderrunError = error.SubstrateUnderrunError

class AbstractPayloadDecoder:
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> None:
        """Decode value with fixed byte length.

        The decoder is allowed to consume as many bytes as necessary.
        """
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> None:
        """Decode value with undefined length.

        The decoder is allowed to consume as many bytes as necessary.
        """

class AbstractSimplePayloadDecoder(AbstractPayloadDecoder):
    @staticmethod
    def substrateCollector(asn1Object, substrate, length, options) -> Generator[Incomplete, None, None]: ...

class RawPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class IntegerPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class BooleanPayloadDecoder(IntegerPayloadDecoder):
    protoComponent: Incomplete

class BitStringPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    supportConstructedForm: bool
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class OctetStringPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    supportConstructedForm: bool
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class NullPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class ObjectIdentifierPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class RealPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class AbstractConstructedPayloadDecoder(AbstractPayloadDecoder):
    protoComponent: Incomplete

class ConstructedPayloadDecoderBase(AbstractConstructedPayloadDecoder):
    protoRecordComponent: Incomplete
    protoSequenceComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class SequenceOrSequenceOfPayloadDecoder(ConstructedPayloadDecoderBase):
    protoRecordComponent: Incomplete
    protoSequenceComponent: Incomplete

class SequencePayloadDecoder(SequenceOrSequenceOfPayloadDecoder):
    protoComponent: Incomplete

class SequenceOfPayloadDecoder(SequenceOrSequenceOfPayloadDecoder):
    protoComponent: Incomplete

class SetOrSetOfPayloadDecoder(ConstructedPayloadDecoderBase):
    protoRecordComponent: Incomplete
    protoSequenceComponent: Incomplete

class SetPayloadDecoder(SetOrSetOfPayloadDecoder):
    protoComponent: Incomplete

class SetOfPayloadDecoder(SetOrSetOfPayloadDecoder):
    protoComponent: Incomplete

class ChoicePayloadDecoder(ConstructedPayloadDecoderBase):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class AnyPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: Incomplete
    def valueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet: Incomplete | None = None, length: Incomplete | None = None, state: Incomplete | None = None, decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, None]: ...

class UTF8StringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class NumericStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class PrintableStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class TeletexStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class VideotexStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class IA5StringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class GraphicStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class VisibleStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class GeneralStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class UniversalStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class BMPStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class ObjectDescriptorPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class GeneralizedTimePayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete

class UTCTimePayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: Incomplete
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemDecoder:
    defaultErrorState = stErrorCondition
    defaultRawDecoder: Incomplete
    supportIndefLength: bool
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP
    def __init__(self, tagMap=..., typeMap=..., **ignored) -> None: ...
    def __call__(self, substrate, asn1Spec: Incomplete | None = None, tagSet: Incomplete | None = None, length: Incomplete | None = None, state=..., decodeFun: Incomplete | None = None, substrateFun: Incomplete | None = None, **options) -> Generator[Incomplete, None, Incomplete]: ...

class StreamingDecoder:
    """Create an iterator that turns BER/CER/DER byte stream into ASN.1 objects.

    On each iteration, consume whatever BER/CER/DER serialization is
    available in the `substrate` stream-like object and turns it into
    one or more, possibly nested, ASN.1 objects.

    Parameters
    ----------
    substrate: :py:class:`file`, :py:class:`io.BytesIO`
        BER/CER/DER serialization in form of a byte stream

    Keyword Args
    ------------
    asn1Spec: :py:class:`~pyasn1.type.base.PyAsn1Item`
        A pyasn1 type object to act as a template guiding the decoder.
        Depending on the ASN.1 structure being decoded, `asn1Spec` may
        or may not be required. One of the reasons why `asn1Spec` may
        me required is that ASN.1 structure is encoded in the *IMPLICIT*
        tagging mode.

    Yields
    ------
    : :py:class:`~pyasn1.type.base.PyAsn1Item`, :py:class:`~pyasn1.error.SubstrateUnderrunError`
        Decoded ASN.1 object (possibly, nested) or
        :py:class:`~pyasn1.error.SubstrateUnderrunError` object indicating
        insufficient BER/CER/DER serialization on input to fully recover ASN.1
        objects from it.
        
        In the latter case the caller is advised to ensure some more data in
        the input stream, then call the iterator again. The decoder will resume
        the decoding process using the newly arrived data.

        The `context` property of :py:class:`~pyasn1.error.SubstrateUnderrunError`
        object might hold a reference to the partially populated ASN.1 object
        being reconstructed.

    Raises
    ------
    ~pyasn1.error.PyAsn1Error, ~pyasn1.error.EndOfStreamError
        `PyAsn1Error` on deserialization error, `EndOfStreamError` on
         premature stream closure.

    Examples
    --------
    Decode BER serialisation without ASN.1 schema

    .. code-block:: pycon

        >>> stream = io.BytesIO(
        ...    b'0\t\x02\x01\x01\x02\x01\x02\x02\x01\x03')
        >>>
        >>> for asn1Object in StreamingDecoder(stream):
        ...     print(asn1Object)
        >>>
        SequenceOf:
         1 2 3

    Decode BER serialisation with ASN.1 schema

    .. code-block:: pycon

        >>> stream = io.BytesIO(
        ...    b'0\t\x02\x01\x01\x02\x01\x02\x02\x01\x03')
        >>>
        >>> schema = SequenceOf(componentType=Integer())
        >>>
        >>> decoder = StreamingDecoder(stream, asn1Spec=schema)
        >>> for asn1Object in decoder:
        ...     print(asn1Object)
        >>>
        SequenceOf:
         1 2 3
    """
    SINGLE_ITEM_DECODER = SingleItemDecoder
    def __init__(self, substrate, asn1Spec: Incomplete | None = None, **options) -> None: ...
    def __iter__(self): ...

class Decoder:
    """Create a BER decoder object.

    Parse BER/CER/DER octet-stream into one, possibly nested, ASN.1 object.
    """
    STREAMING_DECODER = StreamingDecoder
    @classmethod
    def __call__(cls, substrate, asn1Spec: Incomplete | None = None, **options):
        """Turns BER/CER/DER octet stream into an ASN.1 object.

        Takes BER/CER/DER octet-stream in form of :py:class:`bytes` (Python 3)
        or :py:class:`str` (Python 2) and decode it into an ASN.1 object
        (e.g. :py:class:`~pyasn1.type.base.PyAsn1Item` derivative) which
        may be a scalar or an arbitrary nested structure.

        Parameters
        ----------
        substrate: :py:class:`bytes` (Python 3) or :py:class:`str` (Python 2)
            BER/CER/DER octet-stream to parse

        Keyword Args
        ------------
        asn1Spec: :py:class:`~pyasn1.type.base.PyAsn1Item`
            A pyasn1 type object (:py:class:`~pyasn1.type.base.PyAsn1Item`
            derivative) to act as a template guiding the decoder.
            Depending on the ASN.1 structure being decoded, `asn1Spec` may or
            may not be required. Most common reason for it to require is that
            ASN.1 structure is encoded in *IMPLICIT* tagging mode.

        Returns
        -------
        : :py:class:`tuple`
            A tuple of :py:class:`~pyasn1.type.base.PyAsn1Item` object
            recovered from BER/CER/DER substrate and the unprocessed trailing
            portion of the `substrate` (may be empty)

        Raises
        ------
        : :py:class:`~pyasn1.error.PyAsn1Error`
            :py:class:`~pyasn1.error.SubstrateUnderrunError` on insufficient
            input or :py:class:`~pyasn1.error.PyAsn1Error` on decoding error.

        Examples
        --------
        Decode BER/CER/DER serialisation without ASN.1 schema

        .. code-block:: pycon

           >>> s, unprocessed = decode(b'0\t\x02\x01\x01\x02\x01\x02\x02\x01\x03')
           >>> str(s)
           SequenceOf:
            1 2 3

        Decode BER/CER/DER serialisation with ASN.1 schema

        .. code-block:: pycon

           >>> seq = SequenceOf(componentType=Integer())
           >>> s, unprocessed = decode(
                b'0\t\x02\x01\x01\x02\x01\x02\x02\x01\x03', asn1Spec=seq)
           >>> str(s)
           SequenceOf:
            1 2 3

        """

decode: Incomplete
