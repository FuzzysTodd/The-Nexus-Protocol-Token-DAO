from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

md2: Incomplete
md5: Incomplete
id_sha1: Incomplete
id_dsa: Incomplete

class DSAPublicKey(univ.Integer): ...

class Dss_Parms(univ.Sequence):
    componentType: Incomplete

id_dsa_with_sha1: Incomplete

class Dss_Sig_Value(univ.Sequence):
    componentType: Incomplete

pkcs_1: Incomplete
rsaEncryption: Incomplete
md2WithRSAEncryption: Incomplete
md5WithRSAEncryption: Incomplete
sha1WithRSAEncryption: Incomplete

class RSAPublicKey(univ.Sequence):
    componentType: Incomplete

dhpublicnumber: Incomplete

class DHPublicKey(univ.Integer): ...

class ValidationParms(univ.Sequence):
    componentType: Incomplete

class DomainParameters(univ.Sequence):
    componentType: Incomplete

id_keyExchangeAlgorithm: Incomplete

class KEA_Parms_Id(univ.OctetString): ...

ansi_X9_62: Incomplete

class FieldID(univ.Sequence):
    componentType: Incomplete

id_ecSigType: Incomplete
ecdsa_with_SHA1: Incomplete

class ECDSA_Sig_Value(univ.Sequence):
    componentType: Incomplete

id_fieldType: Incomplete
prime_field: Incomplete

class Prime_p(univ.Integer): ...

characteristic_two_field: Incomplete

class Characteristic_two(univ.Sequence):
    componentType: Incomplete

id_characteristic_two_basis: Incomplete
gnBasis: Incomplete
tpBasis: Incomplete

class Trinomial(univ.Integer): ...

ppBasis: Incomplete

class Pentanomial(univ.Sequence):
    componentType: Incomplete

class FieldElement(univ.OctetString): ...
class ECPoint(univ.OctetString): ...

class Curve(univ.Sequence):
    componentType: Incomplete

class ECPVer(univ.Integer):
    namedValues: Incomplete

class ECParameters(univ.Sequence):
    componentType: Incomplete

class EcpkParameters(univ.Choice):
    componentType: Incomplete

id_publicKeyType: Incomplete
id_ecPublicKey: Incomplete
ellipticCurve: Incomplete
c_TwoCurve: Incomplete
c2pnb163v1: Incomplete
c2pnb163v2: Incomplete
c2pnb163v3: Incomplete
c2pnb176w1: Incomplete
c2tnb191v1: Incomplete
c2tnb191v2: Incomplete
c2tnb191v3: Incomplete
c2onb191v4: Incomplete
c2onb191v5: Incomplete
c2pnb208w1: Incomplete
c2tnb239v1: Incomplete
c2tnb239v2: Incomplete
c2tnb239v3: Incomplete
c2onb239v4: Incomplete
c2onb239v5: Incomplete
c2pnb272w1: Incomplete
c2pnb304w1: Incomplete
c2tnb359v1: Incomplete
c2pnb368w1: Incomplete
c2tnb431r1: Incomplete
primeCurve: Incomplete
prime192v1: Incomplete
prime192v2: Incomplete
prime192v3: Incomplete
prime239v1: Incomplete
prime239v2: Incomplete
prime239v3: Incomplete
prime256v1: Incomplete
