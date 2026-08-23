from _typeshed import Incomplete
from pyasn1.type import char, univ
from pyasn1_modules import rfc2315 as rfc2315, rfc5280 as rfc5280, rfc5652 as rfc5652, rfc5958 as rfc5958

pkcs12BagTypeMap: Incomplete
pkcs12CertBagMap: Incomplete
pkcs12CRLBagMap: Incomplete
pkcs12SecretBagMap: Incomplete
DigestInfo: Incomplete
ContentInfo: Incomplete
PKCS12Attribute: Incomplete
EncryptedPrivateKeyInfo: Incomplete
PrivateKeyInfo: Incomplete

class AttributeType(univ.ObjectIdentifier): ...
class AttributeValue(univ.Any): ...
class AttributeValues(univ.SetOf): ...
class CMSSingleAttribute(univ.Sequence): ...

rsadsi: Incomplete
pkcs: Incomplete
pkcs_9: Incomplete
certTypes: Incomplete
crlTypes: Incomplete
pkcs_12: Incomplete
pkcs_12PbeIds: Incomplete
pbeWithSHAAnd128BitRC4: Incomplete
pbeWithSHAAnd40BitRC4: Incomplete
pbeWithSHAAnd3_KeyTripleDES_CBC: Incomplete
pbeWithSHAAnd2_KeyTripleDES_CBC: Incomplete
pbeWithSHAAnd128BitRC2_CBC: Incomplete
pbeWithSHAAnd40BitRC2_CBC: Incomplete

class Pkcs_12PbeParams(univ.Sequence): ...

bagtypes: Incomplete

class BAG_TYPE(univ.Sequence): ...

id_keyBag: Incomplete

class KeyBag(PrivateKeyInfo): ...

id_pkcs8ShroudedKeyBag: Incomplete

class PKCS8ShroudedKeyBag(EncryptedPrivateKeyInfo): ...

id_certBag: Incomplete

class CertBag(univ.Sequence): ...

x509Certificate: Incomplete
sdsiCertificate: Incomplete
id_CRLBag: Incomplete

class CRLBag(univ.Sequence): ...

x509CRL: Incomplete
id_secretBag: Incomplete

class SecretBag(univ.Sequence): ...

id_safeContentsBag: Incomplete

class SafeBag(univ.Sequence): ...
class SafeContents(univ.SequenceOf): ...
class AuthenticatedSafe(univ.SequenceOf): ...
class MacData(univ.Sequence): ...
class PFX(univ.Sequence): ...

pkcs_9_at_localKeyId: Incomplete
localKeyId: Incomplete
pkcs_9_ub_pkcs9String: Incomplete
pkcs_9_ub_friendlyName: Incomplete
pkcs_9_at_friendlyName: Incomplete

class FriendlyName(char.BMPString): ...

friendlyName: Incomplete
