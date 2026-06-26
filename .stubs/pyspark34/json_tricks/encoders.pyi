from .utils import JsonTricksDeprecation as JsonTricksDeprecation, NoEnumException as NoEnumException, NoNumpyException as NoNumpyException, NoPandasException as NoPandasException, filtered_wrapper as filtered_wrapper, get_module_name_from_object as get_module_name_from_object, gzip_compress as gzip_compress, hashodict as hashodict, is_py3 as is_py3, str_type as str_type
from _typeshed import Incomplete
from json import JSONEncoder

def fallback_ignore_unknown(obj, is_changed: Incomplete | None = None, fallback_value: Incomplete | None = None):
    """
\tThis encoder returns None if the object isn't changed by another encoder and isn't a primitive.
\t"""

class TricksEncoder(JSONEncoder):
    """
\tEncoder that runs any number of encoder functions or instances on
\tthe objects that are being encoded.

\tEach encoder should make any appropriate changes and return an object,
\tchanged or not. This will be passes to the other encoders.
\t"""
    obj_encoders: Incomplete
    silence_typeerror: Incomplete
    properties: Incomplete
    primitives: Incomplete
    def __init__(self, obj_encoders: Incomplete | None = None, silence_typeerror: bool = False, primitives: bool = False, fallback_encoders=(), properties: Incomplete | None = None, **json_kwargs) -> None:
        """
\t\t:param obj_encoders: An iterable of functions or encoder instances to try.
\t\t:param silence_typeerror: DEPRECATED - If set to True, ignore the TypeErrors that Encoder instances throw (default False).
\t\t"""
    def default(self, obj, *args, **kwargs):
        """
\t\tThis is the method of JSONEncoders that is called for each object; it calls
\t\tall the encoders with the previous one's output used as input.

\t\tIt works for Encoder instances, but they are expected not to throw
\t\t`TypeError` for unrecognized types (the super method does that by default).

\t\tIt never calls the `super` method so if there are non-primitive types
\t\tleft at the end, you'll get an encoding error.
\t\t"""

def json_date_time_encode(obj, primitives: bool = False):
    """
\tEncode a date, time, datetime or timedelta to a string of a json dictionary, including optional timezone.

\t:param obj: date/time/datetime/timedelta obj
\t:return: (dict) json primitives representation of date, time, datetime or timedelta
\t"""
def enum_instance_encode(obj, primitives: bool = False, with_enum_value: bool = False):
    """Encodes an enum instance to json. Note that it can only be recovered if the environment allows the enum to be
\timported in the same way.
\t:param primitives: If true, encode the enum values as primitive (more readable, but cannot be restored automatically).
\t:param with_enum_value: If true, the value of the enum is also exported (it is not used during import, as it should be constant).
\t"""
def noenum_instance_encode(obj, primitives: bool = False): ...
def class_instance_encode(obj, primitives: bool = False):
    """
\tEncodes a class instance to json. Note that it can only be recovered if the environment allows the class to be
\timported in the same way.
\t"""
def json_complex_encode(obj, primitives: bool = False):
    """
\tEncode a complex number as a json dictionary of its real and imaginary part.

\t:param obj: complex number, e.g. `2+1j`
\t:return: (dict) json primitives representation of `obj`
\t"""
def bytes_encode(obj, primitives: bool = False):
    """
\tEncode bytes as one of these:

\t* A utf8-string with special `__bytes_utf8__` marking, if the bytes are valid utf8 and primitives is False.
\t* A base64 encoded string of the bytes with special `__bytes_b64__` marking, if the bytes are not utf8, or if primitives is True.

\t:param obj: any object, which will be transformed if it is of type bytes
\t:return: (dict) json primitives representation of `obj`
\t"""
def numeric_types_encode(obj, primitives: bool = False):
    """
\tEncode Decimal and Fraction.

\t:param primitives: Encode decimals and fractions as standard floats. You may lose precision. If you do this, you may need to enable `allow_nan` (decimals always allow NaNs but floats do not).
\t"""
def pathlib_encode(obj, primitives: bool = False): ...
def slice_encode(obj, primitives: bool = False): ...

class ClassInstanceEncoder(JSONEncoder):
    """
\tSee `class_instance_encoder`.
\t"""
    encode_cls_instances: Incomplete
    def __init__(self, obj, encode_cls_instances: bool = True, **kwargs) -> None: ...
    def default(self, obj, *args, **kwargs): ...

def json_set_encode(obj, primitives: bool = False):
    """
\tEncode python sets as dictionary with key __set__ and a list of the values.

\tTry to sort the set to get a consistent json representation, use arbitrary order if the data is not ordinal.
\t"""
def pandas_encode(obj, primitives: bool = False): ...
def nopandas_encode(obj): ...
def numpy_encode(obj, primitives: bool = False, properties: Incomplete | None = None):
    """
\tEncodes numpy `ndarray`s as lists with meta data.

\tEncodes numpy scalar types as Python equivalents. Special encoding is not possible,
\tbecause int64 (in py2) and float64 (in py2 and py3) are subclasses of primitives,
\twhich never reach the encoder.

\t:param primitives: If True, arrays are serialized as (nested) lists without meta info.
\t"""

class NumpyEncoder(ClassInstanceEncoder):
    """
\tJSON encoder for numpy arrays.
\t"""
    SHOW_SCALAR_WARNING: bool
    def default(self, obj, *args, **kwargs):
        """
\t\tIf input object is a ndarray it will be converted into a dict holding
\t\tdata type, shape and the data. The object can be restored using json_numpy_obj_hook.
\t\t"""

def nonumpy_encode(obj):
    """
\tRaises an error for numpy arrays.
\t"""

class NoNumpyEncoder(JSONEncoder):
    """
\tSee `nonumpy_encode`.
\t"""
    def default(self, obj, *args, **kwargs): ...
