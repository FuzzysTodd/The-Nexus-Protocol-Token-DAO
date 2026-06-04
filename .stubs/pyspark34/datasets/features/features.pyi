import numpy as np
import pyarrow as pa
from .. import config as config
from ..naming import camelcase_to_snakecase as camelcase_to_snakecase, snakecase_to_camelcase as snakecase_to_camelcase
from ..table import array_cast as array_cast
from ..utils import logging as logging
from ..utils.py_utils import asdict as asdict, first_non_null_value as first_non_null_value, zip_dict as zip_dict
from .audio import Audio as Audio
from .image import Image as Image, encode_pil_image as encode_pil_image
from .translation import Translation as Translation, TranslationVariableLanguages as TranslationVariableLanguages
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import InitVar, dataclass
from pandas.api.extensions import ExtensionArray as PandasExtensionArray, ExtensionDtype as PandasExtensionDtype
from typing import Any, ClassVar, Dict, List, Sequence as Sequence_

logger: Incomplete

def string_to_arrow(datasets_dtype: str) -> pa.DataType:
    """
    string_to_arrow takes a datasets string dtype and converts it to a pyarrow.DataType.

    In effect, `dt == string_to_arrow(_arrow_to_datasets_dtype(dt))`

    This is necessary because the datasets.Value() primitive type is constructed using a string dtype

    Value(dtype=str)

    But Features.type (via `get_nested_type()` expects to resolve Features into a pyarrow Schema,
        which means that each Value() must be able to resolve into a corresponding pyarrow.DataType, which is the
        purpose of this function.
    """
def cast_to_python_objects(obj: Any, only_1d_for_numpy: bool = False, optimize_list_casting: bool = True) -> Any:
    """
    Cast numpy/pytorch/tensorflow/pandas objects to python lists.
    It works recursively.

    If `optimize_list_casting` is True, To avoid iterating over possibly long lists, it first checks (recursively) if the first element that is not None or empty (if it is a sequence) has to be casted.
    If the first element needs to be casted, then all the elements of the list will be casted, otherwise they'll stay the same.
    This trick allows to cast objects that contain tokenizers outputs without iterating over every single token for example.

    Args:
        obj: the object (nested struct) to cast
        only_1d_for_numpy (bool, default ``False``): whether to keep the full multi-dim tensors as multi-dim numpy arrays, or convert them to
            nested lists of 1-dimensional numpy arrays. This can be useful to keep only 1-d arrays to instantiate Arrow arrays.
            Indeed Arrow only support converting 1-dimensional array values.
        optimize_list_casting (bool, default ``True``): whether to optimize list casting by checking the first non-null element to see if it needs to be casted
            and if it doesn't, not checking the rest of the list elements.

    Returns:
        casted_obj: the casted object
    """

@dataclass
class Value:
    """
    The `Value` dtypes are as follows:

    - `null`
    - `bool`
    - `int8`
    - `int16`
    - `int32`
    - `int64`
    - `uint8`
    - `uint16`
    - `uint32`
    - `uint64`
    - `float16`
    - `float32` (alias float)
    - `float64` (alias double)
    - `time32[(s|ms)]`
    - `time64[(us|ns)]`
    - `timestamp[(s|ms|us|ns)]`
    - `timestamp[(s|ms|us|ns), tz=(tzstring)]`
    - `date32`
    - `date64`
    - `duration[(s|ms|us|ns)]`
    - `decimal128(precision, scale)`
    - `decimal256(precision, scale)`
    - `binary`
    - `large_binary`
    - `string`
    - `large_string`

    Example:

    ```py
    >>> from datasets import Features
    >>> features = Features({'stars': Value(dtype='int32')})
    >>> features
    {'stars': Value(dtype='int32', id=None)}
    ```
    """
    dtype: str
    id: str | None = ...
    pa_type: ClassVar[Any] = ...
    def __post_init__(self) -> None: ...
    def __call__(self): ...
    def encode_example(self, value): ...
    def __init__(self, dtype, id) -> None: ...

class _ArrayXD:
    shape: Incomplete
    def __post_init__(self) -> None: ...
    def __call__(self): ...
    def encode_example(self, value): ...

