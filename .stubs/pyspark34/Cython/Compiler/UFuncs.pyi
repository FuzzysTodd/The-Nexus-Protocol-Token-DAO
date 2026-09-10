from . import ExprNodes as ExprNodes, FusedNode as FusedNode, Naming as Naming, Nodes as Nodes, ParseTreeTransforms as ParseTreeTransforms, Pipeline as Pipeline, PyrexTypes as PyrexTypes, TreeFragment as TreeFragment, UtilNodes as UtilNodes
from .Code import TempitaUtilityCode as TempitaUtilityCode, UtilityCode as UtilityCode
from .Errors import error as error
from .UtilityCode import CythonUtilityCode as CythonUtilityCode
from .Visitor import PrintTree as PrintTree, TreeVisitor as TreeVisitor, VisitorTransform as VisitorTransform
from _typeshed import Incomplete

numpy_int_types: Incomplete
numpy_uint_types: Incomplete
numpy_numeric_types: Incomplete

class _FindCFuncDefNode(TreeVisitor):
    """
    Finds the CFuncDefNode in the tree

    The assumption is that there's only one CFuncDefNode
    """
    found_node: Incomplete
    def visit_Node(self, node) -> None: ...
    def visit_CFuncDefNode(self, node) -> None: ...
    def __call__(self, tree): ...

def get_cfunc_from_tree(tree): ...

class _ArgumentInfo:
    '''
    Everything related to defining an input/output argument for a ufunc

    type  - PyrexType
    type_constant  - str such as "NPY_INT8" representing numpy dtype constants
    '''
    type: Incomplete
    type_constant: Incomplete
    def __init__(self, type, type_constant) -> None: ...

class UFuncConversion:
    node: Incomplete
    global_scope: Incomplete
    in_definitions: Incomplete
    out_definitions: Incomplete
    def __init__(self, node) -> None: ...
    def get_in_type_info(self): ...
    def get_out_type_info(self): ...
    def generate_cy_utility_code(self): ...
    def use_generic_utility_code(self) -> None: ...

def convert_to_ufunc(node): ...
def generate_ufunc_initialization(converters, cfunc_nodes, original_node): ...
