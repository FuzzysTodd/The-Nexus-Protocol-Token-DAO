from .checkpoints import AsyncCheckpoints as AsyncCheckpoints, AsyncGenericCheckpointsMixin as AsyncGenericCheckpointsMixin, Checkpoints as Checkpoints, GenericCheckpointsMixin as GenericCheckpointsMixin
from .fileio import AsyncFileManagerMixin as AsyncFileManagerMixin, FileManagerMixin as FileManagerMixin
from _typeshed import Incomplete

class FileCheckpoints(FileManagerMixin, Checkpoints):
    """
    A Checkpoints that caches checkpoints for files in adjacent
    directories.

    Only works with FileContentsManager.  Use GenericFileCheckpoints if
    you want file-based checkpoints with another ContentsManager.
    """
    checkpoint_dir: Incomplete
    root_dir: Incomplete
    def create_checkpoint(self, contents_mgr, path):
        """Create a checkpoint."""
    def restore_checkpoint(self, contents_mgr, checkpoint_id, path) -> None:
        """Restore a checkpoint."""
    def rename_checkpoint(self, checkpoint_id, old_path, new_path) -> None:
        """Rename a checkpoint from old_path to new_path."""
    def delete_checkpoint(self, checkpoint_id, path) -> None:
        """delete a file's checkpoint"""
    def list_checkpoints(self, path):
        """list the checkpoints for a given file

        This contents manager currently only supports one checkpoint per file.
        """
    def checkpoint_path(self, checkpoint_id, path):
        """find the path to a checkpoint"""
    def checkpoint_model(self, checkpoint_id, os_path):
        """construct the info dict for a given checkpoint"""
    def no_such_checkpoint(self, path, checkpoint_id) -> None: ...

class AsyncFileCheckpoints(FileCheckpoints, AsyncFileManagerMixin, AsyncCheckpoints):
    async def create_checkpoint(self, contents_mgr, path):
        """Create a checkpoint."""
    async def restore_checkpoint(self, contents_mgr, checkpoint_id, path) -> None:
        """Restore a checkpoint."""
    async def checkpoint_model(self, checkpoint_id, os_path):
        """construct the info dict for a given checkpoint"""
    async def rename_checkpoint(self, checkpoint_id, old_path, new_path) -> None:
        """Rename a checkpoint from old_path to new_path."""
    async def delete_checkpoint(self, checkpoint_id, path) -> None:
        """delete a file's checkpoint"""
    async def list_checkpoints(self, path):
        """list the checkpoints for a given file

        This contents manager currently only supports one checkpoint per file.
        """

class GenericFileCheckpoints(GenericCheckpointsMixin, FileCheckpoints):
    """
    Local filesystem Checkpoints that works with any conforming
    ContentsManager.
    """
    def create_file_checkpoint(self, content, format, path):
        """Create a checkpoint from the current content of a file."""
    def create_notebook_checkpoint(self, nb, path):
        """Create a checkpoint from the current content of a notebook."""
    def get_notebook_checkpoint(self, checkpoint_id, path):
        """Get a checkpoint for a notebook."""
    def get_file_checkpoint(self, checkpoint_id, path):
        """Get a checkpoint for a file."""

class AsyncGenericFileCheckpoints(AsyncGenericCheckpointsMixin, AsyncFileCheckpoints):
    """
    Asynchronous Local filesystem Checkpoints that works with any conforming
    ContentsManager.
    """
    async def create_file_checkpoint(self, content, format, path):
        """Create a checkpoint from the current content of a file."""
    async def create_notebook_checkpoint(self, nb, path):
        """Create a checkpoint from the current content of a notebook."""
    async def get_notebook_checkpoint(self, checkpoint_id, path):
        """Get a checkpoint for a notebook."""
    async def get_file_checkpoint(self, checkpoint_id, path):
        """Get a checkpoint for a file."""
