from _typeshed import Incomplete
from enum import Enum
from typing import NamedTuple

__all__ = ['RPCExecMode', 'serialize', 'deserialize', 'PythonUDF', 'RemoteException']

class RPCExecMode(Enum):
    SYNC: str
    ASYNC: str
    ASYNC_JIT: str
    REMOTE: str

class _InternalRPCPickler:
    '''
    This class provides serialize() and deserialize() interfaces to serialize
    data to be "binary string + tensor table" format
    So for RPC python UDF function and args, non tensor data will be serialized
    into regular binary string, tensor data will be put into thread local tensor
    tables, this serialization format is consistent with builtin operator and args
    using JIT pickler. This format will make tensor handling in C++ much easier,
    e.g. attach tensor to distributed autograd graph in C++
    '''
    def __init__(self) -> None: ...
    def serialize(self, obj):
        """
        Serialize non tensor data into binary string, tensor data into
        tensor table
        """
    def deserialize(self, binary_data, tensor_table):
        """
        Deserialize binary string + tensor table to original obj
        """

def serialize(obj): ...
def deserialize(binary_data, tensor_table): ...

class PythonUDF(NamedTuple):
    func: Incomplete
    args: Incomplete
    kwargs: Incomplete

class RemoteException(NamedTuple):
    msg: Incomplete
    exception_type: Incomplete

# Names in __all__ with no definition:
#   PythonUDF
#   RemoteException
