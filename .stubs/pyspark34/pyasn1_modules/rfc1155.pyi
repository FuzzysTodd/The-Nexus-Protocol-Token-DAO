from _typeshed import Incomplete
from pyasn1.type import univ

class ObjectName(univ.ObjectIdentifier): ...

class SimpleSyntax(univ.Choice):
    componentType: Incomplete

class IpAddress(univ.OctetString):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class NetworkAddress(univ.Choice):
    componentType: Incomplete

class Counter(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Gauge(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class TimeTicks(univ.Integer):
    tagSet: Incomplete
    subtypeSpec: Incomplete

class Opaque(univ.OctetString):
    tagSet: Incomplete

class ApplicationSyntax(univ.Choice):
    componentType: Incomplete

class ObjectSyntax(univ.Choice):
    componentType: Incomplete
