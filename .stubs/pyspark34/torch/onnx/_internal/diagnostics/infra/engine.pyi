import dataclasses
from torch.onnx._internal.diagnostics import infra as infra
from torch.onnx._internal.diagnostics.infra import formatter as formatter, sarif as sarif, utils as utils
from typing import Callable, Generator, List, Mapping, Type

class DiagnosticError(RuntimeError): ...

@dataclasses.dataclass
class Diagnostic:
    rule: infra.Rule
    level: infra.Level
    message: str | None = ...
    locations: List[infra.Location] = ...
    stacks: List[infra.Stack] = ...
    graphs: List[infra.Graph] = ...
    thread_flow_locations: List[infra.ThreadFlowLocation] = ...
    additional_message: str | None = ...
    tags: List[infra.Tag] = ...
    def sarif(self) -> sarif.Result:
        """Returns the SARIF Result representation of this diagnostic."""
    def with_location(self, location: infra.Location) -> _Diagnostic:
        """Adds a location to the diagnostic."""
    def with_thread_flow_location(self, location: infra.ThreadFlowLocation) -> _Diagnostic:
        """Adds a thread flow location to the diagnostic."""
    def with_stack(self, stack: infra.Stack) -> _Diagnostic:
        """Adds a stack to the diagnostic."""
    def with_graph(self, graph: infra.Graph) -> _Diagnostic:
        """Adds a graph to the diagnostic."""
    def with_additional_message(self, message: str) -> _Diagnostic:
        """Adds an additional message to the diagnostic."""
    def record_python_call_stack(self, frames_to_skip: int) -> infra.Stack:
        """Records the current Python call stack."""
    def record_python_call(self, fn: Callable, state: Mapping[str, str], message: str | None = None, frames_to_skip: int = 0) -> infra.ThreadFlowLocation:
        """Records a python call as one thread flow step."""
    def pretty_print(self, verbose: bool = False, log_level: infra.Level = ...):
        """Prints the diagnostics in a human-readable format.

        Args:
            verbose: If True, prints all information. E.g. stack frames, graphs, etc.
                Otherwise, only prints compact information. E.g., rule name and display message.
            log_level: The minimum level of diagnostics to print.
        """
    def __init__(self, rule, level, message, locations, stacks, graphs, thread_flow_locations, additional_message, tags) -> None: ...

@dataclasses.dataclass
class DiagnosticContext:
    name: str
    version: str
    options: infra.DiagnosticOptions = ...
    diagnostic_type: Type[Diagnostic] = ...
    diagnostics: List[Diagnostic] = ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def sarif(self) -> sarif.Run:
        """Returns the SARIF Run object."""
    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        """Adds a diagnostic to the context.

        Use this method to add diagnostics that are not created by the context.
        Args:
            diagnostic: The diagnostic to add.
        """
    def add_inflight_diagnostic(self, diagnostic: Diagnostic) -> Generator[Diagnostic, None, None]:
        """Adds a diagnostic to the context.

        Use this method to add diagnostics that are not created by the context.
        Args:
            diagnostic: The diagnostic to add.
        """
    def diagnose(self, rule: infra.Rule, level: infra.Level, message: str | None = None, **kwargs) -> Diagnostic:
        """Creates a diagnostic for the given arguments.

        Args:
            rule: The rule that triggered the diagnostic.
            level: The level of the diagnostic.
            message: The message of the diagnostic.
            **kwargs: Additional arguments to pass to the Diagnostic constructor.

        Returns:
            The created diagnostic.

        Raises:
            ValueError: If the rule is not supported by the tool.
        """
    def push_inflight_diagnostic(self, diagnostic: Diagnostic) -> None:
        """Pushes a diagnostic to the inflight diagnostics stack.

        Args:
            diagnostic: The diagnostic to push.

        Raises:
            ValueError: If the rule is not supported by the tool.
        """
    def pop_inflight_diagnostic(self) -> Diagnostic:
        """Pops the last diagnostic from the inflight diagnostics stack.

        Returns:
            The popped diagnostic.
        """
    def inflight_diagnostic(self, rule: infra.Rule | None = None) -> Diagnostic: ...
    def pretty_print(self, verbose: bool | None = None, log_level: infra.Level | None = None) -> None:
        """Prints the diagnostics in a human-readable format.

        Args:
            verbose: Whether to print the diagnostics in verbose mode. See Diagnostic.pretty_print.
                If not specified, uses the value of 'self.options.log_verbose'.
            log_level: The minimum level of diagnostics to print.
                If not specified, uses the value of 'self.options.log_level'.
        """
    def __init__(self, name, version, options, diagnostic_type) -> None: ...

class DiagnosticEngine:
    '''A generic diagnostic engine based on SARIF.

    This class is the main interface for diagnostics. It manages the creation of diagnostic contexts.
    A DiagnosticContext provides the entry point for recording Diagnostics.
    See infra.DiagnosticContext for more details.

    Examples:
        Step 1: Create a set of rules.
        >>> # xdoctest: +REQUIRES(module:torch._C._distributed_c10d)
        >>> rules = infra.RuleCollection.custom_collection_from_list(
        ...     "CustomRuleCollection",
        ...     [
        ...         infra.Rule(
        ...             id="r1",
        ...             name="rule-1",
        ...             message_default_template="Mising xxx",
        ...         ),
        ...     ],
        ... )

        Step 2: Create a diagnostic engine.
        >>> engine = DiagnosticEngine()

        Step 3: Start a new diagnostic context.
        >>> with engine.create_diagnostic_context("torch.onnx.export", version="1.0") as context:
        ...     ...

        Step 4: Add diagnostics in your code.
        ...     context.diagnose(rules.rule1, infra.Level.ERROR)

        Step 5: Afterwards, get the SARIF log.
        >>> sarif_log = engine.sarif_log()
    '''
    contexts: List[DiagnosticContext]
    def __init__(self) -> None: ...
    def sarif_log(self) -> sarif.SarifLog: ...
    def to_json(self) -> str: ...
    def dump(self, file_path: str, compress: bool = False) -> None:
        """Dumps the SARIF log to a file."""
    def clear(self) -> None:
        """Clears all diagnostic contexts."""
    def create_diagnostic_context(self, name: str, version: str, options: infra.DiagnosticOptions | None = None, diagnostic_type: Type[Diagnostic] = ...) -> DiagnosticContext:
        """Creates a new diagnostic context.

        Args:
            name: The subject name for the diagnostic context.
            version: The subject version for the diagnostic context.
            options: The options for the diagnostic context.

        Returns:
            A new diagnostic context.
        """
    def pretty_print(self, verbose: bool = False, level: infra.Level = ...) -> None:
        """Pretty prints all diagnostics in the diagnostic contexts.

        Args:
            verbose: Whether to print the diagnostics in verbose mode. See Diagnostic.pretty_print.
            level: The minimum level of diagnostics to print.
        """
