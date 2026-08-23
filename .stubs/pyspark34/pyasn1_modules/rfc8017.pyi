from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc2437 as rfc2437, rfc3447 as rfc3447, rfc4055 as rfc4055, rfc5280 as rfc5280

MAX: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier

class DigestAlgorithm(AlgorithmIdentifier): ...
class HashAlgorithm(AlgorithmIdentifier): ...
class MaskGenAlgorithm(AlgorithmIdentifier): ...
class PSourceAlgorithm(AlgorithmIdentifier): ...

hashAlgs: Incomplete
id_sha256: Incomplete
id_sha384: Incomplete
id_sha512: Incomplete
id_sha224: Incomplete
id_sha512_224: Incomplete
id_sha512_256: Incomplete
pkcs_1: Incomplete
rsaEncryption: Incomplete
id_RSAES_OAEP: Incomplete
id_pSpecified: Incomplete
id_RSASSA_PSS: Incomplete
md2WithRSAEncryption: Incomplete
md5WithRSAEncryption: Incomplete
sha1WithRSAEncryption: Incomplete
sha224WithRSAEncryption: Incomplete
sha256WithRSAEncryption: Incomplete
sha384WithRSAEncryption: Incomplete
sha512WithRSAEncryption: Incomplete
sha512_224WithRSAEncryption: Incomplete
sha512_256WithRSAEncryption: Incomplete
id_sha1: Incomplete
id_md2: Incomplete
id_md5: Incomplete
id_mgf1: Incomplete
sha1: Incomplete
SHA1Parameters: Incomplete
mgf1SHA1: Incomplete

class EncodingParameters(univ.OctetString):
    subtypeSpec: Incomplete

pSpecifiedEmpty: Incomplete
emptyString: Incomplete

class Version(univ.Integer):
    namedValues: Incomplete

class TrailerField(univ.Integer):
    namedValues: Incomplete

RSAPublicKey: Incomplete
OtherPrimeInfo: Incomplete
OtherPrimeInfos: Incomplete
RSAPrivateKey: Incomplete
RSAES_OAEP_params: Incomplete
rSAES_OAEP_Default_Identifier: Incomplete
RSASSA_PSS_params: Incomplete
rSASSA_PSS_Default_Identifier: Incomplete

class DigestInfo(univ.Sequence):
    componentType: Incomplete
