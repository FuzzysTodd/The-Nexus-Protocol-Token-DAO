from _typeshed import Incomplete
from pandas import DataFrame as DataFrame
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.dtypes.missing import isna as isna
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import get_handle as get_handle
from pandas.io.xml import get_data_from_filepath as get_data_from_filepath, preprocess_data as preprocess_data
from pandas.util._decorators import doc as doc
from typing import Any

class BaseXMLFormatter:
    """
    Subclass for formatting data in XML.

    Parameters
    ----------
    path_or_buffer : str or file-like
        This can be either a string of raw XML, a valid URL,
        file or file-like object.

    index : bool
        Whether to include index in xml document.

    row_name : str
        Name for root of xml document. Default is 'data'.

    root_name : str
        Name for row elements of xml document. Default is 'row'.

    na_rep : str
        Missing data representation.

    attrs_cols : list
        List of columns to write as attributes in row element.

    elem_cols : list
        List of columns to write as children in row element.

    namespaces : dict
        The namespaces to define in XML document as dicts with key
        being namespace and value the URI.

    prefix : str
        The prefix for each element in XML document including root.

    encoding : str
        Encoding of xml object or document.

    xml_declaration : bool
        Whether to include xml declaration at top line item in xml.

    pretty_print : bool
        Whether to write xml document with line breaks and indentation.

    stylesheet : str or file-like
        A URL, file, file-like object, or a raw string containing XSLT.

    {compression_options}

        .. versionchanged:: 1.4.0 Zstandard support.

    {storage_options}

    See also
    --------
    pandas.io.formats.xml.EtreeXMLFormatter
    pandas.io.formats.xml.LxmlXMLFormatter

    """
    frame: Incomplete
    path_or_buffer: Incomplete
    index: Incomplete
    root_name: Incomplete
    row_name: Incomplete
    na_rep: Incomplete
    attr_cols: Incomplete
    elem_cols: Incomplete
    namespaces: Incomplete
    prefix: Incomplete
    encoding: Incomplete
    xml_declaration: Incomplete
    pretty_print: Incomplete
    stylesheet: Incomplete
    compression: Incomplete
    storage_options: Incomplete
    orig_cols: Incomplete
    frame_dicts: Incomplete
    prefix_uri: Incomplete
    def __init__(self, frame: DataFrame, path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None, index: bool = True, root_name: str | None = 'data', row_name: str | None = 'row', na_rep: str | None = None, attr_cols: list[str] | None = None, elem_cols: list[str] | None = None, namespaces: dict[str | None, str] | None = None, prefix: str | None = None, encoding: str = 'utf-8', xml_declaration: bool | None = True, pretty_print: bool | None = True, stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions = None) -> None: ...
    def build_tree(self) -> bytes:
        """
        Build tree from  data.

        This method initializes the root and builds attributes and elements
        with optional namespaces.
        """
    def validate_columns(self) -> None:
        """
        Validate elems_cols and attrs_cols.

        This method will check if columns is list-like.

        Raises
        ------
        ValueError
            * If value is not a list and less then length of nodes.
        """
    def validate_encoding(self) -> None:
        """
        Validate encoding.

        This method will check if encoding is among listed under codecs.

        Raises
        ------
        LookupError
            * If encoding is not available in codecs.
        """
    def process_dataframe(self) -> dict[int | str, dict[str, Any]]:
        """
        Adjust Data Frame to fit xml output.

        This method will adjust underlying data frame for xml output,
        including optionally replacing missing values and including indexes.
        """
    def handle_indexes(self) -> None:
        """
        Handle indexes.

        This method will add indexes into attr_cols or elem_cols.
        """
    def get_prefix_uri(self) -> str:
        """
        Get uri of namespace prefix.

        This method retrieves corresponding URI to prefix in namespaces.

        Raises
        ------
        KeyError
            *If prefix is not included in namespace dict.
        """
    def other_namespaces(self) -> dict:
        """
        Define other namespaces.

        This method will build dictionary of namespaces attributes
        for root element, conditionally with optional namespaces and
        prefix.
        """
    def build_attribs(self, d: dict[str, Any], elem_row: Any) -> Any:
        """
        Create attributes of row.

        This method adds attributes using attr_cols to row element and
        works with tuples for multindex or hierarchical columns.
        """
    def build_elems(self, d: dict[str, Any], elem_row: Any) -> None:
        """
        Create child elements of row.

        This method adds child elements using elem_cols to row element and
        works with tuples for multindex or hierarchical columns.
        """
    def write_output(self) -> str | None: ...

class EtreeXMLFormatter(BaseXMLFormatter):
    """
    Class for formatting data in xml using Python standard library
    modules: `xml.etree.ElementTree` and `xml.dom.minidom`.
    """
    root: Incomplete
    elem_cols: Incomplete
    out_xml: Incomplete
    def build_tree(self) -> bytes: ...
    def get_prefix_uri(self) -> str: ...
    def build_elems(self, d: dict[str, Any], elem_row: Any) -> None: ...
    def prettify_tree(self) -> bytes:
        """
        Output tree for pretty print format.

        This method will pretty print xml with line breaks and indentation.
        """
    def add_declaration(self) -> bytes:
        """
        Add xml declaration.

        This method will add xml declaration of working tree. Currently,
        xml_declaration is supported in etree starting in Python 3.8.
        """
    def remove_declaration(self) -> bytes:
        """
        Remove xml declaration.

        This method will remove xml declaration of working tree. Currently,
        pretty_print is not supported in etree.
        """

class LxmlXMLFormatter(BaseXMLFormatter):
    """
    Class for formatting data in xml using Python standard library
    modules: `xml.etree.ElementTree` and `xml.dom.minidom`.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    root: Incomplete
    elem_cols: Incomplete
    out_xml: Incomplete
    def build_tree(self) -> bytes:
        """
        Build tree from  data.

        This method initializes the root and builds attributes and elements
        with optional namespaces.
        """
    def convert_empty_str_key(self) -> None:
        """
        Replace zero-length string in `namespaces`.

        This method will replace '' with None to align to `lxml`
        requirement that empty string prefixes are not allowed.
        """
    def get_prefix_uri(self) -> str: ...
    def build_elems(self, d: dict[str, Any], elem_row: Any) -> None: ...
    def transform_doc(self) -> bytes:
        """
        Parse stylesheet from file or buffer and run it.

        This method will parse stylesheet object into tree for parsing
        conditionally by its specific object type, then transforms
        original tree with XSLT script.
        """
