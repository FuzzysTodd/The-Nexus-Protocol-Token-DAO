from pyasn1_modules.rfc2459 import *
from _typeshed import Incomplete

class Attributes(univ.SetOf):
    componentType: Incomplete

class Version(univ.Integer): ...

class CertificationRequestInfo(univ.Sequence):
    componentType: Incomplete

class Signature(univ.BitString): ...
class SignatureAlgorithmIdentifier(AlgorithmIdentifier): ...

class CertificationRequest(univ.Sequence):
    componentType: Incomplete
