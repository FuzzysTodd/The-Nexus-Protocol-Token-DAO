from typing import Optional

__all__ = ['stop', 'restartPython', 'help']

def stop(detach: bool = True) -> None:
    """
    Stop the current session.
    
    :param detach: If detach is True, stop session from standard session,
                  or detach current notebook from high concurrency session;
                  if detach is False, stop session in any session. Default is True.
    """

def restartPython() -> None:
    """
    Restart the Python interpreter.
    Note: Not stable probably due to use spark reflection to call the method.
    If in reference run, it will only restart the Python interpreter in the current notebook.
    """

def help(method_name: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.session module or the specified method.

    Examples:
    notebookutils.session.help()
    notebookutils.session.help("stop")
    :param method_name: The name of the method to get help with.
    """
