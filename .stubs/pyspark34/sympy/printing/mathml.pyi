from _typeshed import Incomplete
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.sympify import sympify as sympify
from sympy.printing.conventions import requires_partial as requires_partial, split_super_sub as split_super_sub
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, PRECEDENCE_TRADITIONAL as PRECEDENCE_TRADITIONAL, precedence_traditional as precedence_traditional
from sympy.printing.pretty.pretty_symbology import greek_unicode as greek_unicode
from sympy.printing.printer import Printer as Printer, print_function as print_function

class MathMLPrinterBase(Printer):
    """Contains common code required for MathMLContentPrinter and
    MathMLPresentationPrinter.
    """
    dom: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def doprint(self, expr):
        """
        Prints the expression as MathML.
        """
    def apply_patch(self) -> None: ...
    def restore_patch(self) -> None: ...

class MathMLContentPrinter(MathMLPrinterBase):
    """Prints an expression to the Content MathML markup language.

    References: https://www.w3.org/TR/MathML2/chapter4.html
    """
    printmethod: str
    def mathml_tag(self, e):
        """Returns the MathML tag for an expression."""

class MathMLPresentationPrinter(MathMLPrinterBase):
    """Prints an expression to the Presentation MathML markup language.

    References: https://www.w3.org/TR/MathML2/chapter3.html
    """
    printmethod: str
    def mathml_tag(self, e):
        """Returns the MathML tag for an expression."""
    def parenthesize(self, item, level, strict: bool = False): ...

def mathml(expr, printer: str = 'content', **settings):
    """Returns the MathML representation of expr. If printer is presentation
    then prints Presentation MathML else prints content MathML.
    """
def print_mathml(expr, printer: str = 'content', **settings) -> None:
    """
    Prints a pretty representation of the MathML code for expr. If printer is
    presentation then prints Presentation MathML else prints content MathML.

    Examples
    ========

    >>> ##
    >>> from sympy import print_mathml
    >>> from sympy.abc import x
    >>> print_mathml(x+1) #doctest: +NORMALIZE_WHITESPACE
    <apply>
        <plus/>
        <ci>x</ci>
        <cn>1</cn>
    </apply>
    >>> print_mathml(x+1, printer='presentation')
    <mrow>
        <mi>x</mi>
        <mo>+</mo>
        <mn>1</mn>
    </mrow>

    """
MathMLPrinter = MathMLContentPrinter
