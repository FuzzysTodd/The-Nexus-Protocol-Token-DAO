from .dataclasses import Dataclass as Dataclass
from .fields import FieldInfo as FieldInfo, MAPPING_LIKE_SHAPES as MAPPING_LIKE_SHAPES, ModelField as ModelField, SHAPE_DEQUE as SHAPE_DEQUE, SHAPE_FROZENSET as SHAPE_FROZENSET, SHAPE_GENERIC as SHAPE_GENERIC, SHAPE_ITERABLE as SHAPE_ITERABLE, SHAPE_LIST as SHAPE_LIST, SHAPE_SEQUENCE as SHAPE_SEQUENCE, SHAPE_SET as SHAPE_SET, SHAPE_SINGLETON as SHAPE_SINGLETON, SHAPE_TUPLE as SHAPE_TUPLE, SHAPE_TUPLE_ELLIPSIS as SHAPE_TUPLE_ELLIPSIS
from .json import pydantic_encoder as pydantic_encoder
from .main import BaseModel as BaseModel
from .networks import AnyUrl as AnyUrl, EmailStr as EmailStr
from .types import ConstrainedDecimal as ConstrainedDecimal, ConstrainedFloat as ConstrainedFloat, ConstrainedFrozenSet as ConstrainedFrozenSet, ConstrainedInt as ConstrainedInt, ConstrainedList as ConstrainedList, ConstrainedSet as ConstrainedSet, ConstrainedStr as ConstrainedStr, SecretBytes as SecretBytes, SecretStr as SecretStr, StrictBytes as StrictBytes, StrictStr as StrictStr, conbytes as conbytes, condecimal as condecimal, confloat as confloat, confrozenset as confrozenset, conint as conint, conlist as conlist, conset as conset, constr as constr
from .typing import all_literal_values as all_literal_values, get_args as get_args, get_origin as get_origin, get_sub_types as get_sub_types, is_callable_type as is_callable_type, is_literal_type as is_literal_type, is_namedtuple as is_namedtuple, is_none_type as is_none_type, is_union as is_union
from .utils import ROOT_KEY as ROOT_KEY, get_model as get_model, lenient_issubclass as lenient_issubclass
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Dict, Sequence, Set, Tuple, Type

default_prefix: str
default_ref_template: str
TypeModelOrEnum: Incomplete
TypeModelSet = Set[TypeModelOrEnum]

def schema(models: Sequence[Type['BaseModel'] | Type['Dataclass']], *, by_alias: bool = True, title: str | None = None, description: str | None = None, ref_prefix: str | None = None, ref_template: str = ...) -> Dict[str, Any]:
    '''
    Process a list of models and generate a single JSON Schema with all of them defined in the ``definitions``
    top-level JSON key, including their sub-models.

    :param models: a list of models to include in the generated JSON Schema
    :param by_alias: generate the schemas using the aliases defined, if any
    :param title: title for the generated schema that includes the definitions
    :param description: description for the generated schema
    :param ref_prefix: the JSON Pointer prefix for schema references with ``$ref``, if None, will be set to the
      default of ``#/definitions/``. Update it if you want the schemas to reference the definitions somewhere
      else, e.g. for OpenAPI use ``#/components/schemas/``. The resulting generated schemas will still be at the
      top-level key ``definitions``, so you can extract them from there. But all the references will have the set
      prefix.
    :param ref_template: Use a ``string.format()`` template for ``$ref`` instead of a prefix. This can be useful
      for references that cannot be represented by ``ref_prefix`` such as a definition stored in another file. For
      a sibling json file in a ``/schemas`` directory use ``"/schemas/${model}.json#"``.
    :return: dict with the JSON Schema with a ``definitions`` top-level key including the schema definitions for
      the models and sub-models passed in ``models``.
    '''
def model_schema(model: Type['BaseModel'] | Type['Dataclass'], by_alias: bool = True, ref_prefix: str | None = None, ref_template: str = ...) -> Dict[str, Any]:
    '''
    Generate a JSON Schema for one model. With all the sub-models defined in the ``definitions`` top-level
    JSON key.

    :param model: a Pydantic model (a class that inherits from BaseModel)
    :param by_alias: generate the schemas using the aliases defined, if any
    :param ref_prefix: the JSON Pointer prefix for schema references with ``$ref``, if None, will be set to the
      default of ``#/definitions/``. Update it if you want the schemas to reference the definitions somewhere
      else, e.g. for OpenAPI use ``#/components/schemas/``. The resulting generated schemas will still be at the
      top-level key ``definitions``, so you can extract them from there. But all the references will have the set
      prefix.
    :param ref_template: Use a ``string.format()`` template for ``$ref`` instead of a prefix. This can be useful for
      references that cannot be represented by ``ref_prefix`` such as a definition stored in another file. For a
      sibling json file in a ``/schemas`` directory use ``"/schemas/${model}.json#"``.
    :return: dict with the JSON Schema for the passed ``model``
    '''
