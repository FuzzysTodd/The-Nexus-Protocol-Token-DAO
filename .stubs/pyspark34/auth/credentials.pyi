import abc
from _typeshed import Incomplete

class Credentials(metaclass=abc.ABCMeta):
    """Base class for all credentials.

    All credentials have a :attr:`token` that is used for authentication and
    may also optionally set an :attr:`expiry` to indicate when the token will
    no longer be valid.

    Most credentials will be :attr:`invalid` until :meth:`refresh` is called.
    Credentials can do this automatically before the first HTTP request in
    :meth:`before_request`.

    Although the token and expiration will change as the credentials are
    :meth:`refreshed <refresh>` and used, credentials should be considered
    immutable. Various credentials will accept configuration such as private
    keys, scopes, and other options. These options are not changeable after
    construction. Some classes will provide mechanisms to copy the credentials
    with modifications such as :meth:`ScopedCredentials.with_scopes`.
    """
    token: Incomplete
    expiry: Incomplete
    def __init__(self) -> None: ...
    @property
    def expired(self):
        """Checks if the credentials are expired.

        Note that credentials can be invalid but not expired because
        Credentials with :attr:`expiry` set to None is considered to never
        expire.
        """
    @property
    def valid(self):
        """Checks the validity of the credentials.

        This is True if the credentials have a :attr:`token` and the token
        is not :attr:`expired`.
        """
    @property
    def quota_project_id(self):
        """Project to use for quota and billing purposes."""
    @property
    def universe_domain(self):
        """The universe domain value."""
    @abc.abstractmethod
    def refresh(self, request):
        """Refreshes the access token.

        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.

        Raises:
            google.auth.exceptions.RefreshError: If the credentials could
                not be refreshed.
        """
    def apply(self, headers, token: Incomplete | None = None) -> None:
        """Apply the token to the authentication header.

        Args:
            headers (Mapping): The HTTP request headers.
            token (Optional[str]): If specified, overrides the current access
                token.
        """
    def before_request(self, request, method, url, headers) -> None:
        """Performs credential-specific before request logic.

        Refreshes the credentials if necessary, then calls :meth:`apply` to
        apply the token to the authentication header.

        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.
            method (str): The request's HTTP method or the RPC method being
                invoked.
            url (str): The request's URI or the RPC service's URI.
            headers (Mapping): The request's headers.
        """

class CredentialsWithQuotaProject(Credentials, metaclass=abc.ABCMeta):
    """Abstract base for credentials supporting ``with_quota_project`` factory"""
    def with_quota_project(self, quota_project_id) -> None:
        """Returns a copy of these credentials with a modified quota project.

        Args:
            quota_project_id (str): The project to use for quota and
                billing purposes

        Returns:
            google.oauth2.credentials.Credentials: A new credentials instance.
        """
    def with_quota_project_from_environment(self): ...

class CredentialsWithTokenUri(Credentials, metaclass=abc.ABCMeta):
    """Abstract base for credentials supporting ``with_token_uri`` factory"""
    def with_token_uri(self, token_uri) -> None:
        """Returns a copy of these credentials with a modified token uri.

        Args:
            token_uri (str): The uri to use for fetching/exchanging tokens

        Returns:
            google.oauth2.credentials.Credentials: A new credentials instance.
        """

class AnonymousCredentials(Credentials):
    """Credentials that do not provide any authentication information.

    These are useful in the case of services that support anonymous access or
    local service emulators that do not use credentials.
    """
    @property
    def expired(self):
        """Returns `False`, anonymous credentials never expire."""
    @property
    def valid(self):
        """Returns `True`, anonymous credentials are always valid."""
    def refresh(self, request) -> None:
        """Raises :class:``InvalidOperation``, anonymous credentials cannot be
        refreshed."""
    def apply(self, headers, token: Incomplete | None = None) -> None:
        """Anonymous credentials do nothing to the request.

        The optional ``token`` argument is not supported.

        Raises:
            google.auth.exceptions.InvalidValue: If a token was specified.
        """
    def before_request(self, request, method, url, headers) -> None:
        """Anonymous credentials do nothing to the request."""

