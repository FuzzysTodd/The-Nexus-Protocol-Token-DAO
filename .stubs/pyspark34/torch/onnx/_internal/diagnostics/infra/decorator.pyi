from _typeshed import Incomplete
from torch.onnx._internal.diagnostics import infra as infra
from torch.onnx._internal.diagnostics.infra import formatter as formatter, utils as utils
from typing import Any, Callable, Dict, Tuple, Type

MessageFormatterType = Callable[[Callable, Tuple[Any, ...], Dict[str, Any]], str]

def format_message_in_text(fn: Callable, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> str: ...
def format_exception_in_markdown(exception: Exception) -> str: ...
def format_function_signature_in_markdown(fn: Callable, args: Tuple[Any, ...], kwargs: Dict[str, Any], format_argument: Callable[[Any], str] = ...) -> str: ...
def format_return_values_in_markdown(return_values: Any, format_argument: Callable[[Any], str] = ...) -> str: ...

ModifierCallableType: Incomplete

def modify_diagnostic(diag: infra.Diagnostic, fn: Callable, args: Tuple[Any, ...], kwargs: Dict[str, Any], return_values: Any) -> None: ...
def diagnose_call(get_context: Callable[[], infra.DiagnosticContext | None], rule: infra.Rule, level: infra.Level = ..., exception_report_level: infra.Level = ..., diagnostic_type: Type[infra.Diagnostic] = ..., format_argument: Callable[[Any], str] = ..., diagnostic_message_formatter: MessageFormatterType = ..., diagnostic_modifier: ModifierCallableType = ..., report_criterion: Callable[[Callable, Tuple[Any, ...], Dict[str, Any], Any], bool] = ...) -> Callable: ...
def diagnose_step(get_context: Callable[[], infra.DiagnosticContext | None], rule: infra.Rule | None = None, message_formatter: MessageFormatterType = ..., format_argument: Callable[[Any], str] = ...) -> Callable:
    """Decorator to log a step in the inflight diagnostic.

    Args:
        get_context: A function that returns the diagnostic context where inflight
            diagnostic is retrieved and modified by the decorator.
        rule: The decorator logs this step to the top inflight diagnostic that matches
            the rule. If None, the top inflight diagnostic in the stack will be picked,
            regardless of its rule.

    Returns:
        A decorator that logs a step in the inflight diagnostic.
    """
