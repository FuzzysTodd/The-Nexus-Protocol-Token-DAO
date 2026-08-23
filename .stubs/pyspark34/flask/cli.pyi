import click
import os
import typing as t
from .app import Flask as Flask
from .globals import current_app as current_app
from .helpers import get_debug_flag as get_debug_flag, get_load_dotenv as get_load_dotenv
from _typeshed import Incomplete

class NoAppException(click.UsageError):
    """Raised if an application cannot be found or loaded."""

def find_best_app(module):
    """Given a module instance this tries to find the best possible
    application in the module or raises an exception.
    """
def find_app_by_string(module, app_name):
    """Check if the given string is a variable name or a function. Call
    a function to get the app instance, or return the variable directly.
    """
def prepare_import(path):
    """Given a filename this will try to calculate the python path, add it
    to the search path and return the actual module name that is expected.
    """
def locate_app(module_name, app_name, raise_if_not_found: bool = True): ...
def get_version(ctx, param, value) -> None: ...

version_option: Incomplete

class ScriptInfo:
    """Helper object to deal with Flask applications.  This is usually not
    necessary to interface with as it's used internally in the dispatching
    to click.  In future versions of Flask this object will most likely play
    a bigger role.  Typically it's created automatically by the
    :class:`FlaskGroup` but you can also manually create it and pass it
    onwards as click object.
    """
    app_import_path: Incomplete
    create_app: Incomplete
    data: Incomplete
    set_debug_flag: Incomplete
    def __init__(self, app_import_path: str | None = None, create_app: t.Callable[..., Flask] | None = None, set_debug_flag: bool = True) -> None: ...
    def load_app(self) -> Flask:
        """Loads the Flask app (if not yet loaded) and returns it.  Calling
        this multiple times will just result in the already loaded app to
        be returned.
        """

pass_script_info: Incomplete

def with_appcontext(f):
    """Wraps a callback so that it's guaranteed to be executed with the
    script's application context.

    Custom commands (and their options) registered under ``app.cli`` or
    ``blueprint.cli`` will always have an app context available, this
    decorator is not required in that case.

    .. versionchanged:: 2.2
        The app context is active for subcommands as well as the
        decorated callback. The app context is always available to
        ``app.cli`` command and parameter callbacks.
    """

class AppGroup(click.Group):
    """This works similar to a regular click :class:`~click.Group` but it
    changes the behavior of the :meth:`command` decorator so that it
    automatically wraps the functions in :func:`with_appcontext`.

    Not to be confused with :class:`FlaskGroup`.
    """
    def command(self, *args, **kwargs):
        """This works exactly like the method of the same name on a regular
        :class:`click.Group` but it wraps callbacks in :func:`with_appcontext`
        unless it's disabled by passing ``with_appcontext=False``.
        """
    def group(self, *args, **kwargs):
        """This works exactly like the method of the same name on a regular
        :class:`click.Group` but it defaults the group class to
        :class:`AppGroup`.
        """

class FlaskGroup(AppGroup):
    """Special subclass of the :class:`AppGroup` group that supports
    loading more commands from the configured Flask app.  Normally a
    developer does not have to interface with this class but there are
    some very advanced use cases for which it makes sense to create an
    instance of this. see :ref:`custom-scripts`.

    :param add_default_commands: if this is True then the default run and
        shell commands will be added.
    :param add_version_option: adds the ``--version`` option.
    :param create_app: an optional callback that is passed the script info and
        returns the loaded app.
    :param load_dotenv: Load the nearest :file:`.env` and :file:`.flaskenv`
        files to set environment variables. Will also change the working
        directory to the directory containing the first file found.
    :param set_debug_flag: Set the app's debug flag.

    .. versionchanged:: 2.2
        Added the ``-A/--app``, ``--debug/--no-debug``, ``-e/--env-file`` options.

    .. versionchanged:: 2.2
        An app context is pushed when running ``app.cli`` commands, so
        ``@with_appcontext`` is no longer required for those commands.

    .. versionchanged:: 1.0
        If installed, python-dotenv will be used to load environment variables
        from :file:`.env` and :file:`.flaskenv` files.
    """
    create_app: Incomplete
    load_dotenv: Incomplete
    set_debug_flag: Incomplete
    def __init__(self, add_default_commands: bool = True, create_app: t.Callable[..., Flask] | None = None, add_version_option: bool = True, load_dotenv: bool = True, set_debug_flag: bool = True, **extra: t.Any) -> None: ...
    def get_command(self, ctx, name): ...
    def list_commands(self, ctx): ...
    def make_context(self, info_name: str | None, args: list[str], parent: click.Context | None = None, **extra: t.Any) -> click.Context: ...
    def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]: ...

def load_dotenv(path: str | os.PathLike | None = None) -> bool:
    '''Load "dotenv" files in order of precedence to set environment variables.

    If an env var is already set it is not overwritten, so earlier files in the
    list are preferred over later files.

    This is a no-op if `python-dotenv`_ is not installed.

    .. _python-dotenv: https://github.com/theskumar/python-dotenv#readme

    :param path: Load the file at this location instead of searching.
    :return: ``True`` if a file was loaded.

    .. versionchanged:: 2.0
        The current directory is not changed to the location of the
        loaded file.

    .. versionchanged:: 2.0
        When loading the env files, set the default encoding to UTF-8.

    .. versionchanged:: 1.1.0
        Returns ``False`` when python-dotenv is not installed, or when
        the given path isn\'t a file.

    .. versionadded:: 1.0
    '''
def show_server_banner(debug, app_import_path) -> None:
    """Show extra startup messages the first time the server is run,
    ignoring the reloader.
    """

class CertParamType(click.ParamType):
    """Click option type for the ``--cert`` option. Allows either an
    existing file, the string ``'adhoc'``, or an import for a
    :class:`~ssl.SSLContext` object.
    """
    name: str
    path_type: Incomplete
    def __init__(self) -> None: ...
    def convert(self, value, param, ctx): ...

class SeparatedPathType(click.Path):
    """Click option type that accepts a list of values separated by the
    OS's path separator (``:``, ``;`` on Windows). Each value is
    validated as a :class:`click.Path` type.
    """
    def convert(self, value, param, ctx): ...

def run_command(info, host, port, reload, debugger, with_threads, cert, extra_files, exclude_patterns) -> None:
    """Run a local development server.

    This server is for development purposes only. It does not provide
    the stability, security, or performance of production WSGI servers.

    The reloader and debugger are enabled by default with the '--debug'
    option.
    """
def shell_command() -> None:
    """Run an interactive Python shell in the context of a given
    Flask application.  The application will populate the default
    namespace of this shell according to its configuration.

    This is useful for executing small snippets of management code
    without having to manually configure the application.
    """
def routes_command(sort: str, all_methods: bool) -> None:
    """Show all registered routes with endpoints and methods."""

cli: Incomplete

def main() -> None: ...
