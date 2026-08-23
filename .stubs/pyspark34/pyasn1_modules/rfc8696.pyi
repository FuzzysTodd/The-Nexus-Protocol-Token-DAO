from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5652 as rfc5652

MAX: Incomplete
id_ori: Incomplete
id_ori_keyTransPSK: Incomplete
id_ori_keyAgreePSK: Incomplete

class PreSharedKeyIdentifier(univ.OctetString): ...

class KeyTransRecipientInfos(univ.SequenceOf):
    componentType: Incomplete

class KeyTransPSKRecipientInfo(univ.Sequence):
    componentType: Incomplete

class KeyAgreePSKRecipientInfo(univ.Sequence):
    componentType: Incomplete

class CMSORIforPSKOtherInfo(univ.Sequence):
    componentType: Incomplete
