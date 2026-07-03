from .config import BaseConfig
from .error_wrappers import ValidationError
from .fields import ModelField, ModelPrivateAttr
from .parse import Protocol
from .types import ModelOrDc, StrBytes
from .typing import AbstractSetIntStr, AnyCallable, AnyClassMethod, CallableGenerator, DictAny, DictStrAny, MappingIntStrAny, ReprArgs, SetStr, TupleGenerator
from .utils import Representation
from abc import ABCMeta
from inspect import Signature
from pathlib import Path
from typing import Any, Callable, ClassVar, Dict, List, Mapping, Tuple, Type, TypeVar, overload

__all__ = ['BaseModel', 'create_model', 'validate_model']

Model = TypeVar('Model', bound='BaseModel')

class ModelMetaclass(ABCMeta):
    def __new__(mcs, name, bases, namespace, **kwargs): ...
    def __instancecheck__(self, instance: Any) -> bool:
        """
        Avoid calling ABC _abc_subclasscheck unless we're pretty sure.

        See #3829 and python/cpython#92810
        """

class BaseModel(Representation, metaclass=ModelMetaclass):
    __fields__: ClassVar[Dict[str, ModelField]]
    __include_fields__: ClassVar[Mapping[str, Any] | None]
    __exclude_fields__: ClassVar[Mapping[str, Any] | None]
    __validators__: ClassVar[Dict[str, AnyCallable]]
    __pre_root_validators__: ClassVar[List[AnyCallable]]
    __post_root_validators__: ClassVar[List[Tuple[bool, AnyCallable]]]
    __config__: ClassVar[Type[BaseConfig]]
    __json_encoder__: ClassVar[Callable[[Any], Any]]
    __schema_cache__: ClassVar['DictAny']
    __custom_root_type__: ClassVar[bool]
    __signature__: ClassVar['Signature']
    __private_attributes__: ClassVar[Dict[str, ModelPrivateAttr]]
    __class_vars__: ClassVar[SetStr]
    __fields_set__: ClassVar[SetStr]
    Config = BaseConfig
    __doc__: str
    def __init__(__pydantic_self__, **data: Any) -> None:
        """
        Create a new model by parsing and validating input data from keyword arguments.

        Raises ValidationError if the input data cannot be parsed to form a valid model.
        """
    def __setattr__(self, name, value): ...
    def dict(self, *, include: AbstractSetIntStr | MappingIntStrAny | None = None, exclude: AbstractSetIntStr | MappingIntStrAny | None = None, by_alias: bool = False, skip_defaults: bool | None = None, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False) -> DictStrAny:
        """
        Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

        """
    def json(self, *, include: AbstractSetIntStr | MappingIntStrAny | None = None, exclude: AbstractSetIntStr | MappingIntStrAny | None = None, by_alias: bool = False, skip_defaults: bool | None = None, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False, encoder: Callable[[Any], Any] | None = None, models_as_dict: bool = True, **dumps_kwargs: Any) -> str:
        """
        Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

        `encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.
        """
    @classmethod
    def parse_obj(cls, obj: Any) -> Model: ...
    @classmethod
    def parse_raw(cls, b: StrBytes, *, content_type: str = None, encoding: str = 'utf8', proto: Protocol = None, allow_pickle: bool = False) -> Model: ...
    @classmethod
    def parse_file(cls, path: str | Path, *, content_type: str = None, encoding: str = 'utf8', proto: Protocol = None, allow_pickle: bool = False) -> Model: ...
    @classmethod
    def from_orm(cls, obj: Any) -> Model: ...
    @classmethod
    def construct(cls, _fields_set: SetStr | None = None, **values: Any) -> Model:
        """
        Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.
        Default values are respected, but no other validation is performed.
        Behaves as if `Config.extra = 'allow'` was set since it adds all passed values
        """
    def copy(self, *, include: AbstractSetIntStr | MappingIntStrAny | None = None, exclude: AbstractSetIntStr | MappingIntStrAny | None = None, update: DictStrAny | None = None, deep: bool = False) -> Model:
        """
        Duplicate a model, optionally choose which fields to include, exclude and change.

        :param include: fields to include in new model
        :param exclude: fields to exclude from new model, as with values this takes precedence over include
        :param update: values to change/add in the new model. Note: the data is not validated before creating
            the new model: you should trust this data
        :param deep: set to `True` to make a deep copy of the model
        :return: new model instance
        """
    @classmethod
    def schema(cls, by_alias: bool = True, ref_template: str = ...) -> DictStrAny: ...
    @classmethod
    def schema_json(cls, *, by_alias: bool = True, ref_template: str = ..., **dumps_kwargs: Any) -> str: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def validate(cls, value: Any) -> Model: ...
    @classmethod
    def __try_update_forward_refs__(cls, **localns: Any) -> None:
        """
        Same as update_forward_refs but will not raise exception
        when forward references are not defined.
        """
    @classmethod
    def update_forward_refs(cls, **localns: Any) -> None:
        """
        Try to update ForwardRefs on fields based on this Model, globalns and localns.
        """
    def __iter__(self) -> TupleGenerator:
        """
        so `dict(model)` works
        """
    def __eq__(self, other: Any) -> bool: ...
    def __repr_args__(self) -> ReprArgs: ...

@overload
def create_model(__model_name: str, *, __config__: Type[BaseConfig] | None = None, __base__: None = None, __module__: str = ..., __validators__: Dict[str, 'AnyClassMethod'] = None, __cls_kwargs__: Dict[str, Any] = None, **field_definitions: Any) -> Type['BaseModel']: ...
@overload
def create_model(__model_name: str, *, __config__: Type[BaseConfig] | None = None, __base__: Type['Model'] | Tuple[Type['Model'], ...], __module__: str = ..., __validators__: Dict[str, 'AnyClassMethod'] = None, __cls_kwargs__: Dict[str, Any] = None, **field_definitions: Any) -> Type['Model']: ...
def validate_model(model: Type[BaseModel], input_data: DictStrAny, cls: ModelOrDc = None) -> Tuple['DictStrAny', 'SetStr', ValidationError | None]:
    """
    validate data against a model.
    """
