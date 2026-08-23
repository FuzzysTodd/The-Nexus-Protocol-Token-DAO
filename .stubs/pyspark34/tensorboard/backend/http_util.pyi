from _typeshed import Incomplete
from tensorboard.backend import json_util as json_util

def Respond(request, content, content_type, code: int = 200, expires: int = 0, content_encoding: Incomplete | None = None, encoding: str = 'utf-8', csp_scripts_sha256s: Incomplete | None = None, headers: Incomplete | None = None):
    '''Construct a werkzeug Response.

    Responses are transmitted to the browser with compression if: a) the browser
    supports it; b) it\'s sane to compress the content_type in question; and c)
    the content isn\'t already compressed, as indicated by the content_encoding
    parameter.

    Browser and proxy caching is completely disabled by default. If the expires
    parameter is greater than zero then the response will be able to be cached by
    the browser for that many seconds; however, proxies are still forbidden from
    caching so that developers can bypass the cache with Ctrl+Shift+R.

    For textual content that isn\'t JSON, the encoding parameter is used as the
    transmission charset which is automatically appended to the Content-Type
    header. That is unless of course the content_type parameter contains a
    charset parameter. If the two disagree, the characters in content will be
    transcoded to the latter.

    If content_type declares a JSON media type, then content MAY be a dict, list,
    tuple, or set, in which case this function has an implicit composition with
    json_util.Cleanse and json.dumps. The encoding parameter is used to decode
    byte strings within the JSON object; therefore transmitting binary data
    within JSON is not permitted. JSON is transmitted as ASCII unless the
    content_type parameter explicitly defines a charset parameter, in which case
    the serialized JSON bytes will use that instead of escape sequences.

    Args:
      request: A werkzeug Request object. Used mostly to check the
        Accept-Encoding header.
      content: Payload data as byte string, unicode string, or maybe JSON.
      content_type: Media type and optionally an output charset.
      code: Numeric HTTP status code to use.
      expires: Second duration for browser caching.
      content_encoding: Encoding if content is already encoded, e.g. \'gzip\'.
      encoding: Input charset if content parameter has byte strings.
      csp_scripts_sha256s: List of base64 serialized sha256 of whitelisted script
        elements for script-src of the Content-Security-Policy. If it is None, the
        HTML will disallow any script to execute. It is only be used when the
        content_type is text/html.
      headers: Any additional headers to include on the response, as a
        list of key-value tuples: e.g., `[("Allow", "GET")]`. In case of
        conflict, these may be overridden with headers added by this function.

    Returns:
      A werkzeug Response object (a WSGI application).
    '''
