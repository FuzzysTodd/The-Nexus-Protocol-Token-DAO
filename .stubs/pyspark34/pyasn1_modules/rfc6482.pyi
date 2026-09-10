from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5652 as rfc5652

MAX: Incomplete
id_ct_routeOriginAuthz: Incomplete

class ASID(univ.Integer): ...
class IPAddress(univ.BitString): ...

class ROAIPAddress(univ.Sequence):
    componentType: Incomplete

class ROAIPAddressFamily(univ.Sequence):
    componentType: Incomplete

class RouteOriginAttestation(univ.Sequence):
    componentType: Incomplete
