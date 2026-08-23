from . import packer as packer
from .compat import NumpyRequiredForThisFeature as NumpyRequiredForThisFeature, import_numpy as import_numpy, memoryview_type as memoryview_type
from _typeshed import Incomplete

np: Incomplete
FILE_IDENTIFIER_LENGTH: int

def Get(packer_type, buf, head):
    """ Get decodes a value at buf[head] using `packer_type`. """
def GetVectorAsNumpy(numpy_type, buf, count, offset):
    """ GetVecAsNumpy decodes values starting at buf[head] as
    `numpy_type`, where `numpy_type` is a numpy dtype. """
def Write(packer_type, buf, head, n) -> None:
    """ Write encodes `n` at buf[head] using `packer_type`. """
