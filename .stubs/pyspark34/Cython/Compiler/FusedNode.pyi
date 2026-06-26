from . import Errors as Errors, ExprNodes as ExprNodes, MemoryView as MemoryView, ParseTreeTransforms as ParseTreeTransforms, PyrexTypes as PyrexTypes, StringEncoding as StringEncoding
from ..Utils import OrderedSet as OrderedSet
from .Errors import CannotSpecialize as CannotSpecialize, error as error
from .ExprNodes import CloneNode as CloneNode, ProxyNode as ProxyNode, TupleNode as TupleNode
from .Nodes import CFuncDefNode as CFuncDefNode, DefNode as DefNode, FuncDefNode as FuncDefNode, StatListNode as StatListNode
from _typeshed import Incomplete

class FusedCFuncDefNode(StatListNode):
    """
    This node replaces a function with fused arguments. It deep-copies the
    function for every permutation of fused types, and allocates a new local
    scope for it. It keeps track of the original function in self.node, and
    the entry of the original function in the symbol table is given the
    'fused_cfunction' attribute which points back to us.
    Then when a function lookup occurs (to e.g. call it), the call can be
    dispatched to the right function.

    node    FuncDefNode    the original function
    nodes   [FuncDefNode]  list of copies of node with different specific types
    py_func DefNode        the fused python function subscriptable from
                           Python space
    __signatures__         A DictNode mapping signature specialization strings
                           to PyCFunction nodes
    resulting_fused_function  PyCFunction for the fused DefNode that delegates
                              to specializations
    fused_func_assignment   Assignment of the fused function to the function name
    defaults_tuple          TupleNode of defaults (letting PyCFunctionNode build
                            defaults would result in many different tuples)
    specialized_pycfuncs    List of synthesized pycfunction nodes for the
                            specializations
    code_object             CodeObjectNode shared by all specializations and the
                            fused function

    fused_compound_types    All fused (compound) types (e.g. floating[:])
    """
    __signatures__: Incomplete
    resulting_fused_function: Incomplete
    fused_func_assignment: Incomplete
    defaults_tuple: Incomplete
    decorators: Incomplete
    child_attrs: Incomplete
    nodes: Incomplete
    node: Incomplete
    stats: Incomplete
    def __init__(self, node, env) -> None: ...
    fused_compound_types: Incomplete
    orig_py_func: Incomplete
    py_func: Incomplete
    def copy_def(self, env) -> None:
        """
        Create a copy of the original def or lambda function for specialized
        versions.
        """
    def copy_cdef(self, env) -> None:
        """
        Create a copy of the original c(p)def function for all specialized
        versions.
        """
    def create_new_local_scope(self, node, env, f2s) -> None:
        """
        Create a new local scope for the copied node and append it to
        self.nodes. A new local scope is needed because the arguments with the
        fused types are already in the local scope, and we need the specialized
        entries created after analyse_declarations on each specialized version
        of the (CFunc)DefNode.
        f2s is a dict mapping each fused type to its specialized version
        """
    def specialize_copied_def(self, node, cname, py_entry, f2s, fused_compound_types) -> None:
        """Specialize the copy of a DefNode given the copied node,
        the specialization cname and the original DefNode entry"""
    def replace_fused_typechecks(self, copied_node):
        """
        Branch-prune fused type checks like

            if fused_t is int:
                ...

        Returns whether an error was issued and whether we should stop in
        in order to prevent a flood of errors.
        """
    match: str
    no_match: str
    fragment_scope: Incomplete
    def make_fused_cpdef(self, orig_py_func, env, is_def):
        """
        This creates the function that is indexable from Python and does
        runtime dispatch based on the argument types. The function gets the
        arg tuple and kwargs dict (or None) and the defaults tuple
        as arguments from the Binding Fused Function's tp_call.
        """
    def update_fused_defnode_entry(self, env) -> None: ...
    defaults: Incomplete
    code_object: Incomplete
    def analyse_expressions(self, env):
        """
        Analyse the expressions. Take care to only evaluate default arguments
        once and clone the result for all specializations
        """
    specialized_pycfuncs: Incomplete
    def synthesize_defnodes(self) -> None:
        """
        Create the __signatures__ dict of PyCFunctionNode specializations.
        """
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...
