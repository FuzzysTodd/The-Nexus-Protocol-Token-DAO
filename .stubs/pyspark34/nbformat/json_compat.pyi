from _typeshed import Incomplete

class JsonSchemaValidator:
    """A json schema validator."""
    name: str
    def __init__(self, schema) -> None:
        """Initialize the validator."""
    def validate(self, data) -> None:
        """Validate incoming data."""
    def iter_errors(self, data, schema: Incomplete | None = None):
        """Iterate over errors in incoming data."""
    def error_tree(self, errors):
        """Create an error tree for the errors."""

class FastJsonSchemaValidator(JsonSchemaValidator):
    """A schema validator using fastjsonschema."""
    name: str
    def __init__(self, schema) -> None:
        """Initialize the validator."""
    def validate(self, data) -> None:
        """Validate incoming data."""
    def iter_errors(self, data, schema: Incomplete | None = None):
        """Iterate over errors in incoming data."""
    def error_tree(self, errors) -> None:
        """Create an error tree for the errors."""

VALIDATORS: Incomplete

def get_current_validator():
    """
    Return the default validator based on the value of an environment variable.
    """
