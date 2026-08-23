from _typeshed import Incomplete
from fsspec import AbstractFileSystem as AbstractFileSystem
from fsspec.spec import AbstractBufferedFile as AbstractBufferedFile

class DatabricksException(Exception):
    """
    Helper class for exceptions raised in this module.
    """
    error_code: Incomplete
    message: Incomplete
    def __init__(self, error_code, message) -> None:
        """Create a new DatabricksException"""

class DatabricksFileSystem(AbstractFileSystem):
    """
    Get access to the Databricks filesystem implementation over HTTP.
    Can be used inside and outside of a databricks cluster.
    """
    instance: Incomplete
    token: Incomplete
    session: Incomplete
    def __init__(self, instance, token, **kwargs) -> None:
        """
        Create a new DatabricksFileSystem.

        Parameters
        ----------
        instance: str
            The instance URL of the databricks cluster.
            For example for an Azure databricks cluster, this
            has the form adb-<some-number>.<two digits>.azuredatabricks.net.
        token: str
            Your personal token. Find out more
            here: https://docs.databricks.com/dev-tools/api/latest/authentication.html
        """
    def ls(self, path, detail: bool = True):
        """
        List the contents of the given path.

        Parameters
        ----------
        path: str
            Absolute path
        detail: bool
            Return not only the list of filenames,
            but also additional information on file sizes
            and types.
        """
    def makedirs(self, path, exist_ok: bool = True) -> None:
        """
        Create a given absolute path and all of its parents.

        Parameters
        ----------
        path: str
            Absolute path to create
        exist_ok: bool
            If false, checks if the folder
            exists before creating it (and raises an
            Exception if this is the case)
        """
    def mkdir(self, path, create_parents: bool = True, **kwargs) -> None:
        '''
        Create a given absolute path and all of its parents.

        Parameters
        ----------
        path: str
            Absolute path to create
        create_parents: bool
            Whether to create all parents or not.
            "False" is not implemented so far.
        '''
    def rm(self, path, recursive: bool = False) -> None:
        """
        Remove the file or folder at the given absolute path.

        Parameters
        ----------
        path: str
            Absolute path what to remove
        recursive: bool
            Recursively delete all files in a folder.
        """
    def mv(self, source_path, destination_path, recursive: bool = False, maxdepth: Incomplete | None = None) -> None:
        """
        Move a source to a destination path.

        A note from the original [databricks API manual]
        (https://docs.databricks.com/dev-tools/api/latest/dbfs.html#move).

        When moving a large number of files the API call will time out after
        approximately 60s, potentially resulting in partially moved data.
        Therefore, for operations that move more than 10k files, we strongly
        discourage using the DBFS REST API.

        Parameters
        ----------
        source_path: str
            From where to move (absolute path)
        destination_path: str
            To where to move (absolute path)
        recursive: bool
            Not implemented to far.
        maxdepth:
            Not implemented to far.
        """
    def invalidate_cache(self, path: Incomplete | None = None) -> None: ...

class DatabricksFile(AbstractBufferedFile):
    """
    Helper class for files referenced in the DatabricksFileSystem.
    """
    DEFAULT_BLOCK_SIZE: Incomplete
    def __init__(self, fs, path, mode: str = 'rb', block_size: str = 'default', autocommit: bool = True, cache_type: str = 'readahead', cache_options: Incomplete | None = None, **kwargs) -> None:
        """
        Create a new instance of the DatabricksFile.

        The blocksize needs to be the default one.
        """
