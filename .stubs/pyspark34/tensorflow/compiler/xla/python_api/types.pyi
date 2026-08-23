from _typeshed import Incomplete
from tensorflow.compiler.xla import xla_data_pb2 as xla_data_pb2
from tensorflow.python.framework import dtypes as dtypes
from typing import NamedTuple

class TypeConversionRecord(NamedTuple):
    primitive_type: Incomplete
    numpy_dtype: Incomplete
    literal_field_name: Incomplete
    literal_field_type: Incomplete

MAP_XLA_TYPE_TO_RECORD: Incomplete
MAP_DTYPE_TO_RECORD: Incomplete
