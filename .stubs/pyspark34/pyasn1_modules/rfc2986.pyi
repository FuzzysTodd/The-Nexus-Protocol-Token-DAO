from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
AttributeType = rfc5280.AttributeType
AttributeValue = rfc5280.AttributeValue
AttributeTypeAndValue = rfc5280.AttributeTypeAndValue
Attribute = rfc5280.Attribute
RelativeDistinguishedName = rfc5280.RelativeDistinguishedName
RDNSequence = rfc5280.RDNSequence
Name = rfc5280.Name
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
SubjectPublicKeyInfo = rfc5280.SubjectPublicKeyInfo

class Attributes(univ.SetOf): ...
class CertificationRequestInfo(univ.Sequence): ...
class CertificationRequest(univ.Sequence): ...
