from _typeshed import Incomplete

class RequestContext:
    """Container of request-scoped values.

    This context is for cross-cutting concerns: authentication,
    authorization, auditing, internationalization, logging, and so on.
    It is not simply for passing commonly used parameters to functions.

    `RequestContext` values are to be treated as immutable.

    Fields:
      auth: An `AuthContext`, which may be empty but is never `None`.
      remote_ip: An `ipaddress.IPv4Address` or `ipaddress.IPv6Address` or None.
        Best guess of the IP Address of the end user.
      x_forwarded_for: A tuple of `ipaddress.IPv4Address` or `ipaddress.IPv6Address`,
        which may be empty but is never None. This should be parsed value of X-Forwarded-For
        HTTP header from the request.
      client_feature_flags: A dict of string to arbitrary type. These represent
        feature flag key/value pairs sent by the client application. Usage of
        client_feature_flags should know the name of the feature flag key and
        should know and validate the type of the value.
    """
    def __init__(self, auth: Incomplete | None = None, remote_ip: Incomplete | None = None, x_forwarded_for: Incomplete | None = None, client_feature_flags: Incomplete | None = None) -> None:
        '''Create a request context.

        The argument list is sorted and may be extended in the future;
        therefore, callers must pass only named arguments to this
        initializer.

        Args:
          See "Fields" on class docstring. All arguments are optional
          and will be replaced with default values if appropriate.
        '''
    @property
    def auth(self): ...
    @property
    def remote_ip(self): ...
    @property
    def x_forwarded_for(self): ...
    @property
    def client_feature_flags(self): ...
    def replace(self, **kwargs):
        """Create a copy of this context with updated key-value pairs.

        Analogous to `namedtuple._replace`. For example, to create a new
        request context like `ctx` but with auth context `auth`, call
        `ctx.replace(auth=auth)`.

        Args:
          As to `__init__`.

        Returns:
          A new context like this one but with the specified updates.
        """

def from_environ(environ):
    """Get a `RequestContext` from a WSGI environment.

    See also `set_in_environ`.

    Args:
      environ: A WSGI environment (see PEP 3333).

    Returns:
      The `RequestContext` stored in the WSGI environment, or an empty
      `RequestContext` if none is stored.
    """
def set_in_environ(environ, ctx) -> None:
    """Set the `RequestContext` in a WSGI environment.

    After `set_in_environ(e, ctx)`, `from_environ(e) is ctx`. The input
    environment is mutated.

    Args:
      environ: A WSGI environment to update.
      ctx: A new `RequestContext` value.
    """
