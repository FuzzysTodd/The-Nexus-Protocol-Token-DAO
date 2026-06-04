WSGI_ENVIRON_KEY: str

class ExperimentIdMiddleware:
    """WSGI middleware extracting experiment IDs from URL to environment.

    Any request whose path matches `/experiment/SOME_EID[/...]` will have
    its first two path components stripped, and its experiment ID stored
    onto the WSGI environment with key taken from the `WSGI_ENVIRON_KEY`
    constant. All other requests will have paths unchanged and the
    experiment ID set to the empty string. It noops if the key taken from
    the `WSGI_ENVIRON_KEY` is already present in the environment.

    Instances of this class are WSGI applications (see PEP 3333).
    """
    def __init__(self, application) -> None:
        """Initializes an `ExperimentIdMiddleware`.

        Args:
          application: The WSGI application to wrap (see PEP 3333).
        """
    def __call__(self, environ, start_response): ...
