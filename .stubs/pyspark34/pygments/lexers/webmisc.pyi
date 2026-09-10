from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['DuelLexer', 'SlimLexer', 'XQueryLexer', 'QmlLexer', 'CirruLexer']

class DuelLexer(RegexLexer):
    """
    Lexer for Duel Views Engine (formerly JBST) markup with JavaScript code blocks.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class XQueryLexer(ExtendedRegexLexer):
    """
    An XQuery lexer, parsing a stream and outputting the tokens needed to
    highlight xquery code.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    xquery_parse_state: Incomplete
    ncnamestartchar: str
    ncnamechar: Incomplete
    ncname: Incomplete
    pitarget_namestartchar: str
    pitarget_namechar: Incomplete
    pitarget: Incomplete
    prefixedname: Incomplete
    unprefixedname = ncname
    qname: Incomplete
    entityref: str
    charref: str
    stringdouble: Incomplete
    stringsingle: Incomplete
    elementcontentchar: str
    quotattrcontentchar: str
    aposattrcontentchar: str
    flags: Incomplete
    def punctuation_root_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def operator_root_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def popstate_tag_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def popstate_xmlcomment_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def popstate_kindtest_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def popstate_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_element_content_starttag_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_cdata_section_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_starttag_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_order_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_map_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_root_validate(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_root_validate_withmode(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_processing_instruction_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_element_content_processing_instruction_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_element_content_cdata_section_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_cdata_section_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_element_content_xmlcomment_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_xmlcomment_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_kindtest_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_kindtestforpi_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_kindtest_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_occurrenceindicator_kindtest_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_starttag_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_root_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_root_construct_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_root_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    def pushstate_operator_attribute_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class QmlLexer(RegexLexer):
    """
    For QML files.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class CirruLexer(RegexLexer):
    '''
    * using ``()`` for expressions, but restricted in a same line
    * using ``""`` for strings, with ``\\`` for escaping chars
    * using ``$`` as folding operator
    * using ``,`` as unfolding operator
    * using indentations for nested blocks

    .. versionadded:: 2.0
    '''
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class SlimLexer(ExtendedRegexLexer):
    """
    For Slim markup.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
