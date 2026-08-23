from ...files.handlers import FilesHandler as FilesHandler
from .checkpoints import AsyncCheckpoints as AsyncCheckpoints, Checkpoints as Checkpoints
from _typeshed import Incomplete
from jupyter_server import DEFAULT_EVENTS_SCHEMA_PATH as DEFAULT_EVENTS_SCHEMA_PATH, JUPYTER_SERVER_EVENTS_URI as JUPYTER_SERVER_EVENTS_URI
from jupyter_server.utils import import_item as import_item
from traitlets.config.configurable import LoggingConfigurable

copy_pat: Incomplete

class ContentsManager(LoggingConfigurable):
    """Base class for serving files and directories.

    This serves any text or binary file,
    as well as directories,
    with special handling for JSON notebook documents.

    Most APIs take a path argument,
    which is always an API-style unicode path,
    and always refers to a directory.

    - unicode, not url-escaped
    - '/'-separated
    - leading and trailing '/' will be stripped
    - if unspecified, path defaults to '',
      indicating the root path.

    """
    event_schema_id: Incomplete
    event_logger: Incomplete
    def emit(self, data) -> None:
        """Emit event using the core event schema from Jupyter Server's Contents Manager."""
    root_dir: Incomplete
    preferred_dir: Incomplete
    allow_hidden: Incomplete
    notary: Incomplete
    hide_globs: Incomplete
    untitled_notebook: Incomplete
    untitled_file: Incomplete
    untitled_directory: Incomplete
    pre_save_hook: Incomplete
    post_save_hook: Incomplete
    def run_pre_save_hook(self, model, path, **kwargs) -> None:
        """Run the pre-save hook if defined, and log errors"""
    def run_post_save_hook(self, model, os_path) -> None:
        """Run the post-save hook if defined, and log errors"""
    def register_pre_save_hook(self, hook) -> None:
        """Register a pre save hook."""
    def register_post_save_hook(self, hook) -> None:
        """Register a post save hook."""
    def run_pre_save_hooks(self, model, path, **kwargs) -> None:
        """Run the pre-save hooks if any, and log errors"""
    def run_post_save_hooks(self, model, os_path) -> None:
        """Run the post-save hooks if any, and log errors"""
    checkpoints_class: Incomplete
    checkpoints: Incomplete
    checkpoints_kwargs: Incomplete
    files_handler_class: Incomplete
    files_handler_params: Incomplete
    def get_extra_handlers(self):
        """Return additional handlers

        Default: self.files_handler_class on /files/.*
        """
    def dir_exists(self, path) -> None:
        """Does a directory exist at the given path?

        Like os.path.isdir

        Override this method in subclasses.

        Parameters
        ----------
        path : str
            The path to check

        Returns
        -------
        exists : bool
            Whether the path does indeed exist.
        """
    def is_hidden(self, path) -> None:
        """Is path a hidden directory or file?

        Parameters
        ----------
        path : str
            The path to check. This is an API path (`/` separated,
            relative to root dir).

        Returns
        -------
        hidden : bool
            Whether the path is hidden.

        """
    def file_exists(self, path: str = '') -> None:
        """Does a file exist at the given path?

        Like os.path.isfile

        Override this method in subclasses.

        Parameters
        ----------
        path : str
            The API path of a file to check for.

        Returns
        -------
        exists : bool
            Whether the file exists.
        """
    def exists(self, path):
        """Does a file or directory exist at the given path?

        Like os.path.exists

        Parameters
        ----------
        path : str
            The API path of a file or directory to check for.

        Returns
        -------
        exists : bool
            Whether the target exists.
        """
    def get(self, path, content: bool = True, type: Incomplete | None = None, format: Incomplete | None = None) -> None:
        """Get a file or directory model."""
    def save(self, model, path) -> None:
        """
        Save a file or directory model to path.

        Should return the saved model with no content.  Save implementations
        should call self.run_pre_save_hook(model=model, path=path) prior to
        writing any data.
        """
    def delete_file(self, path) -> None:
        """Delete the file or directory at path."""
    def rename_file(self, old_path, new_path) -> None:
        """Rename a file or directory."""
    def delete(self, path) -> None:
        """Delete a file/directory and any associated checkpoints."""
    def rename(self, old_path, new_path) -> None:
        """Rename a file and any checkpoints associated with that file."""
    def update(self, model, path):
        """Update the file's path

        For use in PATCH requests, to enable renaming a file without
        re-uploading its contents. Only used for renaming at the moment.
        """
    def info_string(self):
        """The information string for the manager."""
    def get_kernel_path(self, path, model: Incomplete | None = None):
        """Return the API path for the kernel

        KernelManagers can turn this value into a filesystem path,
        or ignore it altogether.

        The default value here will start kernels in the directory of the
        notebook server. FileContentsManager overrides this to use the
        directory containing the notebook.
        """
    def increment_filename(self, filename, path: str = '', insert: str = ''):
        """Increment a filename until it is unique.

        Parameters
        ----------
        filename : unicode
            The name of a file, including extension
        path : unicode
            The API path of the target's directory
        insert : unicode
            The characters to insert after the base filename

        Returns
        -------
        name : unicode
            A filename that is unique, based on the input filename.
        """
    def validate_notebook_model(self, model, validation_error: Incomplete | None = None):
        """Add failed-validation message to model"""
    def new_untitled(self, path: str = '', type: str = '', ext: str = ''):
        """Create a new untitled file or directory in path

        path must be a directory

        File extension can be specified.

        Use `new` to create files with a fully specified path (including filename).
        """
    def new(self, model: Incomplete | None = None, path: str = ''):
        """Create a new file or directory and return its model with no content.

        To create a new untitled entity in a directory, use `new_untitled`.
        """
    def copy(self, from_path, to_path: Incomplete | None = None):
        """Copy an existing file and return its new model.

        If to_path not specified, it will be the parent directory of from_path.
        If to_path is a directory, filename will increment `from_path-Copy#.ext`.
        Considering multi-part extensions, the Copy# part will be placed before the first dot for all the extensions except `ipynb`.
        For easier manual searching in case of notebooks, the Copy# part will be placed before the last dot.

        from_path must be a full path to a file.
        """
    def log_info(self) -> None:
        """Log the information string for the manager."""
    def trust_notebook(self, path) -> None:
        """Explicitly trust a notebook

        Parameters
        ----------
        path : str
            The path of a notebook
        """
    def check_and_sign(self, nb, path: str = '') -> None:
        """Check for trusted cells, and sign the notebook.

        Called as a part of saving notebooks.

        Parameters
        ----------
        nb : dict
            The notebook dict
        path : str
            The notebook's path (for logging)
        """
    def mark_trusted_cells(self, nb, path: str = '') -> None:
        """Mark cells as trusted if the notebook signature matches.

        Called as a part of loading notebooks.

        Parameters
        ----------
        nb : dict
            The notebook object (in current nbformat)
        path : str
            The notebook's path (for logging)
        """
    def should_list(self, name):
        """Should this file/directory name be displayed in a listing?"""
    def create_checkpoint(self, path):
        """Create a checkpoint."""
    def restore_checkpoint(self, checkpoint_id, path) -> None:
        """
        Restore a checkpoint.
        """
    def list_checkpoints(self, path): ...
    def delete_checkpoint(self, checkpoint_id, path): ...

