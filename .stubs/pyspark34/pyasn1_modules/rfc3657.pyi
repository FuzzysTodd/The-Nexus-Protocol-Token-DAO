from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280, rfc5751 as rfc5751

id_camellia128_cbc: Incomplete
id_camellia192_cbc: Incomplete
id_camellia256_cbc: Incomplete
id_camellia128_wrap: Incomplete
id_camellia192_wrap: Incomplete
id_camellia256_wrap: Incomplete

class Camellia_IV(univ.OctetString):
    subtypeSpec: Incomplete

class CamelliaSMimeCapability(univ.Null): ...
