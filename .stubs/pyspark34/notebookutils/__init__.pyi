from notebookutils.mssparkutils.handlers import RuntimeHandler
from notebookutils import (
    data, fs, lakehouse, notebook, session, credentials, udf, conf, 
    variableLibrary, connections
)

__all__ = [
    'data', 'fs', 'lakehouse', 'notebook', 'session', 'credentials', 
    'udf', 'conf', 'variableLibrary', 'connections', 'runtime', 
    'help'
]

__version__: str

runtime: RuntimeHandler

def help(module_name: str = '') -> None:
    """
    Provides help for the notebookutils module or the specified method.

    Examples:
    notebookutils.help()
    notebookutils.help("fs")
    :param module_name: The name of the module to get help with.
    """

nbResPath: str
