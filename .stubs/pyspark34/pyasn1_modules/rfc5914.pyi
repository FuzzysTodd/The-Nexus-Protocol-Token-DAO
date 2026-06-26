from _typeshed import Incomplete
from pyasn1.type import char, univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
Certificate = rfc5280.Certificate
Name = rfc5280.Name
Extensions = rfc5280.Extensions
SubjectPublicKeyInfo = rfc5280.SubjectPublicKeyInfo
TBSCertificate = rfc5280.TBSCertificate
CertificatePolicies = rfc5280.CertificatePolicies
KeyIdentifier = rfc5280.KeyIdentifier
NameConstraints = rfc5280.NameConstraints

class CertPolicyFlags(univ.BitString): ...
class CertPathControls(univ.Sequence): ...
class TrustAnchorTitle(char.UTF8String): ...
class TrustAnchorInfoVersion(univ.Integer): ...
class TrustAnchorInfo(univ.Sequence): ...
class TrustAnchorChoice(univ.Choice): ...

id_ct_trustAnchorList: Incomplete

class TrustAnchorList(univ.SequenceOf): ...
