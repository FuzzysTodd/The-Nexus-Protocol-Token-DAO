from . import piping
from _typeshed import Incomplete

__all__ = ['JUPYTER_FORMATS', 'SUPPORTED_JUPYTER_FORMATS', 'DEFAULT_JUPYTER_FORMAT', 'get_jupyter_format_mimetype', 'JupyterIntegration']

JUPYTER_FORMATS: Incomplete
SUPPORTED_JUPYTER_FORMATS: Incomplete
DEFAULT_JUPYTER_FORMAT: Incomplete

def get_jupyter_format_mimetype(jupyter_format: str) -> str: ...

class JupyterIntegration(piping.Pipe):
    """Display rendered graph as SVG in Jupyter Notebooks and QtConsole."""
