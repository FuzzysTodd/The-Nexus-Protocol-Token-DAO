import google.auth.credentials
from _typeshed import Incomplete

def encode(signer, payload, header: Incomplete | None = None, key_id: Incomplete | None = None):
    """Make a signed JWT.

    Args:
        signer (google.auth.crypt.Signer): The signer used to sign the JWT.
        payload (Mapping[str, str]): The JWT payload.
        header (Mapping[str, str]): Additional JWT header payload.
        key_id (str): The key id to add to the JWT header. If the
            signer has a key id it will be used as the default. If this is
            specified it will override the signer's key id.

    Returns:
        bytes: The encoded JWT.
    """
def decode_header(token):
    """Return the decoded header of a token.

    No verification is done. This is useful to extract the key id from
    the header in order to acquire the appropriate certificate to verify
    the token.

    Args:
        token (Union[str, bytes]): the encoded JWT.

    Returns:
        Mapping: The decoded JWT header.
    """
def decode(token, certs: Incomplete | None = None, verify: bool = True, audience: Incomplete | None = None, clock_skew_in_seconds: int = 0):
    """Decode and verify a JWT.

    Args:
        token (str): The encoded JWT.
        certs (Union[str, bytes, Mapping[str, Union[str, bytes]]]): The
            certificate used to validate the JWT signature. If bytes or string,
            it must the the public key certificate in PEM format. If a mapping,
            it must be a mapping of key IDs to public key certificates in PEM
            format. The mapping must contain the same key ID that's specified
            in the token's header.
        verify (bool): Whether to perform signature and claim validation.
            Verification is done by default.
        audience (str or list): The audience claim, 'aud', that this JWT should
            contain. Or a list of audience claims. If None then the JWT's 'aud'
            parameter is not verified.
        clock_skew_in_seconds (int): The clock skew used for `iat` and `exp`
            validation.

    Returns:
        Mapping[str, str]: The deserialized JSON payload in the JWT.

    Raises:
        google.auth.exceptions.InvalidValue: if value validation failed.
        google.auth.exceptions.MalformedError: if schema validation failed.
    """

