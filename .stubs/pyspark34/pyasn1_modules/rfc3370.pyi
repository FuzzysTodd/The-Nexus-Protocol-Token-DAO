from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc3279 as rfc3279, rfc5280 as rfc5280, rfc5751 as rfc5751, rfc5753 as rfc5753, rfc5990 as rfc5990, rfc8018 as rfc8018

AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
dhpublicnumber: Incomplete
dh_public_number = dhpublicnumber
DHPublicKey: Incomplete
DomainParameters: Incomplete
DHDomainParameters = DomainParameters
Dss_Parms: Incomplete
Dss_Sig_Value: Incomplete
md5: Incomplete
md5WithRSAEncryption: Incomplete
RSAPublicKey: Incomplete
rsaEncryption: Incomplete
ValidationParms: Incomplete
id_dsa: Incomplete
id_dsa_with_sha1: Incomplete
id_sha1: Incomplete
sha_1 = id_sha1
sha1WithRSAEncryption: Incomplete
CBCParameter = rfc5753.CBCParameter
CBCParameter = rfc5753.IV
KeyWrapAlgorithm = rfc5753.KeyWrapAlgorithm
id_alg_CMS3DESwrap: Incomplete
des_EDE3_CBC: Incomplete
des_ede3_cbc = des_EDE3_CBC
rc2CBC: Incomplete
rc2_cbc = rc2CBC
RC2_CBC_Parameter = rfc8018.RC2_CBC_Parameter
RC2CBCParameter = RC2_CBC_Parameter
PBKDF2_params = rfc8018.PBKDF2_params
id_PBKDF2: Incomplete
hMAC_SHA1: Incomplete
id_alg_ESDH: Incomplete
id_alg_SSDH: Incomplete
id_alg_CMSRC2wrap: Incomplete

class RC2ParameterVersion(univ.Integer): ...
class RC2wrapParameter(RC2ParameterVersion): ...
class Dss_Pub_Key(univ.Integer): ...
