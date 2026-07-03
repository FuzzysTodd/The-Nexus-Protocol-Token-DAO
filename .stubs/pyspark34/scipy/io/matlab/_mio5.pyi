from ._byteordercodes import native_code as native_code, swapped_code as swapped_code
from ._mio5_params import MDTYPES as MDTYPES, MatlabFunction as MatlabFunction, MatlabObject as MatlabObject, NP_TO_MTYPES as NP_TO_MTYPES, NP_TO_MXTYPES as NP_TO_MXTYPES, mat_struct as mat_struct, mclass_info as mclass_info, miCOMPRESSED as miCOMPRESSED, miINT8 as miINT8, miMATRIX as miMATRIX, miUINT32 as miUINT32, miUTF8 as miUTF8, mxCELL_CLASS as mxCELL_CLASS, mxCHAR_CLASS as mxCHAR_CLASS, mxDOUBLE_CLASS as mxDOUBLE_CLASS, mxOBJECT_CLASS as mxOBJECT_CLASS, mxSPARSE_CLASS as mxSPARSE_CLASS, mxSTRUCT_CLASS as mxSTRUCT_CLASS
from ._mio5_utils import VarReader5 as VarReader5
from ._miobase import MatFileReader as MatFileReader, MatReadError as MatReadError, MatReadWarning as MatReadWarning, MatWriteError as MatWriteError, arr_dtype_number as arr_dtype_number, arr_to_chars as arr_to_chars, docfiller as docfiller, matdims as matdims, read_dtype as read_dtype
from ._streams import ZlibInputStream as ZlibInputStream
from _typeshed import Incomplete

class MatFile5Reader(MatFileReader):
    """ Reader for Mat 5 mat files
    Adds the following attribute to base class

    uint16_codec - char codec to use for uint16 char arrays
        (defaults to system default codec)

    Uses variable reader that has the following stardard interface (see
    abstract class in ``miobase``::

       __init__(self, file_reader)
       read_header(self)
       array_from_header(self)

    and added interface::

       set_stream(self, stream)
       read_full_tag(self)

    """
    uint16_codec: Incomplete
    def __init__(self, mat_stream, byte_order: Incomplete | None = None, mat_dtype: bool = False, squeeze_me: bool = False, chars_as_strings: bool = True, matlab_compatible: bool = False, struct_as_record: bool = True, verify_compressed_data_integrity: bool = True, uint16_codec: Incomplete | None = None, simplify_cells: bool = False) -> None:
        """Initializer for matlab 5 file format reader

    %(matstream_arg)s
    %(load_args)s
    %(struct_arg)s
    uint16_codec : {None, string}
        Set codec to use for uint16 char arrays (e.g., 'utf-8').
        Use system default codec if None
        """
    def guess_byte_order(self):
        """ Guess byte order.
        Sets stream pointer to 0"""
    def read_file_header(self):
        """ Read in mat 5 file header """
    def initialize_read(self) -> None:
        """ Run when beginning read of variables

        Sets up readers from parameters in `self`
        """
    def read_var_header(self):
        """ Read header, return header, next position

        Header has to define at least .name and .is_global

        Parameters
        ----------
        None

        Returns
        -------
        header : object
           object that can be passed to self.read_var_array, and that
           has attributes .name and .is_global
        next_position : int
           position in stream of next variable
        """
    def read_var_array(self, header, process: bool = True):
        """ Read array, given `header`

        Parameters
        ----------
        header : header object
           object with fields defining variable header
        process : {True, False} bool, optional
           If True, apply recursive post-processing during loading of
           array.

        Returns
        -------
        arr : array
           array with post-processing applied or not according to
           `process`.
        """
    def get_variables(self, variable_names: Incomplete | None = None):
        """ get variables from stream as dictionary

        variable_names   - optional list of variable names to get

        If variable_names is None, then get all variables in file
        """
    def list_variables(self):
        """ list variables from stream """

def varmats_from_mat(file_obj):
    """ Pull variables out of mat 5 file as a sequence of mat file objects

    This can be useful with a difficult mat file, containing unreadable
    variables. This routine pulls the variables out in raw form and puts them,
    unread, back into a file stream for saving or reading. Another use is the
    pathological case where there is more than one variable of the same name in
    the file; this routine returns the duplicates, whereas the standard reader
    will overwrite duplicates in the returned dictionary.

    The file pointer in `file_obj` will be undefined. File pointers for the
    returned file-like objects are set at 0.

    Parameters
    ----------
    file_obj : file-like
        file object containing mat file

    Returns
    -------
    named_mats : list
        list contains tuples of (name, BytesIO) where BytesIO is a file-like
        object containing mat file contents as for a single variable. The
        BytesIO contains a string with the original header and a single var. If
        ``var_file_obj`` is an individual BytesIO instance, then save as a mat
        file with something like ``open('test.mat',
        'wb').write(var_file_obj.read())``

    Examples
    --------
    >>> import scipy.io

    BytesIO is from the ``io`` module in Python 3, and is ``cStringIO`` for
    Python < 3.

    >>> mat_fileobj = BytesIO()
    >>> scipy.io.savemat(mat_fileobj, {'b': np.arange(10), 'a': 'a string'})
    >>> varmats = varmats_from_mat(mat_fileobj)
    >>> sorted([name for name, str_obj in varmats])
    ['a', 'b']
    """

