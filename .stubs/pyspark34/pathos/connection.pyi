from _typeshed import Incomplete

__all__ = ['Pipe', 'PipeException']

class PipeException(Exception):
    """Exception for failure to launch a command"""

class Pipe:
    """a popen-based pipe for parallel and distributed computing"""
    verbose: bool
    name: Incomplete
    background: Incomplete
    stdin: Incomplete
    codec: Incomplete
    message: Incomplete
    def __init__(self, name: Incomplete | None = None, **kwds) -> None:
        """create a popen-pipe

Inputs:
    name: a unique identifier (string) for the pipe
    command: a command to send  [default = 'echo <name>']
    background: run in background  [default = False]
    decode: ensure response is 'ascii'  [default = True]
    stdin: file-like object to serve as standard input for the remote process
        """
    def config(self, **kwds):
        """configure the pipe using given keywords

(Re)configure the pipe for the following inputs:
    command: a command to send  [default = 'echo <name>']
    background: run in background  [default = False]
    decode: ensure response is 'ascii'  [default = True]
    stdin: file-like object to serve as standard input for the remote process
        """
    def launch(self) -> None:
        """launch a configured command"""
    def response(self):
        """Return the response from the launched process.
        Return None if no response was received yet from a background process.
        """
    def pid(self):
        """get pipe pid"""
    def kill(self) -> None:
        """terminate the pipe"""
    __call__ = config
