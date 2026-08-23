from . import yaml as yaml
from _typeshed import Incomplete
from referencing import Registry
from typing import Any

draft7_format_checker: Incomplete
METASCHEMA_PATH: Incomplete
EVENT_METASCHEMA_FILEPATH: Incomplete
EVENT_METASCHEMA: Incomplete
EVENT_CORE_SCHEMA_FILEPATH: Incomplete
EVENT_CORE_SCHEMA: Incomplete
PROPERTY_METASCHEMA_FILEPATH: Incomplete
PROPERTY_METASCHEMA: Incomplete
SCHEMA_STORE: Incomplete
resources: Incomplete
METASCHEMA_REGISTRY: Registry[Any]
JUPYTER_EVENTS_SCHEMA_VALIDATOR: Incomplete
JUPYTER_EVENTS_CORE_VALIDATOR: Incomplete

def validate_schema(schema: dict[str, Any]) -> None:
    """Validate a schema dict."""
