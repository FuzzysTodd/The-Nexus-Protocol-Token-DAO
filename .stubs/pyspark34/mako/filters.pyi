from _typeshed import Incomplete

html_escape: Incomplete
xml_escapes: Incomplete

def xml_escape(string): ...
def url_escape(string): ...
def trim(string): ...

class Decode:
    def __getattr__(self, key): ...

decode: Incomplete

class XMLEntityEscaper:
    codepoint2entity: Incomplete
    name2codepoint: Incomplete
    def __init__(self, codepoint2name, name2codepoint) -> None: ...
    def escape_entities(self, text):
        """Replace characters with their character entity references.

        Only characters corresponding to a named entity are replaced.
        """
    def escape(self, text):
        """Replace characters with their character references.

        Replace characters by their named entity references.
        Non-ASCII characters, if they do not have a named entity reference,
        are replaced by numerical character references.

        The return value is guaranteed to be ASCII.
        """
    def unescape(self, text):
        """Unescape character references.

        All character references (both entity references and numerical
        character references) are unescaped.
        """

html_entities_escape: Incomplete
html_entities_unescape: Incomplete

def htmlentityreplace_errors(ex):
    """An encoding error handler.

    This python codecs error handler replaces unencodable
    characters with HTML entities, or, if no HTML entity exists for
    the character, XML character references::

        >>> 'The cost was €12.'.encode('latin1', 'htmlentityreplace')
        'The cost was &euro;12.'
    """

DEFAULT_ESCAPES: Incomplete
