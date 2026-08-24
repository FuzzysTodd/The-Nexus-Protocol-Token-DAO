from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

class ProxyCertPathLengthConstraint(univ.Integer): ...

class ProxyPolicy(univ.Sequence):
    componentType: Incomplete

class ProxyCertInfoExtension(univ.Sequence):
    componentType: Incomplete

id_pkix: Incomplete
id_pe: Incomplete
id_pe_proxyCertInfo: Incomplete
id_ppl: Incomplete
id_ppl_anyLanguage: Incomplete
id_ppl_inheritAll: Incomplete
id_ppl_independent: Incomplete
