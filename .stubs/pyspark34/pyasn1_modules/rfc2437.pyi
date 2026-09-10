from _typeshed import Incomplete
from pyasn1.type import univ as univ
from pyasn1_modules.rfc2459 import AlgorithmIdentifier as AlgorithmIdentifier

pkcs_1: Incomplete
rsaEncryption: Incomplete
md2WithRSAEncryption: Incomplete
md4WithRSAEncryption: Incomplete
md5WithRSAEncryption: Incomplete
sha1WithRSAEncryption: Incomplete
rsaOAEPEncryptionSET: Incomplete
id_RSAES_OAEP: Incomplete
id_mgf1: Incomplete
id_pSpecified: Incomplete
id_sha1: Incomplete
MAX: Incomplete

class Version(univ.Integer): ...

class RSAPrivateKey(univ.Sequence):
    componentType: Incomplete

class RSAPublicKey(univ.Sequence):
    componentType: Incomplete

class RSAES_OAEP_params(univ.Sequence):
    componentType: Incomplete
