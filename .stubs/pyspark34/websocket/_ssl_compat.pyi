import ssl as ssl
from ssl import SSLError as SSLError, SSLWantReadError as SSLWantReadError, SSLWantWriteError as SSLWantWriteError

__all__ = ['HAVE_SSL', 'ssl', 'SSLError', 'SSLWantReadError', 'SSLWantWriteError']

HAVE_SSL: bool

class SSLError(Exception): ...
class SSLWantReadError(Exception): ...
class SSLWantWriteError(Exception): ...
