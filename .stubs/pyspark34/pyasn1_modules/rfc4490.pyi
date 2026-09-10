from _typeshed import Incomplete
from pyasn1.type import char as char, namedval as namedval, univ, useful as useful
from pyasn1_modules import rfc4357 as rfc4357, rfc5280 as rfc5280

id_CryptoPro_algorithms: Incomplete
id_GostR3410_94: Incomplete
id_GostR3410_2001: Incomplete
Gost28147_89_ParamSet: Incomplete
Gost28147_89_EncryptedKey: Incomplete
GostR3410_94_PublicKeyParameters: Incomplete
GostR3410_2001_PublicKeyParameters: Incomplete
SubjectPublicKeyInfo = rfc5280.SubjectPublicKeyInfo

class Gost28147_89_KeyWrapParameters(univ.Sequence):
    componentType: Incomplete

id_Gost28147_89_CryptoPro_KeyWrap: Incomplete
id_Gost28147_89_None_KeyWrap: Incomplete
id_GostR3410_2001_CryptoPro_ESDH: Incomplete
id_GostR3410_94_CryptoPro_ESDH: Incomplete
id_GostR3410_2001_KeyTransportSMIMECapability = id_GostR3410_2001
id_GostR3410_94_KeyTransportSMIMECapability = id_GostR3410_94

class GostR3410_TransportParameters(univ.Sequence):
    componentType: Incomplete

class GostR3410_KeyTransport(univ.Sequence):
    componentType: Incomplete

class GostR3410_94_Signature(univ.OctetString):
    subtypeSpec: Incomplete

class GostR3410_2001_Signature(univ.OctetString):
    subtypeSpec: Incomplete
