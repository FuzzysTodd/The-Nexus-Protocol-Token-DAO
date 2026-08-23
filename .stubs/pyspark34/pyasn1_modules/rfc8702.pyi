from _typeshed import Incomplete
from pyasn1.type import tag as tag, univ
from pyasn1_modules import rfc5280 as rfc5280, rfc8692 as rfc8692

AlgorithmIdentifier = rfc5280.AlgorithmIdentifier
id_shake128: Incomplete
mda_shake128: Incomplete
id_shake256: Incomplete
mda_shake256: Incomplete
id_RSASSA_PSS_SHAKE128: Incomplete
sa_rSASSA_PSS_SHAKE128: Incomplete
pk_rsaSSA_PSS_SHAKE128: Incomplete
id_RSASSA_PSS_SHAKE256: Incomplete
sa_rSASSA_PSS_SHAKE256: Incomplete
pk_rsaSSA_PSS_SHAKE256: Incomplete
id_ecdsa_with_shake128: Incomplete
sa_ecdsa_with_shake128: Incomplete
id_ecdsa_with_shake256: Incomplete
sa_ecdsa_with_shake256: Incomplete
pk_ec: Incomplete
id_KMACWithSHAKE128: Incomplete

class KMACwithSHAKE128_params(univ.Sequence):
    componentType: Incomplete

maca_KMACwithSHAKE128: Incomplete
id_KMACWithSHAKE256: Incomplete

class KMACwithSHAKE256_params(univ.Sequence):
    componentType: Incomplete

maca_KMACwithSHAKE256: Incomplete
