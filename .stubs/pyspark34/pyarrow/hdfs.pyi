import pyarrow._hdfsio as _hdfsio
from _typeshed import Incomplete
from collections.abc import Generator
from pyarrow.filesystem import FileSystem as FileSystem
from pyarrow.util import implements as implements

class HadoopFileSystem(_hdfsio.HadoopFileSystem, FileSystem):
    """
    DEPRECATED: FileSystem interface for HDFS cluster.

    See pyarrow.hdfs.connect for full connection details

    .. deprecated:: 2.0
        ``pyarrow.hdfs.HadoopFileSystem`` is deprecated,
        please use ``pyarrow.fs.HadoopFileSystem`` instead.
    """
    def __init__(self, host: str = 'default', port: int = 0, user: Incomplete | None = None, kerb_ticket: Incomplete | None = None, driver: str = 'libhdfs', extra_conf: Incomplete | None = None) -> None: ...
    def __reduce__(self): ...
    def isdir(self, path): ...
    def isfile(self, path): ...
    def delete(self, path, recursive: bool = False): ...
    def mkdir(self, path, **kwargs):
        """
        Create directory in HDFS.

        Parameters
        ----------
        path : str
            Directory path to create, including any parent directories.

        Notes
        -----
        libhdfs does not support create_parents=False, so we ignore this here
        """
    def rename(self, path, new_path): ...
    def exists(self, path): ...
    def ls(self, path, detail: bool = False):
        """
        Retrieve directory contents and metadata, if requested.

        Parameters
        ----------
        path : str
            HDFS path to retrieve contents of.
        detail : bool, default False
            If False, only return list of paths.

        Returns
        -------
        result : list of dicts (detail=True) or strings (detail=False)
        """
    def walk(self, top_path) -> Generator[Incomplete, Incomplete, None]:
        """
        Directory tree generator for HDFS, like os.walk.

        Parameters
        ----------
        top_path : str
            Root directory for tree traversal.

        Returns
        -------
        Generator yielding 3-tuple (dirpath, dirnames, filename)
        """

def connect(host: str = 'default', port: int = 0, user: Incomplete | None = None, kerb_ticket: Incomplete | None = None, extra_conf: Incomplete | None = None):
    '''
    DEPRECATED: Connect to an HDFS cluster.

    All parameters are optional and should only be set if the defaults need
    to be overridden.

    Authentication should be automatic if the HDFS cluster uses Kerberos.
    However, if a username is specified, then the ticket cache will likely
    be required.

    .. deprecated:: 2.0
        ``pyarrow.hdfs.connect`` is deprecated,
        please use ``pyarrow.fs.HadoopFileSystem`` instead.

    Parameters
    ----------
    host : NameNode. Set to "default" for fs.defaultFS from core-site.xml.
    port : NameNode\'s port. Set to 0 for default or logical (HA) nodes.
    user : Username when connecting to HDFS; None implies login user.
    kerb_ticket : Path to Kerberos ticket cache.
    extra_conf : dict, default None
      extra Key/Value pairs for config; Will override any
      hdfs-site.xml properties

    Notes
    -----
    The first time you call this method, it will take longer than usual due
    to JNI spin-up time.

    Returns
    -------
    filesystem : HadoopFileSystem
    '''
