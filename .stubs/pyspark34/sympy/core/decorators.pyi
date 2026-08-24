from .sympify import SympifyError as SympifyError, sympify as sympify
from _typeshed import Incomplete

def call_highest_priority(method_name):
    """A decorator for binary special methods to handle _op_priority.

    Explanation
    ===========

    Binary special methods in Expr and its subclasses use a special attribute
    '_op_priority' to determine whose special method will be called to
    handle the operation. In general, the object having the highest value of
    '_op_priority' will handle the operation. Expr and subclasses that define
    custom binary special methods (__mul__, etc.) should decorate those
    methods with this decorator to add the priority logic.

    The ``method_name`` argument is the name of the method of the other class
    that will be called.  Use this decorator in the following manner::

        # Call other.__rmul__ if other._op_priority > self._op_priority
        @call_highest_priority('__rmul__')
        def __mul__(self, other):
            ...

        # Call other.__mul__ if other._op_priority > self._op_priority
        @call_highest_priority('__mul__')
        def __rmul__(self, other):
        ...
    """
def sympify_method_args(cls):
    """Decorator for a class with methods that sympify arguments.

    Explanation
    ===========

    The sympify_method_args decorator is to be used with the sympify_return
    decorator for automatic sympification of method arguments. This is
    intended for the common idiom of writing a class like :

    Examples
    ========

    >>> from sympy import Basic, SympifyError, S
    >>> from sympy.core.sympify import _sympify

    >>> class MyTuple(Basic):
    ...     def __add__(self, other):
    ...         try:
    ...             other = _sympify(other)
    ...         except SympifyError:
    ...             return NotImplemented
    ...         if not isinstance(other, MyTuple):
    ...             return NotImplemented
    ...         return MyTuple(*(self.args + other.args))

    >>> MyTuple(S(1), S(2)) + MyTuple(S(3), S(4))
    MyTuple(1, 2, 3, 4)

    In the above it is important that we return NotImplemented when other is
    not sympifiable and also when the sympified result is not of the expected
    type. This allows the MyTuple class to be used cooperatively with other
    classes that overload __add__ and want to do something else in combination
    with instance of Tuple.

    Using this decorator the above can be written as

    >>> from sympy.core.decorators import sympify_method_args, sympify_return

    >>> @sympify_method_args
    ... class MyTuple(Basic):
    ...     @sympify_return([('other', 'MyTuple')], NotImplemented)
    ...     def __add__(self, other):
    ...          return MyTuple(*(self.args + other.args))

    >>> MyTuple(S(1), S(2)) + MyTuple(S(3), S(4))
    MyTuple(1, 2, 3, 4)

    The idea here is that the decorators take care of the boiler-plate code
    for making this happen in each method that potentially needs to accept
    unsympified arguments. Then the body of e.g. the __add__ method can be
    written without needing to worry about calling _sympify or checking the
    type of the resulting object.

    The parameters for sympify_return are a list of tuples of the form
    (parameter_name, expected_type) and the value to return (e.g.
    NotImplemented). The expected_type parameter can be a type e.g. Tuple or a
    string 'Tuple'. Using a string is useful for specifying a Type within its
    class body (as in the above example).

    Notes: Currently sympify_return only works for methods that take a single
    argument (not including self). Specifying an expected_type as a string
    only works for the class in which the method is defined.
    """
def sympify_return(*args):
    """Function/method decorator to sympify arguments automatically

    See the docstring of sympify_method_args for explanation.
    """

class _SympifyWrapper:
    """Internal class used by sympify_return and sympify_method_args"""
    func: Incomplete
    args: Incomplete
    def __init__(self, func, args) -> None: ...
    def make_wrapped(self, cls): ...
