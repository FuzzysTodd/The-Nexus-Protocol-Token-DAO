from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

id_sha1: Incomplete
id_sha256: Incomplete
id_sha384: Incomplete
id_sha512: Incomplete
id_sha224: Incomplete
rsaEncryption: Incomplete
id_mgf1: Incomplete
id_RSAES_OAEP: Incomplete
id_pSpecified: Incomplete
id_RSASSA_PSS: Incomplete
sha256WithRSAEncryption: Incomplete
sha384WithRSAEncryption: Incomplete
sha512WithRSAEncryption: Incomplete
sha224WithRSAEncryption: Incomplete
sha1Identifier: Incomplete
sha224Identifier: Incomplete
sha256Identifier: Incomplete
sha384Identifier: Incomplete
sha512Identifier: Incomplete
mgf1SHA1Identifier: Incomplete
mgf1SHA224Identifier: Incomplete
mgf1SHA256Identifier: Incomplete
mgf1SHA384Identifier: Incomplete
mgf1SHA512Identifier: Incomplete
pSpecifiedEmptyIdentifier: Incomplete

class RSAPublicKey(univ.Sequence): ...
class HashAlgorithm(rfc5280.AlgorithmIdentifier): ...
class MaskGenAlgorithm(rfc5280.AlgorithmIdentifier): ...
class RSAES_OAEP_params(univ.Sequence): ...

rSAES_OAEP_Default_Params: Incomplete
rSAES_OAEP_Default_Identifier: Incomplete
rSAES_OAEP_SHA224_Params: Incomplete
rSAES_OAEP_SHA224_Identifier: Incomplete
rSAES_OAEP_SHA256_Params: Incomplete
rSAES_OAEP_SHA256_Identifier: Incomplete
rSAES_OAEP_SHA384_Params: Incomplete
rSAES_OAEP_SHA384_Identifier: Incomplete
rSAES_OAEP_SHA512_Params: Incomplete
rSAES_OAEP_SHA512_Identifier: Incomplete

class RSASSA_PSS_params(univ.Sequence): ...

rSASSA_PSS_Default_Params: Incomplete
rSASSA_PSS_Default_Identifier: Incomplete
rSASSA_PSS_SHA224_Params: Incomplete
rSASSA_PSS_SHA224_Identifier: Incomplete
rSASSA_PSS_SHA256_Params: Incomplete
rSASSA_PSS_SHA256_Identifier: Incomplete
rSASSA_PSS_SHA384_Params: Incomplete
rSASSA_PSS_SHA384_Identifier: Incomplete
rSASSA_PSS_SHA512_Params: Incomplete
rSASSA_PSS_SHA512_Identifier: Incomplete
