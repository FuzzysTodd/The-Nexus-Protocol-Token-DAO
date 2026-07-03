from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
Attribute = rfc5280.Attribute
AttributeType = rfc5280.AttributeType
AttributeTypeAndValue = rfc5280.AttributeTypeAndValue
AttributeValue = rfc5280.AttributeValue
Certificate = rfc5280.Certificate
CertificateList = rfc5280.CertificateList
DirectoryString = rfc5280.DirectoryString
GeneralName = rfc5280.GeneralName
GeneralNames = rfc5280.GeneralNames
Name = rfc5280.Name
PolicyInformation = rfc5280.PolicyInformation

class CertPolicyId(univ.ObjectIdentifier): ...

class AcceptablePolicySet(univ.SequenceOf):
    componentType: Incomplete

class SignPolExtn(univ.Sequence):
    componentType: Incomplete

class SignPolExtensions(univ.SequenceOf):
    componentType: Incomplete

class AlgAndLength(univ.Sequence):
    componentType: Incomplete

class AlgorithmConstraints(univ.SequenceOf):
    componentType: Incomplete

class AlgorithmConstraintSet(univ.Sequence):
    componentType: Incomplete

class AttributeValueConstraints(univ.SequenceOf):
    componentType: Incomplete

class AttributeTypeConstraints(univ.SequenceOf):
    componentType: Incomplete

class AttributeConstraints(univ.Sequence):
    componentType: Incomplete

class HowCertAttribute(univ.Enumerated):
    namedValues: Incomplete

class SkipCerts(univ.Integer):
    subtypeSpec: Incomplete

class PolicyConstraints(univ.Sequence):
    componentType: Incomplete

class BaseDistance(univ.Integer):
    subtypeSpec: Incomplete

class GeneralSubtree(univ.Sequence):
    componentType: Incomplete

class GeneralSubtrees(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete

class NameConstraints(univ.Sequence):
    componentType: Incomplete

class PathLenConstraint(univ.Integer):
    subtypeSpec: Incomplete

class CertificateTrustPoint(univ.Sequence):
    componentType: Incomplete

class CertificateTrustTrees(univ.SequenceOf):
    componentType: Incomplete

class EnuRevReq(univ.Enumerated):
    namedValues: Incomplete

class RevReq(univ.Sequence):
    componentType: Incomplete

class CertRevReq(univ.Sequence):
    componentType: Incomplete

class AttributeTrustCondition(univ.Sequence):
    componentType: Incomplete

class CMSAttrs(univ.SequenceOf):
    componentType: Incomplete

class CertInfoReq(univ.Enumerated):
    namedValues: Incomplete

class CertRefReq(univ.Enumerated):
    namedValues: Incomplete

class DeltaTime(univ.Sequence):
    componentType: Incomplete

class TimestampTrustCondition(univ.Sequence):
    componentType: Incomplete

class SignerRules(univ.Sequence):
    componentType: Incomplete

class MandatedUnsignedAttr(CMSAttrs): ...

class VerifierRules(univ.Sequence):
    componentType: Incomplete

class SignerAndVerifierRules(univ.Sequence):
    componentType: Incomplete

class SigningCertTrustCondition(univ.Sequence):
    componentType: Incomplete

class CommitmentTypeIdentifier(univ.ObjectIdentifier): ...
class FieldOfApplication(DirectoryString): ...

class CommitmentType(univ.Sequence):
    componentType: Incomplete

class SelectedCommitmentTypes(univ.SequenceOf):
    componentType: Incomplete

class CommitmentRule(univ.Sequence):
    componentType: Incomplete

class CommitmentRules(univ.SequenceOf):
    componentType: Incomplete

class CommonRules(univ.Sequence):
    componentType: Incomplete

class PolicyIssuerName(GeneralNames): ...
class SignPolicyHash(univ.OctetString): ...
class SignPolicyId(univ.ObjectIdentifier): ...

class SigningPeriod(univ.Sequence):
    componentType: Incomplete

class SignatureValidationPolicy(univ.Sequence):
    componentType: Incomplete

class SignPolicyInfo(univ.Sequence):
    componentType: Incomplete

class SignaturePolicy(univ.Sequence):
    componentType: Incomplete
