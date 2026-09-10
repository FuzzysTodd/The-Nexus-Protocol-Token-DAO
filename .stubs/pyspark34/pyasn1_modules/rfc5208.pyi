from pyasn1_modules.rfc2459 import *
from _typeshed import Incomplete
from pyasn1_modules import rfc2251 as rfc2251

class KeyEncryptionAlgorithms(AlgorithmIdentifier): ...
class PrivateKeyAlgorithms(AlgorithmIdentifier): ...
class EncryptedData(univ.OctetString): ...

class EncryptedPrivateKeyInfo(univ.Sequence):
    componentType: Incomplete

class PrivateKey(univ.OctetString): ...

class Attributes(univ.SetOf):
    componentType: Incomplete

class Version(univ.Integer):
    namedValues: Incomplete

class PrivateKeyInfo(univ.Sequence):
    componentType: Incomplete
