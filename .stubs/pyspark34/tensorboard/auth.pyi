import abc

class AuthProvider(metaclass=abc.ABCMeta):
    """Authentication provider for a specific kind of credential."""
    def authenticate(self, environ) -> None:
        """Produce an opaque auth token from a WSGI request environment.

        Args:
          environ: A WSGI environment `dict`; see PEP 3333.

        Returns:
          A Python object representing an auth token. The representation
          and semantics depend on the particular `AuthProvider`
          implementation.

        Raises:
          Exception: Any error, usually `tensorboard.errors.PublicError`
            subclasses (like `PermissionDenied`) but also possibly a
            custom error type that should propagate to a WSGI middleware
            for effecting a redirect-driven auth flow.
        """

class AuthContext:
    """Authentication context within the scope of a single request.

    Auth providers are keyed within an `AuthContext` by arbitrary
    unique keys. It may often make sense for the key used for an
    auth provider to simply be that provider's type object.
    """
    def __init__(self, providers, environ) -> None:
        """Create an auth context.

        Args:
          providers: A mapping from provider keys (opaque values) to
            `AuthProvider` implementations.
          environ: A WSGI environment (see PEP 3333).
        """
    @classmethod
    def empty(cls):
        """Create an auth context with no registered providers.

        Returns:
          A new `AuthContext` value for which any call to `get` will
          fail with a `KeyError`.
        """
    def get(self, provider_key):
        """Get an auth token from the auth provider with the given key.

        If successful, the result will be cached on this auth context.
        If unsuccessful, nothing will be cached, so a future call will
        invoke the underlying `AuthProvider.authenticate` method again.

        This method is not thread-safe. If multiple threads share an
        auth context for a single request, then they must synchronize
        externally when calling this method.

        Returns:
          The result of `provider.authenticate(...)` for the auth
          provider specified by `provider_key`.

        Raises:
          KeyError: If the given `provider_key` does not correspond to
            any registered `AuthProvider`.
          Exception: As raised by the underlying `AuthProvider`.
        """
