from _typeshed import Incomplete

def str_to_array(s):
    '''
    Simplistic converter of strings from repr to float NumPy arrays.

    If the repr representation has ellipsis in it, then this will fail.

    Parameters
    ----------
    s : str
        The repr version of a NumPy array.

    Examples
    --------
    >>> s = "array([ 0.3,  inf,  nan])"
    >>> a = str_to_array(s)

    '''
def float_doctest(sphinx_shell, args, input_lines, found, submitted) -> None:
    """
    Doctest which allow the submitted output to vary slightly from the input.

    Here is how it might appear in an rst file:

    .. code-block:: rst

       .. ipython::

          @doctest float
          In [1]: 0.1 + 0.2
          Out[1]: 0.3

    """

doctests: Incomplete
