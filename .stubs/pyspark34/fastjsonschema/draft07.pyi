from .draft06 import CodeGeneratorDraft06 as CodeGeneratorDraft06
from _typeshed import Incomplete

class CodeGeneratorDraft07(CodeGeneratorDraft06):
    FORMAT_REGEXS: Incomplete
    def __init__(self, definition, resolver: Incomplete | None = None, formats={}, use_default: bool = True) -> None: ...
    def generate_if_then_else(self) -> None:
        """
        Implementation of if-then-else.

        .. code-block:: python

            {
                'if': {
                    'exclusiveMaximum': 0,
                },
                'then': {
                    'minimum': -10,
                },
                'else': {
                    'multipleOf': 2,
                },
            }

        Valid values are any between -10 and 0 or any multiplication of two.
        """
    def generate_content_encoding(self) -> None:
        """
        Means decoding value when it's encoded by base64.

        .. code-block:: python

            {
                'contentEncoding': 'base64',
            }
        """
    def generate_content_media_type(self) -> None:
        """
        Means loading value when it's specified as JSON.

        .. code-block:: python

            {
                'contentMediaType': 'application/json',
            }
        """
