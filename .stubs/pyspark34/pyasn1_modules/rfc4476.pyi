from _typeshed import Incomplete
from pyasn1.type import char, univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
PolicyQualifierId = rfc5280.PolicyQualifierId
PolicyQualifierInfo = rfc5280.PolicyQualifierInfo
UserNotice = rfc5280.UserNotice
id_pkix: Incomplete
id_pe: Incomplete
id_pe_acPolicies: Incomplete
id_qt: Incomplete
id_qt_acps: Incomplete
id_qt_acunotice: Incomplete

class ACUserNotice(UserNotice): ...
class ACPSuri(char.IA5String): ...
class AcPolicyId(univ.ObjectIdentifier): ...

class PolicyInformation(univ.Sequence):
    componentType: Incomplete

class AcPoliciesSyntax(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete
