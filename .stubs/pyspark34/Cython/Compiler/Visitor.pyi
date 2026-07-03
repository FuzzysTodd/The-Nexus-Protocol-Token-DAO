from . import Builtin as Builtin, DebugFlags as DebugFlags, Errors as Errors, ExprNodes as ExprNodes, Future as Future, Nodes as Nodes, TypeSlots as TypeSlots
from _typeshed import Incomplete

class TreeVisitor:
    '''
    Base class for writing visitors for a Cython tree, contains utilities for
    recursing such trees using visitors. Each node is
    expected to have a child_attrs iterable containing the names of attributes
    containing child nodes or lists of child nodes. Lists are not considered
    part of the tree structure (i.e. contained nodes are considered direct
    children of the parent node).

    visit_children visits each of the children of a given node (see the visit_children
    documentation). When recursing the tree using visit_children, an attribute
    access_path is maintained which gives information about the current location
    in the tree as a stack of tuples: (parent_node, attrname, index), representing
    the node, attribute and optional list index that was taken in each step in the path to
    the current node.

    Example:

    >>> class SampleNode(object):
    ...     child_attrs = ["head", "body"]
    ...     def __init__(self, value, head=None, body=None):
    ...         self.value = value
    ...         self.head = head
    ...         self.body = body
    ...     def __repr__(self): return "SampleNode(%s)" % self.value
    ...
    >>> tree = SampleNode(0, SampleNode(1), [SampleNode(2), SampleNode(3)])
    >>> class MyVisitor(TreeVisitor):
    ...     def visit_SampleNode(self, node):
    ...         print("in %s %s" % (node.value, self.access_path))
    ...         self.visitchildren(node)
    ...         print("out %s" % node.value)
    ...
    >>> MyVisitor().visit(tree)
    in 0 []
    in 1 [(SampleNode(0), \'head\', None)]
    out 1
    in 2 [(SampleNode(0), \'body\', 0)]
    out 2
    in 3 [(SampleNode(0), \'body\', 1)]
    out 3
    out 0
    '''
    dispatch_table: Incomplete
    access_path: Incomplete
    def __init__(self) -> None: ...
    def dump_node(self, node): ...
    def find_handler(self, obj): ...
    def visit(self, obj): ...
    def visitchildren(self, parent, attrs: Incomplete | None = None, exclude: Incomplete | None = None): ...

class VisitorTransform(TreeVisitor):
    """
    A tree transform is a base class for visitors that wants to do stream
    processing of the structure (rather than attributes etc.) of a tree.

    It implements __call__ to simply visit the argument node.

    It requires the visitor methods to return the nodes which should take
    the place of the visited node in the result tree (which can be the same
    or one or more replacement). Specifically, if the return value from
    a visitor method is:

    - [] or None; the visited node will be removed (set to None if an attribute and
    removed if in a list)
    - A single node; the visited node will be replaced by the returned node.
    - A list of nodes; the visited nodes will be replaced by all the nodes in the
    list. This will only work if the node was already a member of a list; if it
    was not, an exception will be raised. (Typically you want to ensure that you
    are within a StatListNode or similar before doing this.)
    """
    def visitchildren(self, parent, attrs: Incomplete | None = None, exclude: Incomplete | None = None): ...
    def visitchild(self, parent, attr, idx: int = 0): ...
    def recurse_to_children(self, node): ...
    def __call__(self, root): ...

class CythonTransform(VisitorTransform):
    """
    Certain common conventions and utilities for Cython transforms.

     - Sets up the context of the pipeline in self.context
     - Tracks directives in effect in self.current_directives
    """
    context: Incomplete
    def __init__(self, context) -> None: ...
    current_directives: Incomplete
    def __call__(self, node): ...
    def visit_CompilerDirectivesNode(self, node): ...
    def visit_Node(self, node): ...

class ScopeTrackingTransform(CythonTransform):
    scope_type: str
    scope_node: Incomplete
    def visit_ModuleNode(self, node): ...
    def visit_scope(self, node, scope_type): ...
    def visit_CClassDefNode(self, node): ...
    def visit_PyClassDefNode(self, node): ...
    def visit_FuncDefNode(self, node): ...
    def visit_CStructOrUnionDefNode(self, node): ...

class EnvTransform(CythonTransform):
    """
    This transformation keeps a stack of the environments.
    """
    env_stack: Incomplete
    def __call__(self, root): ...
    def current_env(self): ...
    def current_scope_node(self): ...
    def global_scope(self): ...
    def enter_scope(self, node, scope) -> None: ...
    def exit_scope(self) -> None: ...
    def visit_FuncDefNode(self, node): ...
    def visit_func_outer_attrs(self, node) -> None: ...
    def visit_GeneratorBodyDefNode(self, node): ...
    def visit_ClassDefNode(self, node): ...
    def visit_CStructOrUnionDefNode(self, node): ...
    def visit_ScopedExprNode(self, node): ...
    def visit_CArgDeclNode(self, node): ...

class NodeRefCleanupMixin:
    '''
    Clean up references to nodes that were replaced.

    NOTE: this implementation assumes that the replacement is
    done first, before hitting any further references during
    normal tree traversal.  This needs to be arranged by calling
    "self.visitchildren()" at a proper place in the transform
    and by ordering the "child_attrs" of nodes appropriately.
    '''
    def __init__(self, *args) -> None: ...
    def visit_CloneNode(self, node): ...
    def visit_ResultRefNode(self, node): ...
    def replace(self, node, replacement): ...

find_special_method_for_binary_operator: Incomplete
find_special_method_for_unary_operator: Incomplete

class MethodDispatcherTransform(EnvTransform):
    """
    Base class for transformations that want to intercept on specific
    builtin functions or methods of builtin types, including special
    methods triggered by Python operators.  Must run after declaration
    analysis when entries were assigned.

    Naming pattern for handler methods is as follows:

    * builtin functions: _handle_(general|simple|any)_function_NAME

    * builtin methods: _handle_(general|simple|any)_method_TYPENAME_METHODNAME
    """
    def visit_GeneralCallNode(self, node): ...
    def visit_SimpleCallNode(self, node): ...
    def visit_PrimaryCmpNode(self, node): ...
    def visit_BinopNode(self, node): ...
    def visit_UnopNode(self, node): ...

class RecursiveNodeReplacer(VisitorTransform):
    """
    Recursively replace all occurrences of a node in a subtree by
    another node.
    """
    def __init__(self, orig_node, new_node) -> None: ...
    def visit_CloneNode(self, node): ...
    def visit_Node(self, node): ...

def recursively_replace_node(tree, old_node, new_node) -> None: ...

class NodeFinder(TreeVisitor):
    """
    Find out if a node appears in a subtree.
    """
    node: Incomplete
    found: bool
    def __init__(self, node) -> None: ...
    def visit_Node(self, node) -> None: ...

def tree_contains(tree, node): ...
def replace_node(ptr, value) -> None:
    """Replaces a node. ptr is of the form used on the access path stack
    (parent, attrname, listidx|None)
    """

class PrintTree(TreeVisitor):
    """Prints a representation of the tree to standard output.
    Subclass and override repr_of to provide more information
    about nodes. """
    def __init__(self, start: Incomplete | None = None, end: Incomplete | None = None) -> None: ...
    def indent(self) -> None: ...
    def unindent(self) -> None: ...
    def __call__(self, tree, phase: Incomplete | None = None): ...
    def visit_Node(self, node): ...
    def visit_CloneNode(self, node): ...
    def repr_of(self, node): ...
