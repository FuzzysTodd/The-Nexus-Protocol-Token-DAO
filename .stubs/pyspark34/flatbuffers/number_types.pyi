from . import packer as packer
from .compat import NumpyRequiredForThisFeature as NumpyRequiredForThisFeature, import_numpy as import_numpy
from _typeshed import Incomplete

np: Incomplete

class BoolFlags:
    bytewidth: int
    min_val: bool
    max_val: bool
    py_type = bool
    name: str
    packer_type: Incomplete

class Uint8Flags:
    bytewidth: int
    min_val: int
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Uint16Flags:
    bytewidth: int
    min_val: int
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Uint32Flags:
    bytewidth: int
    min_val: int
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Uint64Flags:
    bytewidth: int
    min_val: int
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Int8Flags:
    bytewidth: int
    min_val: Incomplete
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Int16Flags:
    bytewidth: int
    min_val: Incomplete
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Int32Flags:
    bytewidth: int
    min_val: Incomplete
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Int64Flags:
    bytewidth: int
    min_val: Incomplete
    max_val: Incomplete
    py_type = int
    name: str
    packer_type: Incomplete

class Float32Flags:
    bytewidth: int
    min_val: Incomplete
    max_val: Incomplete
    py_type = float
    name: str
    packer_type: Incomplete

class Float64Flags:
    bytewidth: int
    min_val: Incomplete
    max_val: Incomplete
    py_type = float
    name: str
    packer_type: Incomplete

class SOffsetTFlags(Int32Flags): ...
class UOffsetTFlags(Uint32Flags): ...
class VOffsetTFlags(Uint16Flags): ...

def valid_number(n, flags): ...
def enforce_number(n, flags) -> None: ...
def float32_to_uint32(n): ...
def uint32_to_float32(n): ...
def float64_to_uint64(n): ...
def uint64_to_float64(n): ...
def to_numpy_type(number_type): ...
