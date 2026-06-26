from _typeshed import Incomplete
from pathos.connection import Pipe as _Pipe

__all__ = ['Pipe']

class Pipe(_Pipe):
    """a popen-based ssh-pipe for parallel and distributed computing."""
    launcher: Incomplete
    options: Incomplete
    host: Incomplete
    def __init__(self, name: Incomplete | None = None, **kwds) -> None:
        """create a ssh pipe

Inputs:
    name: a unique identifier (string) for the pipe
    host: hostname to recieve command [user@host is also valid]
    command: a command to send  [default = 'echo <name>']
    launcher: remote service mechanism (i.e. ssh, rsh)  [default = 'ssh']
    options: remote service options (i.e. -v, -N, -L)  [default = '']
    background: run in background  [default = False]
    decode: ensure response is 'ascii'  [default = True]
    stdin: file-like object to serve as standard input for the remote process
        """
    message: Incomplete
    stdin: Incomplete
    background: Incomplete
    codec: Incomplete
    def config(self, **kwds):
        """configure a remote command using given keywords:

(Re)configure the copier for the following inputs:
    host: hostname to recieve command [user@host is also valid]
    command: a command to send  [default = 'echo <name>']
    launcher: remote service mechanism (i.e. ssh, rsh)  [default = 'ssh']
    options: remote service options (i.e. -v, -N, -L)  [default = '']
    background: run in background  [default = False]
    decode: ensure response is 'ascii'  [default = True]
    stdin: file-like object to serve as standard input for the remote process
        """
    __call__ = config
