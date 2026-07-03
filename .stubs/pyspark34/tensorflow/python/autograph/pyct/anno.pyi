import enum
from _typeshed import Incomplete

class NoValue(enum.Enum):
    """Base class for different types of AST annotations."""
    def of(self, node, default: Incomplete | None = None): ...
    def add_to(self, node, value) -> None: ...
    def exists(self, node): ...

class Basic(NoValue):
    """Container for basic annotation keys.

  The enum values are used strictly for documentation purposes.
  """
    QN: str
    SKIP_PROCESSING: str
    INDENT_BLOCK_REMAINDER: str
    ORIGIN: str
    DIRECTIVES: str
    EXTRA_LOOP_TEST: str

class Static(NoValue):
    """Container for static analysis annotation keys.

  The enum values are used strictly for documentation purposes.
  """
    IS_PARAM: str
    SCOPE: str
    ARGS_SCOPE: str
    COND_SCOPE: str
    BODY_SCOPE: str
    ORELSE_SCOPE: str
    DEFINITIONS: str
    ORIG_DEFINITIONS: str
    DEFINED_FNS_IN: str
    DEFINED_VARS_IN: str
    LIVE_VARS_OUT: str
    LIVE_VARS_IN: str
    TYPES: str
    CLOSURE_TYPES: str
    VALUE: str

FAIL: Incomplete

def keys(node, field_name: str = '___pyct_anno'): ...
def getanno(node, key, default=..., field_name: str = '___pyct_anno'): ...
def hasanno(node, key, field_name: str = '___pyct_anno'): ...
def setanno(node, key, value, field_name: str = '___pyct_anno') -> None: ...
def delanno(node, key, field_name: str = '___pyct_anno') -> None: ...
def copyanno(from_node, to_node, key, field_name: str = '___pyct_anno') -> None: ...
def dup(node, copy_map, field_name: str = '___pyct_anno') -> None:
    """Recursively copies annotations in an AST tree.

  Args:
    node: ast.AST
    copy_map: Dict[Hashable, Hashable], maps a source anno key to a destination
        key. All annotations with the source key will be copied to identical
        annotations with the destination key.
    field_name: str
  """
