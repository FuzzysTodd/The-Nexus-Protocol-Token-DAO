class EmptyPathRedirectMiddleware:
    '''WSGI middleware to redirect from "" to "/".'''
    def __init__(self, application) -> None:
        """Initializes this middleware.

        Args:
          application: The WSGI application to wrap (see PEP 3333).
        """
    def __call__(self, environ, start_response): ...
