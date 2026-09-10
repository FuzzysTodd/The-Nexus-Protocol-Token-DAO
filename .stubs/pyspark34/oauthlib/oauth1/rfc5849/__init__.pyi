from . import parameters as parameters, signature as signature
from _typeshed import Incomplete
from oauthlib.common import Request as Request, generate_nonce as generate_nonce, generate_timestamp as generate_timestamp, to_unicode as to_unicode, urlencode as urlencode

log: Incomplete
SIGNATURE_HMAC_SHA1: str
SIGNATURE_HMAC_SHA256: str
SIGNATURE_HMAC_SHA512: str
SIGNATURE_HMAC = SIGNATURE_HMAC_SHA1
SIGNATURE_RSA_SHA1: str
SIGNATURE_RSA_SHA256: str
SIGNATURE_RSA_SHA512: str
SIGNATURE_RSA = SIGNATURE_RSA_SHA1
SIGNATURE_PLAINTEXT: str
SIGNATURE_METHODS: Incomplete
SIGNATURE_TYPE_AUTH_HEADER: str
SIGNATURE_TYPE_QUERY: str
SIGNATURE_TYPE_BODY: str
CONTENT_TYPE_FORM_URLENCODED: str

class Client:
    """A client used to sign OAuth 1.0 RFC 5849 requests."""
    SIGNATURE_METHODS: Incomplete
    @classmethod
    def register_signature_method(cls, method_name, method_callback) -> None: ...
    client_key: Incomplete
    client_secret: Incomplete
    resource_owner_key: Incomplete
    resource_owner_secret: Incomplete
    signature_method: Incomplete
    signature_type: Incomplete
    callback_uri: Incomplete
    rsa_key: Incomplete
    verifier: Incomplete
    realm: Incomplete
    encoding: Incomplete
    decoding: Incomplete
    nonce: Incomplete
    timestamp: Incomplete
    def __init__(self, client_key, client_secret: Incomplete | None = None, resource_owner_key: Incomplete | None = None, resource_owner_secret: Incomplete | None = None, callback_uri: Incomplete | None = None, signature_method=..., signature_type=..., rsa_key: Incomplete | None = None, verifier: Incomplete | None = None, realm: Incomplete | None = None, encoding: str = 'utf-8', decoding: Incomplete | None = None, nonce: Incomplete | None = None, timestamp: Incomplete | None = None) -> None:
        """Create an OAuth 1 client.

        :param client_key: Client key (consumer key), mandatory.
        :param resource_owner_key: Resource owner key (oauth token).
        :param resource_owner_secret: Resource owner secret (oauth token secret).
        :param callback_uri: Callback used when obtaining request token.
        :param signature_method: SIGNATURE_HMAC, SIGNATURE_RSA or SIGNATURE_PLAINTEXT.
        :param signature_type: SIGNATURE_TYPE_AUTH_HEADER (default),
                               SIGNATURE_TYPE_QUERY or SIGNATURE_TYPE_BODY
                               depending on where you want to embed the oauth
                               credentials.
        :param rsa_key: RSA key used with SIGNATURE_RSA.
        :param verifier: Verifier used when obtaining an access token.
        :param realm: Realm (scope) to which access is being requested.
        :param encoding: If you provide non-unicode input you may use this
                         to have oauthlib automatically convert.
        :param decoding: If you wish that the returned uri, headers and body
                         from sign be encoded back from unicode, then set
                         decoding to your preferred encoding, i.e. utf-8.
        :param nonce: Use this nonce instead of generating one. (Mainly for testing)
        :param timestamp: Use this timestamp instead of using current. (Mainly for testing)
        """
    def get_oauth_signature(self, request):
        """Get an OAuth signature to be used in signing a request

        To satisfy `section 3.4.1.2`_ item 2, if the request argument's
        headers dict attribute contains a Host item, its value will
        replace any netloc part of the request argument's uri attribute
        value.

        .. _`section 3.4.1.2`: https://tools.ietf.org/html/rfc5849#section-3.4.1.2
        """
    def get_oauth_params(self, request):
        """Get the basic OAuth parameters to be used in generating a signature.
        """
    def sign(self, uri, http_method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None, realm: Incomplete | None = None):
        """Sign a request

        Signs an HTTP request with the specified parts.

        Returns a 3-tuple of the signed request's URI, headers, and body.
        Note that http_method is not returned as it is unaffected by the OAuth
        signing process. Also worth noting is that duplicate parameters
        will be included in the signature, regardless of where they are
        specified (query, body).

        The body argument may be a dict, a list of 2-tuples, or a formencoded
        string. The Content-Type header must be 'application/x-www-form-urlencoded'
        if it is present.

        If the body argument is not one of the above, it will be returned
        verbatim as it is unaffected by the OAuth signing process. Attempting to
        sign a request with non-formencoded data using the OAuth body signature
        type is invalid and will raise an exception.

        If the body does contain parameters, it will be returned as a properly-
        formatted formencoded string.

        Body may not be included if the http_method is either GET or HEAD as
        this changes the semantic meaning of the request.

        All string data MUST be unicode or be encoded with the same encoding
        scheme supplied to the Client constructor, default utf-8. This includes
        strings inside body dicts, for example.
        """
