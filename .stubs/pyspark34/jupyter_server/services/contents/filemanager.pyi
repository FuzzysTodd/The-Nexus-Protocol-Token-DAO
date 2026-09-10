from .filecheckpoints import AsyncFileCheckpoints as AsyncFileCheckpoints, FileCheckpoints as FileCheckpoints
from .fileio import AsyncFileManagerMixin as AsyncFileManagerMixin, FileManagerMixin as FileManagerMixin
from .manager import AsyncContentsManager as AsyncContentsManager, ContentsManager as ContentsManager, copy_pat as copy_pat
from _typeshed import Incomplete
from jupyter_server.base.handlers import AuthenticatedFileHandler as AuthenticatedFileHandler
from jupyter_server.utils import to_api_path as to_api_path

class FileContentsManager(FileManagerMixin, ContentsManager):
    """A file contents manager."""
    root_dir: Incomplete
    max_copy_folder_size_mb: Incomplete
    delete_to_trash: Incomplete
    always_delete_dir: Incomplete
    def is_hidden(self, path):
        """Does the API style path correspond to a hidden directory or file?

        Parameters
        ----------
        path : str
            The path to check. This is an API path (`/` separated,
            relative to root_dir).

        Returns
        -------
        hidden : bool
            Whether the path exists and is hidden.
        """
    def is_writable(self, path):
        """Does the API style path correspond to a writable directory or file?

        Parameters
        ----------
        path : str
            The path to check. This is an API path (`/` separated,
            relative to root_dir).

        Returns
        -------
        hidden : bool
            Whether the path exists and is writable.
        """
    def file_exists(self, path):
        """Returns True if the file exists, else returns False.

        API-style wrapper for os.path.isfile

        Parameters
        ----------
        path : str
            The relative path to the file (with '/' as separator)

        Returns
        -------
        exists : bool
            Whether the file exists.
        """
    def dir_exists(self, path):
        """Does the API-style path refer to an extant directory?

        API-style wrapper for os.path.isdir

        Parameters
        ----------
        path : str
            The path to check. This is an API path (`/` separated,
            relative to root_dir).

        Returns
        -------
        exists : bool
            Whether the path is indeed a directory.
        """
    def exists(self, path):
        """Returns True if the path exists, else returns False.

        API-style wrapper for os.path.exists

        Parameters
        ----------
        path : str
            The API path to the file (with '/' as separator)

        Returns
        -------
        exists : bool
            Whether the target exists.
        """
    def get(self, path, content: bool = True, type: Incomplete | None = None, format: Incomplete | None = None):
        """Takes a path for an entity and returns its model

        Parameters
        ----------
        path : str
            the API path that describes the relative path for the target
        content : bool
            Whether to include the contents in the reply
        type : str, optional
            The requested type - 'file', 'notebook', or 'directory'.
            Will raise HTTPError 400 if the content doesn't match.
        format : str, optional
            The requested format for file contents. 'text' or 'base64'.
            Ignored if this returns a notebook or directory model.

        Returns
        -------
        model : dict
            the contents model. If content=True, returns the contents
            of the file or directory as well.
        """
    def save(self, model, path: str = ''):
        """Save the file model and return the model with no content."""
    def delete_file(self, path):
        """Delete file at path."""
    def rename_file(self, old_path, new_path) -> None:
        """Rename a file."""
    def info_string(self):
        """Get the information string for the manager."""
    def get_kernel_path(self, path, model: Incomplete | None = None):
        """Return the initial API path of  a kernel associated with a given notebook"""
    def copy(self, from_path, to_path: Incomplete | None = None):
        """
        Copy an existing file or directory and return its new model.
        If to_path not specified, it will be the parent directory of from_path.
        If copying a file and to_path is a directory, filename/directoryname will increment `from_path-Copy#.ext`.
        Considering multi-part extensions, the Copy# part will be placed before the first dot for all the extensions except `ipynb`.
        For easier manual searching in case of notebooks, the Copy# part will be placed before the last dot.
        from_path must be a full path to a file or directory.
        """
    def check_folder_size(self, path) -> None:
        """
        limit the size of folders being copied to be no more than the
        trait max_copy_folder_size_mb to prevent a timeout error
        """

class AsyncFileContentsManager(FileContentsManager, AsyncFileManagerMixin, AsyncContentsManager):
    """An async file contents manager."""
    async def get(self, path, content: bool = True, type: Incomplete | None = None, format: Incomplete | None = None):
        """Takes a path for an entity and returns its model

        Parameters
        ----------
        path : str
            the API path that describes the relative path for the target
        content : bool
            Whether to include the contents in the reply
        type : str, optional
            The requested type - 'file', 'notebook', or 'directory'.
            Will raise HTTPError 400 if the content doesn't match.
        format : str, optional
            The requested format for file contents. 'text' or 'base64'.
            Ignored if this returns a notebook or directory model.

        Returns
        -------
        model : dict
            the contents model. If content=True, returns the contents
            of the file or directory as well.
        """
    async def save(self, model, path: str = ''):
        """Save the file model and return the model with no content."""
    async def delete_file(self, path):
        """Delete file at path."""
    async def rename_file(self, old_path, new_path) -> None:
        """Rename a file."""
    async def dir_exists(self, path):
        """Does a directory exist at the given path"""
    async def file_exists(self, path):
        """Does a file exist at the given path"""
    async def is_hidden(self, path):
        """Is path a hidden directory or file"""
    async def get_kernel_path(self, path, model: Incomplete | None = None):
        """Return the initial API path of a kernel associated with a given notebook"""
    async def copy(self, from_path, to_path: Incomplete | None = None):
        """
        Copy an existing file or directory and return its new model.
        If to_path not specified, it will be the parent directory of from_path.
        If copying a file and to_path is a directory, filename/directoryname will increment `from_path-Copy#.ext`.
        Considering multi-part extensions, the Copy# part will be placed before the first dot for all the extensions except `ipynb`.
        For easier manual searching in case of notebooks, the Copy# part will be placed before the last dot.
        from_path must be a full path to a file or directory.
        """
    async def check_folder_size(self, path: str) -> None:
        """
        limit the size of folders being copied to be no more than the
        trait max_copy_folder_size_mb to prevent a timeout error
        """
