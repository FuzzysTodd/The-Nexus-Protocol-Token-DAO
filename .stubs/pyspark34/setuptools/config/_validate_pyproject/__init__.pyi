from .error_reporting import ValidationError as ValidationError
from .extra_validations import EXTRA_VALIDATIONS as EXTRA_VALIDATIONS
from .fastjsonschema_exceptions import JsonSchemaException as JsonSchemaException, JsonSchemaValueException as JsonSchemaValueException
from typing import Any, Callable, Dict

__all__ = ['validate', 'FORMAT_FUNCTIONS', 'EXTRA_VALIDATIONS', 'ValidationError', 'JsonSchemaException', 'JsonSchemaValueException']

FORMAT_FUNCTIONS: Dict[str, Callable[[str], bool]]

def validate(data: Any) -> bool:
    """Validate the given ``data`` object using JSON Schema
    This function raises ``ValidationError`` if ``data`` is invalid.
    """
