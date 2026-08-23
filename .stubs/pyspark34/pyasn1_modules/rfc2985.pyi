from _typeshed import Incomplete
from pyasn1.type import char, namedval as namedval, tag as tag, univ
from pyasn1_modules import rfc5280 as rfc5280, rfc5652 as rfc5652, rfc5958 as rfc5958, rfc7292 as rfc7292

MAX: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
Attribute = rfc5280.Attribute
EmailAddress = rfc5280.EmailAddress
Extensions = rfc5280.Extensions
Time = rfc5280.Time
X520countryName = rfc5280.X520countryName
X520SerialNumber = rfc5280.X520SerialNumber
ContentInfo = rfc5652.ContentInfo
ContentType = rfc5652.ContentType
Countersignature = rfc5652.Countersignature
MessageDigest = rfc5652.MessageDigest
SignerInfo = rfc5652.SignerInfo
SigningTime = rfc5652.SigningTime
EncryptedPrivateKeyInfo = rfc5958.EncryptedPrivateKeyInfo
PFX = rfc7292.PFX

class AttributeType(univ.ObjectIdentifier): ...
class AttributeValue(univ.Any): ...
class AttributeValues(univ.SetOf): ...
class SingleAttributeValues(univ.SetOf): ...
class SingleAttribute(univ.Sequence): ...
CMSAttribute = rfc5652.Attribute

class CMSSingleAttribute(univ.Sequence): ...
class DirectoryString(univ.Choice): ...
class PKCS9String(univ.Choice): ...

pkcs_9_ub_pkcs9String: Incomplete
pkcs_9_ub_challengePassword: Incomplete
pkcs_9_ub_emailAddress: Incomplete
pkcs_9_ub_friendlyName: Incomplete
pkcs_9_ub_match: Incomplete
pkcs_9_ub_signingDescription: Incomplete
pkcs_9_ub_unstructuredAddress: Incomplete
pkcs_9_ub_unstructuredName: Incomplete
ub_name: Incomplete
pkcs_9_ub_placeOfBirth: Incomplete
pkcs_9_ub_pseudonym: Incomplete
ietf_at: Incomplete
id_at: Incomplete
pkcs_9: Incomplete
pkcs_9_mo: Incomplete
smime: Incomplete
certTypes: Incomplete
crlTypes: Incomplete
pkcs_9_oc: Incomplete
pkcs_9_at: Incomplete
pkcs_9_sx: Incomplete
pkcs_9_mr: Incomplete
pkcs_9_sx_pkcs9String: Incomplete
pkcs_9_sx_signingTime: Incomplete
pkcs_9_oc_pkcsEntity: Incomplete
pkcs_9_oc_naturalPerson: Incomplete
pkcs_9_mr_caseIgnoreMatch: Incomplete
pkcs_9_mr_signingTimeMatch: Incomplete
pkcs_9_at_pkcs7PDU: Incomplete
pKCS7PDU: Incomplete
pkcs_9_at_userPKCS12: Incomplete
userPKCS12: Incomplete
pkcs_9_at_pkcs15Token: Incomplete
pkcs_9_at_encryptedPrivateKeyInfo: Incomplete
encryptedPrivateKeyInfo: Incomplete
pkcs_9_at_emailAddress: Incomplete
emailAddress: Incomplete
pkcs_9_at_unstructuredName: Incomplete
unstructuredName: Incomplete
pkcs_9_at_unstructuredAddress: Incomplete
unstructuredAddress: Incomplete
pkcs_9_at_dateOfBirth: Incomplete
dateOfBirth: Incomplete
pkcs_9_at_placeOfBirth: Incomplete
placeOfBirth: Incomplete

class GenderString(char.PrintableString): ...

pkcs_9_at_gender: Incomplete
gender: Incomplete
pkcs_9_at_countryOfCitizenship: Incomplete
countryOfCitizenship: Incomplete
pkcs_9_at_countryOfResidence: Incomplete
countryOfResidence: Incomplete
id_at_pseudonym: Incomplete
pseudonym: Incomplete
id_at_serialNumber: Incomplete
serialNumber: Incomplete
pkcs_9_at_contentType: Incomplete
contentType: Incomplete
pkcs_9_at_messageDigest: Incomplete
messageDigest: Incomplete
pkcs_9_at_signingTime: Incomplete
signingTime: Incomplete

class RandomNonce(univ.OctetString): ...

pkcs_9_at_randomNonce: Incomplete
randomNonce: Incomplete

class SequenceNumber(univ.Integer): ...

pkcs_9_at_sequenceNumber: Incomplete
sequenceNumber: Incomplete
pkcs_9_at_counterSignature: Incomplete
counterSignature: Incomplete
pkcs_9_at_challengePassword: Incomplete
challengePassword: Incomplete

class ExtensionRequest(Extensions): ...

pkcs_9_at_extensionRequest: Incomplete
extensionRequest: Incomplete

class AttributeSet(univ.SetOf): ...

pkcs_9_at_extendedCertificateAttributes: Incomplete
extendedCertificateAttributes: Incomplete

class FriendlyName(char.BMPString): ...

pkcs_9_at_friendlyName: Incomplete
friendlyName: Incomplete
pkcs_9_at_localKeyId: Incomplete
localKeyId: Incomplete
pkcs_9_at_signingDescription: Incomplete
signingDescription: Incomplete

class SMIMECapability(AlgorithmIdentifier): ...
class SMIMECapabilities(univ.SequenceOf): ...

pkcs_9_at_smimeCapabilities: Incomplete
smimeCapabilities: Incomplete
