from .class_validators import gather_all_validators as gather_all_validators
from .fields import DeferredType as DeferredType
from .main import BaseModel as BaseModel, create_model as create_model
from .types import JsonWrapper as JsonWrapper
from .typing import display_as_type as display_as_type, get_all_type_hints as get_all_type_hints, get_args as get_args, get_origin as get_origin, typing_base as typing_base
from .utils import all_identical as all_identical, lenient_issubclass as lenient_issubclass
from typing import Any, ClassVar, Iterator, Mapping, Tuple, Type, TypeVar
from weakref import WeakKeyDictionary, WeakValueDictionary

GenericModelT = TypeVar('GenericModelT', bound='GenericModel')
TypeVarType = Any
CacheKey = Tuple[Type[Any], Any, Tuple[Any, ...]]
Parametrization = Mapping[TypeVarType, Type[Any]]
GenericTypesCache = WeakValueDictionary[CacheKey, Type[BaseModel]]
AssignedParameters = WeakKeyDictionary[Type[BaseModel], Parametrization]

class GenericModel(BaseModel):
    __concrete__: ClassVar[bool]
    __parameters__: ClassVar[Tuple[TypeVarType, ...]]
    def __class_getitem__(cls, params: Type[Any] | Tuple[Type[Any], ...]) -> Type[Any]:
        """Instantiates a new class from a generic class `cls` and type variables `params`.

        :param params: Tuple of types the class . Given a generic class
            `Model` with 2 type variables and a concrete model `Model[str, int]`,
            the value `(str, int)` would be passed to `params`.
        :return: New model class inheriting from `cls` with instantiated
            types described by `params`. If no parameters are given, `cls` is
            returned as is.

        """
    @classmethod
    def __concrete_name__(cls, params: Tuple[Type[Any], ...]) -> str:
        """Compute class name for child classes.

        :param params: Tuple of types the class . Given a generic class
            `Model` with 2 type variables and a concrete model `Model[str, int]`,
            the value `(str, int)` would be passed to `params`.
        :return: String representing a the new class where `params` are
            passed to `cls` as type variables.

        This method can be overridden to achieve a custom naming scheme for GenericModels.
        """
    @classmethod
    def __parameterized_bases__(cls, typevars_map: Parametrization) -> Iterator[Type[Any]]:
        """
        Returns unbound bases of cls parameterised to given type variables

        :param typevars_map: Dictionary of type applications for binding subclasses.
            Given a generic class `Model` with 2 type variables [S, T]
            and a concrete model `Model[str, int]`,
            the value `{S: str, T: int}` would be passed to `typevars_map`.
        :return: an iterator of generic sub classes, parameterised by `typevars_map`
            and other assigned parameters of `cls`

        e.g.:
        ```
        class A(GenericModel, Generic[T]):
            ...

        class B(A[V], Generic[V]):
            ...

        assert A[int] in B.__parameterized_bases__({V: int})
        ```
        """

def replace_types(type_: Any, type_map: Mapping[Any, Any]) -> Any:
    """Return type with all occurrences of `type_map` keys recursively replaced with their values.

    :param type_: Any type, class or generic alias
    :param type_map: Mapping from `TypeVar` instance to concrete types.
    :return: New type representing the basic structure of `type_` with all
        `typevar_map` keys recursively replaced.

    >>> replace_types(Tuple[str, Union[List[str], float]], {str: int})
    Tuple[int, Union[List[int], float]]

    """
def check_parameters_count(cls, parameters: Tuple[Any, ...]) -> None: ...

DictValues: Type[Any]

def iter_contained_typevars(v: Any) -> Iterator[TypeVarType]:
    """Recursively iterate through all subtypes and type args of `v` and yield any typevars that are found."""
def get_caller_frame_info() -> Tuple[str | None, bool]:
    """
    Used inside a function to check whether it was called globally

    Will only work against non-compiled code, therefore used only in pydantic.generics

    :returns Tuple[module_name, called_globally]
    """
