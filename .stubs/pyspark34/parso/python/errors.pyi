from _typeshed import Incomplete
from collections.abc import Generator
from parso.normalizer import Issue as Issue, Normalizer as Normalizer, NormalizerConfig as NormalizerConfig, Rule as Rule

ALLOWED_FUTURES: Incomplete

class _Context:
    node: Incomplete
    blocks: Incomplete
    parent_context: Incomplete
    def __init__(self, node, add_syntax_error, parent_context: Incomplete | None = None) -> None: ...
    def is_async_funcdef(self): ...
    def is_function(self): ...
    def add_name(self, name) -> None: ...
    def finalize(self):
        """
        Returns a list of nonlocal names that need to be part of that scope.
        """
    def add_block(self, node) -> Generator[None, None, None]: ...
    def add_context(self, node): ...
    def close_child_context(self, child_context) -> None: ...

class ErrorFinder(Normalizer):
    """
    Searches for errors in the syntax tree.
    """
    version: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    context: Incomplete
    def initialize(self, node): ...
    def visit(self, node): ...
    def visit_node(self, node) -> Generator[None, None, None]: ...
    def visit_leaf(self, leaf): ...
    def add_issue(self, node, code, message) -> None: ...
    def finalize(self) -> None: ...

class IndentationRule(Rule):
    code: int

class _ExpectIndentedBlock(IndentationRule):
    message: str
    def get_node(self, node): ...
    def is_issue(self, node): ...

class ErrorFinderConfig(NormalizerConfig):
    normalizer_class = ErrorFinder

class SyntaxRule(Rule):
    code: int

class _InvalidSyntaxRule(SyntaxRule):
    message: str
    fstring_message: str
    def get_node(self, node): ...
    def is_issue(self, node): ...

class _AwaitOutsideAsync(SyntaxRule):
    message: str
    def is_issue(self, leaf): ...
    def get_error_node(self, node): ...

class _BreakOutsideLoop(SyntaxRule):
    message: str
    def is_issue(self, leaf): ...

class _ContinueChecks(SyntaxRule):
    message: str
    message_in_finally: str
    def is_issue(self, leaf): ...

class _YieldFromCheck(SyntaxRule):
    message: str
    def get_node(self, leaf): ...
    def is_issue(self, leaf): ...

class _NameChecks(SyntaxRule):
    message: str
    message_none: str
    def is_issue(self, leaf): ...

class _StringChecks(SyntaxRule):
    message: str
    def is_issue(self, leaf): ...

class _StarCheck(SyntaxRule):
    message: str
    def is_issue(self, leaf): ...

class _StarStarCheck(SyntaxRule):
    message: str
    def is_issue(self, leaf): ...

class _ReturnAndYieldChecks(SyntaxRule):
    message: str
    message_async_yield: str
    def get_node(self, leaf): ...
    def is_issue(self, leaf): ...

class _BytesAndStringMix(SyntaxRule):
    message: str
    def is_issue(self, node): ...

class _TrailingImportComma(SyntaxRule):
    message: str
    def is_issue(self, node): ...

class _ImportStarInFunction(SyntaxRule):
    message: str
    def is_issue(self, node): ...

class _FutureImportRule(SyntaxRule):
    message: str
    def is_issue(self, node): ...

class _StarExprRule(SyntaxRule):
    message_iterable_unpacking: str
    def is_issue(self, node): ...

class _StarExprParentRule(SyntaxRule):
    def is_issue(self, node): ...

class _AnnotatorRule(SyntaxRule):
    message: str
    def get_node(self, node): ...
    def is_issue(self, node): ...

class _ArgumentRule(SyntaxRule):
    def is_issue(self, node) -> None: ...

class _NonlocalModuleLevelRule(SyntaxRule):
    message: str
    def is_issue(self, node): ...

class _ArglistRule(SyntaxRule):
    @property
    def message(self): ...
    def is_issue(self, node): ...

class _ParameterRule(SyntaxRule):
    message: str
    def is_issue(self, node): ...

class _TryStmtRule(SyntaxRule):
    message: str
    def is_issue(self, try_stmt) -> None: ...

class _FStringRule(SyntaxRule):
    message_expr: str
    message_nested: str
    message_conversion: str
    def is_issue(self, fstring) -> None: ...

class _CheckAssignmentRule(SyntaxRule): ...

class _CompForRule(_CheckAssignmentRule):
    message: str
    def is_issue(self, node): ...

class _ExprStmtRule(_CheckAssignmentRule):
    message: str
    extended_message: Incomplete
    def is_issue(self, node): ...

class _WithItemRule(_CheckAssignmentRule):
    def is_issue(self, with_item) -> None: ...

class _DelStmtRule(_CheckAssignmentRule):
    def is_issue(self, del_stmt) -> None: ...

class _ExprListRule(_CheckAssignmentRule):
    def is_issue(self, expr_list) -> None: ...

class _ForStmtRule(_CheckAssignmentRule):
    def is_issue(self, for_stmt) -> None: ...

class _NamedExprRule(_CheckAssignmentRule):
    def is_issue(self, namedexpr_test): ...
