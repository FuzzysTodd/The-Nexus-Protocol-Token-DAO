from _typeshed import Incomplete
from pyasn1.type import univ, useful
from pyasn1_modules import rfc2459 as rfc2459

class CRLReason(univ.Enumerated):
    namedValues: Incomplete

class GeneralName(univ.OctetString): ...

id_kp_OCSPSigning: Incomplete
id_pkix_ocsp: Incomplete
id_pkix_ocsp_basic: Incomplete
id_pkix_ocsp_nonce: Incomplete
id_pkix_ocsp_crl: Incomplete
id_pkix_ocsp_response: Incomplete
id_pkix_ocsp_nocheck: Incomplete
id_pkix_ocsp_archive_cutoff: Incomplete
id_pkix_ocsp_service_locator: Incomplete

class AcceptableResponses(univ.SequenceOf):
    componentType: Incomplete

class ArchiveCutoff(useful.GeneralizedTime): ...
class UnknownInfo(univ.Null): ...

class RevokedInfo(univ.Sequence):
    componentType: Incomplete

class CertID(univ.Sequence):
    componentType: Incomplete

class CertStatus(univ.Choice):
    componentType: Incomplete

class SingleResponse(univ.Sequence):
    componentType: Incomplete

class KeyHash(univ.OctetString): ...

class ResponderID(univ.Choice):
    componentType: Incomplete

class Version(univ.Integer):
    namedValues: Incomplete

class ResponseData(univ.Sequence):
    componentType: Incomplete

class BasicOCSPResponse(univ.Sequence):
    componentType: Incomplete

class ResponseBytes(univ.Sequence):
    componentType: Incomplete

class OCSPResponseStatus(univ.Enumerated):
    namedValues: Incomplete

class OCSPResponse(univ.Sequence):
    componentType: Incomplete

class Request(univ.Sequence):
    componentType: Incomplete

class Signature(univ.Sequence):
    componentType: Incomplete

class TBSRequest(univ.Sequence):
    componentType: Incomplete

class OCSPRequest(univ.Sequence):
    componentType: Incomplete
