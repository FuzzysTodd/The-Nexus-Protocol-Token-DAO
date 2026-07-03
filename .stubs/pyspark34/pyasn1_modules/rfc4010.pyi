from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280, rfc5751 as rfc5751

id_seedCBC: Incomplete
id_npki_app_cmsSeed_wrap: Incomplete

class SeedIV(univ.OctetString):
    subtypeSpec: Incomplete

class SeedCBCParameter(SeedIV): ...
class SeedSMimeCapability(univ.Null): ...
