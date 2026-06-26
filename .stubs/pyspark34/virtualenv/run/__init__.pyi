from _typeshed import Incomplete

__all__ = ['cli_run', 'session_via_cli']

def cli_run(args, options: Incomplete | None = None, setup_logging: bool = True, env: Incomplete | None = None):
    """
    Create a virtual environment given some command line interface arguments.

    :param args: the command line arguments
    :param options: passing in a ``VirtualEnvOptions`` object allows return of the parsed options
    :param setup_logging: ``True`` if setup logging handlers, ``False`` to use handlers already registered
    :param env: environment variables to use
    :return: the session object of the creation (its structure for now is experimental and might change on short notice)
    """
def session_via_cli(args, options: Incomplete | None = None, setup_logging: bool = True, env: Incomplete | None = None):
    """
    Create a virtualenv session (same as cli_run, but this does not perform the creation). Use this if you just want to
    query what the virtual environment would look like, but not actually create it.

    :param args: the command line arguments
    :param options: passing in a ``VirtualEnvOptions`` object allows return of the parsed options
    :param setup_logging: ``True`` if setup logging handlers, ``False`` to use handlers already registered
    :param env: environment variables to use
    :return: the session object of the creation (its structure for now is experimental and might change on short notice)
    """
