from . import Builtin as Builtin, ExprNodes as ExprNodes, Nodes as Nodes, Options as Options, PyrexTypes as PyrexTypes, TypeSlots as TypeSlots, UtilNodes as UtilNodes, Visitor as Visitor
from .. import Utils as Utils
from .Code import TempitaUtilityCode as TempitaUtilityCode, UtilityCode as UtilityCode
from .Errors import error as error, warning as warning
from .ExprNodes import not_a_constant as not_a_constant
from .ParseTreeTransforms import SkipDeclarations as SkipDeclarations
from .StringEncoding import EncodedString as EncodedString, bytes_literal as bytes_literal, encoded_string as encoded_string
from _typeshed import Incomplete

basestring = str

def load_c_utility(name): ...
def unwrap_coerced_node(node, coercion_nodes=...): ...
def unwrap_node(node): ...
def is_common_value(a, b): ...
def filter_none_node(node): ...

class _YieldNodeCollector(Visitor.TreeVisitor):
    """
    YieldExprNode finder for generator expressions.
    """
    yield_stat_nodes: Incomplete
    yield_nodes: Incomplete
    def __init__(self) -> None: ...
    visit_Node: Incomplete
    def visit_YieldExprNode(self, node) -> None: ...
    def visit_ExprStatNode(self, node) -> None: ...
    def visit_GeneratorExpressionNode(self, node) -> None: ...
    def visit_LambdaNode(self, node) -> None: ...
    def visit_FuncDefNode(self, node) -> None: ...

class IterationTransform(Visitor.EnvTransform):
    """Transform some common for-in loop patterns into efficient C loops:

    - for-in-dict loop becomes a while loop calling PyDict_Next()
    - for-in-enumerate is replaced by an external counter variable
    - for-in-range loop becomes a plain C for loop
    """
    def visit_PrimaryCmpNode(self, node): ...
    def visit_ForInStatNode(self, node): ...
    PyBytes_AS_STRING_func_type: Incomplete
    PyBytes_GET_SIZE_func_type: Incomplete
    PyUnicode_READ_func_type: Incomplete
    init_unicode_iteration_func_type: Incomplete
    PyDict_Iterator_func_type: Incomplete
    PySet_Iterator_func_type: Incomplete

class SwitchTransform(Visitor.EnvTransform):
    """
    This transformation tries to turn long if statements into C switch statements.
    The requirement is that every clause be an (or of) var == value, where the var
    is common among all clauses and both var and value are ints.
    """
    NO_MATCH: Incomplete
    def extract_conditions(self, cond, allow_not_in): ...
    def extract_in_string_conditions(self, string_literal): ...
    def extract_common_conditions(self, common_var, condition, allow_not_in): ...
    def has_duplicate_values(self, condition_values): ...
    def visit_IfStatNode(self, node): ...
    def visit_CondExprNode(self, node): ...
    def visit_BoolBinopNode(self, node): ...
    def visit_PrimaryCmpNode(self, node): ...
    def build_simple_switch_statement(self, node, common_var, conditions, not_in, true_val, false_val): ...
    def visit_EvalWithTempExprNode(self, node): ...
    visit_Node: Incomplete

class FlattenInListTransform(Visitor.VisitorTransform, SkipDeclarations):
    '''
    This transformation flattens "x in [val1, ..., valn]" into a sequential list
    of comparisons.
    '''
    def visit_PrimaryCmpNode(self, node): ...
    visit_Node: Incomplete

class DropRefcountingTransform(Visitor.VisitorTransform):
    """Drop ref-counting in safe places.
    """
    visit_Node: Incomplete
    def visit_ParallelAssignmentNode(self, node):
        """
        Parallel swap assignments like 'a,b = b,a' are safe.
        """

class EarlyReplaceBuiltinCalls(Visitor.EnvTransform):
    """Optimize some common calls to builtin types *before* the type
    analysis phase and *after* the declarations analysis phase.

    This transform cannot make use of any argument types, but it can
    restructure the tree in a way that the type analysis phase can
    respond to.

    Introducing C function calls here may not be a good idea.  Move
    them to the OptimizeBuiltinCalls transform instead, which runs
    after type analysis.
    """
    visit_Node: Incomplete
    def visit_SimpleCallNode(self, node): ...
    def visit_GeneralCallNode(self, node): ...
    PySequence_List_func_type: Incomplete

