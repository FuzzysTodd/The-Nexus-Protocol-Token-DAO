import dataclasses
import enum
from _typeshed import Incomplete
from torch.onnx._internal.diagnostics.infra import formatter as formatter, sarif as sarif
from typing import List, Mapping, Sequence, Tuple

class Level(enum.Enum):
    """The level of a diagnostic.

    This class is used to represent the level of a diagnostic. The levels are defined
    by the SARIF specification, and are not modifiable. For alternative categories,
    please use infra.Tag instead. When selecting a level, please consider the following
    guidelines:

    - NONE: Informational result that does not indicate the presence of a problem.
    - NOTE: An opportunity for improvement was found.
    - WARNING: A potential problem was found.
    - ERROR: A serious problem was found.
    """
    NONE: Incomplete
    NOTE: Incomplete
    WARNING: Incomplete
    ERROR: Incomplete
levels = Level

class Tag(enum.Enum):
    """The tag of a diagnostic. This class can be inherited to define custom tags."""

class PatchedPropertyBag(sarif.PropertyBag):
    '''Key/value pairs that provide additional information about the object.

    The definition of PropertyBag via SARIF spec is "A property bag is an object (§3.6)
    containing an unordered set of properties with arbitrary names." However it is not
    reflected in the json file, and therefore not captured by the python representation.
    This patch adds additional **kwargs to the `__init__` method to allow recording
    arbitrary key/value pairs.
    '''
    def __init__(self, tags: List[str] | None = None, **kwargs) -> None: ...

@dataclasses.dataclass(frozen=True)
class Rule:
    id: str
    name: str
    message_default_template: str
    short_description: str | None = ...
    full_description: str | None = ...
    full_description_markdown: str | None = ...
    help_uri: str | None = ...
    @classmethod
    def from_sarif(cls, **kwargs):
        """Returns a rule from the SARIF reporting descriptor."""
    def sarif(self) -> sarif.ReportingDescriptor:
        """Returns a SARIF reporting descriptor of this Rule."""
    def format(self, level: Level, *args, **kwargs) -> Tuple[Rule, Level, str]:
        """Returns a tuple of (rule, level, message) for a diagnostic.

        This method is used to format the message of a diagnostic. The message is
        formatted using the default template of this rule, and the arguments passed in
        as `*args` and `**kwargs`. The level is used to override the default level of
        this rule.
        """
    def format_message(self, *args, **kwargs) -> str:
        """Returns the formatted default message of this Rule.

        This method should be overridden (with code generation) by subclasses to reflect
        the exact arguments needed by the message template. This is a helper method to
        create the default message for a diagnostic.
        """
    def pretty_print(self) -> None: ...
    def __init__(self, id, name, message_default_template, short_description, full_description, full_description_markdown, help_uri) -> None: ...

@dataclasses.dataclass
class Location:
    uri: str | None = ...
    line: int | None = ...
    message: str | None = ...
    start_column: int | None = ...
    end_column: int | None = ...
    snippet: str | None = ...
    function: str | None = ...
    def sarif(self) -> sarif.Location:
        """Returns the SARIF representation of this location."""
    def pretty_print(self) -> None:
        """Prints the location in a traceback style format."""
    def __init__(self, uri, line, message, start_column, end_column, snippet, function) -> None: ...

@dataclasses.dataclass
class StackFrame:
    location: Location
    def sarif(self) -> sarif.StackFrame:
        """Returns the SARIF representation of this stack frame."""
    def pretty_print(self) -> None:
        """Prints the stack frame in a human-readable format."""
    def __init__(self, location) -> None: ...

@dataclasses.dataclass
class Stack:
    """Records a stack trace. The top of the stack is the first element in the list."""
    frames: List[StackFrame] = ...
    message: str | None = ...
    def sarif(self) -> sarif.Stack:
        """Returns the SARIF representation of this stack."""
    def pretty_print(self) -> None:
        """Prints the stack in a human-readable format."""
    def __init__(self, frames, message) -> None: ...

@dataclasses.dataclass
class ThreadFlowLocation:
    """Records code location and the initial state."""
    location: Location
    state: Mapping[str, str]
    index: int
    stack: Stack | None = ...
    def sarif(self) -> sarif.ThreadFlowLocation:
        """Returns the SARIF representation of this thread flow location."""
    def pretty_print(self, verbose: bool = False):
        """Prints the thread flow location in a human-readable format."""
    def __init__(self, location, state, index, stack) -> None: ...

@dataclasses.dataclass
class Graph:
    """A graph of diagnostics.

    This class stores the string representation of a model graph.
    The `nodes` and `edges` fields are unused in the current implementation.
    """
    graph: str
    name: str
    description: str | None = ...
    def sarif(self) -> sarif.Graph:
        """Returns the SARIF representation of this graph."""
    def pretty_print(self, verbose: bool = False):
        """Prints the diagnostics in a human-readable format.

        Args:
            verbose: If True, prints all information. Otherwise, only prints compact
                information. E.g., graph name and description.
            log_level: The minimum level of diagnostics to print.
        """
    def __init__(self, graph, name, description) -> None: ...

@dataclasses.dataclass
class RuleCollection:
    def __post_init__(self) -> None: ...
    def __contains__(self, rule: Rule) -> bool:
        """Checks if the rule is in the collection."""
    @classmethod
    def custom_collection_from_list(cls, new_collection_class_name: str, rules: Sequence[Rule]) -> RuleCollection:
        """Creates a custom class inherited from RuleCollection with the list of rules."""
    def __init__(self) -> None: ...

class Invocation:
    def __init__(self) -> None: ...

@dataclasses.dataclass
class DiagnosticOptions:
    """
    Options for diagnostic context.
    """
    log_verbose: bool = ...
    log_level: Level = ...
    def __init__(self, log_verbose, log_level) -> None: ...
