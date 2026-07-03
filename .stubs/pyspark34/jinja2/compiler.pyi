import typing as t
import typing_extensions as te
from . import nodes as nodes
from .environment import Environment as Environment
from .exceptions import TemplateAssertionError as TemplateAssertionError
from .idtracking import Symbols as Symbols, VAR_LOAD_ALIAS as VAR_LOAD_ALIAS, VAR_LOAD_PARAMETER as VAR_LOAD_PARAMETER, VAR_LOAD_RESOLVE as VAR_LOAD_RESOLVE, VAR_LOAD_UNDEFINED as VAR_LOAD_UNDEFINED
from .nodes import EvalContext as EvalContext
from .optimizer import Optimizer as Optimizer
from .utils import concat as concat
from .visitor import NodeVisitor as NodeVisitor
from _typeshed import Incomplete

F = t.TypeVar('F', bound=t.Callable[..., t.Any])
operators: Incomplete

def optimizeconst(f: F) -> F: ...
def generate(node: nodes.Template, environment: Environment, name: str | None, filename: str | None, stream: t.TextIO | None = None, defer_init: bool = False, optimized: bool = True) -> str | None:
    """Generate the python source for a node tree."""
def has_safe_repr(value: t.Any) -> bool:
    """Does the node have a safe representation?"""
def find_undeclared(nodes: t.Iterable[nodes.Node], names: t.Iterable[str]) -> t.Set[str]:
    """Check if the names passed are accessed undeclared.  The return value
    is a set of all the undeclared names from the sequence of names found.
    """

class MacroRef:
    node: Incomplete
    accesses_caller: bool
    accesses_kwargs: bool
    accesses_varargs: bool
    def __init__(self, node: nodes.Macro | nodes.CallBlock) -> None: ...

class Frame:
    """Holds compile time information for us."""
    eval_ctx: Incomplete
    parent: Incomplete
    symbols: Incomplete
    require_output_check: bool
    buffer: Incomplete
    block: Incomplete
    toplevel: bool
    rootlevel: bool
    loop_frame: bool
    block_frame: bool
    soft_frame: bool
    def __init__(self, eval_ctx: EvalContext, parent: Frame | None = None, level: int | None = None) -> None: ...
    def copy(self) -> Frame:
        """Create a copy of the current one."""
    def inner(self, isolated: bool = False) -> Frame:
        """Return an inner frame."""
    def soft(self) -> Frame:
        """Return a soft frame.  A soft frame may not be modified as
        standalone thing as it shares the resources with the frame it
        was created of, but it's not a rootlevel frame any longer.

        This is only used to implement if-statements and conditional
        expressions.
        """
    __copy__ = copy

class VisitorExit(RuntimeError):
    """Exception used by the `UndeclaredNameVisitor` to signal a stop."""

class DependencyFinderVisitor(NodeVisitor):
    """A visitor that collects filter and test calls."""
    filters: Incomplete
    tests: Incomplete
    def __init__(self) -> None: ...
    def visit_Filter(self, node: nodes.Filter) -> None: ...
    def visit_Test(self, node: nodes.Test) -> None: ...
    def visit_Block(self, node: nodes.Block) -> None:
        """Stop visiting at blocks."""

class UndeclaredNameVisitor(NodeVisitor):
    """A visitor that checks if a name is accessed without being
    declared.  This is different from the frame visitor as it will
    not stop at closure frames.
    """
    names: Incomplete
    undeclared: Incomplete
    def __init__(self, names: t.Iterable[str]) -> None: ...
    def visit_Name(self, node: nodes.Name) -> None: ...
    def visit_Block(self, node: nodes.Block) -> None:
        """Stop visiting a blocks."""

class CompilerExit(Exception):
    """Raised if the compiler encountered a situation where it just
    doesn't make sense to further process the code.  Any block that
    raises such an exception is not further processed.
    """

