from _typeshed import Incomplete
from bs4.builder import HTMLTreeBuilder, TreeBuilder
from bs4.element import ProcessingInstruction, XMLProcessingInstruction
from collections.abc import Generator

__all__ = ['LXMLTreeBuilderForXML', 'LXMLTreeBuilder']

class LXMLTreeBuilderForXML(TreeBuilder):
    DEFAULT_PARSER_CLASS: Incomplete
    is_xml: bool
    processing_instruction_class = XMLProcessingInstruction
    NAME: str
    ALTERNATE_NAMES: Incomplete
    features: Incomplete
    CHUNK_SIZE: int
    DEFAULT_NSMAPS: Incomplete
    DEFAULT_NSMAPS_INVERTED: Incomplete
    def initialize_soup(self, soup) -> None:
        """Let the BeautifulSoup object know about the standard namespace
        mapping.

        :param soup: A `BeautifulSoup`.
        """
    def default_parser(self, encoding):
        """Find the default parser for the given encoding.

        :param encoding: A string.
        :return: Either a parser object or a class, which
          will be instantiated with default arguments.
        """
    def parser_for(self, encoding):
        """Instantiate an appropriate parser for the given encoding.

        :param encoding: A string.
        :return: A parser object such as an `etree.XMLParser`.
        """
    empty_element_tags: Incomplete
    soup: Incomplete
    nsmaps: Incomplete
    active_namespace_prefixes: Incomplete
    def __init__(self, parser: Incomplete | None = None, empty_element_tags: Incomplete | None = None, **kwargs) -> None: ...
    def prepare_markup(self, markup, user_specified_encoding: Incomplete | None = None, exclude_encodings: Incomplete | None = None, document_declared_encoding: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Run any preliminary steps necessary to make incoming markup
        acceptable to the parser.

        lxml really wants to get a bytestring and convert it to
        Unicode itself. So instead of using UnicodeDammit to convert
        the bytestring to Unicode using different encodings, this
        implementation uses EncodingDetector to iterate over the
        encodings, and tell lxml to try to parse the document as each
        one in turn.

        :param markup: Some markup -- hopefully a bytestring.
        :param user_specified_encoding: The user asked to try this encoding.
        :param document_declared_encoding: The markup itself claims to be
            in this encoding.
        :param exclude_encodings: The user asked _not_ to try any of
            these encodings.

        :yield: A series of 4-tuples:
         (markup, encoding, declared encoding,
          has undergone character replacement)

         Each 4-tuple represents a strategy for converting the
         document to Unicode and parsing it. Each strategy will be tried 
         in turn.
        """
    parser: Incomplete
    def feed(self, markup) -> None: ...
    def close(self) -> None: ...
    def start(self, name, attrs, nsmap={}) -> None: ...
    def end(self, name) -> None: ...
    def pi(self, target, data) -> None: ...
    def data(self, content) -> None: ...
    def doctype(self, name, pubid, system) -> None: ...
    def comment(self, content) -> None:
        """Handle comments as Comment objects."""
    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""

class LXMLTreeBuilder(HTMLTreeBuilder, LXMLTreeBuilderForXML):
    NAME = LXML
    ALTERNATE_NAMES: Incomplete
    features: Incomplete
    is_xml: bool
    processing_instruction_class = ProcessingInstruction
    def default_parser(self, encoding): ...
    parser: Incomplete
    def feed(self, markup) -> None: ...
    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
