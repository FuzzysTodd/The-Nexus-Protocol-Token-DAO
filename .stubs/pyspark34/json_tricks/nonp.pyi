from .comment import strip_comments as strip_comments
from .decoders import ClassInstanceHook as ClassInstanceHook, EnumInstanceHook as EnumInstanceHook, TricksPairHook as TricksPairHook, json_bytes_hook as json_bytes_hook, json_complex_hook as json_complex_hook, json_date_time_hook as json_date_time_hook, json_nonumpy_obj_hook as json_nonumpy_obj_hook, json_numpy_obj_hook as json_numpy_obj_hook, json_set_hook as json_set_hook, noenum_hook as noenum_hook, nopandas_hook as nopandas_hook, nopathlib_hook as nopathlib_hook, numeric_types_hook as numeric_types_hook, pandas_hook as pandas_hook, pathlib_hook as pathlib_hook, slice_hook as slice_hook
from .encoders import TricksEncoder as TricksEncoder, bytes_encode as bytes_encode, class_instance_encode as class_instance_encode, enum_instance_encode as enum_instance_encode, json_complex_encode as json_complex_encode, json_date_time_encode as json_date_time_encode, json_set_encode as json_set_encode, noenum_instance_encode as noenum_instance_encode, nonumpy_encode as nonumpy_encode, nopandas_encode as nopandas_encode, numeric_types_encode as numeric_types_encode, numpy_encode as numpy_encode, pandas_encode as pandas_encode, pathlib_encode as pathlib_encode, slice_encode as slice_encode
from .utils import NoNumpyException as NoNumpyException, str_type as str_type
from _typeshed import Incomplete
from json_tricks.utils import JsonTricksDeprecation as JsonTricksDeprecation, dict_default as dict_default, gzip_compress as gzip_compress, gzip_decompress as gzip_decompress, is_py3 as is_py3

ENCODING: str
DEFAULT_ENCODERS: Incomplete
DEFAULT_HOOKS: Incomplete
DEFAULT_NONP_ENCODERS: Incomplete
DEFAULT_NONP_HOOKS: Incomplete

def dumps(obj, sort_keys: Incomplete | None = None, cls: Incomplete | None = None, obj_encoders=..., extra_obj_encoders=(), primitives: bool = False, compression: Incomplete | None = None, allow_nan: bool = False, conv_str_byte: bool = False, fallback_encoders=(), properties: Incomplete | None = None, **jsonkwargs):
    """
\tConvert a nested data structure to a json string.

\t:param obj: The Python object to convert.
\t:param sort_keys: Keep this False if you want order to be preserved.
\t:param cls: The json encoder class to use, defaults to NoNumpyEncoder which gives a warning for numpy arrays.
\t:param obj_encoders: Iterable of encoders to use to convert arbitrary objects into json-able promitives.
\t:param extra_obj_encoders: Like `obj_encoders` but on top of them: use this to add encoders without replacing defaults. Since v3.5 these happen before default encoders.
\t:param fallback_encoders: These are extra `obj_encoders` that 1) are ran after all others and 2) only run if the object hasn't yet been changed.
\t:param allow_nan: Allow NaN and Infinity values, which is a (useful) violation of the JSON standard (default False).
\t:param conv_str_byte: Try to automatically convert between strings and bytes (assuming utf-8) (default False).
\t:param properties: A dictionary of properties that is passed to each encoder that will accept it.
\t:return: The string containing the json-encoded version of obj.

\tOther arguments are passed on to `cls`. Note that `sort_keys` should be false if you want to preserve order.
\t"""
def dump(obj, fp, sort_keys: Incomplete | None = None, cls: Incomplete | None = None, obj_encoders=..., extra_obj_encoders=(), primitives: bool = False, compression: Incomplete | None = None, force_flush: bool = False, allow_nan: bool = False, conv_str_byte: bool = False, fallback_encoders=(), properties: Incomplete | None = None, **jsonkwargs):
    """
\tConvert a nested data structure to a json string.

\t:param fp: File handle or path to write to.
\t:param compression: The gzip compression level, or None for no compression.
\t:param force_flush: If True, flush the file handle used, when possibly also in the operating system (default False).

\tThe other arguments are identical to `dumps`.
\t"""
def loads(string, preserve_order: bool = True, ignore_comments: Incomplete | None = None, decompression: Incomplete | None = None, obj_pairs_hooks=..., extra_obj_pairs_hooks=(), cls_lookup_map: Incomplete | None = None, allow_duplicates: bool = True, conv_str_byte: bool = False, properties: Incomplete | None = None, **jsonkwargs):
    """
\tConvert a nested data structure to a json string.

\t:param string: The string containing a json encoded data structure.
\t:param decode_cls_instances: True to attempt to decode class instances (requires the environment to be similar the the encoding one).
\t:param preserve_order: Whether to preserve order by using OrderedDicts or not.
\t:param ignore_comments: Remove comments (starting with # or //). By default (`None`), try without comments first, and re-try with comments upon failure.
\t:param decompression: True to use gzip decompression, False to use raw data, None to automatically determine (default). Assumes utf-8 encoding!
\t:param obj_pairs_hooks: A list of dictionary hooks to apply.
\t:param extra_obj_pairs_hooks: Like `obj_pairs_hooks` but on top of them: use this to add hooks without replacing defaults. Since v3.5 these happen before default hooks.
\t:param cls_lookup_map: If set to a dict, for example ``globals()``, then classes encoded from __main__ are looked up this dict.
\t:param allow_duplicates: If set to False, an error will be raised when loading a json-map that contains duplicate keys.
\t:param parse_float: A function to parse strings to integers (e.g. Decimal). There is also `parse_int`.
\t:param conv_str_byte: Try to automatically convert between strings and bytes (assuming utf-8) (default False).
\t:return: The string containing the json-encoded version of obj.

\tOther arguments are passed on to json_func.
\t"""
def load(fp, preserve_order: bool = True, ignore_comments: Incomplete | None = None, decompression: Incomplete | None = None, obj_pairs_hooks=..., extra_obj_pairs_hooks=(), cls_lookup_map: Incomplete | None = None, allow_duplicates: bool = True, conv_str_byte: bool = False, properties: Incomplete | None = None, **jsonkwargs):
    """
\tConvert a nested data structure to a json string.

\t:param fp: File handle or path to load from.

\tThe other arguments are identical to loads.
\t"""
