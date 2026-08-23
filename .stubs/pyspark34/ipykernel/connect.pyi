from ipykernel.kernelapp import IPKernelApp
from jupyter_client import write_connection_file as write_connection_file
from subprocess import Popen
from typing import Any

__all__ = ['write_connection_file', 'get_connection_file', 'get_connection_info', 'connect_qtconsole']

def get_connection_file(app: IPKernelApp | None = None) -> str:
    """Return the path to the connection file of an app

    Parameters
    ----------
    app : IPKernelApp instance [optional]
        If unspecified, the currently running app will be used
    """
def get_connection_info(connection_file: str | None = None, unpack: bool = False) -> str | dict[str, Any]:
    """Return the connection information for the current Kernel.

    Parameters
    ----------
    connection_file : str [optional]
        The connection file to be used. Can be given by absolute path, or
        IPython will search in the security directory.
        If run from IPython,

        If unspecified, the connection file for the currently running
        IPython Kernel will be used, which is only allowed from inside a kernel.

    unpack : bool [default: False]
        if True, return the unpacked dict, otherwise just the string contents
        of the file.

    Returns
    -------
    The connection dictionary of the current kernel, as string or dict,
    depending on `unpack`.
    """
def connect_qtconsole(connection_file: str | None = None, argv: list[str] | None = None) -> Popen:
    """Connect a qtconsole to the current kernel.

    This is useful for connecting a second qtconsole to a kernel, or to a
    local notebook.

    Parameters
    ----------
    connection_file : str [optional]
        The connection file to be used. Can be given by absolute path, or
        IPython will search in the security directory.
        If run from IPython,

        If unspecified, the connection file for the currently running
        IPython Kernel will be used, which is only allowed from inside a kernel.

    argv : list [optional]
        Any extra args to be passed to the console.

    Returns
    -------
    :class:`subprocess.Popen` instance running the qtconsole frontend
    """
