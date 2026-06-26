from _typeshed import Incomplete
from collections import OrderedDict

class JsonTricksDeprecation(UserWarning):
    """ Special deprecation warning because the built-in one is ignored by default """
    def __init__(self, msg) -> None: ...

class hashodict(OrderedDict):
    """
\tThis dictionary is hashable. It should NOT be mutated, or all kinds of weird
\tbugs may appear. This is not enforced though, it's only used for encoding.
\t"""
    def __hash__(self): ...

def get_arg_names(callable): ...
def filtered_wrapper(encoder):
    """
\tFilter kwargs passed to encoder.
\t"""

class NoNumpyException(Exception):
    """ Trying to use numpy features, but numpy cannot be found. """
class NoPandasException(Exception):
    """ Trying to use pandas features, but pandas cannot be found. """
class NoEnumException(Exception):
    """ Trying to use enum features, but enum cannot be found. """
class NoPathlibException(Exception):
    """ Trying to use pathlib features, but pathlib cannot be found. """

class ClassInstanceHookBase:
    def get_cls_from_instance_type(self, mod, name, cls_lookup_map): ...

def get_scalar_repr(npscalar): ...
def encode_scalars_inplace(obj):
    """
\tSearches a data structure of lists, tuples and dicts for numpy scalars
\tand replaces them by their dictionary representation, which can be loaded
\tby json-tricks. This happens in-place (the object is changed, use a copy).
\t"""
def encode_intenums_inplace(obj):
    """
\tSearches a data structure of lists, tuples and dicts for IntEnum
\tand replaces them by their dictionary representation, which can be loaded
\tby json-tricks. This happens in-place (the object is changed, use a copy).
\t"""
def get_module_name_from_object(obj): ...
def nested_index(collection, indices): ...
def dict_default(dictionary, key, default_value) -> None: ...
def gzip_compress(data, compresslevel):
    """
\tDo gzip compression, without the timestamp. Similar to gzip.compress, but without timestamp, and also before py3.2.
\t"""
def gzip_decompress(data):
    """
\tDo gzip decompression, without the timestamp. Just like gzip.decompress, but that's py3.2+.
\t"""

is_py3: Incomplete
str_type: Incomplete
