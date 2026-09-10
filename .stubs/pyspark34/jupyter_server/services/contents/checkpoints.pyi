from traitlets.config.configurable import LoggingConfigurable

class Checkpoints(LoggingConfigurable):
    """
    Base class for managing checkpoints for a ContentsManager.

    Subclasses are required to implement:

    create_checkpoint(self, contents_mgr, path)
    restore_checkpoint(self, contents_mgr, checkpoint_id, path)
    rename_checkpoint(self, checkpoint_id, old_path, new_path)
    delete_checkpoint(self, checkpoint_id, path)
    list_checkpoints(self, path)
    """
    def create_checkpoint(self, contents_mgr, path) -> None:
        """Create a checkpoint."""
    def restore_checkpoint(self, contents_mgr, checkpoint_id, path) -> None:
        """Restore a checkpoint"""
    def rename_checkpoint(self, checkpoint_id, old_path, new_path) -> None:
        """Rename a single checkpoint from old_path to new_path."""
    def delete_checkpoint(self, checkpoint_id, path) -> None:
        """delete a checkpoint for a file"""
    def list_checkpoints(self, path) -> None:
        """Return a list of checkpoints for a given file"""
    def rename_all_checkpoints(self, old_path, new_path) -> None:
        """Rename all checkpoints for old_path to new_path."""
    def delete_all_checkpoints(self, path) -> None:
        """Delete all checkpoints for the given path."""

class GenericCheckpointsMixin:
    """
    Helper for creating Checkpoints subclasses that can be used with any
    ContentsManager.

    Provides a ContentsManager-agnostic implementation of `create_checkpoint`
    and `restore_checkpoint` in terms of the following operations:

    - create_file_checkpoint(self, content, format, path)
    - create_notebook_checkpoint(self, nb, path)
    - get_file_checkpoint(self, checkpoint_id, path)
    - get_notebook_checkpoint(self, checkpoint_id, path)

    To create a generic CheckpointManager, add this mixin to a class that
    implement the above four methods plus the remaining Checkpoints API
    methods:

    - delete_checkpoint(self, checkpoint_id, path)
    - list_checkpoints(self, path)
    - rename_checkpoint(self, checkpoint_id, old_path, new_path)
    """
    def create_checkpoint(self, contents_mgr, path): ...
    def restore_checkpoint(self, contents_mgr, checkpoint_id, path) -> None:
        """Restore a checkpoint."""
    def create_file_checkpoint(self, content, format, path) -> None:
        """Create a checkpoint of the current state of a file

        Returns a checkpoint model for the new checkpoint.
        """
    def create_notebook_checkpoint(self, nb, path) -> None:
        """Create a checkpoint of the current state of a file

        Returns a checkpoint model for the new checkpoint.
        """
    def get_file_checkpoint(self, checkpoint_id, path) -> None:
        """Get the content of a checkpoint for a non-notebook file.

        Returns a dict of the form::

            {
                'type': 'file',
                'content': <str>,
                'format': {'text','base64'},
            }
        """
    def get_notebook_checkpoint(self, checkpoint_id, path) -> None:
        """Get the content of a checkpoint for a notebook.

        Returns a dict of the form::

            {
                'type': 'notebook',
                'content': <output of nbformat.read>,
            }
        """

class AsyncCheckpoints(Checkpoints):
    """
    Base class for managing checkpoints for a ContentsManager asynchronously.
    """
    async def create_checkpoint(self, contents_mgr, path) -> None:
        """Create a checkpoint."""
    async def restore_checkpoint(self, contents_mgr, checkpoint_id, path) -> None:
        """Restore a checkpoint"""
    async def rename_checkpoint(self, checkpoint_id, old_path, new_path) -> None:
        """Rename a single checkpoint from old_path to new_path."""
    async def delete_checkpoint(self, checkpoint_id, path) -> None:
        """delete a checkpoint for a file"""
    async def list_checkpoints(self, path) -> None:
        """Return a list of checkpoints for a given file"""
    async def rename_all_checkpoints(self, old_path, new_path) -> None:
        """Rename all checkpoints for old_path to new_path."""
    async def delete_all_checkpoints(self, path) -> None:
        """Delete all checkpoints for the given path."""

class AsyncGenericCheckpointsMixin(GenericCheckpointsMixin):
    """
    Helper for creating Asynchronous Checkpoints subclasses that can be used with any
    ContentsManager.
    """
    async def create_checkpoint(self, contents_mgr, path): ...
    async def restore_checkpoint(self, contents_mgr, checkpoint_id, path) -> None:
        """Restore a checkpoint."""
    async def create_file_checkpoint(self, content, format, path) -> None:
        """Create a checkpoint of the current state of a file

        Returns a checkpoint model for the new checkpoint.
        """
    async def create_notebook_checkpoint(self, nb, path) -> None:
        """Create a checkpoint of the current state of a file

        Returns a checkpoint model for the new checkpoint.
        """
    async def get_file_checkpoint(self, checkpoint_id, path) -> None:
        """Get the content of a checkpoint for a non-notebook file.

        Returns a dict of the form::

            {
                'type': 'file',
                'content': <str>,
                'format': {'text','base64'},
            }
        """
    async def get_notebook_checkpoint(self, checkpoint_id, path) -> None:
        """Get the content of a checkpoint for a notebook.

        Returns a dict of the form::

            {
                'type': 'notebook',
                'content': <output of nbformat.read>,
            }
        """
