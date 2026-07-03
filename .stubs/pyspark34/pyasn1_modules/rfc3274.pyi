from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280, rfc5652 as rfc5652

class CompressionAlgorithmIdentifier(rfc5280.AlgorithmIdentifier): ...

id_ct_compressedData: Incomplete

class CompressedData(univ.Sequence): ...

id_alg_zlibCompress: Incomplete
cpa_zlibCompress: Incomplete
