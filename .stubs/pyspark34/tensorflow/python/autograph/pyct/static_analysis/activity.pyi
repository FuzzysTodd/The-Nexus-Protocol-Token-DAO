from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, qual_names as qual_names, transformer as transformer
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno

class Scope:
    """Encloses local symbol definition and usage information.

  This can track for instance whether a symbol is modified in the current scope.
  Note that scopes do not necessarily align with Python's scopes. For example,
  the body of an if statement may be considered a separate scope.

  Caution - the AST references held by this object are weak.

  Scope objects are mutable during construction only, and must be frozen using
  `Scope.finalize()` before use. Furthermore, a scope is consistent only after
  all its children have been frozen. While analysing code blocks, scopes are
  being gradually built, from the innermost scope outward. Freezing indicates
  that the analysis of a code block is complete. Once frozen, mutation is no
  longer allowed. `is_final` tracks whether the scope is frozen or not. Certain
  properties, like `referenced`, are only accurate when called on frozen scopes.

  Attributes:
    parent: Optional[Scope], the parent scope, if any.
    isolated: bool, whether the scope is a true Python scope (e.g. the scope of
      a function), or just a surrogate tracking an ordinary code block. Using
      the terminology of the Python 3 reference documentation, True roughly
      represents an actual scope, whereas False represents an ordinary code
      block.
    function_name: Optional[str], name of the function owning this scope.
    isolated_names: Set[qual_names.QN], identifiers that are isolated to this
      scope (even if the scope is not isolated).
    annotations: Set[qual_names.QN], identifiers used as type annotations
      in this scope.
    read: Set[qual_names.QN], identifiers read in this scope.
    modified: Set[qual_names.QN], identifiers modified in this scope.
    deleted: Set[qual_names.QN], identifiers deleted in this scope.
    bound: Set[qual_names.QN], names that are bound to this scope. See
      https://docs.python.org/3/reference/executionmodel.html#binding-of-names
      for a precise definition.
    globals: Set[qual_names.QN], names that are explicitly marked as global in
      this scope. Note that this doesn't include free read-only vars bound to
      global symbols.
    nonlocals: Set[qual_names.QN], names that are explicitly marked as nonlocal
      in this scope. Note that this doesn't include free read-only vars bound to
      global symbols.
    free_vars: Set[qual_names.QN], the free variables in this scope. See
      https://docs.python.org/3/reference/executionmodel.html for a precise
      definition.
    params: WeakValueDictionary[qual_names.QN, ast.Node], function arguments
      visible in this scope, mapped to the function node that defines them.
    enclosing_scope: Scope, the innermost isolated scope that is a transitive
      parent of this scope. May be the scope itself.
    referenced: Set[qual_names.QN], the totality of the symbols used by this
      scope and its parents.
    is_final: bool, whether the scope is frozen or not.

  Note - simple statements may never delete and modify a symbol at the same
  time. However, compound ones like if statements can. In that latter case, it's
  undefined whether the symbol is actually modified or deleted upon statement
  exit. Certain analyses like reaching definitions need to be careful about
  this.
  """
    parent: Incomplete
    isolated: Incomplete
    function_name: Incomplete
    isolated_names: Incomplete
    read: Incomplete
    modified: Incomplete
    deleted: Incomplete
    bound: Incomplete
    globals: Incomplete
    nonlocals: Incomplete
    annotations: Incomplete
    params: Incomplete
    is_final: bool
    def __init__(self, parent, isolated: bool = True, function_name: Incomplete | None = None) -> None:
        """Create a new scope.

    Args:
      parent: A Scope or None.
      isolated: Whether the scope is isolated, that is, whether variables
        modified in this scope should be considered modified in the parent
        scope.
      function_name: Name of the function owning this scope.
    """
    @property
    def enclosing_scope(self): ...
    @property
    def referenced(self): ...
    @property
    def free_vars(self): ...
    def copy_from(self, other) -> None:
        """Recursively copies the contents of this scope from another scope."""
    @classmethod
    def copy_of(cls, other): ...
    def merge_from(self, other) -> None:
        """Adds all activity from another scope to this scope."""
    def finalize(self) -> None:
        """Freezes this scope."""
    def mark_param(self, name, owner) -> None: ...

class _Comprehension:
    no_root: bool
    is_list_comp: bool
    targets: Incomplete
    def __init__(self) -> None: ...

class _FunctionOrClass:
    node: Incomplete
    def __init__(self) -> None: ...

class ActivityAnalyzer(transformer.Base):
    """Annotates nodes with local scope information.

  See Scope.

  The use of this class requires that qual_names.resolve() has been called on
  the node. This class will ignore nodes have not been
  annotated with their qualified names.
  """
    allow_skips: bool
    scope: Incomplete
    def __init__(self, context, parent_scope: Incomplete | None = None) -> None: ...
    def visit_Import(self, node): ...
    def visit_ImportFrom(self, node): ...
    def visit_Global(self, node): ...
    def visit_Nonlocal(self, node): ...
    def visit_Expr(self, node): ...
    def visit_Raise(self, node): ...
    def visit_Return(self, node): ...
    def visit_Assign(self, node): ...
    def visit_AnnAssign(self, node): ...
    def visit_AugAssign(self, node): ...
    def visit_Delete(self, node): ...
    def visit_Name(self, node): ...
    def visit_alias(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_Subscript(self, node): ...
    def visit_Print(self, node): ...
    def visit_Assert(self, node): ...
    def visit_Call(self, node): ...
    def visit_comprehension(self, node): ...
    def visit_DictComp(self, node): ...
    def visit_ListComp(self, node): ...
    def visit_SetComp(self, node): ...
    def visit_GeneratorExp(self, node): ...
    def visit_ClassDef(self, node): ...
    def visit_FunctionDef(self, node): ...
    def visit_Lambda(self, node): ...
    def visit_With(self, node): ...
    def visit_withitem(self, node): ...
    def visit_If(self, node): ...
    def visit_For(self, node): ...
    def visit_While(self, node): ...
    def visit_ExceptHandler(self, node): ...

def resolve(node, context, parent_scope: Incomplete | None = None): ...
