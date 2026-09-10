from .class_validators import Validator as Validator, ValidatorsList as ValidatorsList, make_generic_validator as make_generic_validator, prep_validators as prep_validators
from .config import BaseConfig as BaseConfig
from .error_wrappers import ErrorList as ErrorList, ErrorWrapper as ErrorWrapper
from .errors import ConfigError as ConfigError, InvalidDiscriminator as InvalidDiscriminator, MissingDiscriminator as MissingDiscriminator, NoneIsNotAllowedError as NoneIsNotAllowedError
from .types import Json as Json, JsonWrapper as JsonWrapper, ModelOrDc as ModelOrDc
from .typing import AbstractSetIntStr as AbstractSetIntStr, MappingIntStrAny as MappingIntStrAny, NoArgAnyCallable as NoArgAnyCallable, ReprArgs as ReprArgs, convert_generics as convert_generics, display_as_type as display_as_type, get_args as get_args, get_origin as get_origin, is_finalvar as is_finalvar, is_literal_type as is_literal_type, is_new_type as is_new_type, is_none_type as is_none_type, is_typeddict as is_typeddict, is_typeddict_special as is_typeddict_special, is_union as is_union, new_type_supertype as new_type_supertype
from .utils import PyObjectStr as PyObjectStr, Representation as Representation, ValueItems as ValueItems, get_discriminator_alias_and_values as get_discriminator_alias_and_values, get_unique_discriminator_alias as get_unique_discriminator_alias, lenient_isinstance as lenient_isinstance, lenient_issubclass as lenient_issubclass, sequence_like as sequence_like, smart_deepcopy as smart_deepcopy
from .validators import constant_validator as constant_validator, dict_validator as dict_validator, find_validators as find_validators, validate_json as validate_json
from _typeshed import Incomplete
from typing import Any, Dict, Set, Tuple, Type, TypeVar

Required: Any
T = TypeVar('T')

class UndefinedType:
    def __copy__(self) -> T: ...
    def __reduce__(self) -> str: ...
    def __deepcopy__(self, _: Any) -> T: ...

Undefined: Incomplete
ValidateReturn = Tuple[Any | None, ErrorList | None]
LocStr = Tuple[int | str, ...] | str
BoolUndefined = bool | UndefinedType

class FieldInfo(Representation):
    """
    Captures extra information about a field.
    """
    __field_constraints__: Incomplete
    default: Incomplete
    default_factory: Incomplete
    alias: Incomplete
    alias_priority: Incomplete
    title: Incomplete
    description: Incomplete
    exclude: Incomplete
    include: Incomplete
    const: Incomplete
    gt: Incomplete
    ge: Incomplete
    lt: Incomplete
    le: Incomplete
    multiple_of: Incomplete
    allow_inf_nan: Incomplete
    max_digits: Incomplete
    decimal_places: Incomplete
    min_items: Incomplete
    max_items: Incomplete
    unique_items: Incomplete
    min_length: Incomplete
    max_length: Incomplete
    allow_mutation: Incomplete
    regex: Incomplete
    discriminator: Incomplete
    repr: Incomplete
    extra: Incomplete
    def __init__(self, default: Any = ..., **kwargs: Any) -> None: ...
    def __repr_args__(self) -> ReprArgs: ...
    def get_constraints(self) -> Set[str]:
        """
        Gets the constraints set on the field by comparing the constraint value with its default value

        :return: the constraints set on field_info
        """
    def update_from_config(self, from_config: Dict[str, Any]) -> None:
        """
        Update this FieldInfo based on a dict from get_field_info, only fields which have not been set are dated.
        """

def Field(default: Any = ..., *, default_factory: NoArgAnyCallable | None = None, alias: str | None = None, title: str | None = None, description: str | None = None, exclude: AbstractSetIntStr | MappingIntStrAny | Any | None = None, include: AbstractSetIntStr | MappingIntStrAny | Any | None = None, const: bool | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, multiple_of: float | None = None, allow_inf_nan: bool | None = None, max_digits: int | None = None, decimal_places: int | None = None, min_items: int | None = None, max_items: int | None = None, unique_items: bool | None = None, min_length: int | None = None, max_length: int | None = None, allow_mutation: bool = True, regex: str | None = None, discriminator: str | None = None, repr: bool = True, **extra: Any) -> Any:
    '''
    Used to provide extra information about a field, either for the model schema or complex validation. Some arguments
    apply only to number fields (``int``, ``float``, ``Decimal``) and some apply only to ``str``.

    :param default: since this is replacing the field’s default, its first argument is used
      to set the default, use ellipsis (``...``) to indicate the field is required
    :param default_factory: callable that will be called when a default value is needed for this field
      If both `default` and `default_factory` are set, an error is raised.
    :param alias: the public name of the field
    :param title: can be any string, used in the schema
    :param description: can be any string, used in the schema
    :param exclude: exclude this field while dumping.
      Takes same values as the ``include`` and ``exclude`` arguments on the ``.dict`` method.
    :param include: include this field while dumping.
      Takes same values as the ``include`` and ``exclude`` arguments on the ``.dict`` method.
    :param const: this field is required and *must* take it\'s default value
    :param gt: only applies to numbers, requires the field to be "greater than". The schema
      will have an ``exclusiveMinimum`` validation keyword
    :param ge: only applies to numbers, requires the field to be "greater than or equal to". The
      schema will have a ``minimum`` validation keyword
    :param lt: only applies to numbers, requires the field to be "less than". The schema
      will have an ``exclusiveMaximum`` validation keyword
    :param le: only applies to numbers, requires the field to be "less than or equal to". The
      schema will have a ``maximum`` validation keyword
    :param multiple_of: only applies to numbers, requires the field to be "a multiple of". The
      schema will have a ``multipleOf`` validation keyword
    :param allow_inf_nan: only applies to numbers, allows the field to be NaN or infinity (+inf or -inf),
        which is a valid Python float. Default True, set to False for compatibility with JSON.
    :param max_digits: only applies to Decimals, requires the field to have a maximum number
      of digits within the decimal. It does not include a zero before the decimal point or trailing decimal zeroes.
    :param decimal_places: only applies to Decimals, requires the field to have at most a number of decimal places
      allowed. It does not include trailing decimal zeroes.
    :param min_items: only applies to lists, requires the field to have a minimum number of
      elements. The schema will have a ``minItems`` validation keyword
    :param max_items: only applies to lists, requires the field to have a maximum number of
      elements. The schema will have a ``maxItems`` validation keyword
    :param unique_items: only applies to lists, requires the field not to have duplicated
      elements. The schema will have a ``uniqueItems`` validation keyword
    :param min_length: only applies to strings, requires the field to have a minimum length. The
      schema will have a ``minLength`` validation keyword
    :param max_length: only applies to strings, requires the field to have a maximum length. The
      schema will have a ``maxLength`` validation keyword
    :param allow_mutation: a boolean which defaults to True. When False, the field raises a TypeError if the field is
      assigned on an instance.  The BaseModel Config must set validate_assignment to True
    :param regex: only applies to strings, requires the field match against a regular expression
      pattern string. The schema will have a ``pattern`` validation keyword
    :param discriminator: only useful with a (discriminated a.k.a. tagged) `Union` of sub models with a common field.
      The `discriminator` is the name of this common field to shorten validation and improve generated schema
    :param repr: show this field in the representation
    :param **extra: any additional keyword arguments will be added as is to the schema
    '''

