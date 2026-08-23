from _typeshed import Incomplete
from pyasn1.type import char as char, constraint as constraint, namedval as namedval, univ, useful as useful
from pyasn1_modules import rfc5280 as rfc5280, rfc5480 as rfc5480, rfc5652 as rfc5652, rfc5751 as rfc5751, rfc8018 as rfc8018

AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
OriginatorPublicKey: Incomplete
UserKeyingMaterial: Incomplete
ECDSA_Sig_Value: Incomplete
ECParameters: Incomplete
ECPoint: Incomplete
id_ecPublicKey: Incomplete
id_hmacWithSHA224: Incomplete
id_hmacWithSHA256: Incomplete
id_hmacWithSHA384: Incomplete
id_hmacWithSHA512: Incomplete
x9_63_scheme: Incomplete
secg_scheme: Incomplete
dhSinglePass_cofactorDH_sha1kdf_scheme: Incomplete
dhSinglePass_cofactorDH_sha224kdf_scheme: Incomplete
dhSinglePass_cofactorDH_sha256kdf_scheme: Incomplete
dhSinglePass_cofactorDH_sha384kdf_scheme: Incomplete
dhSinglePass_cofactorDH_sha512kdf_scheme: Incomplete
dhSinglePass_stdDH_sha1kdf_scheme: Incomplete
dhSinglePass_stdDH_sha224kdf_scheme: Incomplete
dhSinglePass_stdDH_sha256kdf_scheme: Incomplete
dhSinglePass_stdDH_sha384kdf_scheme: Incomplete
dhSinglePass_stdDH_sha512kdf_scheme: Incomplete
mqvSinglePass_sha1kdf_scheme: Incomplete
mqvSinglePass_sha224kdf_scheme: Incomplete
mqvSinglePass_sha256kdf_scheme: Incomplete
mqvSinglePass_sha384kdf_scheme: Incomplete
mqvSinglePass_sha512kdf_scheme: Incomplete

class IV(univ.OctetString): ...
class CBCParameter(IV): ...
class KeyWrapAlgorithm(AlgorithmIdentifier): ...

class ECC_CMS_SharedInfo(univ.Sequence):
    componentType: Incomplete

class MQVuserKeyingMaterial(univ.Sequence):
    componentType: Incomplete
