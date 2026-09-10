from _typeshed import Incomplete
from pyasn1.type import char as char, univ as univ, useful

MAX: Incomplete
ub_name: Incomplete
ub_common_name: Incomplete
ub_locality_name: Incomplete
ub_state_name: Incomplete
ub_organization_name: Incomplete
ub_organizational_unit_name: Incomplete
ub_title: Incomplete
ub_match: Incomplete
ub_emailaddress_length: Incomplete
ub_common_name_length: Incomplete
ub_country_name_alpha_length: Incomplete
ub_country_name_numeric_length: Incomplete
ub_domain_defined_attributes: Incomplete
ub_domain_defined_attribute_type_length: Incomplete
ub_domain_defined_attribute_value_length: Incomplete
ub_domain_name_length: Incomplete
ub_extension_attributes: Incomplete
ub_e163_4_number_length: Incomplete
ub_e163_4_sub_address_length: Incomplete
ub_generation_qualifier_length: Incomplete
ub_given_name_length: Incomplete
ub_initials_length: Incomplete
ub_integer_options: Incomplete
ub_numeric_user_id_length: Incomplete
ub_organization_name_length: Incomplete
ub_organizational_unit_name_length: Incomplete
ub_organizational_units: Incomplete
ub_pds_name_length: Incomplete
ub_pds_parameter_length: Incomplete
ub_pds_physical_address_lines: Incomplete
ub_postal_code_length: Incomplete
ub_surname_length: Incomplete
ub_terminal_id_length: Incomplete
ub_unformatted_address_length: Incomplete
ub_x121_address_length: Incomplete

class UniversalString(char.UniversalString): ...
class BMPString(char.BMPString): ...
class UTF8String(char.UTF8String): ...

id_pkix: Incomplete
id_pe: Incomplete
id_qt: Incomplete
id_kp: Incomplete
id_ad: Incomplete
id_qt_cps: Incomplete
id_qt_unotice: Incomplete
id_ad_ocsp: Incomplete
id_ad_caIssuers: Incomplete
id_at: Incomplete
id_at_name: Incomplete
id_at_sutname: Incomplete
id_at_surname: Incomplete
id_at_givenName: Incomplete
id_at_initials: Incomplete
id_at_generationQualifier: Incomplete

class X520name(univ.Choice):
    componentType: Incomplete

id_at_commonName: Incomplete

class X520CommonName(univ.Choice):
    componentType: Incomplete

id_at_localityName: Incomplete

class X520LocalityName(univ.Choice):
    componentType: Incomplete

id_at_stateOrProvinceName: Incomplete

class X520StateOrProvinceName(univ.Choice):
    componentType: Incomplete

id_at_organizationName: Incomplete

class X520OrganizationName(univ.Choice):
    componentType: Incomplete

id_at_organizationalUnitName: Incomplete

class X520OrganizationalUnitName(univ.Choice):
    componentType: Incomplete

id_at_title: Incomplete

class X520Title(univ.Choice):
    componentType: Incomplete

id_at_dnQualifier: Incomplete

class X520dnQualifier(char.PrintableString): ...

id_at_countryName: Incomplete

class X520countryName(char.PrintableString):
    subtypeSpec: Incomplete

pkcs_9: Incomplete
emailAddress: Incomplete

class Pkcs9email(char.IA5String):
    subtypeSpec: Incomplete

class DSAPrivateKey(univ.Sequence):
    """PKIX compliant DSA private key structure"""
    componentType: Incomplete

class DirectoryString(univ.Choice):
    componentType: Incomplete

class AlgorithmIdentifier(univ.Sequence):
    componentType: Incomplete

pkcs_1: Incomplete
rsaEncryption: Incomplete
md2WithRSAEncryption: Incomplete
md5WithRSAEncryption: Incomplete
sha1WithRSAEncryption: Incomplete
id_dsa_with_sha1: Incomplete

class Dss_Sig_Value(univ.Sequence):
    componentType: Incomplete

dhpublicnumber: Incomplete

class ValidationParms(univ.Sequence):
    componentType: Incomplete

class DomainParameters(univ.Sequence):
    componentType: Incomplete

id_dsa: Incomplete

class Dss_Parms(univ.Sequence):
    componentType: Incomplete

teletex_domain_defined_attributes: Incomplete

class TeletexDomainDefinedAttribute(univ.Sequence):
    componentType: Incomplete

