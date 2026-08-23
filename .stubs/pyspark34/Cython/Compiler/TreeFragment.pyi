from . import Main as Main, Parsing as Parsing, PyrexTypes as PyrexTypes, UtilNodes as UtilNodes
from .ExprNodes import NameNode as NameNode
from .Nodes import Node as Node, StatListNode as StatListNode
from .Scanning import PyrexScanner as PyrexScanner, StringSourceDescriptor as StringSourceDescriptor
from .Symtab import ModuleScope as ModuleScope
from .Visitor import VisitorTransform as VisitorTransform
from _typeshed import Incomplete

class StringParseContext(Main.Context):
    module_name: Incomplete
    def __init__(self, name, include_directories: Incomplete | None = None, compiler_directives: Incomplete | None = None, cpp: bool = False) -> None: ...
    def find_module(self, module_name, from_module: Incomplete | None = None, pos: Incomplete | None = None, need_pxd: int = 1, absolute_fallback: bool = True, relative_import: bool = False): ...

def parse_from_strings(name, code, pxds: Incomplete | None = None, level: Incomplete | None = None, initial_pos: Incomplete | None = None, context: Incomplete | None = None, allow_struct_enum_decorator: bool = False, in_utility_code: bool = False):
    """
    Utility method to parse a (unicode) string of code. This is mostly
    used for internal Cython compiler purposes (creating code snippets
    that transforms should emit, as well as unit testing).

    code - a unicode string containing Cython (module-level) code
    name - a descriptive name for the code source (to use in error messages etc.)
    in_utility_code - used to suppress some messages from utility code. False by default
                      because some generated code snippets like properties and dataclasses
                      probably want to see those messages.

    RETURNS

    The tree, i.e. a ModuleNode. The ModuleNode's scope attribute is
    set to the scope used when parsing.
    """

class TreeCopier(VisitorTransform):
    def visit_Node(self, node): ...

class ApplyPositionAndCopy(TreeCopier):
    pos: Incomplete
    def __init__(self, pos) -> None: ...
    def visit_Node(self, node): ...

class TemplateTransform(VisitorTransform):
    '''
    Makes a copy of a template tree while doing substitutions.

    A dictionary "substitutions" should be passed in when calling
    the transform; mapping names to replacement nodes. Then replacement
    happens like this:
     - If an ExprStatNode contains a single NameNode, whose name is
       a key in the substitutions dictionary, the ExprStatNode is
       replaced with a copy of the tree given in the dictionary.
       It is the responsibility of the caller that the replacement
       node is a valid statement.
     - If a single NameNode is otherwise encountered, it is replaced
       if its name is listed in the substitutions dictionary in the
       same way. It is the responsibility of the caller to make sure
       that the replacement nodes is a valid expression.

    Also a list "temps" should be passed. Any names listed will
    be transformed into anonymous, temporary names.

    Currently supported for tempnames is:
    NameNode
    (various function and class definition nodes etc. should be added to this)

    Each replacement node gets the position of the substituted node
    recursively applied to every member node.
    '''
    temp_name_counter: int
    substitutions: Incomplete
    pos: Incomplete
    tempmap: Incomplete
    def __call__(self, node, substitutions, temps, pos): ...
    def get_pos(self, node): ...
    def visit_Node(self, node): ...
    def try_substitution(self, node, key): ...
    def visit_NameNode(self, node): ...
    def visit_ExprStatNode(self, node): ...

def copy_code_tree(node): ...
def strip_common_indent(lines):
    """Strips empty lines and common indentation from the list of strings given in lines"""

class TreeFragment:
    root: Incomplete
    temps: Incomplete
    def __init__(self, code, name: Incomplete | None = None, pxds: Incomplete | None = None, temps: Incomplete | None = None, pipeline: Incomplete | None = None, level: Incomplete | None = None, initial_pos: Incomplete | None = None) -> None: ...
    def copy(self): ...
    def substitute(self, nodes: Incomplete | None = None, temps: Incomplete | None = None, pos: Incomplete | None = None): ...

class SetPosTransform(VisitorTransform):
    pos: Incomplete
    def __init__(self, pos) -> None: ...
    def visit_Node(self, node): ...
