from _typeshed import Incomplete
from bleach._vendor.html5lib import HTMLParser as HTMLParser, constants as constants, getTreeWalker as getTreeWalker
from bleach._vendor.html5lib._inputstream import HTMLInputStream as HTMLInputStream
from bleach._vendor.html5lib._tokenizer import HTMLTokenizer as HTMLTokenizer, attributeMap as attributeMap
from bleach._vendor.html5lib._trie import Trie as Trie
from bleach._vendor.html5lib.constants import namespaces as namespaces, prefixes as prefixes
from bleach._vendor.html5lib.filters.base import Filter as Filter
from bleach._vendor.html5lib.filters.sanitizer import allowed_css_properties as allowed_css_properties, allowed_protocols as allowed_protocols, allowed_svg_properties as allowed_svg_properties, attr_val_is_uri as attr_val_is_uri, svg_allow_local_href as svg_allow_local_href, svg_attr_val_allows_ref as svg_attr_val_allows_ref
from bleach._vendor.html5lib.serializer import HTMLSerializer as HTMLSerializer, escape as escape
from collections.abc import Generator

ENTITIES: Incomplete
ENTITIES_TRIE: Incomplete
TAG_TOKEN_TYPES: Incomplete
TAG_TOKEN_TYPE_START: Incomplete
TAG_TOKEN_TYPE_END: Incomplete
TAG_TOKEN_TYPE_CHARACTERS: Incomplete
TAG_TOKEN_TYPE_PARSEERROR: Incomplete
HTML_TAGS: Incomplete
HTML_TAGS_BLOCK_LEVEL: Incomplete

class InputStreamWithMemory:
    """Wraps an HTMLInputStream to remember characters since last <

    This wraps existing HTMLInputStream classes to keep track of the stream
    since the last < which marked an open tag state.

    """
    reset: Incomplete
    position: Incomplete
    def __init__(self, inner_stream) -> None: ...
    @property
    def errors(self): ...
    @property
    def charEncoding(self): ...
    @property
    def changeEncoding(self): ...
    def char(self): ...
    def charsUntil(self, characters, opposite: bool = False): ...
    def unget(self, char): ...
    def get_tag(self):
        '''Returns the stream history since last \'<\'

        Since the buffer starts at the last \'<\' as as seen by tagOpenState(),
        we know that everything from that point to when this method is called
        is the "tag" that is being tokenized.

        '''
    def start_tag(self) -> None:
        """Resets stream history to just '<'

        This gets called by tagOpenState() which marks a '<' that denotes an
        open tag. Any time we see that, we reset the buffer.

        """

class BleachHTMLTokenizer(HTMLTokenizer):
    """Tokenizer that doesn't consume character entities"""
    consume_entities: Incomplete
    stream: Incomplete
    emitted_last_token: Incomplete
    def __init__(self, consume_entities: bool = False, **kwargs) -> None: ...
    def __iter__(self): ...
    def consumeEntity(self, allowedChar: Incomplete | None = None, fromAttribute: bool = False): ...
    def tagOpenState(self): ...
    currentToken: Incomplete
    state: Incomplete
    def emitCurrentToken(self) -> None: ...

class BleachHTMLParser(HTMLParser):
    """Parser that uses BleachHTMLTokenizer"""
    tags: Incomplete
    strip: Incomplete
    consume_entities: Incomplete
    def __init__(self, tags, strip, consume_entities, **kwargs) -> None:
        """
        :arg tags: set of allowed tags--everything else is either stripped or
            escaped; if None, then this doesn't look at tags at all
        :arg strip: whether to strip disallowed tags (True) or escape them (False);
            if tags=None, then this doesn't have any effect
        :arg consume_entities: whether to consume entities (default behavior) or
            leave them as is when tokenizing (BleachHTMLTokenizer-added behavior)

        """

def convert_entity(value):
    """Convert an entity (minus the & and ; part) into what it represents

    This handles numeric, hex, and text entities.

    :arg value: the string (minus the ``&`` and ``;`` part) to convert

    :returns: unicode character or None if it's an ambiguous ampersand that
        doesn't match a character entity

    """
def convert_entities(text):
    """Converts all found entities in the text

    :arg text: the text to convert entities in

    :returns: unicode text with converted entities

    """
def match_entity(stream):
    '''Returns first entity in stream or None if no entity exists

    Note: For Bleach purposes, entities must start with a "&" and end with a
    ";". This ignores ambiguous character entities that have no ";" at the end.

    :arg stream: the character stream

    :returns: the entity string without "&" or ";" if it\'s a valid character
        entity; ``None`` otherwise

    '''

AMP_SPLIT_RE: Incomplete

def next_possible_entity(text) -> Generator[Incomplete, None, None]:
    '''Takes a text and generates a list of possible entities

    :arg text: the text to look at

    :returns: generator where each part (except the first) starts with an
        "&"

    '''

class BleachHTMLSerializer(HTMLSerializer):
    """HTMLSerializer that undoes & -> &amp; in attributes and sets
    escape_rcdata to True
    """
    escape_rcdata: bool
    def escape_base_amp(self, stoken) -> Generator[Incomplete, None, None]:
        """Escapes just bare & in HTML attribute values"""
    def serialize(self, treewalker, encoding: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]:
        """Wrap HTMLSerializer.serialize and conver & to &amp; in attribute values

        Note that this converts & to &amp; in attribute values where the & isn't
        already part of an unambiguous character entity.

        """
