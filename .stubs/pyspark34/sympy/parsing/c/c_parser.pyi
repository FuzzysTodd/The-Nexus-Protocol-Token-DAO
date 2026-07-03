from _typeshed import Incomplete
from sympy.codegen.ast import Assignment as Assignment, CodeBlock as CodeBlock, Float as Float, FunctionCall as FunctionCall, FunctionDefinition as FunctionDefinition, FunctionPrototype as FunctionPrototype, Integer as Integer, Return as Return, Variable as Variable, While as While, aug_assign as aug_assign, bool_ as bool_, float32 as float32, float64 as float64, float80 as float80, int16 as int16, int64 as int64, int8 as int8, intc as intc, none as none, uint16 as uint16, uint32 as uint32, uint64 as uint64, uint8 as uint8
from sympy.codegen.cnodes import PostDecrement as PostDecrement, PostIncrement as PostIncrement, PreDecrement as PreDecrement, PreIncrement as PreIncrement
from sympy.core import Add as Add, Mod as Mod, Mul as Mul, Pow as Pow, Rel as Rel
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.external import import_module as import_module
from sympy.logic.boolalg import And as And, Not as Not, Or as Or, as_Boolean as as_Boolean, false as false, true as true

cin: Incomplete

class BaseParser:
    """Base Class for the C parser"""
    index: Incomplete
    def __init__(self) -> None:
        """Initializes the Base parser creating a Clang AST index"""
    def diagnostics(self, out) -> None:
        """Diagostics function for the Clang AST"""

