from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc3565 as rfc3565, rfc5280 as rfc5280, rfc5652 as rfc5652, rfc5751 as rfc5751, rfc5755 as rfc5755

MAX: Incomplete
glaQueryRRMap: Incomplete
id_aes128_wrap: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
Certificate = rfc5280.Certificate
GeneralName = rfc5280.GeneralName
CertificateSet = rfc5652.CertificateSet
KEKIdentifier = rfc5652.KEKIdentifier
RecipientInfos = rfc5652.RecipientInfos
SMIMECapability = rfc5751.SMIMECapability
AttributeCertificate = rfc5755.AttributeCertificate
id_skd: Incomplete
id_skd_glUseKEK: Incomplete

class Certificates(univ.Sequence):
    componentType: Incomplete

class GLInfo(univ.Sequence):
    componentType: Incomplete

class GLOwnerInfo(univ.Sequence):
    componentType: Incomplete

class GLAdministration(univ.Integer):
    namedValues: Incomplete

requested_algorithm: Incomplete

class GLKeyAttributes(univ.Sequence):
    componentType: Incomplete

class GLUseKEK(univ.Sequence):
    componentType: Incomplete

id_skd_glDelete: Incomplete

class DeleteGL(GeneralName): ...

id_skd_glAddMember: Incomplete

class GLMember(univ.Sequence):
    componentType: Incomplete

class GLAddMember(univ.Sequence):
    componentType: Incomplete

id_skd_glDeleteMember: Incomplete

class GLDeleteMember(univ.Sequence):
    componentType: Incomplete

id_skd_glRekey: Incomplete

class GLNewKeyAttributes(univ.Sequence):
    componentType: Incomplete

class GLRekey(univ.Sequence):
    componentType: Incomplete

id_skd_glAddOwner: Incomplete
id_skd_glRemoveOwner: Incomplete

class GLOwnerAdministration(univ.Sequence):
    componentType: Incomplete

id_skd_glKeyCompromise: Incomplete

class GLKCompromise(GeneralName): ...

id_skd_glkRefresh: Incomplete

class Date(univ.Sequence):
    componentType: Incomplete

class GLKRefresh(univ.Sequence):
    componentType: Incomplete

id_skd_glaQueryRequest: Incomplete

class GLAQueryRequest(univ.Sequence):
    componentType: Incomplete

id_skd_glaQueryResponse: Incomplete

class GLAQueryResponse(univ.Sequence):
    componentType: Incomplete

id_cmc_glaRR: Incomplete
id_cmc_gla_skdAlgRequest: Incomplete

class SKDAlgRequest(univ.Null): ...

id_cmc_gla_skdAlgResponse: Incomplete
SMIMECapabilities = rfc5751.SMIMECapabilities
id_skd_glProvideCert: Incomplete
id_skd_glManageCert: Incomplete

class GLManageCert(univ.Sequence):
    componentType: Incomplete

id_skd_glKey: Incomplete

class GLKey(univ.Sequence):
    componentType: Incomplete

id_cet_skdFailInfo: Incomplete

class SKDFailInfo(univ.Integer):
    namedValues: Incomplete