class EmptyStructMarker:
    """ Class to indicate presence of empty matlab struct on output """

def to_writeable(source):
    """ Convert input object ``source`` to something we can write

    Parameters
    ----------
    source : object

    Returns
    -------
    arr : None or ndarray or EmptyStructMarker
        If `source` cannot be converted to something we can write to a matfile,
        return None.  If `source` is equivalent to an empty dictionary, return
        ``EmptyStructMarker``.  Otherwise return `source` converted to an
        ndarray with contents for writing to matfile.
    """

NDT_FILE_HDR: Incomplete
NDT_TAG_FULL: Incomplete
NDT_TAG_SMALL: Incomplete
NDT_ARRAY_FLAGS: Incomplete

class VarWriter5:
    """ Generic matlab matrix writing class """
    mat_tag: Incomplete
    file_stream: Incomplete
    unicode_strings: Incomplete
    long_field_names: Incomplete
    oned_as: Incomplete
    def __init__(self, file_writer) -> None: ...
    def write_bytes(self, arr) -> None: ...
    def write_string(self, s) -> None: ...
    def write_element(self, arr, mdtype: Incomplete | None = None) -> None:
        """ write tag and data """
    def write_smalldata_element(self, arr, mdtype, byte_count) -> None: ...
    def write_regular_element(self, arr, mdtype, byte_count) -> None: ...
    def write_header(self, shape, mclass, is_complex: bool = False, is_logical: bool = False, nzmax: int = 0) -> None:
        """ Write header for given data options
        shape : sequence
           array shape
        mclass      - mat5 matrix class
        is_complex  - True if matrix is complex
        is_logical  - True if matrix is logical
        nzmax        - max non zero elements for sparse arrays

        We get the name and the global flag from the object, and reset
        them to defaults after we've used them
        """
    def update_matrix_tag(self, start_pos) -> None: ...
    def write_top(self, arr, name, is_global) -> None:
        """ Write variable at top level of mat file

        Parameters
        ----------
        arr : array_like
            array-like object to create writer for
        name : str, optional
            name as it will appear in matlab workspace
            default is empty string
        is_global : {False, True}, optional
            whether variable will be global on load into matlab
        """
    def write(self, arr) -> None:
        """ Write `arr` to stream at top and sub levels

        Parameters
        ----------
        arr : array_like
            array-like object to create writer for
        """
    def write_numeric(self, arr) -> None: ...
    def write_char(self, arr, codec: str = 'ascii') -> None:
        """ Write string array `arr` with given `codec`
        """
    def write_sparse(self, arr) -> None:
        """ Sparse matrices are 2D
        """
    def write_cells(self, arr) -> None: ...
    def write_empty_struct(self) -> None: ...
    def write_struct(self, arr) -> None: ...
    def write_object(self, arr) -> None:
        """Same as writing structs, except different mx class, and extra
        classname element after header
        """

class MatFile5Writer:
    """ Class for writing mat5 files """
    file_stream: Incomplete
    do_compression: Incomplete
    unicode_strings: Incomplete
    global_vars: Incomplete
    long_field_names: Incomplete
    oned_as: Incomplete
    def __init__(self, file_stream, do_compression: bool = False, unicode_strings: bool = False, global_vars: Incomplete | None = None, long_field_names: bool = False, oned_as: str = 'row') -> None:
        """ Initialize writer for matlab 5 format files

        Parameters
        ----------
        %(do_compression)s
        %(unicode_strings)s
        global_vars : None or sequence of strings, optional
            Names of variables to be marked as global for matlab
        %(long_fields)s
        %(oned_as)s
        """
    def write_file_header(self) -> None: ...
    def put_variables(self, mdict, write_header: Incomplete | None = None) -> None:
        """ Write variables in `mdict` to stream

        Parameters
        ----------
        mdict : mapping
           mapping with method ``items`` returns name, contents pairs where
           ``name`` which will appear in the matlab workspace in file load, and
           ``contents`` is something writeable to a matlab file, such as a NumPy
           array.
        write_header : {None, True, False}, optional
           If True, then write the matlab file header before writing the
           variables. If None (the default) then write the file header
           if we are at position 0 in the stream. By setting False
           here, and setting the stream position to the end of the file,
           you can append variables to a matlab file
        """
