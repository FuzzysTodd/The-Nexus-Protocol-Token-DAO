from tensorboard import context as context, errors as errors

class ClientFeatureFlagsMiddleware:
    """Middleware for injecting client-side feature flags into the Context.

    The client webapp is expected to include a json-serialized version of its
    FeatureFlags in the `X-TensorBoard-Feature-Flags` header. This middleware
    extracts the header value and converts it into the client_feature_flags
    property for the DataProvider's Context object, where client_feature_flags
    is a Dict of string keys and arbitrary value types.
    """
    def __init__(self, application) -> None:
        """Initializes this middleware.

        Args:
          application: The WSGI application to wrap (see PEP 3333).
        """
    def __call__(self, environ, start_response): ...
