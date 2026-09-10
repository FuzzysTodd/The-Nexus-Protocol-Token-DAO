from _typeshed import Incomplete

__all__ = ['Schema', 'And', 'Or', 'Regex', 'Optional', 'Use', 'Forbidden', 'Const', 'Literal', 'SchemaError', 'SchemaWrongKeyError', 'SchemaMissingKeyError', 'SchemaForbiddenKeyError', 'SchemaUnexpectedTypeError', 'SchemaOnlyOneAllowedError']

class SchemaError(Exception):
    """Error during Schema validation."""
    autos: Incomplete
    errors: Incomplete
    def __init__(self, autos, errors: Incomplete | None = None) -> None: ...
    @property
    def code(self):
        """
        Removes duplicates values in auto and error list.
        parameters.
        """

class SchemaWrongKeyError(SchemaError):
    """Error Should be raised when an unexpected key is detected within the
    data set being."""
class SchemaMissingKeyError(SchemaError):
    """Error should be raised when a mandatory key is not found within the
    data set being validated"""
class SchemaOnlyOneAllowedError(SchemaError):
    """Error should be raised when an only_one Or key has multiple matching candidates"""
class SchemaForbiddenKeyError(SchemaError):
    """Error should be raised when a forbidden key is found within the
    data set being validated, and its value matches the value that was specified"""
class SchemaUnexpectedTypeError(SchemaError):
    """Error should be raised when a type mismatch is detected within the
    data set being validated."""

class And:
    """
    Utility function to combine validation directives in AND Boolean fashion.
    """
    def __init__(self, *args, **kw) -> None: ...
    @property
    def args(self):
        """The provided parameters"""
    def validate(self, data, **kwargs):
        """
        Validate data using defined sub schema/expressions ensuring all
        values are valid.
        :param data: to be validated with sub defined schemas.
        :return: returns validated data
        """

class Or(And):
    """Utility function to combine validation directives in a OR Boolean
    fashion."""
    only_one: Incomplete
    match_count: int
    def __init__(self, *args, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def validate(self, data, **kwargs):
        """
        Validate data using sub defined schema/expressions ensuring at least
        one value is valid.
        :param data: data to be validated by provided schema.
        :return: return validated data if not validation
        """

class Regex:
    """
    Enables schema.py to validate string using regular expressions.
    """
    NAMES: Incomplete
    def __init__(self, pattern_str, flags: int = 0, error: Incomplete | None = None) -> None: ...
    @property
    def pattern_str(self):
        """The pattern for the represented regular expression"""
    def validate(self, data, **kwargs):
        """
        Validated data using defined regex.
        :param data: data to be validated
        :return: return validated data.
        """

class Use:
    """
    For more general use cases, you can use the Use class to transform
    the data while it is being validate.
    """
    def __init__(self, callable_, error: Incomplete | None = None) -> None: ...
    def validate(self, data, **kwargs): ...

class Schema:
    """
    Entry point of the library, use this class to instantiate validation
    schema for the data that will be validated.
    """
    as_reference: Incomplete
    def __init__(self, schema, error: Incomplete | None = None, ignore_extra_keys: bool = False, name: Incomplete | None = None, description: Incomplete | None = None, as_reference: bool = False) -> None: ...
    @property
    def schema(self): ...
    @property
    def description(self): ...
    @property
    def name(self): ...
    @property
    def ignore_extra_keys(self): ...
    def is_valid(self, data, **kwargs):
        """Return whether the given data has passed all the validations
        that were specified in the given schema.
        """
    def validate(self, data, **kwargs): ...
    def json_schema(self, schema_id, use_refs: bool = False, **kwargs):
        """Generate a draft-07 JSON schema dict representing the Schema.
        This method must be called with a schema_id.

        :param schema_id: The value of the $id on the main schema
        :param use_refs: Enable reusing object references in the resulting JSON schema.
                         Schemas with references are harder to read by humans, but are a lot smaller when there
                         is a lot of reuse
        """

class Optional(Schema):
    """Marker for an optional part of the validation Schema."""
    default: Incomplete
    key: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def reset(self) -> None: ...

class Hook(Schema):
    handler: Incomplete
    key: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class Forbidden(Hook):
    def __init__(self, *args, **kwargs) -> None: ...

class Literal:
    def __init__(self, value, description: Incomplete | None = None) -> None: ...
    @property
    def description(self): ...
    @property
    def schema(self): ...

class Const(Schema):
    def validate(self, data, **kwargs): ...
