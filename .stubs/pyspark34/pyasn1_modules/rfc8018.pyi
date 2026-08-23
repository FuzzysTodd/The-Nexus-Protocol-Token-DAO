from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc3565 as rfc3565, rfc5280 as rfc5280

MAX: Incomplete
AES_IV: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
nistAlgorithms: Incomplete
aes: Incomplete
oiw: Incomplete
rsadsi: Incomplete
pkcs: Incomplete
digestAlgorithm: Incomplete
encryptionAlgorithm: Incomplete
pkcs_5: Incomplete
id_hmacWithSHA1: Incomplete
id_hmacWithSHA224: Incomplete
id_hmacWithSHA256: Incomplete
id_hmacWithSHA384: Incomplete
id_hmacWithSHA512: Incomplete
id_hmacWithSHA512_224: Incomplete
id_hmacWithSHA512_256: Incomplete
pbeWithMD2AndDES_CBC: Incomplete
pbeWithMD2AndRC2_CBC: Incomplete
pbeWithMD5AndDES_CBC: Incomplete
pbeWithMD5AndRC2_CBC: Incomplete
pbeWithSHA1AndDES_CBC: Incomplete
pbeWithSHA1AndRC2_CBC: Incomplete
desCBC: Incomplete
des_EDE3_CBC: Incomplete
rc2CBC: Incomplete
rc5_CBC_PAD: Incomplete
aes128_CBC_PAD: Incomplete
aes192_CBC_PAD: Incomplete
aes256_CBC_PAD: Incomplete

class PBEParameter(univ.Sequence): ...

id_PBES2: Incomplete

class PBES2_params(univ.Sequence): ...

id_PBMAC1: Incomplete

class PBMAC1_params(univ.Sequence): ...

id_PBKDF2: Incomplete
algid_hmacWithSHA1: Incomplete

class PBKDF2_params(univ.Sequence): ...
class RC2_CBC_Parameter(univ.Sequence): ...
class RC5_CBC_Parameters(univ.Sequence): ...
class AES_IV(univ.OctetString): ...
class DES_IV(univ.OctetString): ...
