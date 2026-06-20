from . import yaml as yaml
from .validators import draft7_format_checker as draft7_format_checker, validate_schema as validate_schema
from jsonschema import FormatChecker as FormatChecker
from jsonschema.protocols import Validator
from pathlib import PurePath
from referencing import Registry
from typing import Any

Validator = Any

class EventSchemaUnrecognized(Exception):
    """An error for an unrecognized event schema."""
class EventSchemaLoadingError(Exception):
    """An error for an event schema loading error."""
class EventSchemaFileAbsent(Exception):
    """An error for an absent event schema file."""
SchemaType = dict | str | PurePath

class EventSchema:
    """A validated schema that can be used.

    On instantiation, validate the schema against
    Jupyter Event's metaschema.

    Parameters
    ----------
    schema: dict or str
        JSON schema to validate against Jupyter Events.

    validator_class: jsonschema.validators
        The validator class from jsonschema used to validate instances
        of this event schema. The schema itself will be validated
        against Jupyter Event's metaschema to ensure that
        any schema registered here follows the expected form
        of Jupyter Events.

    registry:
        Registry for nested JSON schema references.
    """
    def __init__(self, schema: SchemaType, validator_class: type[Validator] = ..., format_checker: FormatChecker = ..., registry: Registry[Any] | None = None) -> None:
        """Initialize an event schema."""
    @property
    def id(self) -> str:
        """Schema $id field."""
    @property
    def version(self) -> int:
        """Schema's version."""
    @property
    def properties(self) -> dict[str, Any]: ...
    def validate(self, data: dict[str, Any]) -> None:
        """Validate an incoming instance of this event schema."""
