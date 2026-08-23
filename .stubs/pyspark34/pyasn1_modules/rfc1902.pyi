from _typeshed import Incomplete
from pyasn1.type import univ

class Integer(univ.Integer):
    subtypeSpec: Incomplete

class Integer32(univ.Integer):
    subtypeSpec: Incomplete

class OctetString(univ.OctetString):
    subtypeSpec: Incomplete

class IpAddress(univ.OctetString):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Counter32(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Gauge32(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Unsigned32(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class TimeTicks(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Opaque(univ.OctetString):
    tagSet: Incomplete

class Counter64(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Bits(univ.OctetString): ...
class ObjectName(univ.ObjectIdentifier): ...

class SimpleSyntax(univ.Choice):
    componentType: Incomplete

class ApplicationSyntax(univ.Choice):
    componentType: Incomplete

class ObjectSyntax(univ.Choice):
    componentType: Incomplete
