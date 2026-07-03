from _typeshed import Incomplete
from collections import Mapping
from collections.abc import Generator
from parso.python.prefix import split_prefix as split_prefix
from parso.tree import BaseNode as BaseNode, ErrorLeaf as ErrorLeaf, ErrorNode as ErrorNode, Leaf as Leaf, Node as Node, search_ancestor as search_ancestor
from parso.utils import split_lines as split_lines
from typing import Tuple

class DocstringMixin:
    def get_doc_node(self):
        """
        Returns the string leaf of a docstring. e.g. ``r'''foo'''``.
        """

class PythonMixin:
    """
    Some Python specific utilities.
    """
    def get_name_of_position(self, position):
        """
        Given a (line, column) tuple, returns a :py:class:`Name` or ``None`` if
        there is no name at that position.
        """

class PythonLeaf(PythonMixin, Leaf):
    def get_start_pos_of_prefix(self):
        """
        Basically calls :py:meth:`parso.tree.NodeOrLeaf.get_start_pos_of_prefix`.
        """

class _LeafWithoutNewlines(PythonLeaf):
    """
    Simply here to optimize performance.
    """
    @property
    def end_pos(self) -> Tuple[int, int]: ...

class PythonBaseNode(PythonMixin, BaseNode): ...
class PythonNode(PythonMixin, Node): ...
class PythonErrorNode(PythonMixin, ErrorNode): ...
class PythonErrorLeaf(ErrorLeaf, PythonLeaf): ...

class EndMarker(_LeafWithoutNewlines):
    type: str

class Newline(PythonLeaf):
    """Contains NEWLINE and ENDMARKER tokens."""
    type: str

class Name(_LeafWithoutNewlines):
    """
    A string. Sometimes it is important to know if the string belongs to a name
    or not.
    """
    type: str
    def is_definition(self, include_setitem: bool = False):
        """
        Returns True if the name is being defined.
        """
    def get_definition(self, import_name_always: bool = False, include_setitem: bool = False):
        """
        Returns None if there's no definition for a name.

        :param import_name_always: Specifies if an import name is always a
            definition. Normally foo in `from foo import bar` is not a
            definition.
        """

class Literal(PythonLeaf): ...

class Number(Literal):
    type: str

class String(Literal):
    type: str
    @property
    def string_prefix(self): ...

class FStringString(PythonLeaf):
    """
    f-strings contain f-string expressions and normal python strings. These are
    the string parts of f-strings.
    """
    type: str

class FStringStart(PythonLeaf):
    """
    f-strings contain f-string expressions and normal python strings. These are
    the string parts of f-strings.
    """
    type: str

class FStringEnd(PythonLeaf):
    """
    f-strings contain f-string expressions and normal python strings. These are
    the string parts of f-strings.
    """
    type: str

class _StringComparisonMixin:
    def __eq__(self, other):
        """
        Make comparisons with strings easy.
        Improves the readability of the parser.
        """
    def __hash__(self): ...

class Operator(_LeafWithoutNewlines, _StringComparisonMixin):
    type: str

class Keyword(_LeafWithoutNewlines, _StringComparisonMixin):
    type: str

class Scope(PythonBaseNode, DocstringMixin):
    """
    Super class for the parser tree, which represents the state of a python
    text file.
    A Scope is either a function, class or lambda.
    """
    def __init__(self, children) -> None: ...
    def iter_funcdefs(self):
        """
        Returns a generator of `funcdef` nodes.
        """
    def iter_classdefs(self):
        """
        Returns a generator of `classdef` nodes.
        """
    def iter_imports(self):
        """
        Returns a generator of `import_name` and `import_from` nodes.
        """
    def get_suite(self):
        """
        Returns the part that is executed by the function.
        """

class Module(Scope):
    """
    The top scope, which is always a module.
    Depending on the underlying parser this may be a full module or just a part
    of a module.
    """
    type: str
    def __init__(self, children) -> None: ...
    def get_used_names(self):
        """
        Returns all the :class:`Name` leafs that exist in this module. This
        includes both definitions and references of names.
        """

class Decorator(PythonBaseNode):
    type: str

class ClassOrFunc(Scope):
    @property
    def name(self):
        """
        Returns the `Name` leaf that defines the function or class name.
        """
    def get_decorators(self):
        """
        :rtype: list of :class:`Decorator`
        """

class Class(ClassOrFunc):
    """
    Used to store the parsed contents of a python class.
    """
    type: str
    def __init__(self, children) -> None: ...
    def get_super_arglist(self):
        """
        Returns the `arglist` node that defines the super classes. It returns
        None if there are no arguments.
        """

class Function(ClassOrFunc):
    """
    Used to store the parsed contents of a python function.

    Children::

        0. <Keyword: def>
        1. <Name>
        2. parameter list (including open-paren and close-paren <Operator>s)
        3. or 5. <Operator: :>
        4. or 6. Node() representing function body
        3. -> (if annotation is also present)
        4. annotation (if present)
    """
    type: str
    def __init__(self, children) -> None: ...
    def get_params(self):
        """
        Returns a list of `Param()`.
        """
    @property
    def name(self): ...
    def iter_yield_exprs(self):
        """
        Returns a generator of `yield_expr`.
        """
    def iter_return_stmts(self):
        """
        Returns a generator of `return_stmt`.
        """
    def iter_raise_stmts(self):
        """
        Returns a generator of `raise_stmt`. Includes raise statements inside try-except blocks
        """
    def is_generator(self):
        """
        :return bool: Checks if a function is a generator or not.
        """
    @property
    def annotation(self):
        """
        Returns the test node after `->` or `None` if there is no annotation.
        """

class Lambda(Function):
    """
    Lambdas are basically trimmed functions, so give it the same interface.

    Children::

         0. <Keyword: lambda>
         *. <Param x> for each argument x
        -2. <Operator: :>
        -1. Node() representing body
    """
    type: str
    def __init__(self, children) -> None: ...
    @property
    def name(self) -> None:
        """
        Raises an AttributeError. Lambdas don't have a defined name.
        """
    @property
    def annotation(self) -> None:
        """
        Returns `None`, lambdas don't have annotations.
        """

class Flow(PythonBaseNode): ...

class IfStmt(Flow):
    type: str
    def get_test_nodes(self) -> Generator[Incomplete, None, None]:
        """
        E.g. returns all the `test` nodes that are named as x, below:

            if x:
                pass
            elif x:
                pass
        """
    def get_corresponding_test_node(self, node):
        """
        Searches for the branch in which the node is and returns the
        corresponding test node (see function above). However if the node is in
        the test node itself and not in the suite return None.
        """
    def is_node_after_else(self, node):
        """
        Checks if a node is defined after `else`.
        """

class WhileStmt(Flow):
    type: str

class ForStmt(Flow):
    type: str
    def get_testlist(self):
        """
        Returns the input node ``y`` from: ``for x in y:``.
        """
    def get_defined_names(self, include_setitem: bool = False): ...

class TryStmt(Flow):
    type: str
    def get_except_clause_tests(self) -> Generator[Incomplete, None, None]:
        """
        Returns the ``test`` nodes found in ``except_clause`` nodes.
        Returns ``[None]`` for except clauses without an exception given.
        """

class WithStmt(Flow):
    type: str
    def get_defined_names(self, include_setitem: bool = False):
        """
        Returns the a list of `Name` that the with statement defines. The
        defined names are set after `as`.
        """
    def get_test_node_from_name(self, name): ...

class Import(PythonBaseNode):
    def get_path_for_name(self, name):
        """
        The path is the list of names that leads to the searched name.

        :return list of Name:
        """
    def is_nested(self): ...
    def is_star_import(self): ...

