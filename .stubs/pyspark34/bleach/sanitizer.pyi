from _typeshed import Incomplete
from bleach import html5lib_shim as html5lib_shim, parse_shim as parse_shim
from collections.abc import Generator

ALLOWED_TAGS: Incomplete
ALLOWED_ATTRIBUTES: Incomplete
ALLOWED_PROTOCOLS: Incomplete
INVISIBLE_CHARACTERS: Incomplete
INVISIBLE_CHARACTERS_RE: Incomplete
INVISIBLE_REPLACEMENT_CHAR: str

class NoCssSanitizerWarning(UserWarning): ...

class Cleaner:
    """Cleaner for cleaning HTML fragments of malicious content

    This cleaner is a security-focused function whose sole purpose is to remove
    malicious content from a string such that it can be displayed as content in
    a web page.

    To use::

        from bleach.sanitizer import Cleaner

        cleaner = Cleaner()

        for text in all_the_yucky_things:
            sanitized = cleaner.clean(text)

    .. Note::

       This cleaner is not designed to use to transform content to be used in
       non-web-page contexts.

    .. Warning::

       This cleaner is not thread-safe--the html parser has internal state.
       Create a separate cleaner per thread!


    """
    tags: Incomplete
    attributes: Incomplete
    protocols: Incomplete
    strip: Incomplete
    strip_comments: Incomplete
    filters: Incomplete
    css_sanitizer: Incomplete
    parser: Incomplete
    walker: Incomplete
    serializer: Incomplete
    def __init__(self, tags=..., attributes=..., protocols=..., strip: bool = False, strip_comments: bool = True, filters: Incomplete | None = None, css_sanitizer: Incomplete | None = None) -> None:
        '''Initializes a Cleaner

        :arg set tags: set of allowed tags; defaults to
            ``bleach.sanitizer.ALLOWED_TAGS``

        :arg dict attributes: allowed attributes; can be a callable, list or dict;
            defaults to ``bleach.sanitizer.ALLOWED_ATTRIBUTES``

        :arg list protocols: allowed list of protocols for links; defaults
            to ``bleach.sanitizer.ALLOWED_PROTOCOLS``

        :arg bool strip: whether or not to strip disallowed elements

        :arg bool strip_comments: whether or not to strip HTML comments

        :arg list filters: list of html5lib Filter classes to pass streamed content through

            .. seealso:: http://html5lib.readthedocs.io/en/latest/movingparts.html#filters

            .. Warning::

               Using filters changes the output of ``bleach.Cleaner.clean``.
               Make sure the way the filters change the output are secure.

        :arg CSSSanitizer css_sanitizer: instance with a "sanitize_css" method for
            sanitizing style attribute values and style text; defaults to None

        '''
    def clean(self, text):
        """Cleans text and returns sanitized result as unicode

        :arg str text: text to be cleaned

        :returns: sanitized text as unicode

        :raises TypeError: if ``text`` is not a text type

        """

def attribute_filter_factory(attributes):
    """Generates attribute filter function for the given attributes value

    The attributes value can take one of several shapes. This returns a filter
    function appropriate to the attributes value. One nice thing about this is
    that there's less if/then shenanigans in the ``allow_token`` method.

    """

class BleachSanitizerFilter(html5lib_shim.SanitizerFilter):
    """html5lib Filter that sanitizes text

    This filter can be used anywhere html5lib filters can be used.

    """
    allowed_tags: Incomplete
    allowed_protocols: Incomplete
    attr_filter: Incomplete
    strip_disallowed_tags: Incomplete
    strip_html_comments: Incomplete
    attr_val_is_uri: Incomplete
    svg_attr_val_allows_ref: Incomplete
    css_sanitizer: Incomplete
    svg_allow_local_href: Incomplete
    def __init__(self, source, allowed_tags=..., attributes=..., allowed_protocols=..., attr_val_is_uri=..., svg_attr_val_allows_ref=..., svg_allow_local_href=..., strip_disallowed_tags: bool = False, strip_html_comments: bool = True, css_sanitizer: Incomplete | None = None) -> None:
        '''Creates a BleachSanitizerFilter instance

        :arg source: html5lib TreeWalker stream as an html5lib TreeWalker

        :arg set allowed_tags: set of allowed tags; defaults to
            ``bleach.sanitizer.ALLOWED_TAGS``

        :arg dict attributes: allowed attributes; can be a callable, list or dict;
            defaults to ``bleach.sanitizer.ALLOWED_ATTRIBUTES``

        :arg list allowed_protocols: allowed list of protocols for links; defaults
            to ``bleach.sanitizer.ALLOWED_PROTOCOLS``

        :arg attr_val_is_uri: set of attributes that have URI values

        :arg svg_attr_val_allows_ref: set of SVG attributes that can have
            references

        :arg svg_allow_local_href: set of SVG elements that can have local
            hrefs

        :arg bool strip_disallowed_tags: whether or not to strip disallowed
            tags

        :arg bool strip_html_comments: whether or not to strip HTML comments

        :arg CSSSanitizer css_sanitizer: instance with a "sanitize_css" method for
            sanitizing style attribute values and style text; defaults to None

        '''
    def sanitize_stream(self, token_iterator) -> Generator[Incomplete, Incomplete, None]: ...
    def merge_characters(self, token_iterator) -> Generator[Incomplete, None, None]:
        """Merge consecutive Characters tokens in a stream"""
    def __iter__(self): ...
    def sanitize_token(self, token):
        """Sanitize a token either by HTML-encoding or dropping.

        Unlike sanitizer.Filter, allowed_attributes can be a dict of {'tag':
        ['attribute', 'pairs'], 'tag': callable}.

        Here callable is a function with two arguments of attribute name and
        value. It should return true of false.

        Also gives the option to strip tags instead of encoding.

        :arg dict token: token to sanitize

        :returns: token or list of tokens

        """
    def sanitize_characters(self, token):
        """Handles Characters tokens

        Our overridden tokenizer doesn't do anything with entities. However,
        that means that the serializer will convert all ``&`` in Characters
        tokens to ``&amp;``.

        Since we don't want that, we extract entities here and convert them to
        Entity tokens so the serializer will let them be.

        :arg token: the Characters token to work on

        :returns: a list of tokens

        """
    def sanitize_uri_value(self, value, allowed_protocols):
        """Checks a uri value to see if it's allowed

        :arg value: the uri value to sanitize
        :arg allowed_protocols: list of allowed protocols

        :returns: allowed value or None

        """
    def allow_token(self, token):
        """Handles the case where we're allowing the tag"""
    def disallowed_token(self, token): ...
