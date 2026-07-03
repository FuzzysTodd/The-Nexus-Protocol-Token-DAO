from jupyter_server.services.contents.filemanager import AsyncFileContentsManager as AsyncFileContentsManager, FileContentsManager as FileContentsManager

class LargeFileManager(FileContentsManager):
    """Handle large file upload."""
    def save(self, model, path: str = ''):
        """Save the file model and return the model with no content."""

class AsyncLargeFileManager(AsyncFileContentsManager):
    """Handle large file upload asynchronously"""
    async def save(self, model, path: str = ''):
        """Save the file model and return the model with no content."""
