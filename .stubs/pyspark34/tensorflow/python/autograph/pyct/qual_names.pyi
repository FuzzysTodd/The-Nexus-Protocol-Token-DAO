import gast
from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, parser as parser
from typing import NamedTuple

class CallerMustSetThis: ...
class Symbol(NamedTuple('Symbol', [('name', Incomplete)])):
    """Represents a Python symbol."""
class Literal(NamedTuple('Literal', [('value', Incomplete)])):
    """Represents a Python numeric literal."""

class QN:
    """Represents a qualified name."""
    qn: Incomplete
    def __init__(self, base, attr: Incomplete | None = None, subscript: Incomplete | None = None) -> None: ...
    def is_symbol(self): ...
    def is_simple(self): ...
    def is_composite(self): ...
    def has_subscript(self): ...
    def has_attr(self): ...
    @property
    def attr(self): ...
    @property
    def parent(self): ...
    @property
    def owner_set(self):
        """Returns all the symbols (simple or composite) that own this QN.

    In other words, if this symbol was modified, the symbols in the owner set
    may also be affected.

    Examples:
      'a.b[c.d]' has two owners, 'a' and 'a.b'
    """
    @property
    def support_set(self):
        """Returns the set of simple symbols that this QN relies on.

    This would be the smallest set of symbols necessary for the QN to
    statically resolve (assuming properties and index ranges are verified
    at runtime).

    Examples:
      'a.b' has only one support symbol, 'a'
      'a[i]' has two support symbols, 'a' and 'i'
    """
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...
    def ssf(self):
        """Simple symbol form."""
    def ast(self):
        """AST representation."""

class QnResolver(gast.NodeTransformer):
    """Annotates nodes with QN information.

  Note: Not using NodeAnnos to avoid circular dependencies.
  """
    def visit_Name(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_Subscript(self, node): ...

def resolve(node): ...
def from_str(qn_str): ...
