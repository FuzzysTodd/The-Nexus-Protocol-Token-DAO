from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized
from jupyter_server.base.handlers import APIHandler as APIHandler, JupyterHandler as JupyterHandler, path_regex as path_regex
from jupyter_server.utils import url_escape as url_escape, url_path_join as url_path_join

AUTH_RESOURCE: str

def validate_model(model, expect_content) -> None:
    """
    Validate a model returned by a ContentsManager method.

    If expect_content is True, then we expect non-null entries for 'content'
    and 'format'.
    """

class ContentsAPIHandler(APIHandler):
    """A contents API handler."""
    auth_resource = AUTH_RESOURCE

class ContentsHandler(ContentsAPIHandler):
    """A contents handler."""
    def location_url(self, path):
        '''Return the full URL location of a file.

        Parameters
        ----------
        path : unicode
            The API path of the file, such as "foo/bar.txt".
        '''
    async def get(self, path: str = '') -> None:
        """Return a model for a file or directory.

        A directory model contains a list of models (without content)
        of the files and directories it contains.
        """
    async def patch(self, path: str = '') -> None:
        """PATCH renames a file or directory without re-uploading content."""
    async def post(self, path: str = '') -> None:
        '''Create a new file in the specified path.

        POST creates new files. The server always decides on the name.

        POST /api/contents/path
          New untitled, empty file or directory.
        POST /api/contents/path
          with body {"copy_from" : "/path/to/OtherNotebook.ipynb"}
          New copy of OtherNotebook in path
        '''
    async def put(self, path: str = '') -> None:
        """Saves the file in the location specified by name and path.

        PUT is very similar to POST, but the requester specifies the name,
        whereas with POST, the server picks the name.

        PUT /api/contents/path/Name.ipynb
          Save notebook at ``path/Name.ipynb``. Notebook structure is specified
          in `content` key of JSON request body. If content is not specified,
          create a new empty notebook.
        """
    async def delete(self, path: str = '') -> None:
        """delete a file in the given path"""

class CheckpointsHandler(ContentsAPIHandler):
    """A checkpoints API handler."""
    async def get(self, path: str = '') -> None:
        """get lists checkpoints for a file"""
    async def post(self, path: str = '') -> None:
        """post creates a new checkpoint"""

class ModifyCheckpointsHandler(ContentsAPIHandler):
    """A checkpoints modification handler."""
    async def post(self, path, checkpoint_id) -> None:
        """post restores a file from a checkpoint"""
    async def delete(self, path, checkpoint_id) -> None:
        """delete clears a checkpoint for a given file"""

class NotebooksRedirectHandler(JupyterHandler):
    """Redirect /api/notebooks to /api/contents"""
    SUPPORTED_METHODS: Incomplete
    def get(self, path) -> None:
        """Handle a notebooks redirect."""
    put = get
    patch = get
    post = get
    delete = get

class TrustNotebooksHandler(JupyterHandler):
    """Handles trust/signing of notebooks"""
    async def post(self, path: str = '') -> None:
        """Trust a notebook by path."""

default_handlers: Incomplete
