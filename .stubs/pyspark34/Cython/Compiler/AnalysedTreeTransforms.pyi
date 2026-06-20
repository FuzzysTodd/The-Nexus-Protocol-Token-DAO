from . import Symtab as Symtab
from .ExprNodes import DictItemNode as DictItemNode, DictNode as DictNode, NameNode as NameNode, UnicodeNode as UnicodeNode
from .Nodes import CFuncDefNode as CFuncDefNode, DefNode as DefNode, SingleAssignmentNode as SingleAssignmentNode, StatListNode as StatListNode
from .PyrexTypes import py_object_type as py_object_type
from .StringEncoding import EncodedString as EncodedString
from .Visitor import ScopeTrackingTransform as ScopeTrackingTransform
from _typeshed import Incomplete

class AutoTestDictTransform(ScopeTrackingTransform):
    excludelist: Incomplete
    scope_type: str
    scope_node: Incomplete
    all_docstrings: Incomplete
    cdef_docstrings: Incomplete
    tests: Incomplete
    testspos: Incomplete
    def visit_ModuleNode(self, node): ...
    def add_test(self, testpos, path, doctest) -> None: ...
    def visit_ExprNode(self, node): ...
    def visit_FuncDefNode(self, node): ...
