import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from tensorboard import manager as manager, version as version
from tensorboard.backend import application as application
from tensorboard.data import server_ingester as server_ingester
from tensorboard.plugins.core import core_plugin as core_plugin
from tensorboard.util import tb_logging as tb_logging
from werkzeug import serving

logger: Incomplete

class TensorBoard:
    """Class for running TensorBoard.

    Fields:
      plugin_loaders: Set from plugins passed to constructor.
      assets_zip_provider: Set by constructor.
      server_class: Set by constructor.
      flags: An argparse.Namespace set by the configure() method.
      cache_key: As `manager.cache_key`; set by the configure() method.
    """
    plugin_loaders: Incomplete
    assets_zip_provider: Incomplete
    server_class: Incomplete
    subcommands: Incomplete
    flags: Incomplete
    def __init__(self, plugins: Incomplete | None = None, assets_zip_provider: Incomplete | None = None, server_class: Incomplete | None = None, subcommands: Incomplete | None = None) -> None:
        """Creates new instance.

        Args:
          plugins: A list of TensorBoard plugins to load, as TBPlugin classes or
            TBLoader instances or classes. If not specified, defaults to first-party
            plugins.
          assets_zip_provider: A function that provides a zip file containing
            assets to the application. If `None`, the default TensorBoard web
            assets will be used. (If building from source, your binary must
            explicitly depend on `//tensorboard:assets_lib` if you pass `None`.)
          server_class: An optional factory for a `TensorBoardServer` to use
            for serving the TensorBoard WSGI app. If provided, its callable
            signature should match that of `TensorBoardServer.__init__`.

        :type plugins:
          list[
            base_plugin.TBLoader | Type[base_plugin.TBLoader] |
            Type[base_plugin.TBPlugin]
          ]
        """
    cache_key: Incomplete
    def configure(self, argv=('',), **kwargs):
        '''Configures TensorBoard behavior via flags.

        This method will populate the "flags" property with an argparse.Namespace
        representing flag values parsed from the provided argv list, overridden by
        explicit flags from remaining keyword arguments.

        Args:
          argv: Can be set to CLI args equivalent to sys.argv; the first arg is
            taken to be the name of the path being executed.
          kwargs: Additional arguments will override what was parsed from
            argv. They must be passed as Python data structures, e.g.
            `foo=1` rather than `foo="1"`.

        Returns:
          Either argv[:1] if argv was non-empty, or [\'\'] otherwise, as a mechanism
          for absl.app.run() compatibility.

        Raises:
          ValueError: If flag values are invalid.
        '''
    def main(self, ignored_argv=('',)):
        """Blocking main function for TensorBoard.

        This method is called by `tensorboard.main.run_main`, which is the
        standard entrypoint for the tensorboard command line program. The
        configure() method must be called first.

        Args:
          ignored_argv: Do not pass. Required for Abseil compatibility.

        Returns:
          Process exit code, i.e. 0 if successful or non-zero on failure. In
          practice, an exception will most likely be raised instead of
          returning non-zero.

        :rtype: int
        """
    def launch(self):
        """Python API for launching TensorBoard.

        This method is the same as main() except it launches TensorBoard in
        a separate permanent thread. The configure() method must be called
        first.

        Returns:
          The URL of the TensorBoard web server.

        :rtype: str
        """

class TensorBoardSubcommand(metaclass=ABCMeta):
    """Experimental private API for defining subcommands to tensorboard(1)."""
    @abstractmethod
    def name(self):
        """Name of this subcommand, as specified on the command line.

        This must be unique across all subcommands.

        Returns:
          A string.
        """
    @abstractmethod
    def define_flags(self, parser):
        """Configure an argument parser for this subcommand.

        Flags whose names start with two underscores (e.g., `__foo`) are
        reserved for use by the runtime and must not be defined by
        subcommands.

        Args:
          parser: An `argparse.ArgumentParser` scoped to this subcommand,
            which this function should mutate.
        """
    @abstractmethod
    def run(self, flags):
        """Execute this subcommand with user-provided flags.

        Args:
          flags: An `argparse.Namespace` object with all defined flags.

        Returns:
          An `int` exit code, or `None` as an alias for `0`.
        """
    def help(self) -> None:
        """Short, one-line help text to display on `tensorboard --help`."""
    def description(self) -> None:
        """Description to display on `tensorboard SUBCOMMAND --help`."""

class TensorBoardServer(metaclass=ABCMeta):
    """Class for customizing TensorBoard WSGI app serving."""
    @abstractmethod
    def __init__(self, wsgi_app, flags):
        """Create a flag-configured HTTP server for TensorBoard's WSGI app.

        Args:
          wsgi_app: The TensorBoard WSGI application to create a server for.
          flags: argparse.Namespace instance of TensorBoard flags.
        """
    @abstractmethod
    def serve_forever(self):
        """Blocking call to start serving the TensorBoard server."""
    @abstractmethod
    def get_url(self):
        """Returns a URL at which this server should be reachable."""
    def print_serving_message(self) -> None:
        """Prints a user-friendly message prior to server start.

        This will be called just before `serve_forever`.
        """

class TensorBoardServerException(Exception):
    """Exception raised by TensorBoardServer for user-friendly errors.

    Subclasses of TensorBoardServer can raise this exception in order to
    generate a clean error message for the user rather than a
    stacktrace.
    """
    msg: Incomplete
    def __init__(self, msg) -> None: ...

class TensorBoardPortInUseError(TensorBoardServerException):
    """Error raised when attempting to bind to a port that is in use.

    This should be raised when it is expected that binding to another
    similar port would succeed. It is used as a signal to indicate that
    automatic port searching should continue rather than abort.
    """

def with_port_scanning(cls):
    """Create a server factory that performs port scanning.

    This function returns a callable whose signature matches the
    specification of `TensorBoardServer.__init__`, using `cls` as an
    underlying implementation. It passes through `flags` unchanged except
    in the case that `flags.port is None`, in which case it repeatedly
    instantiates the underlying server with new port suggestions.

    Args:
      cls: A valid implementation of `TensorBoardServer`. This class's
        initializer should raise a `TensorBoardPortInUseError` upon
        failing to bind to a port when it is expected that binding to
        another nearby port might succeed.

        The initializer for `cls` will only ever be invoked with `flags`
        such that `flags.port is not None`.

    Returns:
      A function that implements the `__init__` contract of
      `TensorBoardServer`.
    """

class _WSGIRequestHandler(serving.WSGIRequestHandler):
    """Custom subclass of Werkzeug request handler to use HTTP/1.1."""
    protocol_version: str

class WerkzeugServer(serving.ThreadedWSGIServer, TensorBoardServer, metaclass=abc.ABCMeta):
    """Implementation of TensorBoardServer using the Werkzeug dev server."""
    daemon_threads: bool
    def __init__(self, wsgi_app, flags) -> None: ...
    def server_bind(self) -> None:
        """Override to set custom options on the socket."""
    def handle_error(self, request, client_address) -> None:
        """Override to get rid of noisy EPIPE errors."""
    def get_url(self): ...
    def print_serving_message(self) -> None: ...

create_port_scanning_werkzeug_server: Incomplete