class Credentials(google.auth.credentials.Signing, google.auth.credentials.CredentialsWithQuotaProject):
    '''Credentials that use a JWT as the bearer token.

    These credentials require an "audience" claim. This claim identifies the
    intended recipient of the bearer token.

    The constructor arguments determine the claims for the JWT that is
    sent with requests. Usually, you\'ll construct these credentials with
    one of the helper constructors as shown in the next section.

    To create JWT credentials using a Google service account private key
    JSON file::

        audience = \'https://pubsub.googleapis.com/google.pubsub.v1.Publisher\'
        credentials = jwt.Credentials.from_service_account_file(
            \'service-account.json\',
            audience=audience)

    If you already have the service account file loaded and parsed::

        service_account_info = json.load(open(\'service_account.json\'))
        credentials = jwt.Credentials.from_service_account_info(
            service_account_info,
            audience=audience)

    Both helper methods pass on arguments to the constructor, so you can
    specify the JWT claims::

        credentials = jwt.Credentials.from_service_account_file(
            \'service-account.json\',
            audience=audience,
            additional_claims={\'meta\': \'data\'})

    You can also construct the credentials directly if you have a
    :class:`~google.auth.crypt.Signer` instance::

        credentials = jwt.Credentials(
            signer,
            issuer=\'your-issuer\',
            subject=\'your-subject\',
            audience=audience)

    The claims are considered immutable. If you want to modify the claims,
    you can easily create another instance using :meth:`with_claims`::

        new_audience = (
            \'https://pubsub.googleapis.com/google.pubsub.v1.Subscriber\')
        new_credentials = credentials.with_claims(audience=new_audience)
    '''
    def __init__(self, signer, issuer, subject, audience, additional_claims: Incomplete | None = None, token_lifetime=..., quota_project_id: Incomplete | None = None) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            issuer (str): The `iss` claim.
            subject (str): The `sub` claim.
            audience (str): the `aud` claim. The intended audience for the
                credentials.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT payload.
            token_lifetime (int): The amount of time in seconds for
                which the token is valid. Defaults to 1 hour.
            quota_project_id (Optional[str]): The project ID used for quota
                and billing.
        """
    @classmethod
    def from_service_account_info(cls, info, **kwargs):
        """Creates an Credentials instance from a dictionary.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.jwt.Credentials: The constructed credentials.

        Raises:
            google.auth.exceptions.MalformedError: If the info is not in the expected format.
        """
    @classmethod
    def from_service_account_file(cls, filename, **kwargs):
        """Creates a Credentials instance from a service account .json file
        in Google format.

        Args:
            filename (str): The path to the service account .json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.jwt.Credentials: The constructed credentials.
        """
    @classmethod
    def from_signing_credentials(cls, credentials, audience, **kwargs):
        """Creates a new :class:`google.auth.jwt.Credentials` instance from an
        existing :class:`google.auth.credentials.Signing` instance.

        The new instance will use the same signer as the existing instance and
        will use the existing instance's signer email as the issuer and
        subject by default.

        Example::

            svc_creds = service_account.Credentials.from_service_account_file(
                'service_account.json')
            audience = (
                'https://pubsub.googleapis.com/google.pubsub.v1.Publisher')
            jwt_creds = jwt.Credentials.from_signing_credentials(
                svc_creds, audience=audience)

        Args:
            credentials (google.auth.credentials.Signing): The credentials to
                use to construct the new credentials.
            audience (str): the `aud` claim. The intended audience for the
                credentials.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.jwt.Credentials: A new Credentials instance.
        """
    def with_claims(self, issuer: Incomplete | None = None, subject: Incomplete | None = None, audience: Incomplete | None = None, additional_claims: Incomplete | None = None):
        """Returns a copy of these credentials with modified claims.

        Args:
            issuer (str): The `iss` claim. If unspecified the current issuer
                claim will be used.
            subject (str): The `sub` claim. If unspecified the current subject
                claim will be used.
            audience (str): the `aud` claim. If unspecified the current
                audience claim will be used.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT payload. This will be merged with the current
                additional claims.

        Returns:
            google.auth.jwt.Credentials: A new credentials instance.
        """
    def with_quota_project(self, quota_project_id): ...
    def refresh(self, request) -> None:
        """Refreshes the access token.

        Args:
            request (Any): Unused.
        """
    def sign_bytes(self, message): ...
    @property
    def signer_email(self): ...
    @property
    def signer(self): ...
    @property
    def additional_claims(self):
        """ Additional claims the JWT object was created with."""

class OnDemandCredentials(google.auth.credentials.Signing, google.auth.credentials.CredentialsWithQuotaProject):
    """On-demand JWT credentials.

    Like :class:`Credentials`, this class uses a JWT as the bearer token for
    authentication. However, this class does not require the audience at
    construction time. Instead, it will generate a new token on-demand for
    each request using the request URI as the audience. It caches tokens
    so that multiple requests to the same URI do not incur the overhead
    of generating a new token every time.

    This behavior is especially useful for `gRPC`_ clients. A gRPC service may
    have multiple audience and gRPC clients may not know all of the audiences
    required for accessing a particular service. With these credentials,
    no knowledge of the audiences is required ahead of time.

    .. _grpc: http://www.grpc.io/
    """
    def __init__(self, signer, issuer, subject, additional_claims: Incomplete | None = None, token_lifetime=..., max_cache_size=..., quota_project_id: Incomplete | None = None) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            issuer (str): The `iss` claim.
            subject (str): The `sub` claim.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT payload.
            token_lifetime (int): The amount of time in seconds for
                which the token is valid. Defaults to 1 hour.
            max_cache_size (int): The maximum number of JWT tokens to keep in
                cache. Tokens are cached using :class:`cachetools.LRUCache`.
            quota_project_id (Optional[str]): The project ID used for quota
                and billing.

        """
    @classmethod
    def from_service_account_info(cls, info, **kwargs):
        """Creates an OnDemandCredentials instance from a dictionary.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.jwt.OnDemandCredentials: The constructed credentials.

        Raises:
            google.auth.exceptions.MalformedError: If the info is not in the expected format.
        """
    @classmethod
    def from_service_account_file(cls, filename, **kwargs):
        """Creates an OnDemandCredentials instance from a service account .json
        file in Google format.

        Args:
            filename (str): The path to the service account .json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.jwt.OnDemandCredentials: The constructed credentials.
        """
    @classmethod
    def from_signing_credentials(cls, credentials, **kwargs):
        """Creates a new :class:`google.auth.jwt.OnDemandCredentials` instance
        from an existing :class:`google.auth.credentials.Signing` instance.

        The new instance will use the same signer as the existing instance and
        will use the existing instance's signer email as the issuer and
        subject by default.

        Example::

            svc_creds = service_account.Credentials.from_service_account_file(
                'service_account.json')
            jwt_creds = jwt.OnDemandCredentials.from_signing_credentials(
                svc_creds)

        Args:
            credentials (google.auth.credentials.Signing): The credentials to
                use to construct the new credentials.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.jwt.Credentials: A new Credentials instance.
        """
    def with_claims(self, issuer: Incomplete | None = None, subject: Incomplete | None = None, additional_claims: Incomplete | None = None):
        """Returns a copy of these credentials with modified claims.

        Args:
            issuer (str): The `iss` claim. If unspecified the current issuer
                claim will be used.
            subject (str): The `sub` claim. If unspecified the current subject
                claim will be used.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT payload. This will be merged with the current
                additional claims.

        Returns:
            google.auth.jwt.OnDemandCredentials: A new credentials instance.
        """
    def with_quota_project(self, quota_project_id): ...
    @property
    def valid(self):
        """Checks the validity of the credentials.

        These credentials are always valid because it generates tokens on
        demand.
        """
    def refresh(self, request) -> None:
        """Raises an exception, these credentials can not be directly
        refreshed.

        Args:
            request (Any): Unused.

        Raises:
            google.auth.RefreshError
        """
    def before_request(self, request, method, url, headers) -> None:
        """Performs credential-specific before request logic.

        Args:
            request (Any): Unused. JWT credentials do not need to make an
                HTTP request to refresh.
            method (str): The request's HTTP method.
            url (str): The request's URI. This is used as the audience claim
                when generating the JWT.
            headers (Mapping): The request's headers.
        """
    def sign_bytes(self, message): ...
    @property
    def signer_email(self): ...
    @property
    def signer(self): ...
