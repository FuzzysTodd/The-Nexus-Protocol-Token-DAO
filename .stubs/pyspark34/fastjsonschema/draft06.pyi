from .draft04 import CodeGeneratorDraft04 as CodeGeneratorDraft04, JSON_TYPE_TO_PYTHON_TYPE as JSON_TYPE_TO_PYTHON_TYPE
from .exceptions import JsonSchemaDefinitionException as JsonSchemaDefinitionException
from .generator import enforce_list as enforce_list
from _typeshed import Incomplete

class CodeGeneratorDraft06(CodeGeneratorDraft04):
    FORMAT_REGEXS: Incomplete
    def __init__(self, definition, resolver: Incomplete | None = None, formats={}, use_default: bool = True) -> None: ...
    def generate_boolean_schema(self) -> None:
        """
        Means that schema can be specified by boolean.
        True means everything is valid, False everything is invalid.
        """
    def generate_type(self) -> None:
        """
        Validation of type. Can be one type or list of types.

        Since draft 06 a float without fractional part is an integer.

        .. code-block:: python

            {'type': 'string'}
            {'type': ['string', 'number']}
        """
    def generate_exclusive_minimum(self) -> None: ...
    def generate_exclusive_maximum(self) -> None: ...
    def generate_property_names(self) -> None:
        """
        Means that keys of object must to follow this definition.

        .. code-block:: python

            {
                'propertyNames': {
                    'maxLength': 3,
                },
            }

        Valid keys of object for this definition are foo, bar, ... but not foobar for example.
        """
    def generate_contains(self) -> None:
        """
        Means that array must contain at least one defined item.

        .. code-block:: python

            {
                'contains': {
                    'type': 'number',
                },
            }

        Valid array is any with at least one number.
        """
    def generate_const(self) -> None:
        """
        Means that value is valid when is equeal to const definition.

        .. code-block:: python

            {
                'const': 42,
            }

        Only valid value is 42 in this example.
        """
