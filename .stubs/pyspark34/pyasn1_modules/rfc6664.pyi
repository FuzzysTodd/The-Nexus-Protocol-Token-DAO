from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc3279 as rfc3279, rfc4055 as rfc4055, rfc5280 as rfc5280, rfc5480 as rfc5480, rfc5751 as rfc5751

MAX: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
dhpublicnumber: Incomplete
Dss_Parms: Incomplete
id_dsa: Incomplete
id_ecPublicKey: Incomplete
rsaEncryption: Incomplete
id_mgf1: Incomplete
id_RSAES_OAEP: Incomplete
id_RSASSA_PSS: Incomplete
ECParameters: Incomplete
id_ecDH: Incomplete
id_ecMQV: Incomplete

class RSAKeySize(univ.Integer): ...

class RSAKeyCapabilities(univ.Sequence):
    componentType: Incomplete

class RsaSsa_Pss_sig_caps(univ.Sequence):
    componentType: Incomplete

class DSAKeySize(univ.Integer):
    subtypeSpec: Incomplete

class DSAKeyCapabilities(univ.Choice):
    componentType: Incomplete

class EC_SMimeCaps(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete
