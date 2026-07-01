from _typeshed import Incomplete
from pyasn1.type import char, univ
from pyasn1_modules import rfc3161 as rfc3161, rfc5035 as rfc5035, rfc5280 as rfc5280, rfc5652 as rfc5652, rfc5755 as rfc5755, rfc6960 as rfc6960

MAX: Incomplete
commitmentQualifierMap: Incomplete
sigQualifiersMap: Incomplete
otherRevRefMap: Incomplete
otherRevValMap: Incomplete
ContentInfo = rfc5652.ContentInfo
ContentType = rfc5652.ContentType
SignedData = rfc5652.SignedData
EncapsulatedContentInfo = rfc5652.EncapsulatedContentInfo
SignerInfo = rfc5652.SignerInfo
MessageDigest = rfc5652.MessageDigest
SigningTime = rfc5652.SigningTime
Countersignature = rfc5652.Countersignature
id_data: Incomplete
id_signedData: Incomplete
id_contentType: Incomplete
id_messageDigest: Incomplete
id_signingTime: Incomplete
id_countersignature: Incomplete
SigningCertificate: Incomplete
IssuerSerial: Incomplete
ContentReference: Incomplete
ContentIdentifier: Incomplete
id_aa_contentReference: Incomplete
id_aa_contentIdentifier: Incomplete
id_aa_signingCertificate: Incomplete
id_aa_signingCertificateV2: Incomplete
Certificate = rfc5280.Certificate
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
CertificateList = rfc5280.CertificateList
Name = rfc5280.Name
Attribute = rfc5280.Attribute
GeneralNames = rfc5280.GeneralNames
GeneralName = rfc5280.GeneralName
PolicyInformation = rfc5280.PolicyInformation
DirectoryString = rfc5280.DirectoryString
AttributeCertificate = rfc5755.AttributeCertificate
BasicOCSPResponse = rfc6960.BasicOCSPResponse
ResponderID = rfc6960.ResponderID
TimeStampToken: Incomplete
id_etsi_es_IDUP_Mechanism_v1: Incomplete
id_aa_ets_otherSigCert: Incomplete

class OtherHashValue(univ.OctetString): ...

class OtherHashAlgAndValue(univ.Sequence):
    componentType: Incomplete

class OtherHash(univ.Choice):
    componentType: Incomplete

class OtherCertID(univ.Sequence):
    componentType: Incomplete

class OtherSigningCertificate(univ.Sequence):
    componentType: Incomplete

id_aa_ets_sigPolicyId: Incomplete

class SigPolicyId(univ.ObjectIdentifier): ...
class SigPolicyHash(OtherHashAlgAndValue): ...
class SigPolicyQualifierId(univ.ObjectIdentifier): ...

class SigPolicyQualifierInfo(univ.Sequence):
    componentType: Incomplete

class SignaturePolicyId(univ.Sequence):
    componentType: Incomplete

class SignaturePolicyImplied(univ.Null): ...

class SignaturePolicy(univ.Choice):
    componentType: Incomplete

id_spq_ets_unotice: Incomplete

class DisplayText(univ.Choice):
    componentType: Incomplete

class NoticeReference(univ.Sequence):
    componentType: Incomplete

class SPUserNotice(univ.Sequence):
    componentType: Incomplete

noticeToUser: Incomplete
id_spq_ets_uri: Incomplete

class SPuri(char.IA5String): ...

pointerToSigPolSpec: Incomplete
id_aa_ets_commitmentType: Incomplete

class CommitmentTypeIdentifier(univ.ObjectIdentifier): ...

class CommitmentTypeQualifier(univ.Sequence):
    componentType: Incomplete

class CommitmentTypeIndication(univ.Sequence):
    componentType: Incomplete

id_cti_ets_proofOfOrigin: Incomplete
id_cti_ets_proofOfReceipt: Incomplete
id_cti_ets_proofOfDelivery: Incomplete
id_cti_ets_proofOfSender: Incomplete
id_cti_ets_proofOfApproval: Incomplete
id_cti_ets_proofOfCreation: Incomplete
id_aa_ets_signerLocation: Incomplete

class PostalAddress(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete

class SignerLocation(univ.Sequence):
    componentType: Incomplete

id_aa_signatureTimeStampToken: Incomplete

class SignatureTimeStampToken(TimeStampToken): ...

id_aa_ets_contentTimestamp: Incomplete

class ContentTimestamp(TimeStampToken): ...

id_aa_ets_signerAttr: Incomplete

class ClaimedAttributes(univ.SequenceOf):
    componentType: Incomplete

class CertifiedAttributes(AttributeCertificate): ...

class SignerAttribute(univ.SequenceOf):
    componentType: Incomplete

id_aa_ets_certificateRefs: Incomplete

class CompleteCertificateRefs(univ.SequenceOf):
    componentType: Incomplete

id_aa_ets_revocationRefs: Incomplete

class CrlIdentifier(univ.Sequence):
    componentType: Incomplete

class CrlValidatedID(univ.Sequence):
    componentType: Incomplete

class CRLListID(univ.Sequence):
    componentType: Incomplete

class OcspIdentifier(univ.Sequence):
    componentType: Incomplete

class OcspResponsesID(univ.Sequence):
    componentType: Incomplete

class OcspListID(univ.Sequence):
    componentType: Incomplete

class OtherRevRefType(univ.ObjectIdentifier): ...

class OtherRevRefs(univ.Sequence):
    componentType: Incomplete

class CrlOcspRef(univ.Sequence):
    componentType: Incomplete

class CompleteRevocationRefs(univ.SequenceOf):
    componentType: Incomplete

id_aa_ets_certValues: Incomplete

class CertificateValues(univ.SequenceOf):
    componentType: Incomplete

id_aa_ets_revocationValues: Incomplete

class OtherRevValType(univ.ObjectIdentifier): ...

class OtherRevVals(univ.Sequence):
    componentType: Incomplete

class RevocationValues(univ.Sequence):
    componentType: Incomplete

id_aa_ets_escTimeStamp: Incomplete

class ESCTimeStampToken(TimeStampToken): ...

id_aa_ets_certCRLTimestamp: Incomplete

class TimestampedCertsCRLs(TimeStampToken): ...

id_aa_ets_archiveTimestampV2: Incomplete

class ArchiveTimeStampToken(TimeStampToken): ...

id_aa_ets_attrCertificateRefs: Incomplete

class AttributeCertificateRefs(univ.SequenceOf):
    componentType: Incomplete

id_aa_ets_attrRevocationRefs: Incomplete

class AttributeRevocationRefs(univ.SequenceOf):
    componentType: Incomplete
