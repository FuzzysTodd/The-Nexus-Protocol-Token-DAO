import typing
from tornado.util import unicode_type as unicode_type
from typing import Any, Callable, Dict, List

def xhtml_escape(value: str | bytes) -> str:
    '''Escapes a string so it is valid within HTML or XML.

    Escapes the characters ``<``, ``>``, ``"``, ``\'``, and ``&``.
    When used in attribute values the escaped strings must be enclosed
    in quotes.

    .. versionchanged:: 3.2

       Added the single quote to the list of escaped characters.
    '''
def xhtml_unescape(value: str | bytes) -> str:
    """Un-escapes an XML-escaped string."""
def json_encode(value: Any) -> str:
    """JSON-encodes the given Python object."""
def json_decode(value: str | bytes) -> Any:
    """Returns Python objects for the given JSON string.

    Supports both `str` and `bytes` inputs.
    """
def squeeze(value: str) -> str:
    """Replace all sequences of whitespace chars with a single space."""
def url_escape(value: str | bytes, plus: bool = True) -> str:
    '''Returns a URL-encoded version of the given value.

    If ``plus`` is true (the default), spaces will be represented
    as "+" instead of "%20".  This is appropriate for query strings
    but not for the path component of a URL.  Note that this default
    is the reverse of Python\'s urllib module.

    .. versionadded:: 3.1
        The ``plus`` argument
    '''
@typing.overload
def url_unescape(value: str | bytes, encoding: None, plus: bool = True) -> bytes: ...
@typing.overload
def url_unescape(value: str | bytes, encoding: str = 'utf-8', plus: bool = True) -> str: ...
def parse_qs_bytes(qs: str | bytes, keep_blank_values: bool = False, strict_parsing: bool = False) -> Dict[str, List[bytes]]:
    """Parses a query string like urlparse.parse_qs,
    but takes bytes and returns the values as byte strings.

    Keys still become type str (interpreted as latin1 in python3!)
    because it's too painful to keep them as byte strings in
    python3 and in practice they're nearly always ascii anyway.
    """
@typing.overload
def utf8(value: bytes) -> bytes: ...
@typing.overload
def utf8(value: str) -> bytes: ...
@typing.overload
def utf8(value: None) -> None: ...
@typing.overload
def to_unicode(value: str) -> str: ...
@typing.overload
def to_unicode(value: bytes) -> str: ...
@typing.overload
def to_unicode(value: None) -> None: ...
native_str = to_unicode
to_basestring = to_unicode

def recursive_unicode(obj: Any) -> Any:
    """Walks a simple data structure, converting byte strings to unicode.

    Supports lists, tuples, and dictionaries.
    """
def linkify(text: str | bytes, shorten: bool = False, extra_params: str | Callable[[str], str] = '', require_protocol: bool = False, permitted_protocols: List[str] = ['http', 'https']) -> str:
    '''Converts plain text into HTML with links.

    For example: ``linkify("Hello http://tornadoweb.org!")`` would return
    ``Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!``

    Parameters:

    * ``shorten``: Long urls will be shortened for display.

    * ``extra_params``: Extra text to include in the link tag, or a callable
      taking the link as an argument and returning the extra text
      e.g. ``linkify(text, extra_params=\'rel="nofollow" class="external"\')``,
      or::

          def extra_params_cb(url):
              if url.startswith("http://example.com"):
                  return \'class="internal"\'
              else:
                  return \'class="external" rel="nofollow"\'
          linkify(text, extra_params=extra_params_cb)

    * ``require_protocol``: Only linkify urls which include a protocol. If
      this is False, urls such as www.facebook.com will also be linkified.

    * ``permitted_protocols``: List (or set) of protocols which should be
      linkified, e.g. ``linkify(text, permitted_protocols=["http", "ftp",
      "mailto"])``. It is very unsafe to include protocols such as
      ``javascript``.
    '''
