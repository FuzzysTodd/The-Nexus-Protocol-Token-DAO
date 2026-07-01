from _typeshed import Incomplete
from pyasn1.type import char, univ
from pyasn1_modules import rfc5652 as rfc5652

MAX: Incomplete

class Algorithm(univ.Enumerated):
    namedValues: Incomplete

class HeaderFieldStatus(univ.Integer):
    namedValues: Incomplete

class HeaderFieldName(char.VisibleString):
    subtypeSpec: Incomplete

class HeaderFieldValue(char.UTF8String): ...

class HeaderField(univ.Sequence):
    componentType: Incomplete

class HeaderFields(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete

class SecureHeaderFields(univ.Set):
    componentType: Incomplete

id_aa: Incomplete
id_aa_secureHeaderFieldsIdentifier: Incomplete
