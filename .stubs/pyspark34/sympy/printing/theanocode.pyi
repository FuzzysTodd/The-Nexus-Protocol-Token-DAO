from _typeshed import Incomplete
from sympy.external import import_module as import_module
from sympy.printing.printer import Printer as Printer
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence
from typing import Any

theano: Incomplete
ts: Incomplete
tt: Incomplete
mapping: Incomplete

class TheanoPrinter(Printer):
    """ Code printer which creates Theano symbolic expression graphs.

    Parameters
    ==========

    cache : dict
        Cache dictionary to use. If None (default) will use
        the global cache. To create a printer which does not depend on or alter
        global state pass an empty dictionary. Note: the dictionary is not
        copied on initialization of the printer and will be updated in-place,
        so using the same dict object when creating multiple printers or making
        multiple calls to :func:`.theano_code` or :func:`.theano_function` means
        the cache is shared between all these applications.

    Attributes
    ==========

    cache : dict
        A cache of Theano variables which have been created for SymPy
        symbol-like objects (e.g. :class:`sympy.core.symbol.Symbol` or
        :class:`sympy.matrices.expressions.MatrixSymbol`). This is used to
        ensure that all references to a given symbol in an expression (or
        multiple expressions) are printed as the same Theano variable, which is
        created only once. Symbols are differentiated only by name and type. The
        format of the cache's contents should be considered opaque to the user.
    """
    printmethod: str
    cache: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def emptyPrinter(self, expr): ...
    def doprint(self, expr, dtypes: Incomplete | None = None, broadcastables: Incomplete | None = None):
        """ Convert a SymPy expression to a Theano graph variable.

        The ``dtypes`` and ``broadcastables`` arguments are used to specify the
        data type, dimension, and broadcasting behavior of the Theano variables
        corresponding to the free symbols in ``expr``. Each is a mapping from
        SymPy symbols to the value of the corresponding argument to
        ``theano.tensor.Tensor``.

        See the corresponding `documentation page`__ for more information on
        broadcasting in Theano.

        .. __: http://deeplearning.net/software/theano/tutorial/broadcasting.html

        Parameters
        ==========

        expr : sympy.core.expr.Expr
            SymPy expression to print.

        dtypes : dict
            Mapping from SymPy symbols to Theano datatypes to use when creating
            new Theano variables for those symbols. Corresponds to the ``dtype``
            argument to ``theano.tensor.Tensor``. Defaults to ``'floatX'``
            for symbols not included in the mapping.

        broadcastables : dict
            Mapping from SymPy symbols to the value of the ``broadcastable``
            argument to ``theano.tensor.Tensor`` to use when creating Theano
            variables for those symbols. Defaults to the empty tuple for symbols
            not included in the mapping (resulting in a scalar).

        Returns
        =======

        theano.gof.graph.Variable
            A variable corresponding to the expression's value in a Theano
            symbolic expression graph.

        """

global_cache: dict[Any, Any]

def theano_code(expr, cache: Incomplete | None = None, **kwargs):
    """
    Convert a SymPy expression into a Theano graph variable.

    .. deprecated:: 1.8

      ``sympy.printing.theanocode`` is deprecated. Theano has been renamed to
      Aesara. Use ``sympy.printing.aesaracode`` instead. See
      :ref:`theanocode-deprecated` for more information.

    Parameters
    ==========

    expr : sympy.core.expr.Expr
        SymPy expression object to convert.

    cache : dict
        Cached Theano variables (see :class:`TheanoPrinter.cache
        <TheanoPrinter>`). Defaults to the module-level global cache.

    dtypes : dict
        Passed to :meth:`.TheanoPrinter.doprint`.

    broadcastables : dict
        Passed to :meth:`.TheanoPrinter.doprint`.

    Returns
    =======

    theano.gof.graph.Variable
        A variable corresponding to the expression's value in a Theano symbolic
        expression graph.

    """