def get_field_info_schema(field: ModelField, schema_overrides: bool = False) -> Tuple[Dict[str, Any], bool]: ...
def field_schema(field: ModelField, *, by_alias: bool = True, model_name_map: Dict[TypeModelOrEnum, str], ref_prefix: str | None = None, ref_template: str = ..., known_models: TypeModelSet | None = None) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    '''
    Process a Pydantic field and return a tuple with a JSON Schema for it as the first item.
    Also return a dictionary of definitions with models as keys and their schemas as values. If the passed field
    is a model and has sub-models, and those sub-models don\'t have overrides (as ``title``, ``default``, etc), they
    will be included in the definitions and referenced in the schema instead of included recursively.

    :param field: a Pydantic ``ModelField``
    :param by_alias: use the defined alias (if any) in the returned schema
    :param model_name_map: used to generate the JSON Schema references to other models included in the definitions
    :param ref_prefix: the JSON Pointer prefix to use for references to other schemas, if None, the default of
      #/definitions/ will be used
    :param ref_template: Use a ``string.format()`` template for ``$ref`` instead of a prefix. This can be useful for
      references that cannot be represented by ``ref_prefix`` such as a definition stored in another file. For a
      sibling json file in a ``/schemas`` directory use ``"/schemas/${model}.json#"``.
    :param known_models: used to solve circular references
    :return: tuple of the schema for this field and additional definitions
    '''

numeric_types: Incomplete

def get_field_schema_validations(field: ModelField) -> Dict[str, Any]:
    """
    Get the JSON Schema validation keywords for a ``field`` with an annotation of
    a Pydantic ``FieldInfo`` with validation arguments.
    """
def get_model_name_map(unique_models: TypeModelSet) -> Dict[TypeModelOrEnum, str]:
    '''
    Process a set of models and generate unique names for them to be used as keys in the JSON Schema
    definitions. By default the names are the same as the class name. But if two models in different Python
    modules have the same name (e.g. "users.Model" and "items.Model"), the generated names will be
    based on the Python module path for those conflicting models to prevent name collisions.

    :param unique_models: a Python set of models
    :return: dict mapping models to names
    '''
def get_flat_models_from_model(model: Type['BaseModel'], known_models: TypeModelSet | None = None) -> TypeModelSet:
    """
    Take a single ``model`` and generate a set with itself and all the sub-models in the tree. I.e. if you pass
    model ``Foo`` (subclass of Pydantic ``BaseModel``) as ``model``, and it has a field of type ``Bar`` (also
    subclass of ``BaseModel``) and that model ``Bar`` has a field of type ``Baz`` (also subclass of ``BaseModel``),
    the return value will be ``set([Foo, Bar, Baz])``.

    :param model: a Pydantic ``BaseModel`` subclass
    :param known_models: used to solve circular references
    :return: a set with the initial model and all its sub-models
    """
def get_flat_models_from_field(field: ModelField, known_models: TypeModelSet) -> TypeModelSet:
    """
    Take a single Pydantic ``ModelField`` (from a model) that could have been declared as a subclass of BaseModel
    (so, it could be a submodel), and generate a set with its model and all the sub-models in the tree.
    I.e. if you pass a field that was declared to be of type ``Foo`` (subclass of BaseModel) as ``field``, and that
    model ``Foo`` has a field of type ``Bar`` (also subclass of ``BaseModel``) and that model ``Bar`` has a field of
    type ``Baz`` (also subclass of ``BaseModel``), the return value will be ``set([Foo, Bar, Baz])``.

    :param field: a Pydantic ``ModelField``
    :param known_models: used to solve circular references
    :return: a set with the model used in the declaration for this field, if any, and all its sub-models
    """
def get_flat_models_from_fields(fields: Sequence[ModelField], known_models: TypeModelSet) -> TypeModelSet:
    """
    Take a list of Pydantic  ``ModelField``s (from a model) that could have been declared as subclasses of ``BaseModel``
    (so, any of them could be a submodel), and generate a set with their models and all the sub-models in the tree.
    I.e. if you pass a the fields of a model ``Foo`` (subclass of ``BaseModel``) as ``fields``, and on of them has a
    field of type ``Bar`` (also subclass of ``BaseModel``) and that model ``Bar`` has a field of type ``Baz`` (also
    subclass of ``BaseModel``), the return value will be ``set([Foo, Bar, Baz])``.

    :param fields: a list of Pydantic ``ModelField``s
    :param known_models: used to solve circular references
    :return: a set with any model declared in the fields, and all their sub-models
    """
def get_flat_models_from_models(models: Sequence[Type['BaseModel']]) -> TypeModelSet:
    """
    Take a list of ``models`` and generate a set with them and all their sub-models in their trees. I.e. if you pass
    a list of two models, ``Foo`` and ``Bar``, both subclasses of Pydantic ``BaseModel`` as models, and ``Bar`` has
    a field of type ``Baz`` (also subclass of ``BaseModel``), the return value will be ``set([Foo, Bar, Baz])``.
    """