class ReadOnlyScoped(metaclass=abc.ABCMeta):
    """Interface for credentials whose scopes can be queried.

    OAuth 2.0-based credentials allow limiting access using scopes as described
    in `RFC6749 Section 3.3`_.
    If a credential class implements this interface then the credentials either
    use scopes in their implementation.

    Some credentials require scopes in order to obtain a token. You can check
    if scoping is necessary with :attr:`requires_scopes`::

        if credentials.requires_scopes:
            # Scoping is required.
            credentials = credentials.with_scopes(scopes=['one', 'two'])

    Credentials that require scopes must either be constructed with scopes::

        credentials = SomeScopedCredentials(scopes=['one', 'two'])

    Or must copy an existing instance using :meth:`with_scopes`::

        scoped_credentials = credentials.with_scopes(scopes=['one', 'two'])

    Some credentials have scopes but do not allow or require scopes to be set,
    these credentials can be used as-is.

    .. _RFC6749 Section 3.3: https://tools.ietf.org/html/rfc6749#section-3.3
    """
    def __init__(self) -> None: ...
    @property
    def scopes(self):
        """Sequence[str]: the credentials' current set of scopes."""
    @property
    def default_scopes(self):
        """Sequence[str]: the credentials' current set of default scopes."""
    @property
    @abc.abstractmethod
    def requires_scopes(self):
        """True if these credentials require scopes to obtain an access token.
        """
    def has_scopes(self, scopes):
        """Checks if the credentials have the given scopes.

        .. warning: This method is not guaranteed to be accurate if the
            credentials are :attr:`~Credentials.invalid`.

        Args:
            scopes (Sequence[str]): The list of scopes to check.

        Returns:
            bool: True if the credentials have the given scopes.
        """

class Scoped(ReadOnlyScoped, metaclass=abc.ABCMeta):
    """Interface for credentials whose scopes can be replaced while copying.

    OAuth 2.0-based credentials allow limiting access using scopes as described
    in `RFC6749 Section 3.3`_.
    If a credential class implements this interface then the credentials either
    use scopes in their implementation.

    Some credentials require scopes in order to obtain a token. You can check
    if scoping is necessary with :attr:`requires_scopes`::

        if credentials.requires_scopes:
            # Scoping is required.
            credentials = credentials.create_scoped(['one', 'two'])

    Credentials that require scopes must either be constructed with scopes::

        credentials = SomeScopedCredentials(scopes=['one', 'two'])

    Or must copy an existing instance using :meth:`with_scopes`::

        scoped_credentials = credentials.with_scopes(scopes=['one', 'two'])

    Some credentials have scopes but do not allow or require scopes to be set,
    these credentials can be used as-is.

    .. _RFC6749 Section 3.3: https://tools.ietf.org/html/rfc6749#section-3.3
    """
    @abc.abstractmethod
    def with_scopes(self, scopes, default_scopes: Incomplete | None = None):
        """Create a copy of these credentials with the specified scopes.

        Args:
            scopes (Sequence[str]): The list of scopes to attach to the
                current credentials.

        Raises:
            NotImplementedError: If the credentials' scopes can not be changed.
                This can be avoided by checking :attr:`requires_scopes` before
                calling this method.
        """

def with_scopes_if_required(credentials, scopes, default_scopes: Incomplete | None = None):
    """Creates a copy of the credentials with scopes if scoping is required.

    This helper function is useful when you do not know (or care to know) the
    specific type of credentials you are using (such as when you use
    :func:`google.auth.default`). This function will call
    :meth:`Scoped.with_scopes` if the credentials are scoped credentials and if
    the credentials require scoping. Otherwise, it will return the credentials
    as-is.

    Args:
        credentials (google.auth.credentials.Credentials): The credentials to
            scope if necessary.
        scopes (Sequence[str]): The list of scopes to use.
        default_scopes (Sequence[str]): Default scopes passed by a
            Google client library. Use 'scopes' for user-defined scopes.

    Returns:
        google.auth.credentials.Credentials: Either a new set of scoped
            credentials, or the passed in credentials instance if no scoping
            was required.
    """

class Signing(metaclass=abc.ABCMeta):
    """Interface for credentials that can cryptographically sign messages."""
    @abc.abstractmethod
    def sign_bytes(self, message):
        """Signs the given message.

        Args:
            message (bytes): The message to sign.

        Returns:
            bytes: The message's cryptographic signature.
        """
    @property
    @abc.abstractmethod
    def signer_email(self):
        """Optional[str]: An email address that identifies the signer."""
    @property
    @abc.abstractmethod
    def signer(self):
        """google.auth.crypt.Signer: The signer used to sign bytes."""
