from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

class AES_CCM_ICVlen(univ.Integer): ...
class AES_GCM_ICVlen(univ.Integer): ...
class CCMParameters(univ.Sequence): ...
class GCMParameters(univ.Sequence): ...

aes: Incomplete
id_aes128_CCM: Incomplete
id_aes128_GCM: Incomplete
id_aes192_CCM: Incomplete
id_aes192_GCM: Incomplete
id_aes256_CCM: Incomplete
id_aes256_GCM: Incomplete
