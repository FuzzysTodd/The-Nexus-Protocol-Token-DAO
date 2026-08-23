from _typeshed import Incomplete
from pathos.connection import Pipe as _Pipe

__all__ = ['FileNotFound', 'Copier']

class FileNotFound(Exception):
    """Exception for improper source or destination format"""

class Copier(_Pipe):
    """a popen-based copier for parallel and distributed computing."""
    launcher: Incomplete
    options: Incomplete
    source: Incomplete
    destination: Incomplete
    def __init__(self, name: Incomplete | None = None, **kwds) -> None:
        """create a copier

Inputs:
    name: a unique identifier (string) for the launcher
    source: hostname:path of original  [user@host:path is also valid]
    destination: hostname:path for copy  [user@host:path is also valid]
    launcher: remote service mechanism (i.e. scp, cp)  [default = 'scp']
    options: remote service options (i.e. -v, -P)  [default = '']
    background: run in background  [default = False]
    decode: ensure response is 'ascii'  [default = True]
    stdin: file-like object to serve as standard input for the remote process
        """
    stdin: Incomplete
    background: Incomplete
    codec: Incomplete
    message: Incomplete
    def config(self, **kwds):
        """configure the copier using given keywords:

(Re)configure the copier for the following inputs:
    source: hostname:path of original  [user@host:path is also valid]
    destination: hostname:path for copy  [user@host:path is also valid]
    launcher: remote service mechanism (i.e. scp, cp)  [default = 'scp']
    options: remote service options (i.e. -v, -P)  [default = '']
    background: run in background  [default = False]
    decode: ensure response is 'ascii'  [default = True]
    stdin: file-like object to serve as standard input for the remote process
        """
    __call__ = config
