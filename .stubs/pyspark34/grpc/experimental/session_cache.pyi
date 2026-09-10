def ssl_session_cache_lru(capacity):
    """Creates an SSLSessionCache with LRU replacement policy

    Args:
      capacity: Size of the cache

    Returns:
      An SSLSessionCache with LRU replacement policy that can be passed as a value for
      the grpc.ssl_session_cache option to a grpc.Channel. SSL session caches are used
      to store session tickets, which clients can present to resume previous TLS sessions
      with a server.
    """

class SSLSessionCache:
    """An encapsulation of a session cache used for TLS session resumption.

    Instances of this class can be passed to a Channel as values for the
    grpc.ssl_session_cache option
    """
    def __init__(self, cache) -> None: ...
    def __int__(self) -> int: ...
