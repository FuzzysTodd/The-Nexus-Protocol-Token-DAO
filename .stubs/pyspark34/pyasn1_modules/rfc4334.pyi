from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
id_pe: Incomplete
id_kp: Incomplete
id_aca: Incomplete
id_kp_eapOverPPP: Incomplete
id_kp_eapOverLAN: Incomplete
id_pe_wlanSSID: Incomplete

class SSID(univ.OctetString): ...

class SSIDList(univ.SequenceOf):
    componentType: Incomplete
    subtypeSpec: Incomplete

id_aca_wlanSSID: Incomplete
