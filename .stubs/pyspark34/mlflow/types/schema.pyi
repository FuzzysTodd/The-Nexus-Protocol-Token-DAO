import numpy as np
from _typeshed import Incomplete
from enum import Enum
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.utils.annotations import experimental as experimental
from typing import Any, Dict, List, Tuple, TypedDict

class DataType(Enum):
    """
    MLflow data types.
    """
    def __new__(cls, value, numpy_type, spark_type, pandas_type: Incomplete | None = None, python_type: Incomplete | None = None): ...
    boolean: Incomplete
    integer: Incomplete
    long: Incomplete
    float: Incomplete
    double: Incomplete
    string: Incomplete
    binary: Incomplete
    datetime: Incomplete
    def to_numpy(self) -> np.dtype:
        """Get equivalent numpy data type."""
    def to_pandas(self) -> np.dtype:
        """Get equivalent pandas data type."""
    def to_spark(self): ...
    def to_python(self):
        """Get equivalent python data type."""
    @classmethod
    def is_boolean(cls, value): ...
    @classmethod
    def is_integer(cls, value): ...
    @classmethod
    def is_long(cls, value): ...
    @classmethod
    def is_float(cls, value): ...
    @classmethod
    def is_double(cls, value): ...
    @classmethod
    def is_string(cls, value): ...
    @classmethod
    def is_binary(cls, value): ...
    @classmethod
    def is_datetime(cls, value): ...
    def get_all_types(self): ...
    @classmethod
    def get_spark_types(cls): ...
    @classmethod
    def from_numpy_type(cls, np_type): ...

class ColSpec:
    """
    Specification of name and type of a single column in a dataset.
    """
    def __init__(self, type: DataType | str, name: str | None = None, optional: bool = False) -> None: ...
    @property
    def type(self) -> DataType:
        """The column data type."""
    @property
    def name(self) -> str | None:
        """The column name or None if the columns is unnamed."""
    @property
    def optional(self) -> bool:
        """Whether this column is optional."""
    def to_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other) -> bool: ...

class TensorInfo:
    """
    Representation of the shape and type of a Tensor.
    """
    def __init__(self, dtype: np.dtype, shape: tuple | list) -> None: ...
    @property
    def dtype(self) -> np.dtype:
        """
        A unique character code for each of the 21 different numpy built-in types.
        See https://numpy.org/devdocs/reference/generated/numpy.dtype.html#numpy.dtype for details.
        """
    @property
    def shape(self) -> tuple:
        """The tensor shape"""
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_json_dict(cls, **kwargs):
        """
        Deserialize from a json loaded dictionary.
        The dictionary is expected to contain `dtype` and `shape` keys.
        """

class TensorSpec:
    """
    Specification used to represent a dataset stored as a Tensor.
    """
    def __init__(self, type: np.dtype, shape: tuple | list, name: str | None = None) -> None: ...
    @property
    def type(self) -> np.dtype:
        """
        A unique character code for each of the 21 different numpy built-in types.
        See https://numpy.org/devdocs/reference/generated/numpy.dtype.html#numpy.dtype for details.
        """
    @property
    def name(self) -> str | None:
        """The tensor name or None if the tensor is unnamed."""
    @property
    def shape(self) -> tuple:
        """The tensor shape"""
    @property
    def optional(self) -> bool:
        """Whether this tensor is optional."""
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_json_dict(cls, **kwargs):
        """
        Deserialize from a json loaded dictionary.
        The dictionary is expected to contain `type` and `tensor-spec` keys.
        """
    def __eq__(self, other) -> bool: ...