def dim_handling(inputs, dim: Incomplete | None = None, dims: Incomplete | None = None, broadcastables: Incomplete | None = None):
    '''
    Get value of ``broadcastables`` argument to :func:`.theano_code` from
    keyword arguments to :func:`.theano_function`.

    Included for backwards compatibility.

    Parameters
    ==========

    inputs
        Sequence of input symbols.

    dim : int
        Common number of dimensions for all inputs. Overrides other arguments
        if given.

    dims : dict
        Mapping from input symbols to number of dimensions. Overrides
        ``broadcastables`` argument if given.

    broadcastables : dict
        Explicit value of ``broadcastables`` argument to
        :meth:`.TheanoPrinter.doprint`. If not None function will return this value unchanged.

    Returns
    =======
    dict
        Dictionary mapping elements of ``inputs`` to their "broadcastable"
        values (tuple of ``bool``\\ s).
    '''
def theano_function(inputs, outputs, scalar: bool = False, *, dim: Incomplete | None = None, dims: Incomplete | None = None, broadcastables: Incomplete | None = None, **kwargs):
    """
    Create a Theano function from SymPy expressions.

    .. deprecated:: 1.8

      ``sympy.printing.theanocode`` is deprecated. Theano has been renamed to
      Aesara. Use ``sympy.printing.aesaracode`` instead. See
      :ref:`theanocode-deprecated` for more information.

    The inputs and outputs are converted to Theano variables using
    :func:`.theano_code` and then passed to ``theano.function``.

    Parameters
    ==========

    inputs
        Sequence of symbols which constitute the inputs of the function.

    outputs
        Sequence of expressions which constitute the outputs(s) of the
        function. The free symbols of each expression must be a subset of
        ``inputs``.

    scalar : bool
        Convert 0-dimensional arrays in output to scalars. This will return a
        Python wrapper function around the Theano function object.

    cache : dict
        Cached Theano variables (see :class:`TheanoPrinter.cache
        <TheanoPrinter>`). Defaults to the module-level global cache.

    dtypes : dict
        Passed to :meth:`.TheanoPrinter.doprint`.

    broadcastables : dict
        Passed to :meth:`.TheanoPrinter.doprint`.

    dims : dict
        Alternative to ``broadcastables`` argument. Mapping from elements of
        ``inputs`` to integers indicating the dimension of their associated
        arrays/tensors. Overrides ``broadcastables`` argument if given.

    dim : int
        Another alternative to the ``broadcastables`` argument. Common number of
        dimensions to use for all arrays/tensors.
        ``theano_function([x, y], [...], dim=2)`` is equivalent to using
        ``broadcastables={x: (False, False), y: (False, False)}``.

    Returns
    =======
    callable
        A callable object which takes values of ``inputs`` as positional
        arguments and returns an output array for each of the expressions
        in ``outputs``. If ``outputs`` is a single expression the function will
        return a Numpy array, if it is a list of multiple expressions the
        function will return a list of arrays. See description of the ``squeeze``
        argument above for the behavior when a single output is passed in a list.
        The returned object will either be an instance of
        ``theano.compile.function_module.Function`` or a Python wrapper
        function around one. In both cases, the returned value will have a
        ``theano_function`` attribute which points to the return value of
        ``theano.function``.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.printing.theanocode import theano_function

    A simple function with one input and one output:

    >>> f1 = theano_function([x], [x**2 - 1], scalar=True)
    >>> f1(3)
    8.0

    A function with multiple inputs and one output:

    >>> f2 = theano_function([x, y, z], [(x**z + y**z)**(1/z)], scalar=True)
    >>> f2(3, 4, 2)
    5.0

    A function with multiple inputs and multiple outputs:

    >>> f3 = theano_function([x, y], [x**2 + y**2, x**2 - y**2], scalar=True)
    >>> f3(2, 3)
    [13.0, -5.0]

    See also
    ========

    dim_handling

    """
