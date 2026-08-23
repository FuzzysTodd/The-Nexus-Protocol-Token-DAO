from tensorboard import auth as auth, context as context

class AuthContextMiddleware:
    """WSGI middleware to inject an AuthContext into the RequestContext."""
    def __init__(self, application, auth_providers) -> None:
        """Initializes this middleware.

        Args:
          application: A WSGI application to delegate to.
          auth_providers: The auth_providers to provide to the AuthContext.
        """
    def __call__(self, environ, start_response):
        """Invoke this WSGI application."""
