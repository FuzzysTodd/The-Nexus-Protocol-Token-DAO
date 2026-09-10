from _typeshed import Incomplete
from pyasn1.type import univ

__all__ = ['NumericString', 'PrintableString', 'TeletexString', 'T61String', 'VideotexString', 'IA5String', 'GraphicString', 'VisibleString', 'ISO646String', 'GeneralString', 'UniversalString', 'BMPString', 'UTF8String']

class AbstractCharacterString(univ.OctetString):
    '''Creates |ASN.1| schema or value object.

    |ASN.1| class is based on :class:`~pyasn1.type.base.SimpleAsn1Type`,
    its objects are immutable and duck-type Python 2 :class:`str` or Python 3
    :class:`bytes`. When used in octet-stream context, |ASN.1| type assumes
    "|encoding|" encoding.

    Keyword Args
    ------------
    value: :class:`unicode`, :class:`str`, :class:`bytes` or |ASN.1| object
        :class:`unicode` object (Python 2) or :class:`str` (Python 3),
        alternatively :class:`str` (Python 2) or :class:`bytes` (Python 3)
        representing octet-stream of serialised unicode string
        (note `encoding` parameter) or |ASN.1| class instance.
        If `value` is not given, schema object will be created.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s). Constraints
        verification for |ASN.1| type occurs automatically on object
        instantiation.

    encoding: :py:class:`str`
        Unicode codec ID to encode/decode :class:`unicode` (Python 2) or
        :class:`str` (Python 3) the payload when |ASN.1| object is used
        in octet-stream context.

    Raises
    ------
    ~pyasn1.error.ValueConstraintError, ~pyasn1.error.PyAsn1Error
        On constraint violation or bad initializer.
    '''
    def __bytes__(self) -> bytes: ...
    def prettyIn(self, value): ...
    def asOctets(self, padding: bool = True): ...
    def asNumbers(self, padding: bool = True): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = 0): ...
    def __reversed__(self): ...

class NumericString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class PrintableString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class TeletexString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class T61String(TeletexString):
    __doc__: Incomplete
    typeId: Incomplete

class VideotexString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class IA5String(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class GraphicString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class VisibleString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class ISO646String(VisibleString):
    __doc__: Incomplete
    typeId: Incomplete

class GeneralString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class UniversalString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class BMPString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class UTF8String(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete
