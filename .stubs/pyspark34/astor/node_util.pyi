import ast
import itertools
from _typeshed import Incomplete
from collections.abc import Generator

zip_longest = itertools.zip_longest

class NonExistent:
    """This is not the class you are looking for.
    """

def iter_node(node, name: str = '', unknown: Incomplete | None = None, list=..., getattr=..., isinstance=..., enumerate=..., missing=...) -> Generator[Incomplete, None, None]:
    """Iterates over an object:

       - If the object has a _fields attribute,
         it gets attributes in the order of this
         and returns name, value pairs.

       - Otherwise, if the object is a list instance,
         it returns name, value pairs for each item
         in the list, where the name is passed into
         this function (defaults to blank).

       - Can update an unknown set with information about
         attributes that do not exist in fields.
    """
def dump_tree(node, name: Incomplete | None = None, initial_indent: str = '', indentation: str = '    ', maxline: int = 120, maxmerged: int = 80, iter_node=..., special=..., list=..., isinstance=..., type=..., len=...):
    """Dumps an AST or similar structure:

       - Pretty-prints with indentation
       - Doesn't print line/column/ctx info

    """
def strip_tree(node, iter_node=..., special=..., list=..., isinstance=..., type=..., len=...):
    """Strips an AST by removing all attributes not in _fields.

    Returns a set of the names of all attributes stripped.

    This canonicalizes two trees for comparison purposes.
    """

class ExplicitNodeVisitor(ast.NodeVisitor):
    """This expands on the ast module's NodeVisitor class
    to remove any implicit visits.

    """
    def abort_visit(node) -> None: ...
    def visit(self, node, abort=...):
        """Visit a node."""

def allow_ast_comparison():
    """This ugly little monkey-patcher adds in a helper class
    to all the AST node types.  This helper class allows
    eq/ne comparisons to work, so that entire trees can
    be easily compared by Python's comparison machinery.
    Used by the anti8 functions to compare old and new ASTs.
    Could also be used by the test library.


    """
def fast_compare(tree1, tree2):
    """ This is optimized to compare two AST trees for equality.
        It makes several assumptions that are currently true for
        AST trees used by rtrip, and it doesn't examine the _attributes.
    """
