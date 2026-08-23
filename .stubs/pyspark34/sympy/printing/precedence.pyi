from _typeshed import Incomplete

PRECEDENCE: Incomplete
PRECEDENCE_VALUES: Incomplete

def precedence_Mul(item): ...
def precedence_Rational(item): ...
def precedence_Integer(item): ...
def precedence_Float(item): ...
def precedence_PolyElement(item): ...
def precedence_FracElement(item): ...
def precedence_UnevaluatedExpr(item): ...

PRECEDENCE_FUNCTIONS: Incomplete

def precedence(item):
    """Returns the precedence of a given object.

    This is the precedence for StrPrinter.
    """

PRECEDENCE_TRADITIONAL: Incomplete

def precedence_traditional(item):
    """Returns the precedence of a given object according to the
    traditional rules of mathematics.

    This is the precedence for the LaTeX and pretty printer.
    """
