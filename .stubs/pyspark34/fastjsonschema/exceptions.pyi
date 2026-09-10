from _typeshed import Incomplete

SPLIT_RE: Incomplete

class JsonSchemaException(ValueError):
    """
    Base exception of ``fastjsonschema`` library.
    """

class JsonSchemaValueException(JsonSchemaException):
    """
    Exception raised by validation function. Available properties:

     * ``message`` containing human-readable information what is wrong (e.g. ``data.property[index] must be smaller than or equal to 42``),
     * invalid ``value`` (e.g. ``60``),
     * ``name`` of a path in the data structure (e.g. ``data.property[index]``),
     * ``path`` as an array in the data structure (e.g. ``['data', 'property', 'index']``),
     * the whole ``definition`` which the ``value`` has to fulfil (e.g. ``{'type': 'number', 'maximum': 42}``),
     * ``rule`` which the ``value`` is breaking (e.g. ``maximum``)
     * and ``rule_definition`` (e.g. ``42``).

    .. versionchanged:: 2.14.0
        Added all extra properties.
    """
    message: Incomplete
    value: Incomplete
    name: Incomplete
    definition: Incomplete
    rule: Incomplete
    def __init__(self, message, value: Incomplete | None = None, name: Incomplete | None = None, definition: Incomplete | None = None, rule: Incomplete | None = None) -> None: ...
    @property
    def path(self): ...
    @property
    def rule_definition(self): ...

class JsonSchemaDefinitionException(JsonSchemaException):
    """
    Exception raised by generator of validation function.
    """
