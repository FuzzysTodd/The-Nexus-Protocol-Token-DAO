import fsspec
from _typeshed import Incomplete

class JupyterFileSystem(fsspec.AbstractFileSystem):
    """View of the files as seen by a Jupyter server (notebook or lab)"""
    protocol: Incomplete
    url: Incomplete
    session: Incomplete
    def __init__(self, url, tok: Incomplete | None = None, **kwargs) -> None:
        '''

        Parameters
        ----------
        url : str
            Base URL of the server, like "http://127.0.0.1:8888". May include
            token in the string, which is given by the process when starting up
        tok : str
            If the token is obtained separately, can be given here
        kwargs
        '''
    def ls(self, path, detail: bool = True, **kwargs): ...
    def cat_file(self, path, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs): ...
    def pipe_file(self, path, value, **_) -> None: ...
    def mkdir(self, path, create_parents: bool = True, **kwargs) -> None: ...

class SimpleFileWriter(fsspec.spec.AbstractBufferedFile): ...
