from .element import Tag
from _typeshed import Incomplete

__all__ = ['BeautifulSoup']

class GuessedAtParserWarning(UserWarning):
    """The warning issued when BeautifulSoup has to guess what parser to
    use -- probably because no parser was specified in the constructor.
    """
class MarkupResemblesLocatorWarning(UserWarning):
    """The warning issued when BeautifulSoup is given 'markup' that
    actually looks like a resource locator -- a URL or a path to a file
    on disk.
    """

class BeautifulSoup(Tag):
    '''A data structure representing a parsed HTML or XML document.

    Most of the methods you\'ll call on a BeautifulSoup object are inherited from
    PageElement or Tag.

    Internally, this class defines the basic interface called by the
    tree builders when converting an HTML/XML document into a data
    structure. The interface abstracts away the differences between
    parsers. To write a new tree builder, you\'ll need to understand
    these methods as a whole.

    These methods will be called by the BeautifulSoup constructor:
      * reset()
      * feed(markup)

    The tree builder may call these methods from its feed() implementation:
      * handle_starttag(name, attrs) # See note about return value
      * handle_endtag(name)
      * handle_data(data) # Appends to the current data node
      * endData(containerClass) # Ends the current data node

    No matter how complicated the underlying parser is, you should be
    able to build a tree using \'start tag\' events, \'end tag\' events,
    \'data\' events, and "done with data" events.

    If you encounter an empty-element tag (aka a self-closing tag,
    like HTML\'s <br> tag), call handle_starttag and then
    handle_endtag.
    '''
    ROOT_TAG_NAME: str
    DEFAULT_BUILDER_FEATURES: Incomplete
    ASCII_SPACES: str
    NO_PARSER_SPECIFIED_WARNING: str
    element_classes: Incomplete
    builder: Incomplete
    is_xml: Incomplete
    known_xml: Incomplete
    parse_only: Incomplete
    markup: Incomplete
    def __init__(self, markup: str = '', features: Incomplete | None = None, builder: Incomplete | None = None, parse_only: Incomplete | None = None, from_encoding: Incomplete | None = None, exclude_encodings: Incomplete | None = None, element_classes: Incomplete | None = None, **kwargs) -> None:
        '''Constructor.

        :param markup: A string or a file-like object representing
         markup to be parsed.

        :param features: Desirable features of the parser to be
         used. This may be the name of a specific parser ("lxml",
         "lxml-xml", "html.parser", or "html5lib") or it may be the
         type of markup to be used ("html", "html5", "xml"). It\'s
         recommended that you name a specific parser, so that
         Beautiful Soup gives you the same results across platforms
         and virtual environments.

        :param builder: A TreeBuilder subclass to instantiate (or
         instance to use) instead of looking one up based on
         `features`. You only need to use this if you\'ve implemented a
         custom TreeBuilder.

        :param parse_only: A SoupStrainer. Only parts of the document
         matching the SoupStrainer will be considered. This is useful
         when parsing part of a document that would otherwise be too
         large to fit into memory.

        :param from_encoding: A string indicating the encoding of the
         document to be parsed. Pass this in if Beautiful Soup is
         guessing wrongly about the document\'s encoding.

        :param exclude_encodings: A list of strings indicating
         encodings known to be wrong. Pass this in if you don\'t know
         the document\'s encoding but you know Beautiful Soup\'s guess is
         wrong.

        :param element_classes: A dictionary mapping BeautifulSoup
         classes like Tag and NavigableString, to other classes you\'d
         like to be instantiated instead as the parse tree is
         built. This is useful for subclassing Tag or NavigableString
         to modify default behavior.

        :param kwargs: For backwards compatibility purposes, the
         constructor accepts certain keyword arguments used in
         Beautiful Soup 3. None of these arguments do anything in
         Beautiful Soup 4; they will result in a warning and then be
         ignored.
         
         Apart from this, any keyword arguments passed into the
         BeautifulSoup constructor are propagated to the TreeBuilder
         constructor. This makes it possible to configure a
         TreeBuilder by passing in arguments, not just by saying which
         one to use.
        '''
    hidden: int
    current_data: Incomplete
    currentTag: Incomplete
    tagStack: Incomplete
    open_tag_counter: Incomplete
    preserve_whitespace_tag_stack: Incomplete
    string_container_stack: Incomplete
    def reset(self) -> None:
        """Reset this object to a state as though it had never parsed any
        markup.
        """
    def new_tag(self, name, namespace: Incomplete | None = None, nsprefix: Incomplete | None = None, attrs={}, sourceline: Incomplete | None = None, sourcepos: Incomplete | None = None, **kwattrs):
        """Create a new Tag associated with this BeautifulSoup object.

        :param name: The name of the new Tag.
        :param namespace: The URI of the new Tag's XML namespace, if any.
        :param prefix: The prefix for the new Tag's XML namespace, if any.
        :param attrs: A dictionary of this Tag's attribute values; can
            be used instead of `kwattrs` for attributes like 'class'
            that are reserved words in Python.
        :param sourceline: The line number where this tag was
            (purportedly) found in its source document.
        :param sourcepos: The character position within `sourceline` where this
            tag was (purportedly) found.
        :param kwattrs: Keyword arguments for the new Tag's attribute values.

        """
    def string_container(self, base_class: Incomplete | None = None): ...
    def new_string(self, s, subclass: Incomplete | None = None):
        """Create a new NavigableString associated with this BeautifulSoup
        object.
        """
    def insert_before(self, *args) -> None:
        """This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
        it because there is nothing before or after it in the parse tree.
        """
    def insert_after(self, *args) -> None:
        """This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
        it because there is nothing before or after it in the parse tree.
        """
    def popTag(self):
        """Internal method called by _popToTag when a tag is closed."""
    def pushTag(self, tag) -> None:
        """Internal method called by handle_starttag when a tag is opened."""
    def endData(self, containerClass: Incomplete | None = None) -> None:
        """Method called by the TreeBuilder when the end of a data segment
        occurs.
        """
    def object_was_parsed(self, o, parent: Incomplete | None = None, most_recent_element: Incomplete | None = None) -> None:
        """Method called by the TreeBuilder to integrate an object into the parse tree."""
    def handle_starttag(self, name, namespace, nsprefix, attrs, sourceline: Incomplete | None = None, sourcepos: Incomplete | None = None, namespaces: Incomplete | None = None):
        """Called by the tree builder when a new tag is encountered.

        :param name: Name of the tag.
        :param nsprefix: Namespace prefix for the tag.
        :param attrs: A dictionary of attribute values.
        :param sourceline: The line number where this tag was found in its
            source document.
        :param sourcepos: The character position within `sourceline` where this
            tag was found.
        :param namespaces: A dictionary of all namespace prefix mappings 
            currently in scope in the document.

        If this method returns None, the tag was rejected by an active
        SoupStrainer. You should proceed as if the tag had not occurred
        in the document. For instance, if this was a self-closing tag,
        don't call handle_endtag.
        """
    def handle_endtag(self, name, nsprefix: Incomplete | None = None) -> None:
        """Called by the tree builder when an ending tag is encountered.

        :param name: Name of the tag.
        :param nsprefix: Namespace prefix for the tag.
        """
    def handle_data(self, data) -> None:
        """Called by the tree builder when a chunk of textual data is encountered."""
    def decode(self, pretty_print: bool = False, eventual_encoding=..., formatter: str = 'minimal', iterator: Incomplete | None = None):
        """Returns a string or Unicode representation of the parse tree
            as an HTML or XML document.

        :param pretty_print: If this is True, indentation will be used to
            make the document more readable.
        :param eventual_encoding: The encoding of the final document.
            If this is None, the document will be a Unicode string.
        """

class BeautifulStoneSoup(BeautifulSoup):
    """Deprecated interface to an XML parser."""
    def __init__(self, *args, **kwargs) -> None: ...

class StopParsing(Exception):
    """Exception raised by a TreeBuilder if it's unable to continue parsing."""
class FeatureNotFound(ValueError):
    """Exception raised by the BeautifulSoup constructor if no parser with the
    requested features is found.
    """
