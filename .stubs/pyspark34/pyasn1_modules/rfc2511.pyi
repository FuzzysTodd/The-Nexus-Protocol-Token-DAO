from pyasn1_modules.rfc2459 import *
from _typeshed import Incomplete
from pyasn1_modules import rfc2315 as rfc2315

MAX: Incomplete
id_pkix: Incomplete
id_pkip: Incomplete
id_regCtrl: Incomplete
id_regCtrl_regToken: Incomplete
id_regCtrl_authenticator: Incomplete
id_regCtrl_pkiPublicationInfo: Incomplete
id_regCtrl_pkiArchiveOptions: Incomplete
id_regCtrl_oldCertID: Incomplete
id_regCtrl_protocolEncrKey: Incomplete
id_regInfo: Incomplete
id_regInfo_utf8Pairs: Incomplete
id_regInfo_certReq: Incomplete

class GeneralName(univ.OctetString): ...
class UTF8Pairs(char.UTF8String): ...
class ProtocolEncrKey(SubjectPublicKeyInfo): ...

class CertId(univ.Sequence):
    componentType: Incomplete

class OldCertId(CertId): ...
class KeyGenParameters(univ.OctetString): ...

class EncryptedValue(univ.Sequence):
    componentType: Incomplete

class EncryptedKey(univ.Choice):
    componentType: Incomplete

class PKIArchiveOptions(univ.Choice):
    componentType: Incomplete

class SinglePubInfo(univ.Sequence):
    componentType: Incomplete

class PKIPublicationInfo(univ.Sequence):
    componentType: Incomplete

class Authenticator(char.UTF8String): ...
class RegToken(char.UTF8String): ...

class SubsequentMessage(univ.Integer):
    namedValues: Incomplete

class POPOPrivKey(univ.Choice):
    componentType: Incomplete

class PBMParameter(univ.Sequence):
    componentType: Incomplete

class PKMACValue(univ.Sequence):
    componentType: Incomplete

class POPOSigningKeyInput(univ.Sequence):
    componentType: Incomplete

class POPOSigningKey(univ.Sequence):
    componentType: Incomplete

class ProofOfPossession(univ.Choice):
    componentType: Incomplete

class Controls(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class OptionalValidity(univ.Sequence):
    componentType: Incomplete

class CertTemplate(univ.Sequence):
    componentType: Incomplete

class CertRequest(univ.Sequence):
    componentType: Incomplete

class CertReq(CertRequest): ...

class CertReqMsg(univ.Sequence):
    componentType: Incomplete

class CertReqMessages(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete
