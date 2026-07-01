from _typeshed import Incomplete
from pyasn1.type import univ, useful
from pyasn1_modules import rfc5652 as rfc5652

ContentInfo = rfc5652.ContentInfo
EncapsulatedContentInfo = rfc5652.EncapsulatedContentInfo
id_data: Incomplete
id_KISA: Incomplete
id_npki: Incomplete
id_attribute: Incomplete
id_kisa_tac: Incomplete
id_kisa_tac_token: Incomplete
id_kisa_tac_tokenandblindbash: Incomplete
id_kisa_tac_tokenandpartially: Incomplete

class UserKey(univ.OctetString): ...
class Timeout(useful.GeneralizedTime): ...
class BlinedCertificateHash(univ.OctetString): ...
class PartiallySignedCertificateHash(univ.OctetString): ...
class Token(ContentInfo): ...
class TokenandBlindHash(ContentInfo): ...
class TokenandPartiallySignedCertificateHash(ContentInfo): ...

class TACToken(univ.Sequence):
    componentType: Incomplete

class TACTokenandBlindHash(univ.Sequence):
    componentType: Incomplete

class TACTokenandPartiallySignedCertificateHash(univ.Sequence):
    componentType: Incomplete
