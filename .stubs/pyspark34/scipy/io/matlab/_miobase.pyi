from _typeshed import Incomplete

__all__ = ['MatFileReader', 'MatReadError', 'MatReadWarning', 'MatVarReader', 'MatWriteError', 'arr_dtype_number', 'arr_to_chars', 'convert_dtypes', 'doc_dict', 'docfiller', 'get_matfile_version', 'matdims', 'read_dtype']

class MatReadError(Exception):
    """Exception indicating a read issue."""
class MatWriteError(Exception):
    """Exception indicating a write issue."""
class MatReadWarning(UserWarning):
    """Warning class for read issues."""

doc_dict: Incomplete
docfiller: Incomplete

def convert_dtypes(dtype_template, order_code):
    """ Convert dtypes in mapping to given order

    Parameters
    ----------
    dtype_template : mapping
       mapping with values returning numpy dtype from ``np.dtype(val)``
    order_code : str
       an order code suitable for using in ``dtype.newbyteorder()``

    Returns
    -------
    dtypes : mapping
       mapping where values have been replaced by
       ``np.dtype(val).newbyteorder(order_code)``

    """
def read_dtype(mat_stream, a_dtype):
    """
    Generic get of byte stream data of known type

    Parameters
    ----------
    mat_stream : file_like object
        MATLAB (tm) mat file stream
    a_dtype : dtype
        dtype of array to read. `a_dtype` is assumed to be correct
        endianness.

    Returns
    -------
    arr : ndarray
        Array of dtype `a_dtype` read from stream.

    """
get_matfile_version = matfile_version

def matdims(arr, oned_as: str = 'column'):
    '''
    Determine equivalent MATLAB dimensions for given array

    Parameters
    ----------
    arr : ndarray
        Input array
    oned_as : {\'column\', \'row\'}, optional
        Whether 1-D arrays are returned as MATLAB row or column matrices.
        Default is \'column\'.

    Returns
    -------
    dims : tuple
        Shape tuple, in the form MATLAB expects it.

    Notes
    -----
    We had to decide what shape a 1 dimensional array would be by
    default. ``np.atleast_2d`` thinks it is a row vector. The
    default for a vector in MATLAB (e.g., ``>> 1:12``) is a row vector.

    Versions of scipy up to and including 0.11 resulted (accidentally)
    in 1-D arrays being read as column vectors. For the moment, we
    maintain the same tradition here.

    Examples
    --------
    >>> matdims(np.array(1)) # NumPy scalar
    (1, 1)
    >>> matdims(np.array([1])) # 1-D array, 1 element
    (1, 1)
    >>> matdims(np.array([1,2])) # 1-D array, 2 elements
    (2, 1)
    >>> matdims(np.array([[2],[3]])) # 2-D array, column vector
    (2, 1)
    >>> matdims(np.array([[2,3]])) # 2-D array, row vector
    (1, 2)
    >>> matdims(np.array([[[2,3]]])) # 3-D array, rowish vector
    (1, 1, 2)
    >>> matdims(np.array([])) # empty 1-D array
    (0, 0)
    >>> matdims(np.array([[]])) # empty 2-D array
    (0, 0)
    >>> matdims(np.array([[[]]])) # empty 3-D array
    (0, 0, 0)

    Optional argument flips 1-D shape behavior.

    >>> matdims(np.array([1,2]), \'row\') # 1-D array, 2 elements
    (1, 2)

    The argument has to make sense though

    >>> matdims(np.array([1,2]), \'bizarre\')
    Traceback (most recent call last):
       ...
    ValueError: 1-D option "bizarre" is strange

    '''

class MatVarReader:
    """ Abstract class defining required interface for var readers"""
    def __init__(self, file_reader) -> None: ...
    def read_header(self) -> None:
        """ Returns header """
    def array_from_header(self, header) -> None:
        """ Reads array given header """

class MatFileReader:
    """ Base object for reading mat files

    To make this class functional, you will need to override the
    following methods:

    matrix_getter_factory   - gives object to fetch next matrix from stream
    guess_byte_order        - guesses file byte order from file
    """
    mat_stream: Incomplete
    dtypes: Incomplete
    byte_order: Incomplete
    struct_as_record: Incomplete
    squeeze_me: Incomplete
    chars_as_strings: Incomplete
    mat_dtype: Incomplete
    verify_compressed_data_integrity: Incomplete
    simplify_cells: Incomplete
    def __init__(self, mat_stream, byte_order: Incomplete | None = None, mat_dtype: bool = False, squeeze_me: bool = False, chars_as_strings: bool = True, matlab_compatible: bool = False, struct_as_record: bool = True, verify_compressed_data_integrity: bool = True, simplify_cells: bool = False) -> None:
        """
        Initializer for mat file reader

        mat_stream : file-like
            object with file API, open for reading
    %(load_args)s
        """
    def set_matlab_compatible(self) -> None:
        """ Sets options to return arrays as MATLAB loads them """
    def guess_byte_order(self):
        """ As we do not know what file type we have, assume native """
    def end_of_stream(self): ...

def arr_dtype_number(arr, num):
    """ Return dtype for given number of items per element"""
def arr_to_chars(arr):
    """ Convert string array to char array """
