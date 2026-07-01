import click
from _typeshed import Incomplete
from jupyter_events.schema import EventSchema as EventSchema, EventSchemaFileAbsent as EventSchemaFileAbsent, EventSchemaLoadingError as EventSchemaLoadingError

WIN: Incomplete

class RC:
    """Return code enum."""
    OK: int
    INVALID: int
    UNPARSABLE: int
    NOT_FOUND: int

class EMOJI:
    """Terminal emoji enum"""
    X: Incomplete
    OK: Incomplete

console: Incomplete
error_console: Incomplete

def main() -> None:
    """A simple CLI tool to quickly validate JSON schemas against
    Jupyter Event's custom validator.

    You can see Jupyter Event's meta-schema here:

        https://raw.githubusercontent.com/jupyter/jupyter_events/main/jupyter_events/schemas/event-metaschema.yml
    """
def validate(ctx: click.Context, schema: str) -> int:
    """Validate a SCHEMA against Jupyter Event's meta schema.

    SCHEMA can be a JSON/YAML string or filepath to a schema.
    """
