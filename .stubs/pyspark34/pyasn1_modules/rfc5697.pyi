from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc4055 as rfc4055, rfc5280 as rfc5280

AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
CertificateSerialNumber = rfc5280.CertificateSerialNumber
GeneralNames = rfc5280.GeneralNames
id_sha1: Incomplete

class SCVPIssuerSerial(univ.Sequence):
    componentType: Incomplete

sha1_alg_id: Incomplete

class SCVPCertID(univ.Sequence):
    componentType: Incomplete

id_pe_otherCerts: Incomplete

class OtherCertificates(univ.SequenceOf):
    componentType: Incomplete