class TeletexDomainDefinedAttributes(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

terminal_type: Incomplete

class TerminalType(univ.Integer):
    subtypeSpec: Incomplete
    namedValues: Incomplete

class PresentationAddress(univ.Sequence):
    componentType: Incomplete

extended_network_address: Incomplete

class E163_4_address(univ.Sequence):
    componentType: Incomplete

class ExtendedNetworkAddress(univ.Choice):
    componentType: Incomplete

class PDSParameter(univ.Set):
    componentType: Incomplete

local_postal_attributes: Incomplete

class LocalPostalAttributes(PDSParameter): ...
class UniquePostalName(PDSParameter): ...

unique_postal_name: Incomplete
poste_restante_address: Incomplete

class PosteRestanteAddress(PDSParameter): ...

post_office_box_address: Incomplete

class PostOfficeBoxAddress(PDSParameter): ...

street_address: Incomplete

class StreetAddress(PDSParameter): ...

class UnformattedPostalAddress(univ.Set):
    componentType: Incomplete

physical_delivery_office_name: Incomplete

class PhysicalDeliveryOfficeName(PDSParameter): ...

physical_delivery_office_number: Incomplete

class PhysicalDeliveryOfficeNumber(PDSParameter): ...

extension_OR_address_components: Incomplete

class ExtensionORAddressComponents(PDSParameter): ...

physical_delivery_personal_name: Incomplete

class PhysicalDeliveryPersonalName(PDSParameter): ...

physical_delivery_organization_name: Incomplete

class PhysicalDeliveryOrganizationName(PDSParameter): ...

extension_physical_delivery_address_components: Incomplete

class ExtensionPhysicalDeliveryAddressComponents(PDSParameter): ...

unformatted_postal_address: Incomplete
postal_code: Incomplete

class PostalCode(univ.Choice):
    componentType: Incomplete

class PhysicalDeliveryCountryName(univ.Choice):
    componentType: Incomplete

class PDSName(char.PrintableString):
    subtypeSpec: Incomplete

physical_delivery_country_name: Incomplete

class TeletexOrganizationalUnitName(char.TeletexString):
    subtypeSpec: Incomplete

pds_name: Incomplete
teletex_organizational_unit_names: Incomplete

class TeletexOrganizationalUnitNames(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

teletex_personal_name: Incomplete

class TeletexPersonalName(univ.Set):
    componentType: Incomplete

teletex_organization_name: Incomplete

class TeletexOrganizationName(char.TeletexString):
    subtypeSpec: Incomplete

teletex_common_name: Incomplete

class TeletexCommonName(char.TeletexString):
    subtypeSpec: Incomplete

class CommonName(char.PrintableString):
    subtypeSpec: Incomplete

common_name: Incomplete

class ExtensionAttribute(univ.Sequence):
    componentType: Incomplete

class ExtensionAttributes(univ.SetOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class BuiltInDomainDefinedAttribute(univ.Sequence):
    componentType: Incomplete

class BuiltInDomainDefinedAttributes(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class OrganizationalUnitName(char.PrintableString):
    subtypeSpec: Incomplete

class OrganizationalUnitNames(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class PersonalName(univ.Set):
    componentType: Incomplete

class NumericUserIdentifier(char.NumericString):
    subtypeSpec: Incomplete

class OrganizationName(char.PrintableString):
    subtypeSpec: Incomplete

class PrivateDomainName(univ.Choice):
    componentType: Incomplete

class TerminalIdentifier(char.PrintableString):
    subtypeSpec: Incomplete

class X121Address(char.NumericString):
    subtypeSpec: Incomplete

class NetworkAddress(X121Address): ...

class AdministrationDomainName(univ.Choice):
    tagSet: Incomplete
    componentType: Incomplete

class CountryName(univ.Choice):
    tagSet: Incomplete
    componentType: Incomplete

class BuiltInStandardAttributes(univ.Sequence):
    componentType: Incomplete

class ORAddress(univ.Sequence):
    componentType: Incomplete

id_ce_invalidityDate: Incomplete

class InvalidityDate(useful.GeneralizedTime): ...

id_holdinstruction_none: Incomplete
id_holdinstruction_callissuer: Incomplete
id_holdinstruction_reject: Incomplete
holdInstruction: Incomplete
id_ce_holdInstructionCode: Incomplete

class HoldInstructionCode(univ.ObjectIdentifier): ...

id_ce_cRLReasons: Incomplete

class CRLReason(univ.Enumerated):
    namedValues: Incomplete

id_ce_cRLNumber: Incomplete

class CRLNumber(univ.Integer):
    subtypeSpec: Incomplete

class BaseCRLNumber(CRLNumber): ...

id_kp_serverAuth: Incomplete
id_kp_clientAuth: Incomplete
id_kp_codeSigning: Incomplete
id_kp_emailProtection: Incomplete
id_kp_ipsecEndSystem: Incomplete
id_kp_ipsecTunnel: Incomplete
id_kp_ipsecUser: Incomplete
id_kp_timeStamping: Incomplete
id_pe_authorityInfoAccess: Incomplete
id_ce_extKeyUsage: Incomplete

class KeyPurposeId(univ.ObjectIdentifier): ...

class ExtKeyUsageSyntax(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class ReasonFlags(univ.BitString):
    namedValues: Incomplete

class SkipCerts(univ.Integer):
    subtypeSpec: Incomplete

id_ce_policyConstraints: Incomplete

class PolicyConstraints(univ.Sequence):
    componentType: Incomplete

id_ce_basicConstraints: Incomplete

class BasicConstraints(univ.Sequence):
    componentType: Incomplete

id_ce_subjectDirectoryAttributes: Incomplete

class EDIPartyName(univ.Sequence):
    componentType: Incomplete

id_ce_deltaCRLIndicator: Incomplete

class BaseDistance(univ.Integer):
    subtypeSpec: Incomplete

id_ce_cRLDistributionPoints: Incomplete
id_ce_issuingDistributionPoint: Incomplete
id_ce_nameConstraints: Incomplete

class DisplayText(univ.Choice):
    componentType: Incomplete

class NoticeReference(univ.Sequence):
    componentType: Incomplete

class UserNotice(univ.Sequence):
    componentType: Incomplete

class CPSuri(char.IA5String): ...

class PolicyQualifierId(univ.ObjectIdentifier):
    subtypeSpec: Incomplete

class CertPolicyId(univ.ObjectIdentifier): ...

class PolicyQualifierInfo(univ.Sequence):
    componentType: Incomplete

id_ce_certificatePolicies: Incomplete

class PolicyInformation(univ.Sequence):
    componentType: Incomplete

class CertificatePolicies(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

id_ce_policyMappings: Incomplete

class PolicyMapping(univ.Sequence):
    componentType: Incomplete

class PolicyMappings(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

id_ce_privateKeyUsagePeriod: Incomplete

class PrivateKeyUsagePeriod(univ.Sequence):
    componentType: Incomplete

id_ce_keyUsage: Incomplete

class KeyUsage(univ.BitString):
    namedValues: Incomplete

id_ce: Incomplete
id_ce_authorityKeyIdentifier: Incomplete

class KeyIdentifier(univ.OctetString): ...

id_ce_subjectKeyIdentifier: Incomplete

class SubjectKeyIdentifier(KeyIdentifier): ...

id_ce_certificateIssuer: Incomplete
id_ce_subjectAltName: Incomplete
id_ce_issuerAltName: Incomplete

class AttributeValue(univ.Any): ...
class AttributeType(univ.ObjectIdentifier): ...

certificateAttributesMap: Incomplete

class AttributeTypeAndValue(univ.Sequence):
    componentType: Incomplete

class Attribute(univ.Sequence):
    componentType: Incomplete

class SubjectDirectoryAttributes(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class RelativeDistinguishedName(univ.SetOf):
    componentType: Incomplete

class RDNSequence(univ.SequenceOf):
    componentType: Incomplete

class Name(univ.Choice):
    componentType: Incomplete

class CertificateSerialNumber(univ.Integer): ...

class AnotherName(univ.Sequence):
    componentType: Incomplete

class GeneralName(univ.Choice):
    componentType: Incomplete

class GeneralNames(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class AccessDescription(univ.Sequence):
    componentType: Incomplete

class AuthorityInfoAccessSyntax(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class AuthorityKeyIdentifier(univ.Sequence):
    componentType: Incomplete

class DistributionPointName(univ.Choice):
    componentType: Incomplete

class DistributionPoint(univ.Sequence):
    componentType: Incomplete

class CRLDistPointsSyntax(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class IssuingDistributionPoint(univ.Sequence):
    componentType: Incomplete

class GeneralSubtree(univ.Sequence):
    componentType: Incomplete

class GeneralSubtrees(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class NameConstraints(univ.Sequence):
    componentType: Incomplete

class CertificateIssuer(GeneralNames): ...
class SubjectAltName(GeneralNames): ...
class IssuerAltName(GeneralNames): ...

certificateExtensionsMap: Incomplete

class Extension(univ.Sequence):
    componentType: Incomplete

class Extensions(univ.SequenceOf):
    componentType: Incomplete
    sizeSpec: Incomplete

class SubjectPublicKeyInfo(univ.Sequence):
    componentType: Incomplete

class UniqueIdentifier(univ.BitString): ...

class Time(univ.Choice):
    componentType: Incomplete

class Validity(univ.Sequence):
    componentType: Incomplete

class Version(univ.Integer):
    namedValues: Incomplete

class TBSCertificate(univ.Sequence):
    componentType: Incomplete

class Certificate(univ.Sequence):
    componentType: Incomplete

class RevokedCertificate(univ.Sequence):
    componentType: Incomplete

class TBSCertList(univ.Sequence):
    componentType: Incomplete

class CertificateList(univ.Sequence):
    componentType: Incomplete
