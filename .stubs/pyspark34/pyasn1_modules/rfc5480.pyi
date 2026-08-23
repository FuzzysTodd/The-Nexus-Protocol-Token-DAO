from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc3279 as rfc3279, rfc5280 as rfc5280

DHPublicKey: Incomplete
DSAPublicKey: Incomplete
ValidationParms: Incomplete
DomainParameters: Incomplete
ECDSA_Sig_Value: Incomplete
ECPoint: Incomplete
KEA_Parms_Id: Incomplete
RSAPublicKey: Incomplete
DSS_Parms: Incomplete
DSA_Sig_Value: Incomplete

class ECParameters(univ.Choice): ...

id_md2: Incomplete
id_md5: Incomplete
id_sha1: Incomplete
id_sha224: Incomplete
id_sha256: Incomplete
id_sha384: Incomplete
id_sha512: Incomplete
rsaEncryption: Incomplete
id_dsa: Incomplete
dhpublicnumber: Incomplete
id_keyExchangeAlgorithm: Incomplete
id_ecPublicKey: Incomplete
id_ecDH: Incomplete
id_ecMQV: Incomplete
md2WithRSAEncryption: Incomplete
md5WithRSAEncryption: Incomplete
sha1WithRSAEncryption: Incomplete
id_dsa_with_sha1: Incomplete
id_dsa_with_sha224: Incomplete
id_dsa_with_sha256: Incomplete
ecdsa_with_SHA1: Incomplete
ecdsa_with_SHA224: Incomplete
ecdsa_with_SHA256: Incomplete
ecdsa_with_SHA384: Incomplete
ecdsa_with_SHA512: Incomplete
secp192r1: Incomplete
sect163k1: Incomplete
sect163r2: Incomplete
secp224r1: Incomplete
sect233k1: Incomplete
sect233r1: Incomplete
secp256r1: Incomplete
sect283k1: Incomplete
sect283r1: Incomplete
secp384r1: Incomplete
sect409k1: Incomplete
sect409r1: Incomplete
secp521r1: Incomplete
sect571k1: Incomplete
sect571r1: Incomplete