class ImportFrom(Import):
    type: str
    def get_defined_names(self, include_setitem: bool = False):
        """
        Returns the a list of `Name` that the import defines. The
        defined names are set after `import` or in case an alias - `as` - is
        present that name is returned.
        """
    def get_from_names(self): ...
    @property
    def level(self):
        """The level parameter of ``__import__``."""
    def get_paths(self):
        """
        The import paths defined in an import statement. Typically an array
        like this: ``[<Name: datetime>, <Name: date>]``.

        :return list of list of Name:
        """

class ImportName(Import):
    """For ``import_name`` nodes. Covers normal imports without ``from``."""
    type: str
    def get_defined_names(self, include_setitem: bool = False):
        """
        Returns the a list of `Name` that the import defines. The defined names
        is always the first name after `import` or in case an alias - `as` - is
        present that name is returned.
        """
    @property
    def level(self):
        """The level parameter of ``__import__``."""
    def get_paths(self): ...
    def is_nested(self):
        """
        This checks for the special case of nested imports, without aliases and
        from statement::

            import foo.bar
        """

class KeywordStatement(PythonBaseNode):
    """
    For the following statements: `assert`, `del`, `global`, `nonlocal`,
    `raise`, `return`, `yield`.

    `pass`, `continue` and `break` are not in there, because they are just
    simple keywords and the parser reduces it to a keyword.
    """
    @property
    def type(self):
        """
        Keyword statements start with the keyword and end with `_stmt`. You can
        crosscheck this with the Python grammar.
        """
    @property
    def keyword(self): ...
    def get_defined_names(self, include_setitem: bool = False): ...

class AssertStmt(KeywordStatement):
    @property
    def assertion(self): ...

class GlobalStmt(KeywordStatement):
    def get_global_names(self): ...

class ReturnStmt(KeywordStatement): ...

class YieldExpr(PythonBaseNode):
    type: str

class ExprStmt(PythonBaseNode, DocstringMixin):
    type: str
    def get_defined_names(self, include_setitem: bool = False):
        """
        Returns a list of `Name` defined before the `=` sign.
        """
    def get_rhs(self):
        """Returns the right-hand-side of the equals."""
    def yield_operators(self) -> Generator[Incomplete, Incomplete, None]:
        """
        Returns a generator of `+=`, `=`, etc. or None if there is no operation.
        """

class NamedExpr(PythonBaseNode):
    type: str
    def get_defined_names(self, include_setitem: bool = False): ...

class Param(PythonBaseNode):
    """
    It's a helper class that makes business logic with params much easier. The
    Python grammar defines no ``param`` node. It defines it in a different way
    that is not really suited to working with parameters.
    """
    type: str
    parent: Incomplete
    def __init__(self, children, parent: Incomplete | None = None) -> None: ...
    @property
    def star_count(self):
        """
        Is `0` in case of `foo`, `1` in case of `*foo` or `2` in case of
        `**foo`.
        """
    @property
    def default(self):
        """
        The default is the test node that appears after the `=`. Is `None` in
        case no default is present.
        """
    @property
    def annotation(self):
        """
        The default is the test node that appears after `:`. Is `None` in case
        no annotation is present.
        """
    @property
    def name(self):
        """
        The `Name` leaf of the param.
        """
    def get_defined_names(self, include_setitem: bool = False): ...
    @property
    def position_index(self):
        """
        Property for the positional index of a paramter.
        """
    def get_parent_function(self):
        """
        Returns the function/lambda of a parameter.
        """
    def get_code(self, include_prefix: bool = True, include_comma: bool = True):
        """
        Like all the other get_code functions, but includes the param
        `include_comma`.

        :param include_comma bool: If enabled includes the comma in the string output.
        """

class SyncCompFor(PythonBaseNode):
    type: str
    def get_defined_names(self, include_setitem: bool = False):
        """
        Returns the a list of `Name` that the comprehension defines.
        """
CompFor = SyncCompFor

class UsedNamesMapping(Mapping):
    """
    This class exists for the sole purpose of creating an immutable dict.
    """
    def __init__(self, dct) -> None: ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
