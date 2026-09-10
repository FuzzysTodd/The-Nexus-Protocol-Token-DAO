from .exceptions import JsonSchemaDefinitionException as JsonSchemaDefinitionException
from .generator import CodeGenerator as CodeGenerator, enforce_list as enforce_list
from _typeshed import Incomplete

JSON_TYPE_TO_PYTHON_TYPE: Incomplete
DOLLAR_FINDER: Incomplete

class CodeGeneratorDraft04(CodeGenerator):
    FORMAT_REGEXS: Incomplete
    def __init__(self, definition, resolver: Incomplete | None = None, formats={}, use_default: bool = True) -> None: ...
    @property
    def global_state(self): ...
    def generate_type(self) -> None:
        """
        Validation of type. Can be one type or list of types.

        .. code-block:: python

            {'type': 'string'}
            {'type': ['string', 'number']}
        """
    def generate_enum(self) -> None:
        """
        Means that only value specified in the enum is valid.

        .. code-block:: python

            {
                'enum': ['a', 'b'],
            }
        """
    def generate_all_of(self) -> None:
        """
        Means that value have to be valid by all of those definitions. It's like put it in
        one big definition.

        .. code-block:: python

            {
                'allOf': [
                    {'type': 'number'},
                    {'minimum': 5},
                ],
            }

        Valid values for this definition are 5, 6, 7, ... but not 4 or 'abc' for example.
        """
    def generate_any_of(self) -> None:
        """
        Means that value have to be valid by any of those definitions. It can also be valid
        by all of them.

        .. code-block:: python

            {
                'anyOf': [
                    {'type': 'number', 'minimum': 10},
                    {'type': 'number', 'maximum': 5},
                ],
            }

        Valid values for this definition are 3, 4, 5, 10, 11, ... but not 8 for example.
        """
    def generate_one_of(self) -> None:
        """
        Means that value have to be valid by only one of those definitions. It can't be valid
        by two or more of them.

        .. code-block:: python

            {
                'oneOf': [
                    {'type': 'number', 'multipleOf': 3},
                    {'type': 'number', 'multipleOf': 5},
                ],
            }

        Valid values for this definition are 3, 5, 6, ... but not 15 for example.
        """
    def generate_not(self) -> None:
        """
        Means that value have not to be valid by this definition.

        .. code-block:: python

            {'not': {'type': 'null'}}

        Valid values for this definition are 'hello', 42, {} ... but not None.

        Since draft 06 definition can be boolean. False means nothing, True
        means everything is invalid.
        """
    def generate_min_length(self) -> None: ...
    def generate_max_length(self) -> None: ...
    def generate_pattern(self) -> None: ...
    def generate_format(self) -> None:
        """
        Means that value have to be in specified format. For example date, email or other.

        .. code-block:: python

            {'format': 'email'}

        Valid value for this definition is user@example.com but not @username
        """
    def generate_minimum(self) -> None: ...
    def generate_maximum(self) -> None: ...
    def generate_multiple_of(self) -> None: ...
    def generate_min_items(self) -> None: ...
    def generate_max_items(self) -> None: ...
    def generate_unique_items(self) -> None:
        '''
        With Python 3.4 module ``timeit`` recommended this solutions:

        .. code-block:: python

            >>> timeit.timeit("len(x) > len(set(x))", "x=range(100)+range(100)", number=100000)
            0.5839540958404541
            >>> timeit.timeit("len({}.fromkeys(x)) == len(x)", "x=range(100)+range(100)", number=100000)
            0.7094449996948242
            >>> timeit.timeit("seen = set(); any(i in seen or seen.add(i) for i in x)", "x=range(100)+range(100)", number=100000)
            2.0819358825683594
            >>> timeit.timeit("np.unique(x).size == len(x)", "x=range(100)+range(100); import numpy as np", number=100000)
            2.1439831256866455
        '''
    def generate_items(self) -> None:
        """
        Means array is valid only when all items are valid by this definition.

        .. code-block:: python

            {
                'items': [
                    {'type': 'integer'},
                    {'type': 'string'},
                ],
            }

        Valid arrays are those with integers or strings, nothing else.

        Since draft 06 definition can be also boolean. True means nothing, False
        means everything is invalid.
        """
    def generate_min_properties(self) -> None: ...
    def generate_max_properties(self) -> None: ...
    def generate_required(self) -> None: ...
    def generate_properties(self) -> None:
        """
        Means object with defined keys.

        .. code-block:: python

            {
                'properties': {
                    'key': {'type': 'number'},
                },
            }

        Valid object is containing key called 'key' and value any number.
        """
    def generate_pattern_properties(self) -> None:
        """
        Means object with defined keys as patterns.

        .. code-block:: python

            {
                'patternProperties': {
                    '^x': {'type': 'number'},
                },
            }

        Valid object is containing key starting with a 'x' and value any number.
        """
    def generate_additional_properties(self) -> None:
        """
        Means object with keys with values defined by definition.

        .. code-block:: python

            {
                'properties': {
                    'key': {'type': 'number'},
                }
                'additionalProperties': {'type': 'string'},
            }

        Valid object is containing key called 'key' and it's value any number and
        any other key with any string.
        """
    def generate_dependencies(self) -> None:
        """
        Means when object has property, it needs to have also other property.

        .. code-block:: python

            {
                'dependencies': {
                    'bar': ['foo'],
                },
            }

        Valid object is containing only foo, both bar and foo or none of them, but not
        object with only bar.

        Since draft 06 definition can be boolean or empty array. True and empty array
        means nothing, False means that key cannot be there at all.
        """