class Schema:
    """
    Specification of a dataset.

    Schema is represented as a list of :py:class:`ColSpec` or :py:class:`TensorSpec`. A combination
    of `ColSpec` and `TensorSpec` is not allowed.

    The dataset represented by a schema can be named, with unique non empty names for every input.
    In the case of :py:class:`ColSpec`, the dataset columns can be unnamed with implicit integer
    index defined by their list indices.
    Combination of named and unnamed data inputs are not allowed.
    """
    def __init__(self, inputs: List[ColSpec | TensorSpec]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def inputs(self) -> List[ColSpec | TensorSpec]:
        """Representation of a dataset that defines this schema."""
    def is_tensor_spec(self) -> bool:
        """Return true iff this schema is specified using TensorSpec"""
    def input_names(self) -> List[str | int]:
        """Get list of data names or range of indices if the schema has no names."""
    def required_input_names(self) -> List[str | int]:
        """Get list of required data names or range of indices if schema has no names."""
    def optional_input_names(self) -> List[str | int]:
        """Get list of optional data names or range of indices if schema has no names."""
    def has_input_names(self) -> bool:
        """Return true iff this schema declares names, false otherwise."""
    def input_types(self) -> List[DataType | np.dtype]:
        """Get types for each column in the schema."""
    def input_types_dict(self) -> Dict[str, DataType | np.dtype]:
        """Maps column names to types, iff this schema declares names."""
    def numpy_types(self) -> List[np.dtype]:
        """Convenience shortcut to get the datatypes as numpy types."""
    def pandas_types(self) -> List[np.dtype]:
        """Convenience shortcut to get the datatypes as pandas types. Unsupported by TensorSpec."""
    def as_spark_schema(self):
        """Convert to Spark schema. If this schema is a single unnamed column, it is converted
        directly the corresponding spark data type, otherwise it's returned as a struct (missing
        column names are filled with an integer sequence).
        Unsupported by TensorSpec.
        """
    def to_json(self) -> str:
        """Serialize into json string."""
    def to_dict(self) -> List[Dict[str, Any]]:
        """Serialize into a jsonable dictionary."""
    @classmethod
    def from_json(cls, json_str: str):
        """Deserialize from a json string."""
    def __eq__(self, other) -> bool: ...

class ParamSpec:
    """
    Specification used to represent parameters for the model.
    """
    def __init__(self, name: str, dtype: DataType | str, default: DataType | List[DataType] | None, shape: Tuple[int, ...] | None = None) -> None: ...
    @classmethod
    def validate_param_spec(cls, value: DataType | List[DataType] | None, param_spec: ParamSpec): ...
    @classmethod
    def enforce_param_datatype(cls, name, value, dtype: DataType):
        """
        Enforce the value matches the data type.

        The following type conversions are allowed:

        1. int -> long, float, double
        2. long -> float, double
        3. float -> double
        4. any -> datetime (try conversion)

        Any other type mismatch will raise error.

        :param name: parameter name
        :param value: parameter value
        :param t: expected data type
        """
    @classmethod
    def validate_type_and_shape(cls, spec: str, value: DataType | List[DataType] | None, value_type: DataType, shape: Tuple[int, ...] | None):
        """
        Validate that the value has the expected type and shape.
        """
    @property
    def name(self) -> str:
        """The name of the parameter."""
    @property
    def dtype(self) -> DataType:
        """The parameter data type."""
    @property
    def default(self) -> DataType | List[DataType] | None:
        """Default value of the parameter."""
    @property
    def shape(self) -> tuple | None:
        """
        The parameter shape.
        If shape is None, the parameter is a scalar.
        """
    class ParamSpecTypedDict(TypedDict):
        name: str
        dtype: str
        default: DataType | List[DataType] | None
        shape: Tuple[int, ...] | None
    def to_dict(self) -> ParamSpecTypedDict: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def from_json_dict(cls, **kwargs):
        """
        Deserialize from a json loaded dictionary.
        The dictionary is expected to contain `name`, `dtype` and `default` keys.
        """

class ParamSchema:
    """
    Specification of parameters applicable to the model.
    ParamSchema is represented as a list of :py:class:`ParamSpec`.
    """
    def __init__(self, params: List[ParamSpec]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def params(self) -> List[ParamSpec]:
        """Representation of ParamSchema as a list of ParamSpec."""
    def to_json(self) -> str:
        """Serialize into json string."""
    @classmethod
    def from_json(cls, json_str: str):
        """Deserialize from a json string."""
    def to_dict(self) -> List[Dict[str, Any]]:
        """Serialize into a jsonable dictionary."""
    def __eq__(self, other) -> bool: ...
