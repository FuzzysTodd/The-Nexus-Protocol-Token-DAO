from _typeshed import Incomplete
from sympy.codegen.ast import Attribute as Attribute, CodeBlock as CodeBlock, Declaration as Declaration, FunctionCall as FunctionCall, Node as Node, String as String, Token as Token, Type as Type, none as none
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.sympify import sympify as sympify

void: Incomplete
restrict: Incomplete
volatile: Incomplete
static: Incomplete

def alignof(arg):
    """ Generate of FunctionCall instance for calling 'alignof' """
def sizeof(arg):
    """ Generate of FunctionCall instance for calling 'sizeof'

    Examples
    ========

    >>> from sympy.codegen.ast import real
    >>> from sympy.codegen.cnodes import sizeof
    >>> from sympy import ccode
    >>> ccode(sizeof(real))
    'sizeof(double)'
    """

class CommaOperator(Basic):
    """ Represents the comma operator in C """
    def __new__(cls, *args): ...

class Label(Node):
    """ Label for use with e.g. goto statement.

    Examples
    ========

    >>> from sympy import ccode, Symbol
    >>> from sympy.codegen.cnodes import Label, PreIncrement
    >>> print(ccode(Label('foo')))
    foo:
    >>> print(ccode(Label('bar', [PreIncrement(Symbol('a'))])))
    bar:
    ++(a);

    """
    defaults: Incomplete

class goto(Token):
    """ Represents goto in C """

class PreDecrement(Basic):
    """ Represents the pre-decrement operator

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cnodes import PreDecrement
    >>> from sympy import ccode
    >>> ccode(PreDecrement(x))
    '--(x)'

    """
    nargs: int

class PostDecrement(Basic):
    """ Represents the post-decrement operator """
    nargs: int

class PreIncrement(Basic):
    """ Represents the pre-increment operator """
    nargs: int

class PostIncrement(Basic):
    """ Represents the post-increment operator """
    nargs: int

class struct(Node):
    """ Represents a struct in C """
    defaults: Incomplete

class union(struct):
    """ Represents a union in C """
