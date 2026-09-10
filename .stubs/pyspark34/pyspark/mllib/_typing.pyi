from _typeshed import Incomplete
from numpy import ndarray
from py4j.java_gateway import JavaObject
from pyspark.mllib.linalg import Vector as Vector
from typing import List, Tuple, TypeVar

VectorLike = ndarray | Vector | List[float] | Tuple[float, ...]
C = TypeVar('C', bound=type)
JavaObjectOrPickleDump = JavaObject | bytearray | bytes
CorrMethodType: Incomplete
KolmogorovSmirnovTestDistNameType: Incomplete
NormType: Incomplete
