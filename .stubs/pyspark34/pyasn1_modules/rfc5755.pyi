from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280, rfc5652 as rfc5652

MAX: Incomplete
securityCategoryMap: Incomplete
ContentInfo: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
Attribute = rfc5280.Attribute
AuthorityInfoAccessSyntax = rfc5280.AuthorityInfoAccessSyntax
AuthorityKeyIdentifier = rfc5280.AuthorityKeyIdentifier
CertificateSerialNumber = rfc5280.CertificateSerialNumber
CRLDistributionPoints = rfc5280.CRLDistributionPoints
Extensions = rfc5280.Extensions
Extension = rfc5280.Extension
GeneralNames = rfc5280.GeneralNames
GeneralName = rfc5280.GeneralName
UniqueIdentifier = rfc5280.UniqueIdentifier
id_pkix: Incomplete
id_pe: Incomplete
id_kp: Incomplete
id_aca: Incomplete
id_ad: Incomplete
id_at: Incomplete
id_ce: Incomplete

class AttCertVersion(univ.Integer):
    namedValues: Incomplete

class IssuerSerial(univ.Sequence):
    componentType: Incomplete

class ObjectDigestInfo(univ.Sequence):
    componentType: Incomplete

class Holder(univ.Sequence):
    componentType: Incomplete

class V2Form(univ.Sequence):
    componentType: Incomplete

class AttCertIssuer(univ.Choice):
    componentType: Incomplete

class AttCertValidityPeriod(univ.Sequence):
    componentType: Incomplete

class AttributeCertificateInfo(univ.Sequence):
    componentType: Incomplete

class AttributeCertificate(univ.Sequence):
    componentType: Incomplete

id_pe_ac_auditIdentity: Incomplete
id_ce_noRevAvail: Incomplete
id_ce_targetInformation: Incomplete

class TargetCert(univ.Sequence):
    componentType: Incomplete

class Target(univ.Choice):
    componentType: Incomplete

class Targets(univ.SequenceOf):
    componentType: Incomplete

id_pe_ac_proxying: Incomplete

class ProxyInfo(univ.SequenceOf):
    componentType: Incomplete

id_pe_aaControls: Incomplete

class AttrSpec(univ.SequenceOf):
    componentType: Incomplete

class AAControls(univ.Sequence):
    componentType: Incomplete

id_aca_authenticationInfo: Incomplete
id_aca_accessIdentity: Incomplete

class SvceAuthInfo(univ.Sequence):
    componentType: Incomplete

id_aca_chargingIdentity: Incomplete
id_aca_group: Incomplete

class IetfAttrSyntax(univ.Sequence):
    componentType: Incomplete

id_at_role: Incomplete

class RoleSyntax(univ.Sequence):
    componentType: Incomplete

class ClassList(univ.BitString):
    namedValues: Incomplete

class SecurityCategory(univ.Sequence):
    componentType: Incomplete

id_at_clearance: Incomplete

class Clearance(univ.Sequence):
    componentType: Incomplete

id_at_clearance_rfc3281: Incomplete

class Clearance_rfc3281(univ.Sequence):
    componentType: Incomplete

id_aca_encAttrs: Incomplete

class ACClearAttrs(univ.Sequence):
    componentType: Incomplete
