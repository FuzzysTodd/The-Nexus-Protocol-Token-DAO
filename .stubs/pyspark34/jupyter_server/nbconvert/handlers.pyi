from ..base.handlers import FilesRedirectHandler as FilesRedirectHandler, JupyterHandler as JupyterHandler, path_regex as path_regex
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized

AUTH_RESOURCE: str
date_format: str

def find_resource_files(output_files_dir):
    """Find the resource files in a directory."""
def respond_zip(handler, name, output, resources):
    """Zip up the output and resource files and respond with the zip file.

    Returns True if it has served a zip file, False if there are no resource
    files, in which case we serve the plain output file.
    """
def get_exporter(format, **kwargs):
    """get an exporter, raising appropriate errors"""

class NbconvertFileHandler(JupyterHandler):
    """An nbconvert file handler."""
    auth_resource = AUTH_RESOURCE
    SUPPORTED_METHODS: Incomplete
    async def get(self, format, path):
        """Get a notebook file in a desired format."""

class NbconvertPostHandler(JupyterHandler):
    """An nbconvert post handler."""
    SUPPORTED_METHODS: Incomplete
    auth_resource = AUTH_RESOURCE
    async def post(self, format):
        """Convert a notebook file to a desired format."""

default_handlers: Incomplete