class CCodeConverter(BaseParser):
    """The Code Convereter for Clang AST

        The converter object takes the C source code or file as input and
        converts them to SymPy Expressions.
        """
    def __init__(self) -> None:
        """Initializes the code converter"""
    tu: Incomplete
    def parse(self, filenames, flags):
        """Function to parse a file with C source code

            It takes the filename as an attribute and creates a Clang AST
            Translation Unit parsing the file.
            Then the transformation function is called on the translation unit,
            whose reults are collected into a list which is returned by the
            function.

            Parameters
            ==========

            filenames : string
                Path to the C file to be parsed

            flags: list
                Arguments to be passed to Clang while parsing the C code

            Returns
            =======

            py_nodes: list
                A list of SymPy AST nodes

            """
    def parse_str(self, source, flags):
        """Function to parse a string with C source code

            It takes the source code as an attribute, stores it in a temporary
            file and creates a Clang AST Translation Unit parsing the file.
            Then the transformation function is called on the translation unit,
            whose reults are collected into a list which is returned by the
            function.

            Parameters
            ==========

            source : string
                Path to the C file to be parsed

            flags: list
                Arguments to be passed to Clang while parsing the C code

            Returns
            =======

            py_nodes: list
                A list of SymPy AST nodes

            """
    def transform(self, node):
        """Transformation Function for Clang AST nodes

            It determines the kind of node and calls the respective
            transformation function for that node.

            Raises
            ======

            NotImplementedError : if the transformation for the provided node
            is not implemented

            """
    def transform_var_decl(self, node):
        """Transformation Function for Variable Declaration

            Used to create nodes for variable declarations and assignments with
            values or function call for the respective nodes in the clang AST

            Returns
            =======

            A variable node as Declaration, with the initial value if given

            Raises
            ======

            NotImplementedError : if called for data types not currently
            implemented

            Notes
            =====

            The function currently supports following data types:

            Boolean:
                bool, _Bool

            Integer:
                8-bit: signed char and unsigned char
                16-bit: short, short int, signed short,
                    signed short int, unsigned short, unsigned short int
                32-bit: int, signed int, unsigned int
                64-bit: long, long int, signed long,
                    signed long int, unsigned long, unsigned long int

            Floating point:
                Single Precision: float
                Double Precision: double
                Extended Precision: long double

            """
    def transform_function_decl(self, node):
        """Transformation Function For Function Declaration

            Used to create nodes for function declarations and definitions for
            the respective nodes in the clang AST

            Returns
            =======

            function : Codegen AST node
                - FunctionPrototype node if function body is not present
                - FunctionDefinition node if the function body is present


            """
    def transform_parm_decl(self, node):
        """Transformation function for Parameter Declaration

            Used to create parameter nodes for the required functions for the
            respective nodes in the clang AST

            Returns
            =======

            param : Codegen AST Node
                Variable node with the value and type of the variable

            Raises
            ======

            ValueError if multiple children encountered in the parameter node

            """
    def transform_integer_literal(self, node):
        """Transformation function for integer literal

            Used to get the value and type of the given integer literal.

            Returns
            =======

            val : list
                List with two arguments type and Value
                type contains the type of the integer
                value contains the value stored in the variable

            Notes
            =====

            Only Base Integer type supported for now

            """
    def transform_floating_literal(self, node):
        """Transformation function for floating literal

            Used to get the value and type of the given floating literal.

            Returns
            =======

            val : list
                List with two arguments type and Value
                type contains the type of float
                value contains the value stored in the variable

            Notes
            =====

            Only Base Float type supported for now

            """
    def transform_string_literal(self, node) -> None: ...
    def transform_character_literal(self, node):
        """Transformation function for character literal

            Used to get the value of the given character literal.

            Returns
            =======

            val : int
                val contains the ascii value of the character literal

            Notes
            =====

            Only for cases where character is assigned to a integer value,
            since character literal is not in SymPy AST

            """
    def transform_cxx_bool_literal_expr(self, node):
        """Transformation function for boolean literal

            Used to get the value of the given boolean literal.

            Returns
            =======

            value : bool
                value contains the boolean value of the variable

            """
    def transform_unexposed_decl(self, node) -> None:
        """Transformation function for unexposed declarations"""
    def transform_unexposed_expr(self, node):
        """Transformation function for unexposed expression

            Unexposed expressions are used to wrap float, double literals and
            expressions

            Returns
            =======

            expr : Codegen AST Node
                the result from the wrapped expression

            None : NoneType
                No childs are found for the node

            Raises
            ======

            ValueError if the expression contains multiple children

            """
    def transform_decl_ref_expr(self, node):
        """Returns the name of the declaration reference"""
    def transform_call_expr(self, node):
        """Transformation function for a call expression

            Used to create function call nodes for the function calls present
            in the C code

            Returns
            =======

            FunctionCall : Codegen AST Node
                FunctionCall node with parameters if any parameters are present

            """
    def transform_return_stmt(self, node):
        """Returns the Return Node for a return statement"""
    def transform_compound_stmt(self, node):
        """Transformation function for compond statemets

            Returns
            =======

            expr : list
                list of Nodes for the expressions present in the statement

            None : NoneType
                if the compound statement is empty

            """
    def transform_decl_stmt(self, node):
        """Transformation function for declaration statements

            These statements are used to wrap different kinds of declararions
            like variable or function declaration
            The function calls the transformer function for the child of the
            given node

            Returns
            =======

            statement : Codegen AST Node
                contains the node returned by the children node for the type of
                declaration

            Raises
            ======

            ValueError if multiple children present

            """
    def transform_paren_expr(self, node):
        """Transformation function for Parenthesized expressions

            Returns the result from its children nodes

            """
    def transform_compound_assignment_operator(self, node):
        """Transformation function for handling shorthand operators

            Returns
            =======

            augmented_assignment_expression: Codegen AST node
                    shorthand assignment expression represented as Codegen AST

            Raises
            ======

            NotImplementedError
                If the shorthand operator for bitwise operators
                (~=, ^=, &=, |=, <<=, >>=) is encountered

            """
    def transform_unary_operator(self, node):
        """Transformation function for handling unary operators

            Returns
            =======

            unary_expression: Codegen AST node
                    simplified unary expression represented as Codegen AST

            Raises
            ======

            NotImplementedError
                If dereferencing operator(*), address operator(&) or
                bitwise NOT operator(~) is encountered

            """
    def transform_binary_operator(self, node):
        """Transformation function for handling binary operators

            Returns
            =======

            binary_expression: Codegen AST node
                    simplified binary expression represented as Codegen AST

            Raises
            ======

            NotImplementedError
                If a bitwise operator or
                unary operator(which is a child of any binary
                operator in Clang AST) is encountered

            """
    def priority_of(self, op):
        """To get the priority of given operator"""
    def perform_operation(self, lhs, rhs, op):
        """Performs operation supported by the SymPy core

            Returns
            =======

            combined_variable: list
                contains variable content and type of variable

            """
    def get_expr_for_operand(self, combined_variable):
        """Gives out SymPy Codegen AST node

            AST node returned is corresponding to
            combined variable passed.Combined variable contains
            variable content and type of variable

            """
    def transform_null_stmt(self, node):
        """Handles Null Statement and returns None"""
    def transform_while_stmt(self, node):
        """Transformation function for handling while statement

            Returns
            =======

            while statement : Codegen AST Node
                contains the while statement node having condition and
                statement block

            """

class CCodeConverter:
    def __init__(self, *args, **kwargs) -> None: ...

def parse_c(source):
    """Function for converting a C source code

    The function reads the source code present in the given file and parses it
    to give out SymPy Expressions

    Returns
    =======

    src : list
        List of Python expression strings

    """
