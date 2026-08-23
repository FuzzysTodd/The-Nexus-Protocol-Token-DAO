from _typeshed import Incomplete

class Node:
    def children(self) -> None:
        """ A sequence of all children that are Nodes
        """
    def show(self, buf=..., offset: int = 0, attrnames: bool = False, nodenames: bool = False, showcoord: bool = False, _my_node_name: Incomplete | None = None) -> None:
        """ Pretty print the Node and all its attributes and
            children (recursively) to a buffer.

            buf:
                Open IO buffer into which the Node is printed.

            offset:
                Initial offset (amount of leading spaces)

            attrnames:
                True if you want to see the attribute names in
                name=value pairs. False to only see the values.

            nodenames:
                True if you want to see the actual node names
                within their parents.

            showcoord:
                Do you want the coordinates of each Node to be
                displayed.
        """

class NodeVisitor:
    """ A base NodeVisitor class for visiting c_ast nodes.
        Subclass it and define your own visit_XXX methods, where
        XXX is the class name you want to visit with these
        methods.

        For example:

        class ConstantVisitor(NodeVisitor):
            def __init__(self):
                self.values = []

            def visit_Constant(self, node):
                self.values.append(node.value)

        Creates a list of values of all the constant nodes
        encountered below the given node. To use it:

        cv = ConstantVisitor()
        cv.visit(node)

        Notes:

        *   generic_visit() will be called for AST nodes for which
            no visit_XXX method was defined.
        *   The children of nodes for which a visit_XXX was
            defined will not be visited - if you need this, call
            generic_visit() on the node.
            You can use:
                NodeVisitor.generic_visit(self, node)
        *   Modeled after Python's own AST visiting facilities
            (the ast module of Python 3.0)
    """
    def visit(self, node):
        """ Visit a node.
        """
    def generic_visit(self, node) -> None:
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """

class ArrayDecl(Node):
    type: Incomplete
    dim: Incomplete
    dim_quals: Incomplete
    coord: Incomplete
    def __init__(self, type, dim, dim_quals, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class ArrayRef(Node):
    name: Incomplete
    subscript: Incomplete
    coord: Incomplete
    def __init__(self, name, subscript, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Assignment(Node):
    op: Incomplete
    lvalue: Incomplete
    rvalue: Incomplete
    coord: Incomplete
    def __init__(self, op, lvalue, rvalue, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Alignas(Node):
    alignment: Incomplete
    coord: Incomplete
    def __init__(self, alignment, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class BinaryOp(Node):
    op: Incomplete
    left: Incomplete
    right: Incomplete
    coord: Incomplete
    def __init__(self, op, left, right, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Break(Node):
    coord: Incomplete
    def __init__(self, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Case(Node):
    expr: Incomplete
    stmts: Incomplete
    coord: Incomplete
    def __init__(self, expr, stmts, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Cast(Node):
    to_type: Incomplete
    expr: Incomplete
    coord: Incomplete
    def __init__(self, to_type, expr, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Compound(Node):
    block_items: Incomplete
    coord: Incomplete
    def __init__(self, block_items, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class CompoundLiteral(Node):
    type: Incomplete
    init: Incomplete
    coord: Incomplete
    def __init__(self, type, init, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Constant(Node):
    type: Incomplete
    value: Incomplete
    coord: Incomplete
    def __init__(self, type, value, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Continue(Node):
    coord: Incomplete
    def __init__(self, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Decl(Node):
    name: Incomplete
    quals: Incomplete
    align: Incomplete
    storage: Incomplete
    funcspec: Incomplete
    type: Incomplete
    init: Incomplete
    bitsize: Incomplete
    coord: Incomplete
    def __init__(self, name, quals, align, storage, funcspec, type, init, bitsize, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class DeclList(Node):
    decls: Incomplete
    coord: Incomplete
    def __init__(self, decls, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Default(Node):
    stmts: Incomplete
    coord: Incomplete
    def __init__(self, stmts, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class DoWhile(Node):
    cond: Incomplete
    stmt: Incomplete
    coord: Incomplete
    def __init__(self, cond, stmt, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class EllipsisParam(Node):
    coord: Incomplete
    def __init__(self, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class EmptyStatement(Node):
    coord: Incomplete
    def __init__(self, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Enum(Node):
    name: Incomplete
    values: Incomplete
    coord: Incomplete
    def __init__(self, name, values, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Enumerator(Node):
    name: Incomplete
    value: Incomplete
    coord: Incomplete
    def __init__(self, name, value, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class EnumeratorList(Node):
    enumerators: Incomplete
    coord: Incomplete
    def __init__(self, enumerators, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class ExprList(Node):
    exprs: Incomplete
    coord: Incomplete
    def __init__(self, exprs, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class FileAST(Node):
    ext: Incomplete
    coord: Incomplete
    def __init__(self, ext, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class For(Node):
    init: Incomplete
    cond: Incomplete
    next: Incomplete
    stmt: Incomplete
    coord: Incomplete
    def __init__(self, init, cond, next, stmt, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class FuncCall(Node):
    name: Incomplete
    args: Incomplete
    coord: Incomplete
    def __init__(self, name, args, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class FuncDecl(Node):
    args: Incomplete
    type: Incomplete
    coord: Incomplete
    def __init__(self, args, type, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class FuncDef(Node):
    decl: Incomplete
    param_decls: Incomplete
    body: Incomplete
    coord: Incomplete
    def __init__(self, decl, param_decls, body, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Goto(Node):
    name: Incomplete
    coord: Incomplete
    def __init__(self, name, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class ID(Node):
    name: Incomplete
    coord: Incomplete
    def __init__(self, name, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class IdentifierType(Node):
    names: Incomplete
    coord: Incomplete
    def __init__(self, names, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class If(Node):
    cond: Incomplete
    iftrue: Incomplete
    iffalse: Incomplete
    coord: Incomplete
    def __init__(self, cond, iftrue, iffalse, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class InitList(Node):
    exprs: Incomplete
    coord: Incomplete
    def __init__(self, exprs, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Label(Node):
    name: Incomplete
    stmt: Incomplete
    coord: Incomplete
    def __init__(self, name, stmt, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class NamedInitializer(Node):
    name: Incomplete
    expr: Incomplete
    coord: Incomplete
    def __init__(self, name, expr, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class ParamList(Node):
    params: Incomplete
    coord: Incomplete
    def __init__(self, params, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class PtrDecl(Node):
    quals: Incomplete
    type: Incomplete
    coord: Incomplete
    def __init__(self, quals, type, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Return(Node):
    expr: Incomplete
    coord: Incomplete
    def __init__(self, expr, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class StaticAssert(Node):
    cond: Incomplete
    message: Incomplete
    coord: Incomplete
    def __init__(self, cond, message, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Struct(Node):
    name: Incomplete
    decls: Incomplete
    coord: Incomplete
    def __init__(self, name, decls, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class StructRef(Node):
    name: Incomplete
    type: Incomplete
    field: Incomplete
    coord: Incomplete
    def __init__(self, name, type, field, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Switch(Node):
    cond: Incomplete
    stmt: Incomplete
    coord: Incomplete
    def __init__(self, cond, stmt, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class TernaryOp(Node):
    cond: Incomplete
    iftrue: Incomplete
    iffalse: Incomplete
    coord: Incomplete
    def __init__(self, cond, iftrue, iffalse, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class TypeDecl(Node):
    declname: Incomplete
    quals: Incomplete
    align: Incomplete
    type: Incomplete
    coord: Incomplete
    def __init__(self, declname, quals, align, type, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Typedef(Node):
    name: Incomplete
    quals: Incomplete
    storage: Incomplete
    type: Incomplete
    coord: Incomplete
    def __init__(self, name, quals, storage, type, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Typename(Node):
    name: Incomplete
    quals: Incomplete
    align: Incomplete
    type: Incomplete
    coord: Incomplete
    def __init__(self, name, quals, align, type, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class UnaryOp(Node):
    op: Incomplete
    expr: Incomplete
    coord: Incomplete
    def __init__(self, op, expr, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Union(Node):
    name: Incomplete
    decls: Incomplete
    coord: Incomplete
    def __init__(self, name, decls, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class While(Node):
    cond: Incomplete
    stmt: Incomplete
    coord: Incomplete
    def __init__(self, cond, stmt, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete

class Pragma(Node):
    string: Incomplete
    coord: Incomplete
    def __init__(self, string, coord: Incomplete | None = None) -> None: ...
    def children(self): ...
    def __iter__(self): ...
    attr_names: Incomplete
