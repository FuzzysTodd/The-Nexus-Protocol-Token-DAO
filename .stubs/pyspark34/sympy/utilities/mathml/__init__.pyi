from _typeshed import Incomplete
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.pkgdata import get_resource as get_resource

__doctest_requires__: Incomplete

def add_mathml_headers(s): ...
def apply_xsl(mml, xsl):
    '''Apply a xsl to a MathML string.

    Parameters
    ==========

    mml
        A string with MathML code.
    xsl
        A string representing a path to a xsl (xml stylesheet) file.
        This file name is relative to the PYTHONPATH.

    Examples
    ========

    >>> from sympy.utilities.mathml import apply_xsl
    >>> xsl = \'mathml/data/simple_mmlctop.xsl\'
    >>> mml = \'<apply> <plus/> <ci>a</ci> <ci>b</ci> </apply>\'
    >>> res = apply_xsl(mml,xsl)
    >>> \'\'.join(res.splitlines())
    \'<?xml version="1.0"?><mrow xmlns="http://www.w3.org/1998/Math/MathML">  <mi>a</mi>  <mo> + </mo>  <mi>b</mi></mrow>\'
    '''
def c2p(mml, simple: bool = False):
    """Transforms a document in MathML content (like the one that sympy produces)
    in one document in MathML presentation, more suitable for printing, and more
    widely accepted

    Examples
    ========

    >>> from sympy.utilities.mathml import c2p
    >>> mml = '<apply> <exp/> <cn>2</cn> </apply>'
    >>> c2p(mml,simple=True) != c2p(mml,simple=False)
    True

    """
