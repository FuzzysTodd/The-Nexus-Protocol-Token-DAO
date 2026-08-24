from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc1155 as rfc1155

class Version(univ.Integer):
    namedValues: Incomplete
    defaultValue: int

class Community(univ.OctetString): ...
class RequestID(univ.Integer): ...

class ErrorStatus(univ.Integer):
    namedValues: Incomplete

class ErrorIndex(univ.Integer): ...

class VarBind(univ.Sequence):
    componentType: Incomplete

class VarBindList(univ.SequenceOf):
    componentType: Incomplete

class _RequestBase(univ.Sequence):
    componentType: Incomplete

class GetRequestPDU(_RequestBase):
    tagSet: Incomplete

class GetNextRequestPDU(_RequestBase):
    tagSet: Incomplete

class GetResponsePDU(_RequestBase):
    tagSet: Incomplete

class SetRequestPDU(_RequestBase):
    tagSet: Incomplete

class TrapPDU(univ.Sequence):
    componentType: Incomplete

class Pdus(univ.Choice):
    componentType: Incomplete

class Message(univ.Sequence):
    componentType: Incomplete
