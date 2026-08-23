from .schema import EventSchema as EventSchema
from typing import Any

class SchemaRegistryException(Exception):
    """Exception class for Jupyter Events Schema Registry Errors."""

class SchemaRegistry:
    """A convenient API for storing and searching a group of schemas."""
    def __init__(self, schemas: dict[str, EventSchema] | None = None) -> None:
        """Initialize the registry."""
    def __contains__(self, key: str) -> bool:
        """Syntax sugar to check if a schema is found in the registry"""
    @property
    def schema_ids(self) -> list[str]: ...
    def register(self, schema: dict[str, Any] | str | EventSchema) -> EventSchema:
        """Add a valid schema to the registry.

        All schemas are validated against the Jupyter Events meta-schema
        found here:
        """
    def get(self, id_: str) -> EventSchema:
        """Fetch a given schema. If the schema is not found,
        this will raise a KeyError.
        """
    def remove(self, id_: str) -> None:
        """Remove a given schema. If the schema is not found,
        this will raise a KeyError.
        """
    def validate_event(self, id_: str, data: dict[str, Any]) -> None:
        """Validate an event against a schema within this
        registry.
        """
