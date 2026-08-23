from .utils import ClassInstanceHookBase as ClassInstanceHookBase, filtered_wrapper as filtered_wrapper, gzip_decompress as gzip_decompress, nested_index as nested_index, str_type as str_type
from _typeshed import Incomplete
from json_tricks import NoEnumException as NoEnumException, NoNumpyException as NoNumpyException, NoPandasException as NoPandasException

class DuplicateJsonKeyException(Exception):
    """ Trying to load a json map which contains duplicate keys, but allow_duplicates is False """

class TricksPairHook:
    """
\tHook that converts json maps to the appropriate python type (dict or OrderedDict)
\tand then runs any number of hooks on the individual maps.
\t"""
    properties: Incomplete
    map_type: Incomplete
    obj_pairs_hooks: Incomplete
    allow_duplicates: Incomplete
    def __init__(self, ordered: bool = True, obj_pairs_hooks: Incomplete | None = None, allow_duplicates: bool = True, properties: Incomplete | None = None) -> None:
        """
\t\t:param ordered: True if maps should retain their ordering.
\t\t:param obj_pairs_hooks: An iterable of hooks to apply to elements.
\t\t"""
    def __call__(self, pairs): ...

def json_date_time_hook(dct):
    """
\tReturn an encoded date, time, datetime or timedelta to it's python representation, including optional timezone.

\t:param dct: (dict) json encoded date, time, datetime or timedelta
\t:return: (date/time/datetime/timedelta obj) python representation of the above
\t"""
def json_complex_hook(dct):
    """
\tReturn an encoded complex number to Python complex type.

\t:param dct: (dict) json encoded complex number (__complex__)
\t:return: python complex number
\t"""
def json_bytes_hook(dct):
    """
\tReturn encoded bytes, either base64 or utf8, back to Python bytes.

\t:param dct: any object, if it is a dict containing encoded bytes, they will be converted
\t:return: python complex number
\t"""
def numeric_types_hook(dct): ...
def noenum_hook(dct): ...
def pathlib_hook(dct): ...
def nopathlib_hook(dct): ...
def slice_hook(dct): ...

class EnumInstanceHook(ClassInstanceHookBase):
    """
\tThis hook tries to convert json encoded by enum_instance_encode back to it's original instance.
\tIt only works if the environment is the same, e.g. the enum is similarly importable and hasn't changed.
\t"""
    def __call__(self, dct, properties: Incomplete | None = None): ...

class ClassInstanceHook(ClassInstanceHookBase):
    """
\tThis hook tries to convert json encoded by class_instance_encoder back to it's original instance.
\tIt only works if the environment is the same, e.g. the class is similarly importable and hasn't changed.
\t"""
    def __call__(self, dct, properties: Incomplete | None = None): ...

def json_set_hook(dct):
    """
\tReturn an encoded set to it's python representation.
\t"""
def pandas_hook(dct): ...
def nopandas_hook(dct): ...
def json_numpy_obj_hook(dct):
    """
\tReplace any numpy arrays previously encoded by `numpy_encode` to their proper
\tshape, data type and data.

\t:param dct: (dict) json encoded ndarray
\t:return: (ndarray) if input was an encoded ndarray
\t"""
def json_nonumpy_obj_hook(dct):
    """
\tThis hook has no effect except to check if you're trying to decode numpy arrays without support, and give you a useful message.
\t"""
