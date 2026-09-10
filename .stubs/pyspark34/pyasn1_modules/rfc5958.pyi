from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280, rfc5652 as rfc5652

MAX: Incomplete

class KeyEncryptionAlgorithmIdentifier(rfc5280.AlgorithmIdentifier): ...
class PrivateKeyAlgorithmIdentifier(rfc5280.AlgorithmIdentifier): ...
class EncryptedData(univ.OctetString): ...

class EncryptedPrivateKeyInfo(univ.Sequence):
    componentType: Incomplete

class Version(univ.Integer):
    namedValues: Incomplete

class PrivateKey(univ.OctetString): ...

class Attributes(univ.SetOf):
    componentType: Incomplete

class PublicKey(univ.BitString): ...

class OneAsymmetricKey(univ.Sequence):
    componentType: Incomplete

class PrivateKeyInfo(OneAsymmetricKey): ...

id_ct_KP_aKeyPackage: Incomplete

class AsymmetricKeyPackage(univ.SequenceOf): ...