class InlineDefNodeCalls(Visitor.NodeRefCleanupMixin, Visitor.EnvTransform):
    visit_Node: Incomplete
    def get_constant_value_node(self, name_node): ...
    def visit_SimpleCallNode(self, node): ...

class OptimizeBuiltinCalls(Visitor.NodeRefCleanupMixin, Visitor.MethodDispatcherTransform):
    """Optimize some common methods calls and instantiation patterns
    for builtin types *after* the type analysis phase.

    Running after type analysis, this transform can only perform
    function replacements that do not alter the function return type
    in a way that was not anticipated by the type analysis.
    """
    def visit_PyTypeTestNode(self, node):
        """Flatten redundant type checks after tree changes.
        """
    def visit_ExprStatNode(self, node):
        """
        Drop dead code and useless coercions.
        """
    def visit_CoerceToBooleanNode(self, node):
        """Drop redundant conversion nodes after tree changes.
        """
    PyNumber_Float_func_type: Incomplete
    def visit_CoerceToPyTypeNode(self, node):
        """Drop redundant conversion nodes after tree changes."""
    def visit_CoerceFromPyTypeNode(self, node):
        """Drop redundant conversion nodes after tree changes.

        Also, optimise away calls to Python's builtin int() and
        float() if the result is going to be coerced back into a C
        type anyway.
        """
    PyBytes_GetItemInt_func_type: Incomplete
    float_float_func_types: Incomplete
    pyucs4_int_func_type: Incomplete
    pyucs4_double_func_type: Incomplete
    PyObject_String_func_type: Incomplete
    PyObject_Unicode_func_type: Incomplete
    def visit_FormattedValueNode(self, node):
        """Simplify or avoid plain string formatting of a unicode value.
        This seems misplaced here, but plain unicode formatting is essentially
        a call to the unicode() builtin, which is optimised right above.
        """
    PyDict_Copy_func_type: Incomplete
    PySequence_List_func_type: Incomplete
    PyList_AsTuple_func_type: Incomplete
    PySet_New_func_type: Incomplete
    PyFrozenSet_New_func_type: Incomplete
    PyObject_AsDouble_func_type: Incomplete
    PyNumber_Int_func_type: Incomplete
    PyInt_FromDouble_func_type: Incomplete
    PyMemoryView_FromObject_func_type: Incomplete
    PyMemoryView_FromBuffer_func_type: Incomplete
    Pyx_ssize_strlen_func_type: Incomplete
    Pyx_Py_UNICODE_strlen_func_type: Incomplete
    PyObject_Size_func_type: Incomplete
    Pyx_Type_func_type: Incomplete
    Py_type_check_func_type: Incomplete
    Pyx_tp_new_func_type: Incomplete
    Pyx_tp_new_kwargs_func_type: Incomplete
    PyObject_Append_func_type: Incomplete
    PyByteArray_Append_func_type: Incomplete
    PyByteArray_AppendObject_func_type: Incomplete
    PyObject_Pop_func_type: Incomplete
    PyObject_PopIndex_func_type: Incomplete
    single_param_func_type: Incomplete
    Pyx_PyDict_GetItem_func_type: Incomplete
    Pyx_PyDict_SetDefault_func_type: Incomplete
    PyDict_Pop_func_type: Incomplete
    Pyx_BinopInt_func_types: Incomplete
    PyUnicode_uchar_predicate_func_type: Incomplete
    PyUnicode_uchar_conversion_func_type: Incomplete
    PyUnicode_Splitlines_func_type: Incomplete
    PyUnicode_Split_func_type: Incomplete
    PyUnicode_Join_func_type: Incomplete
    PyString_Tailmatch_func_type: Incomplete
    PyUnicode_Find_func_type: Incomplete
    PyUnicode_Count_func_type: Incomplete
    PyUnicode_Replace_func_type: Incomplete
    PyUnicode_AsEncodedString_func_type: Incomplete
    PyUnicode_AsXyzString_func_type: Incomplete
    PyUnicode_DecodeXyz_func_ptr_type: Incomplete
    obj_to_obj_func_type: Incomplete

def optimise_numeric_binop(operator, node, ret_type, arg0, arg1):
    """
    Optimise math operators for (likely) float or small integer operations.
    """

