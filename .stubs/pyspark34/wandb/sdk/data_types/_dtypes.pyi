import typing as t
from _typeshed import Incomplete
from wandb.sdk.artifacts.artifact import Artifact

__all__ = ['TypeRegistry', 'InvalidType', 'UnknownType', 'AnyType', 'NoneType', 'StringType', 'NumberType', 'TimestampType', 'BooleanType', 'ListType', 'TypedDictType', 'UnionType', 'PythonObjectType', 'ConstType', 'OptionalType', 'Type', 'NDArrayType']

class TypeRegistry:
    """A resolver for python objects that can deserialize JSON dicts.

    Additional types can be registered via the .add call.
    """
    @staticmethod
    def types_by_name(): ...
    @staticmethod
    def types_by_class(): ...
    @staticmethod
    def add(wb_type: t.Type['Type']) -> None: ...
    @staticmethod
    def type_of(py_obj: t.Any | None) -> Type: ...
    @staticmethod
    def type_from_dict(json_dict: t.Dict[str, t.Any], artifact: Artifact | None = None) -> Type: ...
    @staticmethod
    def type_from_dtype(dtype: ConvertableToType) -> Type: ...

class Type:
    """The most generic type that all types subclass.

    It provides simple serialization and deserialization as well as equality checks.
    A name class-level property must be uniquely set by subclasses.
    """
    name: t.ClassVar[str]
    legacy_names: t.ClassVar[t.List[str]]
    types: t.ClassVar[t.List[type]]
    def __init__(*args, **kwargs) -> None: ...
    @property
    def params(self): ...
    def assign(self, py_obj: t.Any | None = None) -> Type:
        """Assign a python object to the type.

        May to be overridden by subclasses

        Args:
            py_obj (any, optional): Any python object which the user wishes to assign to
            this type

        Returns:
            Type: a new type representing the result of the assignment.
        """
    def assign_type(self, wb_type: Type) -> Type: ...
    def to_json(self, artifact: Artifact | None = None) -> t.Dict[str, t.Any]:
        """Generate a jsonable dictionary serialization the type.

        If overridden by subclass, ensure that `from_json` is equivalently overridden.

        Args:
            artifact (wandb.Artifact, optional): If the serialization is being performed
            for a particular artifact, pass that artifact. Defaults to None.

        Returns:
            dict: Representation of the type
        """
    @classmethod
    def from_json(cls, json_dict: t.Dict[str, t.Any], artifact: Artifact | None = None) -> Type:
        """Construct a new instance of the type using a JSON dictionary.

        The mirror function of `to_json`. If overridden by subclass, ensure that
        `to_json` is equivalently overridden.

        Returns:
            _Type: an instance of a subclass of the _Type class.
        """
    @classmethod
    def from_obj(cls, py_obj: t.Any | None = None) -> Type: ...
    def explain(self, other: t.Any, depth: int = 0) -> str:
        """Explain why an item is not assignable to a type.

        Assumes that the caller has already validated that the assignment fails.

        Args:
            other (any): Any object depth (int, optional): depth of the type checking.
                Defaults to 0.

        Returns:
            str: human-readable explanation
        """
    def __eq__(self, other): ...

class InvalidType(Type):
    """A disallowed type.

    Assignments to a InvalidType result in a Never Type. InvalidType is basically the
    invalid case.
    """
    name: str
    types: t.ClassVar[t.List[type]]
    def assign_type(self, wb_type: Type) -> InvalidType: ...

class AnyType(Type):
    """An object that can be any type.

    Assignments to an AnyType result in the AnyType except None which results in an
    InvalidType.
    """
    name: str
    types: t.ClassVar[t.List[type]]
    def assign_type(self, wb_type: Type) -> AnyType | InvalidType: ...

class UnknownType(Type):
    """An object with an unknown type.

    All assignments to an UnknownType result in the type of the assigned object except
    `None` which results in a InvalidType.
    """
    name: str
    types: t.ClassVar[t.List[type]]
    def assign_type(self, wb_type: Type) -> Type: ...