def get_long_model_name(model: TypeModelOrEnum) -> str: ...
def field_type_schema(field: ModelField, *, by_alias: bool, model_name_map: Dict[TypeModelOrEnum, str], ref_template: str, schema_overrides: bool = False, ref_prefix: str | None = None, known_models: TypeModelSet) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    """
    Used by ``field_schema()``, you probably should be using that function.

    Take a single ``field`` and generate the schema for its type only, not including additional
    information as title, etc. Also return additional schema definitions, from sub-models.
    """
def model_process_schema(model: TypeModelOrEnum, *, by_alias: bool = True, model_name_map: Dict[TypeModelOrEnum, str], ref_prefix: str | None = None, ref_template: str = ..., known_models: TypeModelSet | None = None, field: ModelField | None = None) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    """
    Used by ``model_schema()``, you probably should be using that function.

    Take a single ``model`` and generate its schema. Also return additional schema definitions, from sub-models. The
    sub-models of the returned schema will be referenced, but their definitions will not be included in the schema. All
    the definitions are returned as the second value.
    """
def model_type_schema(model: Type['BaseModel'], *, by_alias: bool, model_name_map: Dict[TypeModelOrEnum, str], ref_template: str, ref_prefix: str | None = None, known_models: TypeModelSet) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    """
    You probably should be using ``model_schema()``, this function is indirectly used by that function.

    Take a single ``model`` and generate the schema for its type only, not including additional
    information as title, etc. Also return additional schema definitions, from sub-models.
    """
def enum_process_schema(enum: Type[Enum], *, field: ModelField | None = None) -> Dict[str, Any]:
    """
    Take a single `enum` and generate its schema.

    This is similar to the `model_process_schema` function, but applies to ``Enum`` objects.
    """
def field_singleton_sub_fields_schema(field: ModelField, *, by_alias: bool, model_name_map: Dict[TypeModelOrEnum, str], ref_template: str, schema_overrides: bool = False, ref_prefix: str | None = None, known_models: TypeModelSet) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    '''
    This function is indirectly used by ``field_schema()``, you probably should be using that function.

    Take a list of Pydantic ``ModelField`` from the declaration of a type with parameters, and generate their
    schema. I.e., fields used as "type parameters", like ``str`` and ``int`` in ``Tuple[str, int]``.
    '''

field_class_to_schema: Tuple[Tuple[Any, Dict[str, Any]], ...]
json_scheme: Incomplete

def add_field_type_to_schema(field_type: Any, schema_: Dict[str, Any]) -> None:
    """
    Update the given `schema` with the type-specific metadata for the given `field_type`.

    This function looks through `field_class_to_schema` for a class that matches the given `field_type`,
    and then modifies the given `schema` with the information from that type.
    """
def get_schema_ref(name: str, ref_prefix: str | None, ref_template: str, schema_overrides: bool) -> Dict[str, Any]: ...
def field_singleton_schema(field: ModelField, *, by_alias: bool, model_name_map: Dict[TypeModelOrEnum, str], ref_template: str, schema_overrides: bool = False, ref_prefix: str | None = None, known_models: TypeModelSet) -> Tuple[Dict[str, Any], Dict[str, Any], Set[str]]:
    """
    This function is indirectly used by ``field_schema()``, you should probably be using that function.

    Take a single Pydantic ``ModelField``, and return its schema and any additional definitions from sub-models.
    """
def multitypes_literal_field_for_schema(values: Tuple[Any, ...], field: ModelField) -> ModelField:
    """
    To support `Literal` with values of different types, we split it into multiple `Literal` with same type
    e.g. `Literal['qwe', 'asd', 1, 2]` becomes `Union[Literal['qwe', 'asd'], Literal[1, 2]]`
    """
def encode_default(dft: Any) -> Any: ...
def get_annotation_from_field_info(annotation: Any, field_info: FieldInfo, field_name: str, validate_assignment: bool = False) -> Type[Any]:
    """
    Get an annotation with validation implemented for numbers and strings based on the field_info.
    :param annotation: an annotation from a field specification, as ``str``, ``ConstrainedStr``
    :param field_info: an instance of FieldInfo, possibly with declarations for validations and JSON Schema
    :param field_name: name of the field for use in error messages
    :param validate_assignment: default False, flag for BaseModel Config value of validate_assignment
    :return: the same ``annotation`` if unmodified or a new annotation with validation in place
    """
def get_annotation_with_constraints(annotation: Any, field_info: FieldInfo) -> Tuple[Type[Any], Set[str]]:
    """
    Get an annotation with used constraints implemented for numbers and strings based on the field_info.

    :param annotation: an annotation from a field specification, as ``str``, ``ConstrainedStr``
    :param field_info: an instance of FieldInfo, possibly with declarations for validations and JSON Schema
    :return: the same ``annotation`` if unmodified or a new annotation along with the used constraints.
    """
def normalize_name(name: str) -> str:
    """
    Normalizes the given name. This can be applied to either a model *or* enum.
    """

class SkipField(Exception):
    """
    Utility exception used to exclude fields from schema.
    """
    message: Incomplete
    def __init__(self, message: str) -> None: ...