@dataclass
class Array2D(_ArrayXD):
    """Create a two-dimensional array.

    Args:
        shape (`tuple`):
            The size of each dimension.
        dtype (`str`):
            The value of the data type.

    Example:

    ```py
    >>> from datasets import Features
    >>> features = Features({'x': Array2D(shape=(1, 3), dtype='int32')})
    ```
    """
    shape: tuple
    dtype: str
    id: str | None = ...
    def __init__(self, shape, dtype, id) -> None: ...

@dataclass
class Array3D(_ArrayXD):
    """Create a three-dimensional array.

    Args:
        shape (`tuple`):
            The size of each dimension.
        dtype (`str`):
            The value of the data type.

    Example:

    ```py
    >>> from datasets import Features
    >>> features = Features({'x': Array3D(shape=(1, 2, 3), dtype='int32')})
    ```
    """
    shape: tuple
    dtype: str
    id: str | None = ...
    def __init__(self, shape, dtype, id) -> None: ...

@dataclass
class Array4D(_ArrayXD):
    """Create a four-dimensional array.

    Args:
        shape (`tuple`):
            The size of each dimension.
        dtype (`str`):
            The value of the data type.

    Example:

    ```py
    >>> from datasets import Features
    >>> features = Features({'x': Array4D(shape=(1, 2, 2, 3), dtype='int32')})
    ```
    """
    shape: tuple
    dtype: str
    id: str | None = ...
    def __init__(self, shape, dtype, id) -> None: ...

@dataclass
class Array5D(_ArrayXD):
    """Create a five-dimensional array.

    Args:
        shape (`tuple`):
            The size of each dimension.
        dtype (`str`):
            The value of the data type.

    Example:

    ```py
    >>> from datasets import Features
    >>> features = Features({'x': Array5D(shape=(1, 2, 2, 3, 3), dtype='int32')})
    ```
    """
    shape: tuple
    dtype: str
    id: str | None = ...
    def __init__(self, shape, dtype, id) -> None: ...

class _ArrayXDExtensionType(pa.PyExtensionType):
    ndims: int | None
    shape: Incomplete
    value_type: Incomplete
    storage_dtype: Incomplete
    def __init__(self, shape: tuple, dtype: str) -> None: ...
    def __reduce__(self): ...
    def __hash__(self): ...
    def __arrow_ext_class__(self): ...
    def to_pandas_dtype(self): ...

class Array2DExtensionType(_ArrayXDExtensionType):
    ndims: int

class Array3DExtensionType(_ArrayXDExtensionType):
    ndims: int

class Array4DExtensionType(_ArrayXDExtensionType):
    ndims: int

class Array5DExtensionType(_ArrayXDExtensionType):
    ndims: int

class ArrayExtensionArray(pa.ExtensionArray):
    def __array__(self): ...
    def __getitem__(self, i): ...
    def to_numpy(self, zero_copy_only: bool = True): ...
    def to_pylist(self): ...

