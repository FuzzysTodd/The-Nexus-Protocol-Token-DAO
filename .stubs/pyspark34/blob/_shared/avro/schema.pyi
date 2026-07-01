import abc
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete
DEBUG_VERBOSE: int
NULL: str
BOOLEAN: str
STRING: str
BYTES: str
INT: str
LONG: str
FLOAT: str
DOUBLE: str
FIXED: str
ENUM: str
RECORD: str
ERROR: str
ARRAY: str
MAP: str
UNION: str
REQUEST: str
ERROR_UNION: str
PRIMITIVE_TYPES: Incomplete
NAMED_TYPES: Incomplete
VALID_TYPES: Incomplete
SCHEMA_RESERVED_PROPS: Incomplete
FIELD_RESERVED_PROPS: Incomplete
VALID_FIELD_SORT_ORDERS: Incomplete

class Error(Exception):
    """Base class for errors in this module."""
class AvroException(Error):
    """Generic Avro schema error."""
class SchemaParseException(AvroException):
    """Error while parsing a JSON schema descriptor."""

class Schema(metaclass=abc.ABCMeta):
    """Abstract base class for all Schema classes."""
    def __init__(self, data_type, other_props: Incomplete | None = None) -> None:
        """Initializes a new schema object.

        Args:
          data_type: Type of the schema to initialize.
          other_props: Optional dictionary of additional properties.
        """
    @property
    def namespace(self):
        """Returns: the namespace this schema belongs to, if any, or None."""
    @property
    def type(self):
        """Returns: the type of this schema."""
    @property
    def doc(self):
        """Returns: the documentation associated to this schema, if any, or None."""
    @property
    def props(self):
        """Reports all the properties of this schema.

        Includes all properties, reserved and non reserved.
        JSON properties of this schema are directly generated from this dict.

        Returns:
          A dictionary of properties associated to this schema.
        """
    @property
    def other_props(self):
        """Returns: the dictionary of non-reserved properties."""
    @abc.abstractmethod
    def to_json(self, names): ...

class Name:
    """Representation of an Avro name."""
    def __init__(self, name, namespace: Incomplete | None = None) -> None:
        """Parses an Avro name.

        Args:
          name: Avro name to parse (relative or absolute).
          namespace: Optional explicit namespace if the name is relative.
        """
    def __eq__(self, other): ...
    @property
    def simple_name(self):
        """Returns: the simple name part of this name."""
    @property
    def namespace(self):
        """Returns: this name's namespace, possible the empty string."""
    @property
    def fullname(self):
        """Returns: the full name."""

class Names:
    """Tracks Avro named schemas and default namespace during parsing."""
    def __init__(self, default_namespace: Incomplete | None = None, names: Incomplete | None = None) -> None:
        """Initializes a new name tracker.

        Args:
          default_namespace: Optional default namespace.
          names: Optional initial mapping of known named schemas.
        """
    @property
    def names(self):
        """Returns: the mapping of known named schemas."""
    @property
    def default_namespace(self):
        """Returns: the default namespace, if any, or None."""
    def new_with_default_namespace(self, namespace):
        """Creates a new name tracker from this tracker, but with a new default ns.

        :param Any namespace: New default namespace to use.
        :returns: New name tracker with the specified default namespace.
        :rtype: Names
        """
    def get_name(self, name, namespace: Incomplete | None = None):
        """Resolves the Avro name according to this name tracker's state.

        :param Any name: Name to resolve (absolute or relative).
        :param Optional[Any] namespace: Optional explicit namespace.
        :returns: The specified name, resolved according to this tracker.
        :rtype: Name
        """
    def get_schema(self, name, namespace: Incomplete | None = None):
        """Resolves an Avro schema by name.

        :param Any name: Name (absolute or relative) of the Avro schema to look up.
        :param Optional[Any] namespace: Optional explicit namespace.
        :returns: The schema with the specified name, if any, or None
        :rtype: Union[Any, None]
        """
    def prune_namespace(self, properties): ...
    def register(self, schema) -> None:
        """Registers a new named schema in this tracker.

        :param Any schema: Named Avro schema to register in this tracker.
        """

class NamedSchema(Schema, metaclass=abc.ABCMeta):
    """Abstract base class for named schemas.

    Named schemas are enumerated in NAMED_TYPES.
    """
    def __init__(self, data_type, name: Incomplete | None = None, namespace: Incomplete | None = None, names: Incomplete | None = None, other_props: Incomplete | None = None) -> None:
        """Initializes a new named schema object.

        Args:
          data_type: Type of the named schema.
          name: Name (absolute or relative) of the schema.
          namespace: Optional explicit namespace if name is relative.
          names: Tracker to resolve and register Avro names.
          other_props: Optional map of additional properties of the schema.
        """
    @property
    def avro_name(self):
        """Returns: the Name object describing this schema's name."""
    @property
    def name(self): ...
    @property
    def namespace(self): ...
    @property
    def fullname(self): ...
    def name_ref(self, names):
        """Reports this schema name relative to the specified name tracker.

        :param Any names: Avro name tracker to relativize this schema name against.
        :returns: This schema name, relativized against the specified name tracker.
        :rtype: Any
        """
    @abc.abstractmethod
    def to_json(self, names): ...

