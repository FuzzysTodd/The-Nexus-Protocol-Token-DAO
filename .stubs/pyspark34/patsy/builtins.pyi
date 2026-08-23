from patsy.categorical import C as C
from patsy.contrasts import ContrastMatrix as ContrastMatrix, Diff as Diff, Helmert as Helmert, Poly as Poly, Sum as Sum, Treatment as Treatment
from patsy.mgcv_cubic_splines import cc as cc, cr as cr, te as te
from patsy.splines import bs as bs
from patsy.state import center as center, scale as scale, standardize as standardize

__all__ = ['I', 'Q', 'ContrastMatrix', 'Treatment', 'Poly', 'Sum', 'Helmert', 'Diff', 'C', 'center', 'standardize', 'scale', 'bs', 'cr', 'cc', 'te']

def I(x):
    """The identity function. Simply returns its input unchanged.

    Since Patsy's formula parser ignores anything inside a function call
    syntax, this is useful to 'hide' arithmetic operations from it. For
    instance::

      y ~ x1 + x2

    has ``x1`` and ``x2`` as two separate predictors. But in::

      y ~ I(x1 + x2)

    we instead have a single predictor, defined to be the sum of ``x1`` and
    ``x2``."""
def Q(name):
    '''A way to \'quote\' variable names, especially ones that do not otherwise
    meet Python\'s variable name rules.

    If ``x`` is a variable, ``Q("x")`` returns the value of ``x``. (Note that
    ``Q`` takes the *string* ``"x"``, not the value of ``x`` itself.) This
    works even if instead of ``x``, we have a variable name that would not
    otherwise be legal in Python.

    For example, if you have a column of data named ``weight.in.kg``, then you
    can\'t write::

      y ~ weight.in.kg

    because Python will try to find a variable named ``weight``, that has an
    attribute named ``in``, that has an attribute named ``kg``. (And worse
    yet, ``in`` is a reserved word, which makes this example doubly broken.)
    Instead, write::

      y ~ Q("weight.in.kg")

    and all will be well. Note, though, that this requires embedding a Python
    string inside your formula, which may require some care with your quote
    marks. Some standard options include::

      my_fit_function("y ~ Q(\'weight.in.kg\')", ...)
      my_fit_function(\'y ~ Q("weight.in.kg")\', ...)
      my_fit_function("y ~ Q(\\"weight.in.kg\\")", ...)

    Note also that ``Q`` is an ordinary Python function, which means that you
    can use it in more complex expressions. For example, this is a legal
    formula::

      y ~ np.sqrt(Q("weight.in.kg"))
    '''
