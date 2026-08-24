from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
AlgorithmIdentifier = rfc5280.AlgorithmIdentifier

class NullParms(univ.Null): ...

is18033_2: Incomplete
nistAlgorithm: Incomplete
pkcs_1: Incomplete
x9_44: Incomplete
x9_44_components: Incomplete

class Camellia_KeyWrappingScheme(AlgorithmIdentifier): ...
class DataEncapsulationMechanism(AlgorithmIdentifier): ...
class KDF2_HashFunction(AlgorithmIdentifier): ...
class KDF3_HashFunction(AlgorithmIdentifier): ...
class KeyDerivationFunction(AlgorithmIdentifier): ...
class KeyEncapsulationMechanism(AlgorithmIdentifier): ...
class X9_SymmetricKeyWrappingScheme(AlgorithmIdentifier): ...

id_rsa_kem: Incomplete

class GenericHybridParameters(univ.Sequence): ...

rsa_kem: Incomplete
id_kem_rsa: Incomplete

class KeyLength(univ.Integer): ...
class RsaKemParameters(univ.Sequence): ...

kem_rsa: Incomplete
id_kdf_kdf2: Incomplete
id_kdf_kdf3: Incomplete
kdf2: Incomplete
kdf3: Incomplete
id_sha1: Incomplete
id_sha224: Incomplete
id_sha256: Incomplete
id_sha384: Incomplete
id_sha512: Incomplete
sha1: Incomplete
sha224: Incomplete
sha256: Incomplete
sha384: Incomplete
sha512: Incomplete
id_aes128_Wrap: Incomplete
id_aes192_Wrap: Incomplete
id_aes256_Wrap: Incomplete
id_alg_CMS3DESwrap: Incomplete
id_camellia128_Wrap: Incomplete
id_camellia192_Wrap: Incomplete
id_camellia256_Wrap: Incomplete
aes128_Wrap: Incomplete
aes192_Wrap: Incomplete
aes256_Wrap: Incomplete
tdes_Wrap: Incomplete
camellia128_Wrap: Incomplete
camellia192_Wrap: Incomplete
camellia256_Wrap: Incomplete