class PandasArrayExtensionDtype(PandasExtensionDtype):
    def __init__(self, value_type: PandasArrayExtensionDtype | np.dtype) -> None: ...
    def __from_arrow__(self, array: pa.Array | pa.ChunkedArray): ...
    @classmethod
    def construct_array_type(cls): ...
    @property
    def type(self) -> type: ...
    @property
    def kind(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value_type(self) -> np.dtype: ...

class PandasArrayExtensionArray(PandasExtensionArray):
    def __init__(self, data: np.ndarray, copy: bool = False) -> None: ...
    def __array__(self, dtype: Incomplete | None = None):
        """
        Convert to NumPy Array.
        Note that Pandas expects a 1D array when dtype is set to object.
        But for other dtypes, the returned shape is the same as the one of ``data``.

        More info about pandas 1D requirement for PandasExtensionArray here:
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray

        """
    def copy(self, deep: bool = False) -> PandasArrayExtensionArray: ...
    @property
    def dtype(self) -> PandasArrayExtensionDtype: ...
    @property
    def nbytes(self) -> int: ...
    def isna(self) -> np.ndarray: ...
    def __setitem__(self, key: int | slice | np.ndarray, value: Any) -> None: ...
    def __getitem__(self, item: int | slice | np.ndarray) -> np.ndarray | PandasArrayExtensionArray: ...
    def take(self, indices: Sequence_[int], allow_fill: bool = False, fill_value: bool = None) -> PandasArrayExtensionArray: ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> np.ndarray: ...

def pandas_types_mapper(dtype): ...

@dataclass
class ClassLabel:
    """Feature type for integer class labels.

    There are 3 ways to define a `ClassLabel`, which correspond to the 3 arguments:

     * `num_classes`: Create 0 to (num_classes-1) labels.
     * `names`: List of label strings.
     * `names_file`: File containing the list of labels.

    Under the hood the labels are stored as integers.
    You can use negative integers to represent unknown/missing labels.

    Args:
        num_classes (`int`, *optional*):
            Number of classes. All labels must be < `num_classes`.
        names (`list` of `str`, *optional*):
            String names for the integer classes.
            The order in which the names are provided is kept.
        names_file (`str`, *optional*):
            Path to a file with names for the integer classes, one per line.

    Example:

    ```py
    >>> from datasets import Features
    >>> features = Features({'label': ClassLabel(num_classes=3, names=['bad', 'ok', 'good'])})
    >>> features
    {'label': ClassLabel(num_classes=3, names=['bad', 'ok', 'good'], id=None)}
    ```
    """
    num_classes: InitVar[int | None] = ...
    names: List[str] = ...
    names_file: InitVar[str | None] = ...
    id: str | None = ...
    dtype: ClassVar[str] = ...
    pa_type: ClassVar[Any] = ...
    def __post_init__(self, num_classes, names_file) -> None: ...
    def __call__(self): ...
    def str2int(self, values: str | Iterable) -> int | Iterable:
        '''Conversion class name `string` => `integer`.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train")
        >>> ds.features["label"].str2int(\'neg\')
        0
        ```
        '''
    def int2str(self, values: int | Iterable) -> str | Iterable:
        '''Conversion `integer` => class name `string`.

        Regarding unknown/missing labels: passing negative integers raises `ValueError`.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train")
        >>> ds.features["label"].int2str(0)
        \'neg\'
        ```
        '''
    def encode_example(self, example_data): ...
    def cast_storage(self, storage: pa.StringArray | pa.IntegerArray) -> pa.Int64Array:
        """Cast an Arrow array to the `ClassLabel` arrow storage type.
        The Arrow types that can be converted to the `ClassLabel` pyarrow storage type are:

        - `pa.string()`
        - `pa.int()`

        Args:
            storage (`Union[pa.StringArray, pa.IntegerArray]`):
                PyArrow array to cast.

        Returns:
            `pa.Int64Array`: Array in the `ClassLabel` arrow storage type.
        """
    def __init__(self, names, id) -> None: ...

@dataclass
class Sequence:
    """Construct a list of feature from a single type or a dict of types.
    Mostly here for compatiblity with tfds.

    Args:
        feature:
            A list of features of a single type or a dictionary of types.
        length (`int`):
            Length of the sequence.

    Example:

    ```py
    >>> from datasets import Features, Sequence, Value, ClassLabel
    >>> features = Features({'post': Sequence(feature={'text': Value(dtype='string'), 'upvotes': Value(dtype='int32'), 'label': ClassLabel(num_classes=2, names=['hot', 'cold'])})})
    >>> features
    {'post': Sequence(feature={'text': Value(dtype='string', id=None), 'upvotes': Value(dtype='int32', id=None), 'label': ClassLabel(num_classes=2, names=['hot', 'cold'], id=None)}, length=-1, id=None)}
    ```
    """
    feature: Any
    length: int = ...
    id: str | None = ...
    dtype: ClassVar[str] = ...
    pa_type: ClassVar[Any] = ...
    def __init__(self, feature, length, id) -> None: ...
FeatureType = dict | list | tuple | Value | ClassLabel | Translation | TranslationVariableLanguages | Sequence | Array2D | Array3D | Array4D | Array5D | Audio | Image

def get_nested_type(schema: FeatureType) -> pa.DataType:
    """
    get_nested_type() converts a datasets.FeatureType into a pyarrow.DataType, and acts as the inverse of
        generate_from_arrow_type().

    It performs double-duty as the implementation of Features.type and handles the conversion of
        datasets.Feature->pa.struct
    """
def encode_nested_example(schema, obj, level: int = 0):
    """Encode a nested example.
    This is used since some features (in particular ClassLabel) have some logic during encoding.

    To avoid iterating over possibly long lists, it first checks (recursively) if the first element that is not None or empty (if it is a sequence) has to be encoded.
    If the first element needs to be encoded, then all the elements of the list will be encoded, otherwise they'll stay the same.
    """
def decode_nested_example(schema, obj, token_per_repo_id: Dict[str, str | bool | None] | None = None):
    """Decode a nested example.
    This is used since some features (in particular Audio and Image) have some logic during decoding.

    To avoid iterating over possibly long lists, it first checks (recursively) if the first element that is not None or empty (if it is a sequence) has to be decoded.
    If the first element needs to be decoded, then all the elements of the list will be decoded, otherwise they'll stay the same.
    """
def generate_from_dict(obj: Any):
    """Regenerate the nested feature object from a deserialized dict.
    We use the '_type' fields to get the dataclass name to load.

    generate_from_dict is the recursive helper for Features.from_dict, and allows for a convenient constructor syntax
    to define features from deserialized JSON dictionaries. This function is used in particular when deserializing
    a :class:`DatasetInfo` that was dumped to a JSON object. This acts as an analogue to
    :meth:`Features.from_arrow_schema` and handles the recursive field-by-field instantiation, but doesn't require any
    mapping to/from pyarrow, except for the fact that it takes advantage of the mapping of pyarrow primitive dtypes
    that :class:`Value` automatically performs.
    """
def generate_from_arrow_type(pa_type: pa.DataType) -> FeatureType:
    """
    generate_from_arrow_type accepts an arrow DataType and returns a datasets FeatureType to be used as the type for
        a single field.

    This is the high-level arrow->datasets type conversion and is inverted by get_nested_type().

    This operates at the individual *field* level, whereas Features.from_arrow_schema() operates at the
        full schema level and holds the methods that represent the bijection from Features<->pyarrow.Schema
    """
def numpy_to_pyarrow_listarray(arr: np.ndarray, type: pa.DataType = None) -> pa.ListArray:
    """Build a PyArrow ListArray from a multidimensional NumPy array"""
def list_of_pa_arrays_to_pyarrow_listarray(l_arr: List[pa.Array | None]) -> pa.ListArray: ...
def list_of_np_array_to_pyarrow_listarray(l_arr: List[np.ndarray], type: pa.DataType = None) -> pa.ListArray:
    """Build a PyArrow ListArray from a possibly nested list of NumPy arrays"""
def contains_any_np_array(data: Any):
    """Return `True` if data is a NumPy ndarray or (recursively) if first non-null value in list is a NumPy ndarray.

    Args:
        data (Any): Data.

    Returns:
        bool
    """
def any_np_array_to_pyarrow_listarray(data: np.ndarray | List, type: pa.DataType = None) -> pa.ListArray:
    """Convert to PyArrow ListArray either a NumPy ndarray or (recursively) a list that may contain any NumPy ndarray.

    Args:
        data (Union[np.ndarray, List]): Data.
        type (pa.DataType): Explicit PyArrow DataType passed to coerce the ListArray data type.

    Returns:
        pa.ListArray
    """
def to_pyarrow_listarray(data: Any, pa_type: _ArrayXDExtensionType) -> pa.Array:
    """Convert to PyArrow ListArray.

    Args:
        data (Any): Sequence, iterable, np.ndarray or pd.Series.
        pa_type (_ArrayXDExtensionType): Any of the ArrayNDExtensionType.

    Returns:
        pyarrow.Array
    """
def require_decoding(feature: FeatureType, ignore_decode_attribute: bool = False) -> bool:
    """Check if a (possibly nested) feature requires decoding.

    Args:
        feature (FeatureType): the feature type to be checked
        ignore_decode_attribute (:obj:`bool`, default ``False``): Whether to ignore the current value
            of the `decode` attribute of the decodable feature types.
    Returns:
        :obj:`bool`
    """
def require_storage_cast(feature: FeatureType) -> bool:
    """Check if a (possibly nested) feature requires storage casting.

    Args:
        feature (FeatureType): the feature type to be checked
    Returns:
        :obj:`bool`
    """
def require_storage_embed(feature: FeatureType) -> bool:
    """Check if a (possibly nested) feature requires embedding data into storage.

    Args:
        feature (FeatureType): the feature type to be checked
    Returns:
        :obj:`bool`
    """
def keep_features_dicts_synced(func):
    """
    Wrapper to keep the secondary dictionary, which tracks whether keys are decodable, of the :class:`datasets.Features` object
    in sync with the main dictionary.
    """

class Features(dict):
    '''A special dictionary that defines the internal structure of a dataset.

    Instantiated with a dictionary of type `dict[str, FieldType]`, where keys are the desired column names,
    and values are the type of that column.

    `FieldType` can be one of the following:
        - a [`~datasets.Value`] feature specifies a single typed value, e.g. `int64` or `string`.
        - a [`~datasets.ClassLabel`] feature specifies a field with a predefined set of classes which can have labels
          associated to them and will be stored as integers in the dataset.
        - a python `dict` which specifies that the field is a nested field containing a mapping of sub-fields to sub-fields
          features. It\'s possible to have nested fields of nested fields in an arbitrary manner.
        - a python `list` or a [`~datasets.Sequence`] specifies that the field contains a list of objects. The python
          `list` or [`~datasets.Sequence`] should be provided with a single sub-feature as an example of the feature
          type hosted in this list.

          <Tip>

           A [`~datasets.Sequence`] with a internal dictionary feature will be automatically converted into a dictionary of
           lists. This behavior is implemented to have a compatilbity layer with the TensorFlow Datasets library but may be
           un-wanted in some cases. If you don\'t want this behavior, you can use a python `list` instead of the
           [`~datasets.Sequence`].

          </Tip>

        - a [`Array2D`], [`Array3D`], [`Array4D`] or [`Array5D`] feature for multidimensional arrays.
        - an [`Audio`] feature to store the absolute path to an audio file or a dictionary with the relative path
          to an audio file ("path" key) and its bytes content ("bytes" key). This feature extracts the audio data.
        - an [`Image`] feature to store the absolute path to an image file, an `np.ndarray` object, a `PIL.Image.Image` object
          or a dictionary with the relative path to an image file ("path" key) and its bytes content ("bytes" key). This feature extracts the image data.
        - [`~datasets.Translation`] and [`~datasets.TranslationVariableLanguages`], the two features specific to Machine Translation.
    '''
    def __init__(*args, **kwargs) -> None: ...
    __setitem__: Incomplete
    __delitem__: Incomplete
    update: Incomplete
    setdefault: Incomplete
    pop: Incomplete
    popitem: Incomplete
    clear: Incomplete
    def __reduce__(self): ...
    @property
    def type(self):
        """
        Features field types.

        Returns:
            :obj:`pyarrow.DataType`
        """
    @property
    def arrow_schema(self):
        """
        Features schema.

        Returns:
            :obj:`pyarrow.Schema`
        """
    @classmethod
    def from_arrow_schema(cls, pa_schema: pa.Schema) -> Features:
        """
        Construct [`Features`] from Arrow Schema.
        It also checks the schema metadata for Hugging Face Datasets features.
        Non-nullable fields are not supported and set to nullable.

        Args:
            pa_schema (`pyarrow.Schema`):
                Arrow Schema.

        Returns:
            [`Features`]
        """
    @classmethod
    def from_dict(cls, dic) -> Features:
        """
        Construct [`Features`] from dict.

        Regenerate the nested feature object from a deserialized dict.
        We use the `_type` key to infer the dataclass name of the feature `FieldType`.

        It allows for a convenient constructor syntax
        to define features from deserialized JSON dictionaries. This function is used in particular when deserializing
        a [`DatasetInfo`] that was dumped to a JSON object. This acts as an analogue to
        [`Features.from_arrow_schema`] and handles the recursive field-by-field instantiation, but doesn't require
        any mapping to/from pyarrow, except for the fact that it takes advantage of the mapping of pyarrow primitive
        dtypes that [`Value`] automatically performs.

        Args:
            dic (`dict[str, Any]`):
                Python dictionary.

        Returns:
            `Features`

        Example::
            >>> Features.from_dict({'_type': {'dtype': 'string', 'id': None, '_type': 'Value'}})
            {'_type': Value(dtype='string', id=None)}
        """
    def to_dict(self): ...
    def encode_example(self, example):
        """
        Encode example into a format for Arrow.

        Args:
            example (`dict[str, Any]`):
                Data in a Dataset row.

        Returns:
            `dict[str, Any]`
        """
    def encode_column(self, column, column_name: str):
        """
        Encode column into a format for Arrow.

        Args:
            column (`list[Any]`):
                Data in a Dataset column.
            column_name (`str`):
                Dataset column name.

        Returns:
            `list[Any]`
        """
    def encode_batch(self, batch):
        """
        Encode batch into a format for Arrow.

        Args:
            batch (`dict[str, list[Any]]`):
                Data in a Dataset batch.

        Returns:
            `dict[str, list[Any]]`
        """
    def decode_example(self, example: dict, token_per_repo_id: Dict[str, str | bool | None] | None = None):
        """Decode example with custom feature decoding.

        Args:
            example (`dict[str, Any]`):
                Dataset row data.
            token_per_repo_id (`dict`, *optional*):
                To access and decode audio or image files from private repositories on the Hub, you can pass
                a dictionary `repo_id (str) -> token (bool or str)`.

        Returns:
            `dict[str, Any]`
        """
    def decode_column(self, column: list, column_name: str):
        """Decode column with custom feature decoding.

        Args:
            column (`list[Any]`):
                Dataset column data.
            column_name (`str`):
                Dataset column name.

        Returns:
            `list[Any]`
        """
    def decode_batch(self, batch: dict, token_per_repo_id: Dict[str, str | bool | None] | None = None):
        """Decode batch with custom feature decoding.

        Args:
            batch (`dict[str, list[Any]]`):
                Dataset batch data.
            token_per_repo_id (`dict`, *optional*):
                To access and decode audio or image files from private repositories on the Hub, you can pass
                a dictionary repo_id (str) -> token (bool or str)

        Returns:
            `dict[str, list[Any]]`
        """
    def copy(self) -> Features:
        '''
        Make a deep copy of [`Features`].

        Returns:
            [`Features`]

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("rotten_tomatoes", split="train")
        >>> copy_of_features = ds.features.copy()
        >>> copy_of_features
        {\'label\': ClassLabel(num_classes=2, names=[\'neg\', \'pos\'], id=None),
         \'text\': Value(dtype=\'string\', id=None)}
        ```
        '''
    def reorder_fields_as(self, other: Features) -> Features:
        '''
        Reorder Features fields to match the field order of other [`Features`].

        The order of the fields is important since it matters for the underlying arrow data.
        Re-ordering the fields allows to make the underlying arrow data type match.

        Args:
            other ([`Features`]):
                The other [`Features`] to align with.

        Returns:
            [`Features`]

        Example::

            >>> from datasets import Features, Sequence, Value
            >>> # let\'s say we have to features with a different order of nested fields (for a and b for example)
            >>> f1 = Features({"root": Sequence({"a": Value("string"), "b": Value("string")})})
            >>> f2 = Features({"root": {"b": Sequence(Value("string")), "a": Sequence(Value("string"))}})
            >>> assert f1.type != f2.type
            >>> # re-ordering keeps the base structure (here Sequence is defined at the root level), but make the fields order match
            >>> f1.reorder_fields_as(f2)
            {\'root\': Sequence(feature={\'b\': Value(dtype=\'string\', id=None), \'a\': Value(dtype=\'string\', id=None)}, length=-1, id=None)}
            >>> assert f1.reorder_fields_as(f2).type == f2.type
        '''
    def flatten(self, max_depth: int = 16) -> Features:
        '''Flatten the features. Every dictionary column is removed and is replaced by
        all the subfields it contains. The new fields are named by concatenating the
        name of the original column and the subfield name like this: `<original>.<subfield>`.

        If a column contains nested dictionaries, then all the lower-level subfields names are
        also concatenated to form new columns: `<original>.<subfield>.<subsubfield>`, etc.

        Returns:
            [`Features`]:
                The flattened features.

        Example:

        ```py
        >>> from datasets import load_dataset
        >>> ds = load_dataset("squad", split="train")
        >>> ds.features.flatten()
        {\'answers.answer_start\': Sequence(feature=Value(dtype=\'int32\', id=None), length=-1, id=None),
         \'answers.text\': Sequence(feature=Value(dtype=\'string\', id=None), length=-1, id=None),
         \'context\': Value(dtype=\'string\', id=None),
         \'id\': Value(dtype=\'string\', id=None),
         \'question\': Value(dtype=\'string\', id=None),
         \'title\': Value(dtype=\'string\', id=None)}
        ```
        '''
