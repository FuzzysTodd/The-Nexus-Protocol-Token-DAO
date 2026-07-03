from ._version import VERSION
from .comment import strip_comment_line_with_symbol as strip_comment_line_with_symbol, strip_comments as strip_comments
from .decoders import ClassInstanceHook as ClassInstanceHook, DuplicateJsonKeyException as DuplicateJsonKeyException, TricksPairHook as TricksPairHook, json_bytes_hook as json_bytes_hook, json_complex_hook as json_complex_hook, json_date_time_hook as json_date_time_hook, json_nonumpy_obj_hook as json_nonumpy_obj_hook, json_numpy_obj_hook as json_numpy_obj_hook, json_set_hook as json_set_hook, nopandas_hook as nopandas_hook, numeric_types_hook as numeric_types_hook, pandas_hook as pandas_hook, pathlib_hook as pathlib_hook
from .encoders import ClassInstanceEncoder as ClassInstanceEncoder, NoNumpyEncoder as NoNumpyEncoder, NumpyEncoder as NumpyEncoder, TricksEncoder as TricksEncoder, bytes_encode as bytes_encode, class_instance_encode as class_instance_encode, fallback_ignore_unknown as fallback_ignore_unknown, json_complex_encode as json_complex_encode, json_date_time_encode as json_date_time_encode, json_set_encode as json_set_encode, nonumpy_encode as nonumpy_encode, nopandas_encode as nopandas_encode, numeric_types_encode as numeric_types_encode, numpy_encode as numpy_encode, pandas_encode as pandas_encode, pathlib_encode as pathlib_encode, slice_encode as slice_encode
from .nonp import dump as dump, dumps as dumps, load as load, loads as loads
from .utils import NoEnumException as NoEnumException, NoNumpyException as NoNumpyException, NoPandasException as NoPandasException, encode_intenums_inplace as encode_intenums_inplace, encode_scalars_inplace as encode_scalars_inplace, get_scalar_repr as get_scalar_repr, hashodict as hashodict
from json import JSONDecodeError as JSONDecodeError

__version__ = VERSION
NUMPY_MODE: bool
