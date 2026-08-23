from .datastructures import iter_multi_items as iter_multi_items

def uri_to_iri(uri: str) -> str:
    '''Convert a URI to an IRI. All valid UTF-8 characters are unquoted,
    leaving all reserved and invalid characters quoted. If the URL has
    a domain, it is decoded from Punycode.

    >>> uri_to_iri("http://xn--n3h.net/p%C3%A5th?q=%C3%A8ry%DF")
    \'http://\\u2603.net/p\\xe5th?q=\\xe8ry%DF\'

    :param uri: The URI to convert.

    .. versionchanged:: 3.0
        Passing a tuple or bytes, and the ``charset`` and ``errors`` parameters,
        are removed.

    .. versionchanged:: 2.3
        Which characters remain quoted is specific to each part of the URL.

    .. versionchanged:: 0.15
        All reserved and invalid characters remain quoted. Previously,
        only some reserved characters were preserved, and invalid bytes
        were replaced instead of left quoted.

    .. versionadded:: 0.6
    '''
def iri_to_uri(iri: str) -> str:
    """Convert an IRI to a URI. All non-ASCII and unsafe characters are
    quoted. If the URL has a domain, it is encoded to Punycode.

    >>> iri_to_uri('http://\\u2603.net/p\\xe5th?q=\\xe8ry%DF')
    'http://xn--n3h.net/p%C3%A5th?q=%C3%A8ry%DF'

    :param iri: The IRI to convert.

    .. versionchanged:: 3.0
        Passing a tuple or bytes, the ``charset`` and ``errors`` parameters,
        and the ``safe_conversion`` parameter, are removed.

    .. versionchanged:: 2.3
        Which characters remain unquoted is specific to each part of the URL.

    .. versionchanged:: 0.15
        All reserved characters remain unquoted. Previously, only some reserved
        characters were left unquoted.

    .. versionchanged:: 0.9.6
       The ``safe_conversion`` parameter was added.

    .. versionadded:: 0.6
    """
