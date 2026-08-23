__all__ = ['ChannelOptions', 'ExperimentalApiWarning', 'UsageError', 'insecure_channel_credentials', 'wrap_server_method_handler']

class ChannelOptions:
    """Indicates a channel option unique to gRPC Python.

     This enumeration is part of an EXPERIMENTAL API.

     Attributes:
       SingleThreadedUnaryStream: Perform unary-stream RPCs on a single thread.
    """
    SingleThreadedUnaryStream: str

class UsageError(Exception):
    """Raised by the gRPC library to indicate usage not allowed by the API."""

def insecure_channel_credentials():
    """Creates a ChannelCredentials for use with an insecure channel.

    THIS IS AN EXPERIMENTAL API.
    """

class ExperimentalApiWarning(Warning):
    """A warning that an API is experimental."""

def wrap_server_method_handler(wrapper, handler):
    """Wraps the server method handler function.

    The server implementation requires all server handlers being wrapped as
    RpcMethodHandler objects. This helper function ease the pain of writing
    server handler wrappers.

    Args:
        wrapper: A wrapper function that takes in a method handler behavior
          (the actual function) and returns a wrapped function.
        handler: A RpcMethodHandler object to be wrapped.

    Returns:
        A newly created RpcMethodHandler.
    """
