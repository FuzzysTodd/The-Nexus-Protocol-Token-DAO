import gast
from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, qual_names as qual_names, transformer as transformer
from tensorflow.python.autograph.pyct.static_analysis import activity as activity, annos as annos
from typing import Any, Dict, Set

class Resolver:
    """Resolver objects handle the process of looking up actual names and types.

  Unless noted otherwise, all resolve_* methods:
    * have a first namespace argument, mapping string to actual values
    * have a second types_namespace argument, mapping string to actual inferred
      types
    * specify names as QN objects
    * specify types as a Set of inferred types

  Unless noted otherwise, all resolve_* methods must return either:
    * a set of `type` objects
    * None
  """
    def res_name(self, ns, types_ns, name) -> None:
        """Resolves the type/value an external (e.g. closure, global) variable.

    Args:
      ns: namespace
      types_ns: types namespace
      name: symbol name
    Returns:
      Tuple (type, static_value). The first element is the type to use for
      inferrence. The second is the static value to use. Return None to treat it
      as unknown.
    """
    def res_value(self, ns, value) -> None:
        """Resolves the type a literal or static value."""
    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local) -> None:
        """Resolves the type of a (possibly annotated) function argument.

    Args:
      ns: namespace
      types_ns: types namespace
      f_name: str, the function name
      name: str, the argument name
      type_anno: the type annotating the argument, if any
      f_is_local: bool, whether the function is a local function
    Returns:
      Set of the argument types.
    """
    def res_call(self, ns, types_ns, node, f_type, args, keywords) -> None:
        """Resolves the return type an external function or method call.

    Args:
      ns: namespace
      types_ns: types namespace
      node: str, the function name
      f_type: types of the actual function being called, if known
      args: types of each respective argument in node.args
      keywords: types of each respective argument in node.keywords

    Returns:
      Tuple (return_type, side_effect_types). The first element is just the
      return types of the function. The second element is a map from
      argument names to sets of types, and allow modelling side effects of
      functions (for example via global or nonlocal).
    """
    def res_slice(self, ns, types_ns, node_or_slice, value, slice_) -> None:
        """Resolves the return type of slice operation."""
    def res_compare(self, ns, types_ns, node, left, right) -> None:
        """Resolves the return type of a unary operation."""
    def res_unop(self, ns, types_ns, node, opnd) -> None:
        """Resolves the return type of a unary operation."""
    def res_binop(self, ns, types_ns, node, left, right) -> None:
        """Resolves the return type of a binary operation."""
    def res_list_literal(self, ns, elt_types) -> None:
        """Resolves the type of a list literal from its elements."""

class _TypeMap:
    """Abstraction for the state of the CFG walk for type inference.

  This is a value type. Only implements the strictly necessary operators.

  Attributes:
    types: Dict[qual_names.QN, Set[Type]], mapping symbols to the set of
      possible types.
  """
    types: Incomplete
    def __init__(self, init_from: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __or__(self, other): ...

NO_VALUE: Incomplete

class StmtInferrer(gast.NodeVisitor):
    """Runs type inference on a single AST statement.

  This visitor annotates most nodes with type information. It also sets types
  for the symbols modified by this statement in its types_out property.

  Note: this inferrer is able to capture side effects of functions, however,
  these side effects will not be applied to the current expression. Doing so
  would create too much of a dependence on the runtime's internal rules about
  execution order.
  Example:

    def f():
      nonlocal a
      a = 1
      return a

    a = 0.0
    b = f() + a  # a = float; side effect of f() ignored
    print(a)  # a = int; side effect of f() accounted for
  """
    resolver: Incomplete
    scope: Incomplete
    namespace: Incomplete
    closure_types: Incomplete
    types_in: Incomplete
    new_symbols: Incomplete
    rtype: Incomplete
    def __init__(self, resolver: Resolver, scope: activity.Scope, namespace: Dict[qual_names.QN, Any], closure_types: Dict[qual_names.QN, Set[Any]], types_in: _TypeMap) -> None: ...
    def visit(self, node): ...
    def visit_Constant(self, node): ...
    def visit_Tuple(self, node): ...
    def visit_List(self, node): ...
    def visit_Set(self, node) -> None: ...
    def visit_Name(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_FunctionDef(self, node) -> None: ...
    def visit_Call(self, node): ...
    def visit_Expr(self, node): ...
    def visit_Assign(self, node) -> None: ...
    def visit_Subscript(self, node): ...
    def visit_Compare(self, node): ...
    def visit_BinOp(self, node): ...
    def visit_UnaryOp(self, node): ...

class Analyzer(cfg.GraphVisitor):
    """CFG visitor that propagates type information across statements."""
    resolver: Incomplete
    namespace: Incomplete
    scope: Incomplete
    closure_types: Incomplete
    context_types: Incomplete
    def __init__(self, graph, resolver, namespace, scope, closure_types) -> None:
        """Creates a new analyzer.

    Args:
      graph: cfg.Graph
      resolver: Resolver
      namespace: Dict[str, Any]
      scope: activity.Scope
      closure_types: Dict[QN, Set]
    """
    def init_state(self, _): ...
    def visit_node(self, node): ...

class FunctionVisitor(transformer.Base):
    """AST visitor that applies type inference to each function separately."""
    graphs: Incomplete
    resolver: Incomplete
    def __init__(self, source_info, graphs, resolver) -> None: ...
    def visit_FunctionDef(self, node): ...

def resolve(node, source_info, graphs, resolver):
    """Performs type inference.

  Args:
    node: ast.AST
    source_info: transformer.SourceInfo
    graphs: Dict[ast.FunctionDef, cfg.Graph]
    resolver: Resolver

  Returns:
    ast.AST
  """