class NoneType(Type):
    name: str
    types: t.ClassVar[t.List[type]]

class StringType(Type):
    name: str
    types: t.ClassVar[t.List[type]]

class NumberType(Type):
    name: str
    types: t.ClassVar[t.List[type]]

class TimestampType(Type):
    name: str
    types: t.ClassVar[t.List[type]]

class BooleanType(Type):
    name: str
    types: t.ClassVar[t.List[type]]

class PythonObjectType(Type):
    """A backup type that keeps track of the python object name."""
    name: str
    legacy_names: Incomplete
    types: t.ClassVar[t.List[type]]
    def __init__(self, class_name: str) -> None: ...
    @classmethod
    def from_obj(cls, py_obj: t.Any | None = None) -> PythonObjectType: ...

class ConstType(Type):
    """A constant value (currently only primitives supported)."""
    name: str
    types: t.ClassVar[t.List[type]]
    def __init__(self, val: t.Any | None = None, is_set: bool | None = False) -> None: ...
    def assign(self, py_obj: t.Any | None = None) -> Type: ...
    @classmethod
    def from_obj(cls, py_obj: t.Any | None = None) -> ConstType: ...

class UnionType(Type):
    '''An "or" of types.'''
    name: str
    types: t.ClassVar[t.List[type]]
    def __init__(self, allowed_types: t.Sequence[ConvertableToType] | None = None) -> None: ...
    def assign(self, py_obj: t.Any | None = None) -> UnionType | InvalidType: ...
    def assign_type(self, wb_type: Type) -> UnionType | InvalidType: ...
    def explain(self, other: t.Any, depth: int = 0) -> str: ...

def OptionalType(dtype: ConvertableToType) -> UnionType:
    '''Function that mimics the Type class API for constructing an "Optional Type".

    This is just a Union[wb_type, NoneType].

    Args:
        dtype (Type): type to be optional

    Returns:
        Type: Optional version of the type.
    '''

class ListType(Type):
    """A list of homogenous types."""
    name: str
    types: t.ClassVar[t.List[type]]
    def __init__(self, element_type: ConvertableToType | None = None, length: int | None = None) -> None: ...
    @classmethod
    def from_obj(cls, py_obj: t.Any | None = None) -> ListType: ...
    def assign_type(self, wb_type: Type) -> ListType | InvalidType: ...
    def assign(self, py_obj: t.Any | None = None) -> ListType | InvalidType: ...
    def explain(self, other: t.Any, depth: int = 0) -> str: ...

class NDArrayType(Type):
    """Represents a list of homogenous types."""
    name: str
    types: t.ClassVar[t.List[type]]
    def __init__(self, shape: t.Sequence[int], serialization_path: t.Dict[str, str] | None = None) -> None: ...
    @classmethod
    def from_obj(cls, py_obj: t.Any | None = None) -> NDArrayType: ...
    def assign_type(self, wb_type: Type) -> NDArrayType | InvalidType: ...
    def assign(self, py_obj: t.Any | None = None) -> NDArrayType | InvalidType: ...
    def to_json(self, artifact: Artifact | None = None) -> t.Dict[str, t.Any]: ...

class TypedDictType(Type):
    """Represents a dictionary object where each key can have a type."""
    name: str
    legacy_names: Incomplete
    types: t.ClassVar[t.List[type]]
    def __init__(self, type_map: t.Dict[str, ConvertableToType] | None = None) -> None: ...
    @classmethod
    def from_obj(cls, py_obj: t.Any | None = None) -> TypedDictType: ...
    def assign_type(self, wb_type: Type) -> TypedDictType | InvalidType: ...
    def assign(self, py_obj: t.Any | None = None) -> TypedDictType | InvalidType: ...
    def explain(self, other: t.Any, depth: int = 0) -> str: ...
