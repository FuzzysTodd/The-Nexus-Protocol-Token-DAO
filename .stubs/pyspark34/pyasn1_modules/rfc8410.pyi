from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc3565 as rfc3565, rfc4055 as rfc4055, rfc5280 as rfc5280

class SignatureAlgorithmIdentifier(rfc5280.AlgorithmIdentifier): ...
class KeyEncryptionAlgorithmIdentifier(rfc5280.AlgorithmIdentifier): ...
class CurvePrivateKey(univ.OctetString): ...

id_X25519: Incomplete
id_X448: Incomplete
id_Ed25519: Incomplete
id_Ed448: Incomplete
id_sha512: Incomplete
id_aes128_wrap: Incomplete
id_aes256_wrap: Incomplete