class Field:
    """Representation of the schema of a field in a record."""
    def __init__(self, data_type, name, index, has_default, default=..., order: Incomplete | None = None, doc: Incomplete | None = None, other_props: Incomplete | None = None) -> None:
        """Initializes a new Field object.

        Args:
          data_type: Avro schema of the field.
          name: Name of the field.
          index: 0-based position of the field.
          has_default:
          default:
          order:
          doc:
          other_props:
        """
    @property
    def type(self):
        """Returns: the schema of this field."""
    @property
    def name(self):
        """Returns: this field name."""
    @property
    def index(self):
        """Returns: the 0-based index of this field in the record."""
    @property
    def default(self): ...
    @property
    def has_default(self): ...
    @property
    def order(self): ...
    @property
    def doc(self): ...
    @property
    def props(self): ...
    @property
    def other_props(self): ...
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class PrimitiveSchema(Schema):
    """Schema of a primitive Avro type.

    Valid primitive types are defined in PRIMITIVE_TYPES.
    """
    def __init__(self, data_type, other_props: Incomplete | None = None) -> None:
        """Initializes a new schema object for the specified primitive type.

        Args:
          data_type: Type of the schema to construct. Must be primitive.
        """
    @property
    def name(self):
        """Returns: the simple name of this schema."""
    @property
    def fullname(self):
        """Returns: the fully qualified name of this schema."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class FixedSchema(NamedSchema):
    def __init__(self, name, namespace, size, names: Incomplete | None = None, other_props: Incomplete | None = None) -> None: ...
    @property
    def size(self):
        """Returns: the size of this fixed schema, in bytes."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class EnumSchema(NamedSchema):
    def __init__(self, name, namespace, symbols, names: Incomplete | None = None, doc: Incomplete | None = None, other_props: Incomplete | None = None) -> None:
        """Initializes a new enumeration schema object.

        Args:
          name: Simple name of this enumeration.
          namespace: Optional namespace.
          symbols: Ordered list of symbols defined in this enumeration.
          names:
          doc:
          other_props:
        """
    @property
    def symbols(self):
        """Returns: the symbols defined in this enum."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class ArraySchema(Schema):
    """Schema of an array."""
    def __init__(self, items, other_props: Incomplete | None = None) -> None:
        """Initializes a new array schema object.

        Args:
          items: Avro schema of the array items.
          other_props:
        """
    @property
    def items(self):
        """Returns: the schema of the items in this array."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class MapSchema(Schema):
    """Schema of a map."""
    def __init__(self, values, other_props: Incomplete | None = None) -> None:
        """Initializes a new map schema object.

        Args:
          values: Avro schema of the map values.
          other_props:
        """
    @property
    def values(self):
        """Returns: the schema of the values in this map."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class UnionSchema(Schema):
    """Schema of a union."""
    def __init__(self, schemas) -> None:
        """Initializes a new union schema object.

        Args:
          schemas: Ordered collection of schema branches in the union.
        """
    @property
    def schemas(self):
        """Returns: the ordered list of schema branches in the union."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

class ErrorUnionSchema(UnionSchema):
    """Schema representing the declared errors of a protocol message."""
    def __init__(self, schemas) -> None:
        """Initializes an error-union schema.

        Args:
          schema: collection of error schema.
        """
    def to_json(self, names: Incomplete | None = None): ...

class RecordSchema(NamedSchema):
    """Schema of a record."""
    @staticmethod
    def make_field_list(field_desc_list, names) -> Generator[Incomplete, None, None]:
        """Builds field schemas from a list of field JSON descriptors.
        Guarantees field name unicity.

        :param Any field_desc_list: Collection of field JSON descriptors.
        :param Any names: The names for this schema.
        :returns: Field schemas.
        :rtype: Field
        """
    def __init__(self, name, namespace, fields: Incomplete | None = None, make_fields: Incomplete | None = None, names: Incomplete | None = None, record_type=..., doc: Incomplete | None = None, other_props: Incomplete | None = None) -> None:
        """Initializes a new record schema object.

        Args:
          name: Name of the record (absolute or relative).
          namespace: Optional namespace the record belongs to, if name is relative.
          fields: collection of fields to add to this record.
              Exactly one of fields or make_fields must be specified.
          make_fields: function creating the fields that belong to the record.
              The function signature is: make_fields(names) -> ordered field list.
              Exactly one of fields or make_fields must be specified.
          names:
          record_type: Type of the record: one of RECORD, ERROR or REQUEST.
              Protocol requests are not named.
          doc:
          other_props:
        """
    @property
    def fields(self):
        """Returns: the field schemas, as an ordered tuple."""
    @property
    def field_map(self):
        """Returns: a read-only map of the field schemas index by field names."""
    def to_json(self, names: Incomplete | None = None): ...
    def __eq__(self, that): ...

def filter_keys_out(items, keys) -> Generator[Incomplete, None, None]:
    """Filters a collection of (key, value) items.
    Exclude any item whose key belongs to keys.

    :param Dict[Any, Any] items: Dictionary of items to filter the keys out of.
    :param Dict[Any, Any] keys: Dictionary of keys to filter the extracted keys against.
    :returns: Filtered items.
    :rtype: Tuple(Any, Any)
    """
def schema_from_json_data(json_data, names: Incomplete | None = None):
    """Builds an Avro Schema from its JSON descriptor.
    Raises SchemaParseException if the descriptor is invalid.

    :param Any json_data: JSON data representing the descriptor of the Avro schema.
    :param Any names: Optional tracker for Avro named schemas.
    :returns: The Avro schema parsed from the JSON descriptor.
    :rtype: Any
    """
def parse(json_string):
    """Constructs a Schema from its JSON descriptor in text form.
    Raises SchemaParseException if a JSON parsing error is met, or if the JSON descriptor is invalid.

    :param str json_string: String representation of the JSON descriptor of the schema.
    :returns: The parsed schema.
    :rtype: Any
    """
