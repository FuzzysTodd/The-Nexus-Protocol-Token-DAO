from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['is_valid_einsum_char', 'has_valid_einsum_chars_only', 'get_symbol', 'gen_unused_symbols', 'convert_to_valid_einsum_chars', 'alpha_canonicalize', 'find_output_str', 'find_output_shape', 'possibly_convert_to_numpy', 'parse_einsum_input']

def is_valid_einsum_char(x):
    '''Check if the character ``x`` is valid for numpy einsum.

    Examples
    --------
    >>> is_valid_einsum_char("a")
    True

    >>> is_valid_einsum_char("Ǵ")
    False
    '''
def has_valid_einsum_chars_only(einsum_str):
    '''Check if ``einsum_str`` contains only valid characters for numpy einsum.

    Examples
    --------
    >>> has_valid_einsum_chars_only("abAZ")
    True

    >>> has_valid_einsum_chars_only("Över")
    False
    '''
def get_symbol(i):
    """Get the symbol corresponding to int ``i`` - runs through the usual 52
    letters before resorting to unicode characters, starting at ``chr(192)``.

    Examples
    --------
    >>> get_symbol(2)
    'c'

    >>> get_symbol(200)
    'Ŕ'

    >>> get_symbol(20000)
    '京'
    """
def gen_unused_symbols(used, n) -> Generator[Incomplete, None, None]:
    '''Generate ``n`` symbols that are not already in ``used``.

    Examples
    --------
    >>> list(oe.parser.gen_unused_symbols("abd", 2))
    [\'c\', \'e\']
    '''
def convert_to_valid_einsum_chars(einsum_str):
    '''Convert the str ``einsum_str`` to contain only the alphabetic characters
    valid for numpy einsum. If there are too many symbols, let the backend
    throw an error.

    Examples
    --------
    >>> oe.parser.convert_to_valid_einsum_chars("Ĥěļļö")
    \'cbdda\'
    '''
def alpha_canonicalize(equation):
    '''Alpha convert an equation in an order-independent canonical way.

    Examples
    --------
    >>> oe.parser.alpha_canonicalize("dcba")
    \'abcd\'

    >>> oe.parser.alpha_canonicalize("Ĥěļļö")
    \'abccd\'
    '''
def find_output_str(subscripts):
    '''
    Find the output string for the inputs ``subscripts`` under canonical einstein summation rules. That is, repeated indices are summed over by default.

    Examples
    --------
    >>> oe.parser.find_output_str("ab,bc")
    \'ac\'

    >>> oe.parser.find_output_str("a,b")
    \'ab\'

    >>> oe.parser.find_output_str("a,a,b,b")
    \'\'
    '''
def find_output_shape(inputs, shapes, output):
    '''Find the output shape for given inputs, shapes and output string, taking
    into account broadcasting.

    Examples
    --------
    >>> oe.parser.find_output_shape(["ab", "bc"], [(2, 3), (3, 4)], "ac")
    (2, 4)

    # Broadcasting is accounted for
    >>> oe.parser.find_output_shape(["a", "a"], [(4, ), (1, )], "a")
    (4,)
    '''
def possibly_convert_to_numpy(x):
    """Convert things without a 'shape' to ndarrays, but leave everything else.

    Examples
    --------
    >>> oe.parser.possibly_convert_to_numpy(5)
    array(5)

    >>> oe.parser.possibly_convert_to_numpy([5, 3])
    array([5, 3])

    >>> oe.parser.possibly_convert_to_numpy(np.array([5, 3]))
    array([5, 3])

    # Any class with a shape is passed through
    >>> class Shape:
    ...     def __init__(self, shape):
    ...         self.shape = shape
    ...

    >>> myshape = Shape((5, 5))
    >>> oe.parser.possibly_convert_to_numpy(myshape)
    <__main__.Shape object at 0x10f850710>
    """
def parse_einsum_input(operands):
    """
    A reproduction of einsum c side einsum parsing in python.

    Returns
    -------
    input_strings : str
        Parsed input strings
    output_string : str
        Parsed output string
    operands : list of array_like
        The operands to use in the numpy contraction

    Examples
    --------
    The operand list is simplified to reduce printing:

    >>> a = np.random.rand(4, 4)
    >>> b = np.random.rand(4, 4, 4)
    >>> parse_einsum_input(('...a,...a->...', a, b))
    ('za,xza', 'xz', [a, b])

    >>> parse_einsum_input((a, [Ellipsis, 0], b, [Ellipsis, 0]))
    ('za,xza', 'xz', [a, b])
    """
