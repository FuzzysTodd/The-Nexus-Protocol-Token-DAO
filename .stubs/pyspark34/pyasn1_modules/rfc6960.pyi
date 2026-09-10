from _typeshed import Incomplete
from pyasn1.type import constraint as constraint, namedval as namedval, univ
from pyasn1_modules import rfc2560 as rfc2560, rfc5280 as rfc5280

MAX: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
AuthorityInfoAccessSyntax = rfc5280.AuthorityInfoAccessSyntax
Certificate = rfc5280.Certificate
CertificateSerialNumber = rfc5280.CertificateSerialNumber
CRLReason = rfc5280.CRLReason
Extensions = rfc5280.Extensions
GeneralName = rfc5280.GeneralName
Name = rfc5280.Name
id_kp: Incomplete
id_ad_ocsp: Incomplete
AcceptableResponses: Incomplete
ArchiveCutoff: Incomplete
CertStatus: Incomplete
KeyHash: Incomplete
OCSPResponse: Incomplete
OCSPResponseStatus: Incomplete
ResponseBytes: Incomplete
RevokedInfo: Incomplete
UnknownInfo: Incomplete
Version: Incomplete
id_kp_OCSPSigning: Incomplete
id_pkix_ocsp: Incomplete
id_pkix_ocsp_archive_cutoff: Incomplete
id_pkix_ocsp_basic: Incomplete
id_pkix_ocsp_crl: Incomplete
id_pkix_ocsp_nocheck: Incomplete
id_pkix_ocsp_nonce: Incomplete
id_pkix_ocsp_response: Incomplete
id_pkix_ocsp_service_locator: Incomplete
id_pkix_ocsp_pref_sig_algs: Incomplete
id_pkix_ocsp_extended_revoke: Incomplete

class CertID(univ.Sequence):
    componentType: Incomplete

class SingleResponse(univ.Sequence):
    componentType: Incomplete

class ResponderID(univ.Choice):
    componentType: Incomplete

class ResponseData(univ.Sequence):
    componentType: Incomplete

class BasicOCSPResponse(univ.Sequence):
    componentType: Incomplete

class Request(univ.Sequence):
    componentType: Incomplete

class Signature(univ.Sequence):
    componentType: Incomplete

class TBSRequest(univ.Sequence):
    componentType: Incomplete

class OCSPRequest(univ.Sequence):
    componentType: Incomplete

class ServiceLocator(univ.Sequence):
    componentType: Incomplete

class CrlID(univ.Sequence):
    componentType: Incomplete

class PreferredSignatureAlgorithm(univ.Sequence):
    componentType: Incomplete

class PreferredSignatureAlgorithms(univ.SequenceOf):
    componentType: Incomplete

ocspResponseMap: Incomplete
