from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc2634 as rfc2634, rfc4055 as rfc4055, rfc5280 as rfc5280, rfc5652 as rfc5652

ContentType = rfc5652.ContentType
IssuerAndSerialNumber = rfc5652.IssuerAndSerialNumber
SubjectKeyIdentifier = rfc5652.SubjectKeyIdentifier
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
PolicyInformation = rfc5280.PolicyInformation
GeneralNames = rfc5280.GeneralNames
CertificateSerialNumber = rfc5280.CertificateSerialNumber
id_aa_signingCertificate: Incomplete
id_aa_signingCertificateV2: Incomplete
Hash: Incomplete
IssuerSerial: Incomplete
ESSCertID: Incomplete
SigningCertificate: Incomplete
sha256AlgId: Incomplete

class ESSCertIDv2(univ.Sequence): ...
class SigningCertificateV2(univ.Sequence): ...

id_aa_mlExpandHistory: Incomplete
ub_ml_expansion_history: Incomplete
EntityIdentifier: Incomplete
MLReceiptPolicy: Incomplete
MLData: Incomplete
MLExpansionHistory: Incomplete
id_aa_securityLabel: Incomplete
ub_privacy_mark_length: Incomplete
ub_security_categories: Incomplete
ub_integer_options: Incomplete
ESSPrivacyMark: Incomplete
SecurityClassification: Incomplete
SecurityPolicyIdentifier: Incomplete
SecurityCategory: Incomplete
SecurityCategories: Incomplete
ESSSecurityLabel: Incomplete
id_aa_equivalentLabels: Incomplete
EquivalentLabels: Incomplete
id_aa_contentIdentifier: Incomplete
ContentIdentifier: Incomplete
id_aa_contentReference: Incomplete
ContentReference: Incomplete
id_aa_msgSigDigest: Incomplete
MsgSigDigest: Incomplete
id_aa_contentHint: Incomplete
ContentHints: Incomplete
AllOrFirstTier: Incomplete
ReceiptsFrom: Incomplete
id_aa_receiptRequest: Incomplete
ub_receiptsTo: Incomplete
ReceiptRequest: Incomplete
ESSVersion: Incomplete
id_ct_receipt: Incomplete
Receipt: Incomplete
