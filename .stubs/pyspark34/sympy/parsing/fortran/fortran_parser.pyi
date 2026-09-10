from _typeshed import Incomplete
from sympy.codegen.ast import Assignment as Assignment, FloatBaseType as FloatBaseType, FunctionDefinition as FunctionDefinition, IntBaseType as IntBaseType, Return as Return, String as String, Variable as Variable
from sympy.core import Add as Add, Float as Float, Integer as Integer, Mul as Mul
from sympy.core.symbol import Symbol as Symbol
from sympy.external import import_module as import_module

lfortran: Incomplete
asr_mod: Incomplete
asr: Incomplete
src_to_ast: Incomplete
ast_to_asr: Incomplete

class ASR2PyVisitor(asr.ASTVisitor):
    """
        Visitor Class for LFortran ASR

        It is a Visitor class derived from asr.ASRVisitor which visits all the
        nodes of the LFortran ASR and creates corresponding AST node for each
        ASR node

        """
    def __init__(self) -> None:
        """Initialize the Parser"""
    def visit_TranslationUnit(self, node) -> None:
        """
            Function to visit all the elements of the Translation Unit
            created by LFortran ASR
            """
    def visit_Assignment(self, node) -> None:
        """Visitor Function for Assignment

            Visits each Assignment is the LFortran ASR and creates corresponding
            assignment for SymPy.

            Notes
            =====

            The function currently only supports variable assignment and binary
            operation assignments of varying multitudes. Any type of numberS or
            array is not supported.

            Raises
            ======

            NotImplementedError() when called for Numeric assignments or Arrays

            """
    def visit_BinOp(self, node) -> None:
        """Visitor Function for Binary Operations

            Visits each binary operation present in the LFortran ASR like addition,
            subtraction, multiplication, division and creates the corresponding
            operation node in SymPy's AST

            In case of more than one binary operations, the function calls the
            call_visitor() function on the child nodes of the binary operations
            recursively until all the operations have been processed.

            Notes
            =====

            The function currently only supports binary operations with Variables
            or other binary operations. Numerics are not supported as of yet.

            Raises
            ======

            NotImplementedError() when called for Numeric assignments

            """
    def visit_Variable(self, node) -> None:
        """Visitor Function for Variable Declaration

            Visits each variable declaration present in the ASR and creates a
            Symbol declaration for each variable

            Notes
            =====

            The functions currently only support declaration of integer and
            real variables. Other data types are still under development.

            Raises
            ======

            NotImplementedError() when called for unsupported data types

            """
    def visit_Sequence(self, seq) -> None:
        """Visitor Function for code sequence

            Visits a code sequence/ block and calls the visitor function on all the
            children of the code block to create corresponding code in python

            """
    def visit_Num(self, node) -> None:
        """Visitor Function for Numbers in ASR

            This function is currently under development and will be updated
            with improvements in the LFortran ASR

            """
    def visit_Function(self, node) -> None:
        """Visitor Function for function Definitions

            Visits each function definition present in the ASR and creates a
            function definition node in the Python AST with all the elements of the
            given function

            The functions declare all the variables required as SymPy symbols in
            the function before the function definition

            This function also the call_visior_function to parse the contents of
            the function body

            """
    def ret_ast(self):
        """Returns the AST nodes"""

class ASR2PyVisitor:
    def __init__(self, *args, **kwargs) -> None: ...

def call_visitor(fort_node):
    """Calls the AST Visitor on the Module

    This function is used to call the AST visitor for a program or module
    It imports all the required modules and calls the visit() function
    on the given node

    Parameters
    ==========

    fort_node : LFortran ASR object
        Node for the operation for which the NodeVisitor is called

    Returns
    =======

    res_ast : list
        list of SymPy AST Nodes

    """
def src_to_sympy(src):
    """Wrapper function to convert the given Fortran source code to SymPy Expressions

    Parameters
    ==========

    src : string
        A string with the Fortran source code

    Returns
    =======

    py_src : string
        A string with the Python source code compatible with SymPy

    """