SHAPE_SINGLETON: int
SHAPE_LIST: int
SHAPE_SET: int
SHAPE_MAPPING: int
SHAPE_TUPLE: int
SHAPE_TUPLE_ELLIPSIS: int
SHAPE_SEQUENCE: int
SHAPE_FROZENSET: int
SHAPE_ITERABLE: int
SHAPE_GENERIC: int
SHAPE_DEQUE: int
SHAPE_DICT: int
SHAPE_DEFAULTDICT: int
SHAPE_COUNTER: int
SHAPE_NAME_LOOKUP: Incomplete
MAPPING_LIKE_SHAPES: Set[int]

class ModelField(Representation):
    name: Incomplete
    has_alias: Incomplete
    alias: Incomplete
    annotation: Incomplete
    type_: Incomplete
    outer_type_: Incomplete
    class_validators: Incomplete
    default: Incomplete
    default_factory: Incomplete
    required: Incomplete
    final: Incomplete
    model_config: Incomplete
    field_info: Incomplete
    discriminator_key: Incomplete
    discriminator_alias: Incomplete
    allow_none: bool
    validate_always: bool
    sub_fields: Incomplete
    sub_fields_mapping: Incomplete
    key_field: Incomplete
    validators: Incomplete
    pre_validators: Incomplete
    post_validators: Incomplete
    parse_json: bool
    shape: Incomplete
    def __init__(self, *, name: str, type_: Type[Any], class_validators: Dict[str, Validator] | None, model_config: Type['BaseConfig'], default: Any = None, default_factory: NoArgAnyCallable | None = None, required: BoolUndefined = ..., final: bool = False, alias: str | None = None, field_info: FieldInfo | None = None) -> None: ...
    def get_default(self) -> Any: ...
    @classmethod
    def infer(cls, *, name: str, value: Any, annotation: Any, class_validators: Dict[str, Validator] | None, config: Type['BaseConfig']) -> ModelField: ...
    def set_config(self, config: Type['BaseConfig']) -> None: ...
    @property
    def alt_alias(self) -> bool: ...
    def prepare(self) -> None:
        """
        Prepare the field but inspecting self.default, self.type_ etc.

        Note: this method is **not** idempotent (because _type_analysis is not idempotent),
        e.g. calling it it multiple times may modify the field and configure it incorrectly.
        """
    def prepare_discriminated_union_sub_fields(self) -> None:
        """
        Prepare the mapping <discriminator key> -> <ModelField> and update `sub_fields`
        Note that this process can be aborted if a `ForwardRef` is encountered
        """
    def populate_validators(self) -> None:
        """
        Prepare self.pre_validators, self.validators, and self.post_validators based on self.type_'s  __get_validators__
        and class validators. This method should be idempotent, e.g. it should be safe to call multiple times
        without mis-configuring the field.
        """
    def validate(self, v: Any, values: Dict[str, Any], *, loc: LocStr, cls: ModelOrDc | None = None) -> ValidateReturn: ...
    def is_complex(self) -> bool:
        '''
        Whether the field is "complex" eg. env variables should be parsed as JSON.
        '''
    def __repr_args__(self) -> ReprArgs: ...

class ModelPrivateAttr(Representation):
    default: Incomplete
    default_factory: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: NoArgAnyCallable | None = None) -> None: ...
    def get_default(self) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...

def PrivateAttr(default: Any = ..., *, default_factory: NoArgAnyCallable | None = None) -> Any:
    """
    Indicates that attribute is only used internally and never mixed with regular fields.

    Types or values of private attrs are not checked by pydantic and it's up to you to keep them relevant.

    Private attrs are stored in model __slots__.

    :param default: the attribute’s default value
    :param default_factory: callable that will be called when a default value is needed for this attribute
      If both `default` and `default_factory` are set, an error is raised.
    """

class DeferredType:
    """
    Used to postpone field preparation, while creating recursive generic models.
    """

def is_finalvar_with_default_val(type_: Type[Any], val: Any) -> bool: ...
