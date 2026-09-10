from _typeshed import Incomplete
from collections.abc import Generator
from typing import Iterator, List, Tuple
from typing_extensions import TypedDict

__author_email__: str
__version__: str
ArffDenseDataType = Iterator[List]
ArffSparseDataType = Tuple[List, ...]

class ArffContainerType(TypedDict):
    description: str
    relation: str
    attributes: List
    data: ArffDenseDataType | ArffSparseDataType

DENSE: int
COO: int
LOD: int
DENSE_GEN: int
LOD_GEN: int

class ArffException(Exception):
    message: str | None
    line: int
    def __init__(self) -> None: ...

class BadRelationFormat(ArffException):
    """Error raised when the relation declaration is in an invalid format."""
    message: str

class BadAttributeFormat(ArffException):
    """Error raised when some attribute declaration is in an invalid format."""
    message: str

class BadDataFormat(ArffException):
    """Error raised when some data instance is in an invalid format."""
    message: Incomplete
    def __init__(self, value) -> None: ...

class BadAttributeType(ArffException):
    """Error raised when some invalid type is provided into the attribute
    declaration."""
    message: str

class BadAttributeName(ArffException):
    """Error raised when an attribute name is provided twice the attribute
    declaration."""
    message: Incomplete
    def __init__(self, value, value2) -> None: ...

class BadNominalValue(ArffException):
    """Error raised when a value in used in some data instance but is not
    declared into it respective attribute declaration."""
    message: Incomplete
    def __init__(self, value) -> None: ...

class BadNominalFormatting(ArffException):
    """Error raised when a nominal value with space is not properly quoted."""
    message: Incomplete
    def __init__(self, value) -> None: ...

class BadNumericalValue(ArffException):
    """Error raised when and invalid numerical value is used in some data
    instance."""
    message: str

class BadStringValue(ArffException):
    """Error raise when a string contains space but is not quoted."""
    message: str

class BadLayout(ArffException):
    """Error raised when the layout of the ARFF file has something wrong."""
    message: str
    def __init__(self, msg: str = '') -> None: ...

class BadObject(ArffException):
    """Error raised when the object representing the ARFF file has something
    wrong."""
    msg: Incomplete
    def __init__(self, msg: str = 'Invalid object.') -> None: ...

def encode_string(s): ...

class EncodedNominalConversor:
    values: Incomplete
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class NominalConversor:
    values: Incomplete
    zero_value: Incomplete
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class DenseGeneratorData:
    """Internal helper class to allow for different matrix types without
    making the code a huge collection of if statements."""
    def decode_rows(self, stream, conversors) -> Generator[Incomplete, None, None]: ...
    def encode_data(self, data, attributes) -> Generator[Incomplete, None, None]:
        """(INTERNAL) Encodes a line of data.

        Data instances follow the csv format, i.e, attribute values are
        delimited by commas. After converted from csv.

        :param data: a list of values.
        :param attributes: a list of attributes. Used to check if data is valid.
        :return: a string with the encoded data line.
        """

class _DataListMixin:
    """Mixin to return a list from decode_rows instead of a generator"""
    def decode_rows(self, stream, conversors): ...

class Data(_DataListMixin, DenseGeneratorData): ...

class COOData:
    def decode_rows(self, stream, conversors): ...
    def encode_data(self, data, attributes) -> Generator[Incomplete, None, None]: ...

class LODGeneratorData:
    def decode_rows(self, stream, conversors) -> Generator[Incomplete, None, None]: ...
    def encode_data(self, data, attributes) -> Generator[Incomplete, None, None]: ...

class LODData(_DataListMixin, LODGeneratorData): ...

class ArffDecoder:
    """An ARFF decoder."""
    def __init__(self) -> None:
        """Constructor."""
    def decode(self, s, encode_nominal: bool = False, return_type=...):
        """Returns the Python representation of a given ARFF file.

        When a file object is passed as an argument, this method reads lines
        iteratively, avoiding to load unnecessary information to the memory.

        :param s: a string or file object with the ARFF file.
        :param encode_nominal: boolean, if True perform a label encoding
            while reading the .arff file.
        :param return_type: determines the data structure used to store the
            dataset. Can be one of `arff.DENSE`, `arff.COO`, `arff.LOD`,
            `arff.DENSE_GEN` or `arff.LOD_GEN`.
            Consult the sections on `working with sparse data`_ and `loading
            progressively`_.
        """

class ArffEncoder:
    """An ARFF encoder."""
    def encode(self, obj):
        """Encodes a given object to an ARFF file.

        :param obj: the object containing the ARFF information.
        :return: the ARFF file as an string.
        """
    def iter_encode(self, obj) -> Generator[Incomplete, Incomplete, None]:
        """The iterative version of `arff.ArffEncoder.encode`.

        This encodes iteratively a given object and return, one-by-one, the
        lines of the ARFF file.

        :param obj: the object containing the ARFF information.
        :return: (yields) the ARFF file as strings.
        """

def load(fp, encode_nominal: bool = False, return_type=...):
    """Load a file-like object containing the ARFF document and convert it into
    a Python object.

    :param fp: a file-like object.
    :param encode_nominal: boolean, if True perform a label encoding
        while reading the .arff file.
    :param return_type: determines the data structure used to store the
        dataset. Can be one of `arff.DENSE`, `arff.COO`, `arff.LOD`,
        `arff.DENSE_GEN` or `arff.LOD_GEN`.
        Consult the sections on `working with sparse data`_ and `loading
        progressively`_.
    :return: a dictionary.
     """
def loads(s, encode_nominal: bool = False, return_type=...):
    """Convert a string instance containing the ARFF document into a Python
    object.

    :param s: a string object.
    :param encode_nominal: boolean, if True perform a label encoding
        while reading the .arff file.
    :param return_type: determines the data structure used to store the
        dataset. Can be one of `arff.DENSE`, `arff.COO`, `arff.LOD`,
        `arff.DENSE_GEN` or `arff.LOD_GEN`.
        Consult the sections on `working with sparse data`_ and `loading
        progressively`_.
    :return: a dictionary.
    """
def dump(obj, fp):
    """Serialize an object representing the ARFF document to a given file-like
    object.

    :param obj: a dictionary.
    :param fp: a file-like object.
    """
def dumps(obj):
    """Serialize an object representing the ARFF document, returning a string.

    :param obj: a dictionary.
    :return: a string with the ARFF document.
    """