class CodeGenerator(NodeVisitor):
    environment: Incomplete
    name: Incomplete
    filename: Incomplete
    stream: Incomplete
    created_block_context: bool
    defer_init: Incomplete
    optimizer: Incomplete
    import_aliases: Incomplete
    blocks: Incomplete
    extends_so_far: int
    has_known_extends: bool
    code_lineno: int
    tests: Incomplete
    filters: Incomplete
    debug_info: Incomplete
    def __init__(self, environment: Environment, name: str | None, filename: str | None, stream: t.TextIO | None = None, defer_init: bool = False, optimized: bool = True) -> None: ...
    @property
    def optimized(self) -> bool: ...
    def fail(self, msg: str, lineno: int) -> te.NoReturn:
        """Fail with a :exc:`TemplateAssertionError`."""
    def temporary_identifier(self) -> str:
        """Get a new unique identifier."""
    def buffer(self, frame: Frame) -> None:
        """Enable buffering for the frame from that point onwards."""
    def return_buffer_contents(self, frame: Frame, force_unescaped: bool = False) -> None:
        """Return the buffer contents of the frame."""
    def indent(self) -> None:
        """Indent by one."""
    def outdent(self, step: int = 1) -> None:
        """Outdent by step."""
    def start_write(self, frame: Frame, node: nodes.Node | None = None) -> None:
        """Yield or write into the frame buffer."""
    def end_write(self, frame: Frame) -> None:
        """End the writing process started by `start_write`."""
    def simple_write(self, s: str, frame: Frame, node: nodes.Node | None = None) -> None:
        """Simple shortcut for start_write + write + end_write."""
    def blockvisit(self, nodes: t.Iterable[nodes.Node], frame: Frame) -> None:
        """Visit a list of nodes as block in a frame.  If the current frame
        is no buffer a dummy ``if 0: yield None`` is written automatically.
        """
    def write(self, x: str) -> None:
        """Write a string into the output stream."""
    def writeline(self, x: str, node: nodes.Node | None = None, extra: int = 0) -> None:
        """Combination of newline and write."""
    def newline(self, node: nodes.Node | None = None, extra: int = 0) -> None:
        """Add one or more newlines before the next write."""
    def signature(self, node: nodes.Call | nodes.Filter | nodes.Test, frame: Frame, extra_kwargs: t.Mapping[str, t.Any] | None = None) -> None:
        """Writes a function call to the stream for the current node.
        A leading comma is added automatically.  The extra keyword
        arguments may not include python keywords otherwise a syntax
        error could occur.  The extra keyword arguments should be given
        as python dict.
        """
    def pull_dependencies(self, nodes: t.Iterable[nodes.Node]) -> None:
        """Find all filter and test names used in the template and
        assign them to variables in the compiled namespace. Checking
        that the names are registered with the environment is done when
        compiling the Filter and Test nodes. If the node is in an If or
        CondExpr node, the check is done at runtime instead.

        .. versionchanged:: 3.0
            Filters and tests in If and CondExpr nodes are checked at
            runtime instead of compile time.
        """
    def enter_frame(self, frame: Frame) -> None: ...
    def leave_frame(self, frame: Frame, with_python_scope: bool = False) -> None: ...
    def choose_async(self, async_value: str = 'async ', sync_value: str = '') -> str: ...
    def func(self, name: str) -> str: ...
    def macro_body(self, node: nodes.Macro | nodes.CallBlock, frame: Frame) -> t.Tuple[Frame, MacroRef]:
        """Dump the function def of a macro or call block."""
    def macro_def(self, macro_ref: MacroRef, frame: Frame) -> None:
        """Dump the macro definition for the def created by macro_body."""
    def position(self, node: nodes.Node) -> str:
        """Return a human readable position for the node."""
    def dump_local_context(self, frame: Frame) -> str: ...
    def write_commons(self) -> None:
        """Writes a common preamble that is used by root and block functions.
        Primarily this sets up common local helpers and enforces a generator
        through a dead branch.
        """
    def push_parameter_definitions(self, frame: Frame) -> None:
        """Pushes all parameter targets from the given frame into a local
        stack that permits tracking of yet to be assigned parameters.  In
        particular this enables the optimization from `visit_Name` to skip
        undefined expressions for parameters in macros as macros can reference
        otherwise unbound parameters.
        """
    def pop_parameter_definitions(self) -> None:
        """Pops the current parameter definitions set."""
    def mark_parameter_stored(self, target: str) -> None:
        """Marks a parameter in the current parameter definitions as stored.
        This will skip the enforced undefined checks.
        """
    def push_context_reference(self, target: str) -> None: ...
    def pop_context_reference(self) -> None: ...
    def get_context_ref(self) -> str: ...
    def get_resolve_func(self) -> str: ...
    def derive_context(self, frame: Frame) -> str: ...
    def parameter_is_undeclared(self, target: str) -> bool:
        """Checks if a given target is an undeclared parameter."""
    def push_assign_tracking(self) -> None:
        """Pushes a new layer for assignment tracking."""
    def pop_assign_tracking(self, frame: Frame) -> None:
        """Pops the topmost level for assignment tracking and updates the
        context variables if necessary.
        """
    def visit_Template(self, node: nodes.Template, frame: Frame | None = None) -> None: ...
    def visit_Block(self, node: nodes.Block, frame: Frame) -> None:
        """Call a block and register it for the template."""
    def visit_Extends(self, node: nodes.Extends, frame: Frame) -> None:
        """Calls the extender."""
    def visit_Include(self, node: nodes.Include, frame: Frame) -> None:
        """Handles includes."""
    def visit_Import(self, node: nodes.Import, frame: Frame) -> None:
        """Visit regular imports."""
    def visit_FromImport(self, node: nodes.FromImport, frame: Frame) -> None:
        """Visit named imports."""
    def visit_For(self, node: nodes.For, frame: Frame) -> None: ...
    def visit_If(self, node: nodes.If, frame: Frame) -> None: ...
    def visit_Macro(self, node: nodes.Macro, frame: Frame) -> None: ...
    def visit_CallBlock(self, node: nodes.CallBlock, frame: Frame) -> None: ...
    def visit_FilterBlock(self, node: nodes.FilterBlock, frame: Frame) -> None: ...
    def visit_With(self, node: nodes.With, frame: Frame) -> None: ...
    def visit_ExprStmt(self, node: nodes.ExprStmt, frame: Frame) -> None: ...
    class _FinalizeInfo(t.NamedTuple):
        const: t.Callable[..., str] | None
        src: str | None
    def visit_Output(self, node: nodes.Output, frame: Frame) -> None: ...
    def visit_Assign(self, node: nodes.Assign, frame: Frame) -> None: ...
    def visit_AssignBlock(self, node: nodes.AssignBlock, frame: Frame) -> None: ...
    def visit_Name(self, node: nodes.Name, frame: Frame) -> None: ...
    def visit_NSRef(self, node: nodes.NSRef, frame: Frame) -> None: ...
    def visit_Const(self, node: nodes.Const, frame: Frame) -> None: ...
    def visit_TemplateData(self, node: nodes.TemplateData, frame: Frame) -> None: ...
    def visit_Tuple(self, node: nodes.Tuple, frame: Frame) -> None: ...
    def visit_List(self, node: nodes.List, frame: Frame) -> None: ...
    def visit_Dict(self, node: nodes.Dict, frame: Frame) -> None: ...
    visit_Add: Incomplete
    visit_Sub: Incomplete
    visit_Mul: Incomplete
    visit_Div: Incomplete
    visit_FloorDiv: Incomplete
    visit_Pow: Incomplete
    visit_Mod: Incomplete
    visit_And: Incomplete
    visit_Or: Incomplete
    visit_Pos: Incomplete
    visit_Neg: Incomplete
    visit_Not: Incomplete
    def visit_Concat(self, node: nodes.Concat, frame: Frame) -> None: ...
    def visit_Compare(self, node: nodes.Compare, frame: Frame) -> None: ...
    def visit_Operand(self, node: nodes.Operand, frame: Frame) -> None: ...
    def visit_Getattr(self, node: nodes.Getattr, frame: Frame) -> None: ...
    def visit_Getitem(self, node: nodes.Getitem, frame: Frame) -> None: ...
    def visit_Slice(self, node: nodes.Slice, frame: Frame) -> None: ...
    def visit_Filter(self, node: nodes.Filter, frame: Frame) -> None: ...
    def visit_Test(self, node: nodes.Test, frame: Frame) -> None: ...
    def visit_CondExpr(self, node: nodes.CondExpr, frame: Frame) -> None: ...
    def visit_Call(self, node: nodes.Call, frame: Frame, forward_caller: bool = False) -> None: ...
    def visit_Keyword(self, node: nodes.Keyword, frame: Frame) -> None: ...
    def visit_MarkSafe(self, node: nodes.MarkSafe, frame: Frame) -> None: ...
    def visit_MarkSafeIfAutoescape(self, node: nodes.MarkSafeIfAutoescape, frame: Frame) -> None: ...
    def visit_EnvironmentAttribute(self, node: nodes.EnvironmentAttribute, frame: Frame) -> None: ...
    def visit_ExtensionAttribute(self, node: nodes.ExtensionAttribute, frame: Frame) -> None: ...
    def visit_ImportedName(self, node: nodes.ImportedName, frame: Frame) -> None: ...
    def visit_InternalName(self, node: nodes.InternalName, frame: Frame) -> None: ...
    def visit_ContextReference(self, node: nodes.ContextReference, frame: Frame) -> None: ...
    def visit_DerivedContextReference(self, node: nodes.DerivedContextReference, frame: Frame) -> None: ...
    def visit_Continue(self, node: nodes.Continue, frame: Frame) -> None: ...
    def visit_Break(self, node: nodes.Break, frame: Frame) -> None: ...
    def visit_Scope(self, node: nodes.Scope, frame: Frame) -> None: ...
    def visit_OverlayScope(self, node: nodes.OverlayScope, frame: Frame) -> None: ...
    def visit_EvalContextModifier(self, node: nodes.EvalContextModifier, frame: Frame) -> None: ...
    def visit_ScopedEvalContextModifier(self, node: nodes.ScopedEvalContextModifier, frame: Frame) -> None: ...
