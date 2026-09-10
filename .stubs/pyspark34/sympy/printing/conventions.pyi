from sympy.core.function import Derivative as Derivative

def split_super_sub(text):
    '''Split a symbol name into a name, superscripts and subscripts

    The first part of the symbol name is considered to be its actual
    \'name\', followed by super- and subscripts. Each superscript is
    preceded with a "^" character or by "__". Each subscript is preceded
    by a "_" character.  The three return values are the actual name, a
    list with superscripts and a list with subscripts.

    Examples
    ========

    >>> from sympy.printing.conventions import split_super_sub
    >>> split_super_sub(\'a_x^1\')
    (\'a\', [\'1\'], [\'x\'])
    >>> split_super_sub(\'var_sub1__sup_sub2\')
    (\'var\', [\'sup\'], [\'sub1\', \'sub2\'])

    '''
def requires_partial(expr):
    """Return whether a partial derivative symbol is required for printing

    This requires checking how many free variables there are,
    filtering out the ones that are integers. Some expressions do not have
    free variables. In that case, check its variable list explicitly to
    get the context of the expression.
    """
