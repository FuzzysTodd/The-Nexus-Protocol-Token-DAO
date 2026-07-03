import ort_flatbuffers_py.fbs as fbs
from _typeshed import Incomplete

class FbsTypeInfo:
    """Class to provide conversion between ORT flatbuffers schema values and C++ types"""
    tensordatatype_to_string: Incomplete
    @staticmethod
    def typeinfo_to_str(type: fbs.TypeInfo): ...

def get_typeinfo(name: str, value_name_to_typeinfo: dict) -> fbs.TypeInfo:
    """Lookup a name in a dictionary mapping value name to TypeInfo."""
def value_name_to_typestr(name: str, value_name_to_typeinfo: dict):
    """Lookup TypeInfo for value name and convert to a string representing the C++ type."""
