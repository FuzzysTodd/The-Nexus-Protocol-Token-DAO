from _typeshed import Incomplete
from pyasn1.type import char, univ
from pyasn1_modules import rfc2634 as rfc2634, rfc4108 as rfc4108, rfc5280 as rfc5280, rfc5652 as rfc5652, rfc6010 as rfc6010, rfc6019 as rfc6019, rfc7191 as rfc7191

MAX: Incomplete
id_aa_contentHint: Incomplete
ContentHints: Incomplete
id_aa_securityLabel: Incomplete
SecurityPolicyIdentifier: Incomplete
SecurityClassification: Incomplete
ESSPrivacyMark: Incomplete
SecurityCategories: Incomplete
ESSSecurityLabel: Incomplete
id_aa_communityIdentifiers: Incomplete
CommunityIdentifier: Incomplete
CommunityIdentifiers: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
Name = rfc5280.Name
Certificate = rfc5280.Certificate
GeneralNames = rfc5280.GeneralNames
GeneralName = rfc5280.GeneralName
SubjectInfoAccessSyntax = rfc5280.SubjectInfoAccessSyntax
id_pkix: Incomplete
id_pe: Incomplete
id_pe_subjectInfoAccess: Incomplete
CMSContentConstraints: Incomplete
BinaryTime: Incomplete
id_aa_binarySigningTime: Incomplete
BinarySigningTime: Incomplete
Attribute: Incomplete
CertificateSet: Incomplete
CertificateChoices: Incomplete
id_contentType: Incomplete
ContentType: Incomplete
id_messageDigest: Incomplete
MessageDigest: Incomplete
SIREntityName: Incomplete
id_aa_KP_keyPkgIdAndReceiptReq: Incomplete
KeyPkgIdentifierAndReceiptReq: Incomplete
id_aa_KP_keyProvinceV2: Incomplete

class KeyProvinceV2(univ.ObjectIdentifier): ...

aa_keyProvince_v2: Incomplete
id_aa_KP_manifest: Incomplete

class ShortTitle(char.PrintableString): ...
class Manifest(univ.SequenceOf): ...

aa_manifest: Incomplete
id_kma_keyAlgorithm: Incomplete

class KeyAlgorithm(univ.Sequence): ...

aa_keyAlgorithm: Incomplete
id_at_userCertificate: Incomplete
aa_userCertificate: Incomplete
id_kma_keyPkgReceiversV2: Incomplete

class KeyPkgReceiver(univ.Choice): ...
class KeyPkgReceiversV2(univ.SequenceOf): ...

aa_keyPackageReceivers_v2: Incomplete
id_kma_TSECNomenclature: Incomplete

class CharEdition(char.PrintableString): ...
class CharEditionRange(univ.Sequence): ...
class NumEdition(univ.Integer): ...
class NumEditionRange(univ.Sequence): ...
class EditionID(univ.Choice): ...
class Register(univ.Integer): ...
class RegisterRange(univ.Sequence): ...
class RegisterID(univ.Choice): ...
class SegmentNumber(univ.Integer): ...
class SegmentRange(univ.Sequence): ...
class SegmentID(univ.Choice): ...
class TSECNomenclature(univ.Sequence): ...

aa_tsecNomenclature: Incomplete
id_kma_keyPurpose: Incomplete

class KeyPurpose(univ.Enumerated): ...

aa_keyPurpose: Incomplete
id_kma_keyUse: Incomplete

class KeyUse(univ.Enumerated): ...

aa_keyUse: Incomplete
id_kma_transportKey: Incomplete

class TransOp(univ.Enumerated): ...

aa_transportKey: Incomplete
id_kma_keyDistPeriod: Incomplete

class KeyDistPeriod(univ.Sequence): ...

aa_keyDistributionPeriod: Incomplete
id_kma_keyValidityPeriod: Incomplete

class KeyValidityPeriod(univ.Sequence): ...

aa_keyValidityPeriod: Incomplete
id_kma_keyDuration: Incomplete
ub_KeyDuration_months: Incomplete
ub_KeyDuration_hours: Incomplete
ub_KeyDuration_days: Incomplete
ub_KeyDuration_weeks: Incomplete
ub_KeyDuration_years: Incomplete

class KeyDuration(univ.Choice): ...

aa_keyDurationPeriod: Incomplete
id_aa_KP_classification: Incomplete
id_enumeratedPermissiveAttributes: Incomplete
id_enumeratedRestrictiveAttributes: Incomplete
id_informativeAttributes: Incomplete

class SecurityAttribute(univ.Integer): ...
class EnumeratedTag(univ.Sequence): ...
class FreeFormField(univ.Choice): ...
class InformativeTag(univ.Sequence): ...
class Classification(ESSSecurityLabel): ...

aa_classification: Incomplete
id_kma_splitID: Incomplete

class SplitID(univ.Sequence): ...

aa_splitIdentifier: Incomplete
id_kma_keyPkgType: Incomplete

class KeyPkgType(univ.ObjectIdentifier): ...

aa_keyPackageType: Incomplete
id_kma_sigUsageV3: Incomplete

class SignatureUsage(CMSContentConstraints): ...

aa_signatureUsage_v3: Incomplete
id_kma_otherCertFormats: Incomplete
aa_otherCertificateFormats: Incomplete
id_at_pkiPath: Incomplete

class PkiPath(univ.SequenceOf): ...

aa_pkiPath: Incomplete
id_kma_usefulCerts: Incomplete
aa_usefulCertificates: Incomplete
id_kma_keyWrapAlgorithm: Incomplete
aa_keyWrapAlgorithm: Incomplete
id_aa_KP_contentDecryptKeyID: Incomplete

class ContentDecryptKeyID(univ.OctetString): ...

aa_contentDecryptKeyIdentifier: Incomplete
aa_certificatePointers: Incomplete
id_aa_KP_crlPointers: Incomplete
aa_cRLDistributionPoints: Incomplete
id_errorCodes: Incomplete
id_missingKeyType: Incomplete
id_privacyMarkTooLong: Incomplete
id_unrecognizedSecurityPolicy: Incomplete
