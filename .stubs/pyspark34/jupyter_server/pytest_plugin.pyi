from _typeshed import Incomplete
from jupyter_server.services.contents.filemanager import AsyncFileContentsManager as AsyncFileContentsManager
from jupyter_server.services.contents.largefilemanager import AsyncLargeFileManager as AsyncLargeFileManager

pytest_plugins: Incomplete
some_resource: str
sample_kernel_json: Incomplete

def jp_kernelspecs(jp_data_dir) -> None:
    """Configures some sample kernelspecs in the Jupyter data directory."""
def jp_contents_manager(request, tmp_path):
    """Returns an AsyncFileContentsManager instance based on the use_atomic_writing parameter value."""
def jp_large_contents_manager(tmp_path):
    """Returns an AsyncLargeFileManager instance."""
