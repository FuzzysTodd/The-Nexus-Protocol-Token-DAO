from .fastjsonschema_exceptions import JsonSchemaValueException as JsonSchemaValueException
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Dict, List, Sequence

class ValidationError(JsonSchemaValueException):
    """Report violations of a given JSON schema.

    This class extends :exc:`~fastjsonschema.JsonSchemaValueException`
    by adding the following properties:

    - ``summary``: an improved version of the ``JsonSchemaValueException`` error message
      with only the necessary information)

    - ``details``: more contextual information about the error like the failing schema
      itself and the value that violates the schema.

    Depending on the level of the verbosity of the ``logging`` configuration
    the exception message will be only ``summary`` (default) or a combination of
    ``summary`` and ``details`` (when the logging level is set to :obj:`logging.DEBUG`).
    """
    summary: str
    details: str

def detailed_errors() -> Generator[None, None, None]: ...

class _ErrorFormatting:
    ex: Incomplete
    name: Incomplete
    def __init__(self, ex: JsonSchemaValueException) -> None: ...
    @property
    def summary(self) -> str: ...
    @property
    def details(self) -> str: ...

class _SummaryWriter:
    jargon: Incomplete
    def __init__(self, jargon: Dict[str, str] | None = None) -> None: ...
    def __call__(self, schema: dict | List[dict], prefix: str = '', *, _path: Sequence[str] = ()) -> str: ...
