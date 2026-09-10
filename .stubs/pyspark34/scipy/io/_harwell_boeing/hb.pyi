from _typeshed import Incomplete

__all__ = ['MalformedHeader', 'hb_read', 'hb_write', 'HBInfo', 'HBFile', 'HBMatrixType']

class MalformedHeader(Exception): ...
class LineOverflow(Warning): ...

class HBInfo:
    @classmethod
    def from_data(cls, m, title: str = 'Default title', key: str = '0', mxtype: Incomplete | None = None, fmt: Incomplete | None = None):
        """Create a HBInfo instance from an existing sparse matrix.

        Parameters
        ----------
        m : sparse matrix
            the HBInfo instance will derive its parameters from m
        title : str
            Title to put in the HB header
        key : str
            Key
        mxtype : HBMatrixType
            type of the input matrix
        fmt : dict
            not implemented

        Returns
        -------
        hb_info : HBInfo instance
        """
    @classmethod
    def from_file(cls, fid):
        """Create a HBInfo instance from a file object containing a matrix in the
        HB format.

        Parameters
        ----------
        fid : file-like matrix
            File or file-like object containing a matrix in the HB format.

        Returns
        -------
        hb_info : HBInfo instance
        """
    title: Incomplete
    key: Incomplete
    total_nlines: Incomplete
    pointer_nlines: Incomplete
    indices_nlines: Incomplete
    values_nlines: Incomplete
    pointer_format: Incomplete
    indices_format: Incomplete
    values_format: Incomplete
    pointer_dtype: Incomplete
    indices_dtype: Incomplete
    values_dtype: Incomplete
    pointer_nbytes_full: Incomplete
    indices_nbytes_full: Incomplete
    values_nbytes_full: Incomplete
    nrows: Incomplete
    ncols: Incomplete
    nnon_zeros: Incomplete
    nelementals: Incomplete
    mxtype: Incomplete
    def __init__(self, title, key, total_nlines, pointer_nlines, indices_nlines, values_nlines, mxtype, nrows, ncols, nnon_zeros, pointer_format_str, indices_format_str, values_format_str, right_hand_sides_nlines: int = 0, nelementals: int = 0) -> None:
        """Do not use this directly, but the class ctrs (from_* functions)."""
    def dump(self):
        """Gives the header corresponding to this instance as a string."""

class HBMatrixType:
    """Class to hold the matrix type."""
    @classmethod
    def from_fortran(cls, fmt): ...
    value_type: Incomplete
    structure: Incomplete
    storage: Incomplete
    def __init__(self, value_type, structure, storage: str = 'assembled') -> None: ...
    @property
    def fortran_format(self): ...

class HBFile:
    def __init__(self, file, hb_info: Incomplete | None = None) -> None:
        """Create a HBFile instance.

        Parameters
        ----------
        file : file-object
            StringIO work as well
        hb_info : HBInfo, optional
            Should be given as an argument for writing, in which case the file
            should be writable.
        """
    @property
    def title(self): ...
    @property
    def key(self): ...
    @property
    def type(self): ...
    @property
    def structure(self): ...
    @property
    def storage(self): ...
    def read_matrix(self): ...
    def write_matrix(self, m): ...

def hb_read(path_or_open_file):
    '''Read HB-format file.

    Parameters
    ----------
    path_or_open_file : path-like or file-like
        If a file-like object, it is used as-is. Otherwise, it is opened
        before reading.

    Returns
    -------
    data : scipy.sparse.csc_matrix instance
        The data read from the HB file as a sparse matrix.

    Notes
    -----
    At the moment not the full Harwell-Boeing format is supported. Supported
    features are:

        - assembled, non-symmetric, real matrices
        - integer for pointer/indices
        - exponential format for float values, and int format

    Examples
    --------
    We can read and write a harwell-boeing format file:

    >>> from scipy.io import hb_read, hb_write
    >>> from scipy.sparse import csr_matrix, eye
    >>> data = csr_matrix(eye(3))  # create a sparse matrix
    >>> hb_write("data.hb", data)  # write a hb file
    >>> print(hb_read("data.hb"))  # read a hb file
      (0, 0)\t1.0
      (1, 1)\t1.0
      (2, 2)\t1.0

    '''
def hb_write(path_or_open_file, m, hb_info: Incomplete | None = None):
    '''Write HB-format file.

    Parameters
    ----------
    path_or_open_file : path-like or file-like
        If a file-like object, it is used as-is. Otherwise, it is opened
        before writing.
    m : sparse-matrix
        the sparse matrix to write
    hb_info : HBInfo
        contains the meta-data for write

    Returns
    -------
    None

    Notes
    -----
    At the moment not the full Harwell-Boeing format is supported. Supported
    features are:

        - assembled, non-symmetric, real matrices
        - integer for pointer/indices
        - exponential format for float values, and int format

    Examples
    --------
    We can read and write a harwell-boeing format file:

    >>> from scipy.io import hb_read, hb_write
    >>> from scipy.sparse import csr_matrix, eye
    >>> data = csr_matrix(eye(3))  # create a sparse matrix
    >>> hb_write("data.hb", data)  # write a hb file
    >>> print(hb_read("data.hb"))  # read a hb file
      (0, 0)\t1.0
      (1, 1)\t1.0
      (2, 2)\t1.0

    '''