class AsyncContentsManager(ContentsManager):
    """Base class for serving files and directories asynchronously."""
    checkpoints_class: Incomplete
    checkpoints: Incomplete
    checkpoints_kwargs: Incomplete
    async def dir_exists(self, path) -> None:
        """Does a directory exist at the given path?

        Like os.path.isdir

        Override this method in subclasses.

        Parameters
        ----------
        path : str
            The path to check

        Returns
        -------
        exists : bool
            Whether the path does indeed exist.
        """
    async def is_hidden(self, path) -> None:
        """Is path a hidden directory or file?

        Parameters
        ----------
        path : str
            The path to check. This is an API path (`/` separated,
            relative to root dir).

        Returns
        -------
        hidden : bool
            Whether the path is hidden.

        """
    async def file_exists(self, path: str = '') -> None:
        """Does a file exist at the given path?

        Like os.path.isfile

        Override this method in subclasses.

        Parameters
        ----------
        path : str
            The API path of a file to check for.

        Returns
        -------
        exists : bool
            Whether the file exists.
        """
    async def exists(self, path):
        """Does a file or directory exist at the given path?

        Like os.path.exists

        Parameters
        ----------
        path : str
            The API path of a file or directory to check for.

        Returns
        -------
        exists : bool
            Whether the target exists.
        """
    async def get(self, path, content: bool = True, type: Incomplete | None = None, format: Incomplete | None = None) -> None:
        """Get a file or directory model."""
    async def save(self, model, path) -> None:
        """
        Save a file or directory model to path.

        Should return the saved model with no content.  Save implementations
        should call self.run_pre_save_hook(model=model, path=path) prior to
        writing any data.
        """
    async def delete_file(self, path) -> None:
        """Delete the file or directory at path."""
    async def rename_file(self, old_path, new_path) -> None:
        """Rename a file or directory."""
    async def delete(self, path) -> None:
        """Delete a file/directory and any associated checkpoints."""
    async def rename(self, old_path, new_path) -> None:
        """Rename a file and any checkpoints associated with that file."""
    async def update(self, model, path):
        """Update the file's path

        For use in PATCH requests, to enable renaming a file without
        re-uploading its contents. Only used for renaming at the moment.
        """
    async def increment_filename(self, filename, path: str = '', insert: str = ''):
        """Increment a filename until it is unique.

        Parameters
        ----------
        filename : unicode
            The name of a file, including extension
        path : unicode
            The API path of the target's directory
        insert : unicode
            The characters to insert after the base filename

        Returns
        -------
        name : unicode
            A filename that is unique, based on the input filename.
        """
    async def new_untitled(self, path: str = '', type: str = '', ext: str = ''):
        """Create a new untitled file or directory in path

        path must be a directory

        File extension can be specified.

        Use `new` to create files with a fully specified path (including filename).
        """
    async def new(self, model: Incomplete | None = None, path: str = ''):
        """Create a new file or directory and return its model with no content.

        To create a new untitled entity in a directory, use `new_untitled`.
        """
    async def copy(self, from_path, to_path: Incomplete | None = None):
        """Copy an existing file and return its new model.

        If to_path not specified, it will be the parent directory of from_path.
        If to_path is a directory, filename will increment `from_path-Copy#.ext`.
        Considering multi-part extensions, the Copy# part will be placed before the first dot for all the extensions except `ipynb`.
        For easier manual searching in case of notebooks, the Copy# part will be placed before the last dot.

        from_path must be a full path to a file.
        """
    async def trust_notebook(self, path) -> None:
        """Explicitly trust a notebook

        Parameters
        ----------
        path : str
            The path of a notebook
        """
    async def create_checkpoint(self, path):
        """Create a checkpoint."""
    async def restore_checkpoint(self, checkpoint_id, path) -> None:
        """
        Restore a checkpoint.
        """
    async def list_checkpoints(self, path):
        """List the checkpoints for a path."""
    async def delete_checkpoint(self, checkpoint_id, path):
        """Delete a checkpoint for a path by id."""
