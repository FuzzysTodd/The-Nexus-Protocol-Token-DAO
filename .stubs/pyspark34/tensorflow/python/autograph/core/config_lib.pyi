import enum

class Rule:
    """Base class for conversion rules."""
    def __init__(self, module_prefix) -> None: ...
    def matches(self, module_name): ...

class Action(enum.Enum):
    NONE: int
    CONVERT: int
    DO_NOT_CONVERT: int

class DoNotConvert(Rule):
    """Indicates that this module should be not converted."""
    def get_action(self, module): ...

class Convert(Rule):
    """Indicates that this module should be converted."""
    def get_action(self, module): ...