unicode_tailmatch_utility_code: Incomplete
bytes_tailmatch_utility_code: Incomplete
str_tailmatch_utility_code: Incomplete

class ConstantFolding(Visitor.VisitorTransform, SkipDeclarations):
    """Calculate the result of constant expressions to store it in
    ``expr_node.constant_result``, and replace trivial cases by their
    constant result.

    General rules:

    - We calculate float constants to make them available to the
      compiler, but we do not aggregate them into a single literal
      node to prevent any loss of precision.

    - We recursively calculate constants from non-literal nodes to
      make them available to the compiler, but we only aggregate
      literal nodes at each step.  Non-literal nodes are never merged
      into a single node.
    """
    reevaluate: Incomplete
    def __init__(self, reevaluate: bool = False) -> None:
        """
        The reevaluate argument specifies whether constant values that were
        previously computed should be recomputed.
        """
    NODE_TYPE_ORDER: Incomplete
    def visit_ExprNode(self, node): ...
    def visit_UnopNode(self, node): ...
    def visit_BoolBinopNode(self, node): ...
    def visit_BinopNode(self, node): ...
    def visit_AddNode(self, node): ...
    def visit_MulNode(self, node): ...
    def visit_ModNode(self, node): ...
    def visit_FormattedValueNode(self, node): ...
    def visit_JoinedStrNode(self, node):
        """
        Clean up after the parser by discarding empty Unicode strings and merging
        substring sequences.  Empty or single-value join lists are not uncommon
        because f-string format specs are always parsed into JoinedStrNodes.
        """
    def visit_MergedDictNode(self, node):
        """Unpack **args in place if we can."""
    def visit_MergedSequenceNode(self, node):
        """Unpack *args in place if we can."""
    def visit_SequenceNode(self, node):
        """Unpack *args in place if we can."""
    def visit_PrimaryCmpNode(self, node): ...
    def visit_CondExprNode(self, node): ...
    def visit_IfStatNode(self, node): ...
    def visit_SliceIndexNode(self, node): ...
    def visit_ComprehensionNode(self, node): ...
    def visit_ForInStatNode(self, node): ...
    def visit_WhileStatNode(self, node): ...
    def visit_ExprStatNode(self, node): ...
    def visit_GILStatNode(self, node): ...
    visit_Node: Incomplete

class FinalOptimizePhase(Visitor.EnvTransform, Visitor.NodeRefCleanupMixin):
    """
    This visitor handles several commuting optimizations, and is run
    just before the C code generation phase.

    The optimizations currently implemented in this class are:
        - eliminate None assignment and refcounting for first assignment.
        - isinstance -> typecheck for cdef types
        - eliminate checks for None and/or types that became redundant after tree changes
        - eliminate useless string formatting steps
        - inject branch hints for unlikely if-cases that only raise exceptions
        - replace Python function calls that look like method calls by a faster PyMethodCallNode
    """
    in_loop: bool
    def visit_SingleAssignmentNode(self, node):
        """Avoid redundant initialisation of local variables before their
        first assignment.
        """
    def visit_SimpleCallNode(self, node):
        """
        Replace generic calls to isinstance(x, type) by a more efficient type check.
        Replace likely Python method calls by a specialised PyMethodCallNode.
        """
    def visit_NumPyMethodCallNode(self, node): ...
    def visit_PyTypeTestNode(self, node):
        """Remove tests for alternatively allowed None values from
        type tests when we know that the argument cannot be None
        anyway.
        """
    def visit_NoneCheckNode(self, node):
        """Remove None checks from expressions that definitely do not
        carry a None value.
        """
    def visit_LoopNode(self, node):
        """Remember when we enter a loop as some expensive optimisations might still be worth it there.
        """
    def visit_IfStatNode(self, node):
        """Assign 'unlikely' branch hints to if-clauses that only raise exceptions.
        """

class ConsolidateOverflowCheck(Visitor.CythonTransform):
    """
    This class facilitates the sharing of overflow checking among all nodes
    of a nested arithmetic expression.  For example, given the expression
    a*b + c, where a, b, and x are all possibly overflowing ints, the entire
    sequence will be evaluated and the overflow bit checked only at the end.
    """
    overflow_bit_node: Incomplete
    def visit_Node(self, node): ...
    def visit_NumBinopNode(self, node): ...
