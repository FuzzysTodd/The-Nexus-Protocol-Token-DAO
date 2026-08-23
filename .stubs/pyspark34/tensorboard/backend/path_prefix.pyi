from tensorboard import errors as errors

class PathPrefixMiddleware:
    """WSGI middleware for path prefixes.

    All requests to this middleware must begin with the specified path
    prefix (otherwise, a 404 will be returned immediately). Requests
    will be forwarded to the underlying application with the path prefix
    stripped and appended to `SCRIPT_NAME` (see the WSGI spec, PEP 3333,
    for details).
    """
    def __init__(self, application, path_prefix) -> None:
        '''Initializes this middleware.

        Args:
          application: The WSGI application to wrap (see PEP 3333).
          path_prefix: A string path prefix to be stripped from incoming
            requests. If empty, this middleware is a no-op. If non-empty,
            the path prefix must start with a slash and not end with one
            (e.g., "/tensorboard").
        '''
    def __call__(self, environ, start_response): ...
