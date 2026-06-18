from _typeshed import Incomplete
from sympy.core.numbers import I as I, NumberSymbol as NumberSymbol, oo as oo, zoo as zoo
from sympy.core.symbol import Symbol as Symbol
from sympy.external import import_module as import_module
from sympy.utilities.iterables import numbered_symbols as numbered_symbols

class vectorized_lambdify:
    """ Return a sufficiently smart, vectorized and lambdified function.

    Returns only reals.

    Explanation
    ===========

    This function uses experimental_lambdify to created a lambdified
    expression ready to be used with numpy. Many of the functions in SymPy
    are not implemented in numpy so in some cases we resort to Python cmath or
    even to evalf.

    The following translations are tried:
      only numpy complex
      - on errors raised by SymPy trying to work with ndarray:
          only Python cmath and then vectorize complex128

    When using Python cmath there is no need for evalf or float/complex
    because Python cmath calls those.

    This function never tries to mix numpy directly with evalf because numpy
    does not understand SymPy Float. If this is needed one can use the
    float_wrap_evalf/complex_wrap_evalf options of experimental_lambdify or
    better one can be explicit about the dtypes that numpy works with.
    Check numpy bug http://projects.scipy.org/numpy/ticket/1013 to know what
    types of errors to expect.
    """
    args: Incomplete
    expr: Incomplete
    np: Incomplete
    lambda_func_1: Incomplete
    vector_func_1: Incomplete
    lambda_func_2: Incomplete
    vector_func_2: Incomplete
    vector_func: Incomplete
    failure: bool
    def __init__(self, args, expr) -> None: ...
    def __call__(self, *args): ...

class lambdify:
    """Returns the lambdified function.

    Explanation
    ===========

    This function uses experimental_lambdify to create a lambdified
    expression. It uses cmath to lambdify the expression. If the function
    is not implemented in Python cmath, Python cmath calls evalf on those
    functions.
    """
    args: Incomplete
    expr: Incomplete
    lambda_func_1: Incomplete
    lambda_func_2: Incomplete
    lambda_func_3: Incomplete
    lambda_func: Incomplete
    failure: bool
    def __init__(self, args, expr) -> None: ...
    def __call__(self, args): ...

def experimental_lambdify(*args, **kwargs): ...

class Lambdifier:
    print_lambda: Incomplete
    use_evalf: Incomplete
    float_wrap_evalf: Incomplete
    complex_wrap_evalf: Incomplete
    use_np: Incomplete
    use_python_math: Incomplete
    use_python_cmath: Incomplete
    use_interval: Incomplete
    dict_str: Incomplete
    dict_fun: Incomplete
    eval_str: Incomplete
    lambda_func: Incomplete
    def __init__(self, args, expr, print_lambda: bool = False, use_evalf: bool = False, float_wrap_evalf: bool = False, complex_wrap_evalf: bool = False, use_np: bool = False, use_python_math: bool = False, use_python_cmath: bool = False, use_interval: bool = False) -> None: ...
    def __call__(self, *args, **kwargs): ...
    builtin_functions_different: Incomplete
    builtin_not_functions: Incomplete
    numpy_functions_same: Incomplete
    numpy_functions_different: Incomplete
    numpy_not_functions: Incomplete
    math_functions_same: Incomplete
    math_functions_different: Incomplete
    math_not_functions: Incomplete
    cmath_functions_same: Incomplete
    cmath_functions_different: Incomplete
    cmath_not_functions: Incomplete
    interval_not_functions: Incomplete
    interval_functions_same: Incomplete
    interval_functions_different: Incomplete
    def get_dict_str(self): ...
    def get_dict_fun(self): ...
    def str2tree(self, exprstr):
        """Converts an expression string to a tree.

        Explanation
        ===========

        Functions are represented by ('func_name(', tree_of_arguments).
        Other expressions are (head_string, mid_tree, tail_str).
        Expressions that do not contain functions are directly returned.

        Examples
        ========

        >>> from sympy.abc import x, y, z
        >>> from sympy import Integral, sin
        >>> from sympy.plotting.experimental_lambdify import Lambdifier
        >>> str2tree = Lambdifier([x], x).str2tree

        >>> str2tree(str(Integral(x, (x, 1, y))))
        ('', ('Integral(', 'x, (x, 1, y)'), ')')
        >>> str2tree(str(x+y))
        'x + y'
        >>> str2tree(str(x+y*sin(z)+1))
        ('x + y*', ('sin(', 'z'), ') + 1')
        >>> str2tree('sin(y*(y + 1.1) + (sin(y)))')
        ('', ('sin(', ('y*(y + 1.1) + (', ('sin(', 'y'), '))')), ')')
        """
    @classmethod
    def tree2str(cls, tree):
        """Converts a tree to string without translations.

        Examples
        ========

        >>> from sympy.abc import x, y, z
        >>> from sympy import sin
        >>> from sympy.plotting.experimental_lambdify import Lambdifier
        >>> str2tree = Lambdifier([x], x).str2tree
        >>> tree2str = Lambdifier([x], x).tree2str

        >>> tree2str(str2tree(str(x+y*sin(z)+1)))
        'x + y*sin(z) + 1'
        """
    def tree2str_translate(self, tree):
        """Converts a tree to string with translations.

        Explanation
        ===========

        Function names are translated by translate_func.
        Other strings are translated by translate_str.
        """
    def translate_str(self, estr):
        """Translate substrings of estr using in order the dictionaries in
        dict_tuple_str."""
    def translate_func(self, func_name, argtree):
        """Translate function names and the tree of arguments.

        Explanation
        ===========

        If the function name is not in the dictionaries of dict_tuple_fun then the
        function is surrounded by a float((...).evalf()).

        The use of float is necessary as np.<function>(sympy.Float(..)) raises an
        error."""
    @classmethod
    def sympy_expression_namespace(cls, expr):
        """Traverses the (func, args) tree of an expression and creates a SymPy
        namespace. All other modules are imported only as a module name. That way
        the namespace is not polluted and rests quite small. It probably causes much
        more variable lookups and so it takes more time, but there are no tests on
        that for the moment."""
    @staticmethod
    def sympy_atoms_namespace(expr):
        """For no real reason this function is separated from
        sympy_expression_namespace. It can be moved to it."""
