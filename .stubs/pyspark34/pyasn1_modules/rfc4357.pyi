from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
id_CryptoPro: Incomplete
id_CryptoPro_modules: Incomplete
id_CryptoPro_extensions: Incomplete
id_CryptoPro_policyIds: Incomplete
id_CryptoPro_policyQt: Incomplete
cryptographic_Gost_Useful_Definitions: Incomplete
gostR3411_94_DigestSyntax: Incomplete
gostR3410_94_PKISyntax: Incomplete
gostR3410_94_SignatureSyntax: Incomplete
gost28147_89_EncryptionSyntax: Incomplete
gostR3410_EncryptionSyntax: Incomplete
gost28147_89_ParamSetSyntax: Incomplete
gostR3411_94_ParamSetSyntax: Incomplete
gostR3410_94_ParamSetSyntax: Incomplete
gostR3410_2001_PKISyntax: Incomplete
gostR3410_2001_SignatureSyntax: Incomplete
gostR3410_2001_ParamSetSyntax: Incomplete
gost_CryptoPro_ExtendedKeyUsage: Incomplete
gost_CryptoPro_PrivateKey: Incomplete
gost_CryptoPro_PKIXCMP: Incomplete
gost_CryptoPro_TLS: Incomplete
gost_CryptoPro_Policy: Incomplete
gost_CryptoPro_Constants: Incomplete
id_CryptoPro_algorithms = id_CryptoPro
id_GostR3411_94_with_GostR3410_2001: Incomplete
id_GostR3411_94_with_GostR3410_94: Incomplete
id_GostR3411_94: Incomplete
id_Gost28147_89_None_KeyMeshing: Incomplete
id_Gost28147_89_CryptoPro_KeyMeshing: Incomplete
id_GostR3410_2001: Incomplete
id_GostR3410_94: Incomplete
id_Gost28147_89: Incomplete
id_Gost28147_89_MAC: Incomplete
id_CryptoPro_hashes: Incomplete
id_CryptoPro_encrypts: Incomplete
id_CryptoPro_signs: Incomplete
id_CryptoPro_exchanges: Incomplete
id_CryptoPro_ecc_signs: Incomplete
id_CryptoPro_ecc_exchanges: Incomplete
id_CryptoPro_private_keys: Incomplete
id_CryptoPro_pkixcmp_infos: Incomplete
id_CryptoPro_audit_service_types: Incomplete
id_CryptoPro_audit_record_types: Incomplete
id_CryptoPro_attributes: Incomplete
id_CryptoPro_name_service_types: Incomplete
id_GostR3410_2001DH: Incomplete
id_GostR3410_94DH: Incomplete
id_Gost28147_89_TestParamSet: Incomplete
id_Gost28147_89_CryptoPro_A_ParamSet: Incomplete
id_Gost28147_89_CryptoPro_B_ParamSet: Incomplete
id_Gost28147_89_CryptoPro_C_ParamSet: Incomplete
id_Gost28147_89_CryptoPro_D_ParamSet: Incomplete
id_Gost28147_89_CryptoPro_Oscar_1_1_ParamSet: Incomplete
id_Gost28147_89_CryptoPro_Oscar_1_0_ParamSet: Incomplete
id_Gost28147_89_CryptoPro_RIC_1_ParamSet: Incomplete
id_GostR3410_2001_TestParamSet: Incomplete
id_GostR3410_2001_CryptoPro_A_ParamSet: Incomplete
id_GostR3410_2001_CryptoPro_B_ParamSet: Incomplete
id_GostR3410_2001_CryptoPro_C_ParamSet: Incomplete
id_GostR3410_2001_CryptoPro_XchA_ParamSet: Incomplete
id_GostR3410_2001_CryptoPro_XchB_ParamSet: Incomplete
id_GostR3410_94_TestParamSet: Incomplete
id_GostR3410_94_CryptoPro_A_ParamSet: Incomplete
id_GostR3410_94_CryptoPro_B_ParamSet: Incomplete
id_GostR3410_94_CryptoPro_C_ParamSet: Incomplete
id_GostR3410_94_CryptoPro_D_ParamSet: Incomplete
id_GostR3410_94_CryptoPro_XchA_ParamSet: Incomplete
id_GostR3410_94_CryptoPro_XchB_ParamSet: Incomplete
id_GostR3410_94_CryptoPro_XchC_ParamSet: Incomplete
id_GostR3410_94_a: Incomplete
id_GostR3410_94_aBis: Incomplete
id_GostR3410_94_b: Incomplete
id_GostR3410_94_bBis: Incomplete
id_GostR3411_94_TestParamSet: Incomplete
id_GostR3411_94_CryptoProParamSet: Incomplete

class Gost28147_89_ParamSet(univ.ObjectIdentifier): ...
class Gost28147_89_BlobParameters(univ.Sequence): ...
class Gost28147_89_MAC(univ.OctetString): ...
class Gost28147_89_Key(univ.OctetString): ...
class Gost28147_89_EncryptedKey(univ.Sequence): ...
class Gost28147_89_IV(univ.OctetString): ...
class Gost28147_89_UZ(univ.OctetString): ...
class Gost28147_89_ParamSetParameters(univ.Sequence): ...
class Gost28147_89_Parameters(univ.Sequence): ...
class GostR3410_2001_CertificateSignature(univ.BitString): ...
class GostR3410_2001_ParamSetParameters(univ.Sequence): ...
class GostR3410_2001_PublicKey(univ.OctetString): ...
class GostR3410_2001_PublicKeyParameters(univ.Sequence): ...
class GostR3410_94_CertificateSignature(univ.BitString): ...
class GostR3410_94_ParamSetParameters_t(univ.Integer): ...
class GostR3410_94_ParamSetParameters(univ.Sequence): ...
class GostR3410_94_PublicKey(univ.OctetString): ...
class GostR3410_94_PublicKeyParameters(univ.Sequence): ...
class GostR3410_94_ValidationBisParameters_c(univ.Integer): ...
class GostR3410_94_ValidationBisParameters(univ.Sequence): ...
class GostR3410_94_ValidationParameters_c(univ.Integer): ...
class GostR3410_94_ValidationParameters(univ.Sequence): ...
class GostR3411_94_Digest(univ.OctetString): ...
class GostR3411_94_DigestParameters(univ.ObjectIdentifier): ...
class GostR3411_94_ParamSetParameters(univ.Sequence): ...
