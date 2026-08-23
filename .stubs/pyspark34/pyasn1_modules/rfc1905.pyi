from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc1902 as rfc1902

max_bindings: Incomplete

class _BindValue(univ.Choice):
    componentType: Incomplete

class VarBind(univ.Sequence):
    componentType: Incomplete

class VarBindList(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class PDU(univ.Sequence):
    componentType: Incomplete

class BulkPDU(univ.Sequence):
    componentType: Incomplete

class GetRequestPDU(PDU):
    tagSet: Incomplete

class GetNextRequestPDU(PDU):
    tagSet: Incomplete

class ResponsePDU(PDU):
    tagSet: Incomplete

class SetRequestPDU(PDU):
    tagSet: Incomplete

class GetBulkRequestPDU(BulkPDU):
    tagSet: Incomplete

class InformRequestPDU(PDU):
    tagSet: Incomplete

class SNMPv2TrapPDU(PDU):
    tagSet: Incomplete

class ReportPDU(PDU):
    tagSet: Incomplete

class PDUs(univ.Choice):
    componentType: Incomplete
