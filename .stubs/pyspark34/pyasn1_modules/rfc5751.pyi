from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5652 as rfc5652, rfc8018 as rfc8018

IssuerAndSerialNumber: Incomplete
RecipientKeyIdentifier: Incomplete
SubjectKeyIdentifier: Incomplete
rc2CBC: Incomplete
smimeCapabilities: Incomplete
smimeCapabilityMap: Incomplete

class SMIMECapability(univ.Sequence): ...
class SMIMECapabilities(univ.SequenceOf): ...
class SMIMECapabilitiesParametersForRC2CBC(univ.Integer): ...

id_smime: Incomplete
id_aa: Incomplete
id_aa_encrypKeyPref: Incomplete

class SMIMEEncryptionKeyPreference(univ.Choice): ...

id_cap: Incomplete
id_cap_preferBinaryInside: Incomplete
