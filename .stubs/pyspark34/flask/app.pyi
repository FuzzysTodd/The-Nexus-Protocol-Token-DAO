import os
import typing as t
from . import cli as cli, typing as ft
from .ctx import AppContext as AppContext, RequestContext as RequestContext
from .globals import current_app as current_app, g as g, request as request, request_ctx as request_ctx, session as session
from .helpers import get_debug_flag as get_debug_flag, get_flashed_messages as get_flashed_messages, get_load_dotenv as get_load_dotenv, send_from_directory as send_from_directory
from .sansio.app import App as App
from .sessions import SecureCookieSessionInterface as SecureCookieSessionInterface, SessionInterface as SessionInterface
from .signals import appcontext_tearing_down as appcontext_tearing_down, got_request_exception as got_request_exception, request_finished as request_finished, request_started as request_started, request_tearing_down as request_tearing_down
from .templating import Environment as Environment
from .testing import FlaskCliRunner as FlaskCliRunner, FlaskClient as FlaskClient
from .wrappers import Request as Request, Response as Response
from _typeshed import Incomplete
from types import TracebackType
from werkzeug.exceptions import HTTPException
from werkzeug.routing import MapAdapter as MapAdapter, Rule as Rule

T_shell_context_processor = t.TypeVar('T_shell_context_processor', bound=ft.ShellContextProcessorCallable)
T_teardown = t.TypeVar('T_teardown', bound=ft.TeardownCallable)
T_template_filter = t.TypeVar('T_template_filter', bound=ft.TemplateFilterCallable)
T_template_global = t.TypeVar('T_template_global', bound=ft.TemplateGlobalCallable)
T_template_test = t.TypeVar('T_template_test', bound=ft.TemplateTestCallable)

class Flask(App):
    """The flask object implements a WSGI application and acts as the central
    object.  It is passed the name of the module or package of the
    application.  Once it is created it will act as a central registry for
    the view functions, the URL rules, template configuration and much more.

    The name of the package is used to resolve resources from inside the
    package or the folder the module is contained in depending on if the
    package parameter resolves to an actual python package (a folder with
    an :file:`__init__.py` file inside) or a standard module (just a ``.py`` file).

    For more information about resource loading, see :func:`open_resource`.

    Usually you create a :class:`Flask` instance in your main module or
    in the :file:`__init__.py` file of your package like this::

        from flask import Flask
        app = Flask(__name__)

    .. admonition:: About the First Parameter

        The idea of the first parameter is to give Flask an idea of what
        belongs to your application.  This name is used to find resources
        on the filesystem, can be used by extensions to improve debugging
        information and a lot more.

        So it's important what you provide there.  If you are using a single
        module, `__name__` is always the correct value.  If you however are
        using a package, it's usually recommended to hardcode the name of
        your package there.

        For example if your application is defined in :file:`yourapplication/app.py`
        you should create it with one of the two versions below::

            app = Flask('yourapplication')
            app = Flask(__name__.split('.')[0])

        Why is that?  The application will work even with `__name__`, thanks
        to how resources are looked up.  However it will make debugging more
        painful.  Certain extensions can make assumptions based on the
        import name of your application.  For example the Flask-SQLAlchemy
        extension will look for the code in your application that triggered
        an SQL query in debug mode.  If the import name is not properly set
        up, that debugging information is lost.  (For example it would only
        pick up SQL queries in `yourapplication.app` and not
        `yourapplication.views.frontend`)

    .. versionadded:: 0.7
       The `static_url_path`, `static_folder`, and `template_folder`
       parameters were added.

    .. versionadded:: 0.8
       The `instance_path` and `instance_relative_config` parameters were
       added.

    .. versionadded:: 0.11
       The `root_path` parameter was added.

    .. versionadded:: 1.0
       The ``host_matching`` and ``static_host`` parameters were added.

    .. versionadded:: 1.0
       The ``subdomain_matching`` parameter was added. Subdomain
       matching needs to be enabled manually now. Setting
       :data:`SERVER_NAME` does not implicitly enable it.

    :param import_name: the name of the application package
    :param static_url_path: can be used to specify a different path for the
                            static files on the web.  Defaults to the name
                            of the `static_folder` folder.
    :param static_folder: The folder with static files that is served at
        ``static_url_path``. Relative to the application ``root_path``
        or an absolute path. Defaults to ``'static'``.
    :param static_host: the host to use when adding the static route.
        Defaults to None. Required when using ``host_matching=True``
        with a ``static_folder`` configured.
    :param host_matching: set ``url_map.host_matching`` attribute.
        Defaults to False.
    :param subdomain_matching: consider the subdomain relative to
        :data:`SERVER_NAME` when matching routes. Defaults to False.
    :param template_folder: the folder that contains the templates that should
                            be used by the application.  Defaults to
                            ``'templates'`` folder in the root path of the
                            application.
    :param instance_path: An alternative instance path for the application.
                          By default the folder ``'instance'`` next to the
                          package or module is assumed to be the instance
                          path.
    :param instance_relative_config: if set to ``True`` relative filenames
                                     for loading the config are assumed to
                                     be relative to the instance path instead
                                     of the application root.
    :param root_path: The path to the root of the application files.
        This should only be set manually when it can't be detected
        automatically, such as for namespace packages.
    """
    default_config: Incomplete
    request_class = Request
    response_class = Response
    session_interface: SessionInterface
    def __init__(self, import_name: str, static_url_path: str | None = None, static_folder: str | os.PathLike | None = 'static', static_host: str | None = None, host_matching: bool = False, subdomain_matching: bool = False, template_folder: str | os.PathLike | None = 'templates', instance_path: str | None = None, instance_relative_config: bool = False, root_path: str | None = None) -> None: ...
    def get_send_file_max_age(self, filename: str | None) -> int | None:
        """Used by :func:`send_file` to determine the ``max_age`` cache
        value for a given file path if it wasn't passed.

        By default, this returns :data:`SEND_FILE_MAX_AGE_DEFAULT` from
        the configuration of :data:`~flask.current_app`. This defaults
        to ``None``, which tells the browser to use conditional requests
        instead of a timed cache, which is usually preferable.

        Note this is a duplicate of the same method in the Flask
        class.

        .. versionchanged:: 2.0
            The default configuration is ``None`` instead of 12 hours.

        .. versionadded:: 0.9
        """
    def send_static_file(self, filename: str) -> Response:
        """The view function used to serve files from
        :attr:`static_folder`. A route is automatically registered for
        this view at :attr:`static_url_path` if :attr:`static_folder` is
        set.

        Note this is a duplicate of the same method in the Flask
        class.

        .. versionadded:: 0.5

        """
    def open_resource(self, resource: str, mode: str = 'rb') -> t.IO[t.AnyStr]:
        '''Open a resource file relative to :attr:`root_path` for
        reading.

        For example, if the file ``schema.sql`` is next to the file
        ``app.py`` where the ``Flask`` app is defined, it can be opened
        with:

        .. code-block:: python

            with app.open_resource("schema.sql") as f:
                conn.executescript(f.read())

        :param resource: Path to the resource relative to
            :attr:`root_path`.
        :param mode: Open the file in this mode. Only reading is
            supported, valid values are "r" (or "rt") and "rb".

        Note this is a duplicate of the same method in the Flask
        class.

        '''
    def open_instance_resource(self, resource: str, mode: str = 'rb') -> t.IO[t.AnyStr]:
        """Opens a resource from the application's instance folder
        (:attr:`instance_path`).  Otherwise works like
        :meth:`open_resource`.  Instance resources can also be opened for
        writing.

        :param resource: the name of the resource.  To access resources within
                         subfolders use forward slashes as separator.
        :param mode: resource file opening mode, default is 'rb'.
        """
    def create_jinja_environment(self) -> Environment:
        """Create the Jinja environment based on :attr:`jinja_options`
        and the various Jinja-related methods of the app. Changing
        :attr:`jinja_options` after this will have no effect. Also adds
        Flask-related globals and filters to the environment.

        .. versionchanged:: 0.11
           ``Environment.auto_reload`` set in accordance with
           ``TEMPLATES_AUTO_RELOAD`` configuration option.

        .. versionadded:: 0.5
        """
    def create_url_adapter(self, request: Request | None) -> MapAdapter | None:
        """Creates a URL adapter for the given request. The URL adapter
        is created at a point where the request context is not yet set
        up so the request is passed explicitly.

        .. versionadded:: 0.6

        .. versionchanged:: 0.9
           This can now also be called without a request object when the
           URL adapter is created for the application context.

        .. versionchanged:: 1.0
            :data:`SERVER_NAME` no longer implicitly enables subdomain
            matching. Use :attr:`subdomain_matching` instead.
        """
    def raise_routing_exception(self, request: Request) -> t.NoReturn:
        """Intercept routing exceptions and possibly do something else.

        In debug mode, intercept a routing redirect and replace it with
        an error if the body will be discarded.

        With modern Werkzeug this shouldn't occur, since it now uses a
        308 status which tells the browser to resend the method and
        body.

        .. versionchanged:: 2.1
            Don't intercept 307 and 308 redirects.

        :meta private:
        :internal:
        """
    def update_template_context(self, context: dict) -> None:
        """Update the template context with some commonly used variables.
        This injects request, session, config and g into the template
        context as well as everything template context processors want
        to inject.  Note that the as of Flask 0.6, the original values
        in the context will not be overridden if a context processor
        decides to return a value with the same key.

        :param context: the context as a dictionary that is updated in place
                        to add extra variables.
        """
    def make_shell_context(self) -> dict:
        """Returns the shell context for an interactive shell for this
        application.  This runs all the registered shell context
        processors.

        .. versionadded:: 0.11
        """
    debug: Incomplete
    def run(self, host: str | None = None, port: int | None = None, debug: bool | None = None, load_dotenv: bool = True, **options: t.Any) -> None:
        """Runs the application on a local development server.

        Do not use ``run()`` in a production setting. It is not intended to
        meet security and performance requirements for a production server.
        Instead, see :doc:`/deploying/index` for WSGI server recommendations.

        If the :attr:`debug` flag is set the server will automatically reload
        for code changes and show a debugger in case an exception happened.

        If you want to run the application in debug mode, but disable the
        code execution on the interactive debugger, you can pass
        ``use_evalex=False`` as parameter.  This will keep the debugger's
        traceback screen active, but disable code execution.

        It is not recommended to use this function for development with
        automatic reloading as this is badly supported.  Instead you should
        be using the :command:`flask` command line script's ``run`` support.

        .. admonition:: Keep in Mind

           Flask will suppress any server error with a generic error page
           unless it is in debug mode.  As such to enable just the
           interactive debugger without the code reloading, you have to
           invoke :meth:`run` with ``debug=True`` and ``use_reloader=False``.
           Setting ``use_debugger`` to ``True`` without being in debug mode
           won't catch any exceptions because there won't be any to
           catch.

        :param host: the hostname to listen on. Set this to ``'0.0.0.0'`` to
            have the server available externally as well. Defaults to
            ``'127.0.0.1'`` or the host in the ``SERVER_NAME`` config variable
            if present.
        :param port: the port of the webserver. Defaults to ``5000`` or the
            port defined in the ``SERVER_NAME`` config variable if present.
        :param debug: if given, enable or disable debug mode. See
            :attr:`debug`.
        :param load_dotenv: Load the nearest :file:`.env` and :file:`.flaskenv`
            files to set environment variables. Will also change the working
            directory to the directory containing the first file found.
        :param options: the options to be forwarded to the underlying Werkzeug
            server. See :func:`werkzeug.serving.run_simple` for more
            information.

        .. versionchanged:: 1.0
            If installed, python-dotenv will be used to load environment
            variables from :file:`.env` and :file:`.flaskenv` files.

            The :envvar:`FLASK_DEBUG` environment variable will override :attr:`debug`.

            Threaded mode is enabled by default.

        .. versionchanged:: 0.10
            The default port is now picked from the ``SERVER_NAME``
            variable.
        """
    def test_client(self, use_cookies: bool = True, **kwargs: t.Any) -> FlaskClient:
        '''Creates a test client for this application.  For information
        about unit testing head over to :doc:`/testing`.

        Note that if you are testing for assertions or exceptions in your
        application code, you must set ``app.testing = True`` in order for the
        exceptions to propagate to the test client.  Otherwise, the exception
        will be handled by the application (not visible to the test client) and
        the only indication of an AssertionError or other exception will be a
        500 status code response to the test client.  See the :attr:`testing`
        attribute.  For example::

            app.testing = True
            client = app.test_client()

        The test client can be used in a ``with`` block to defer the closing down
        of the context until the end of the ``with`` block.  This is useful if
        you want to access the context locals for testing::

            with app.test_client() as c:
                rv = c.get(\'/?vodka=42\')
                assert request.args[\'vodka\'] == \'42\'

        Additionally, you may pass optional keyword arguments that will then
        be passed to the application\'s :attr:`test_client_class` constructor.
        For example::

            from flask.testing import FlaskClient

            class CustomClient(FlaskClient):
                def __init__(self, *args, **kwargs):
                    self._authentication = kwargs.pop("authentication")
                    super(CustomClient,self).__init__( *args, **kwargs)

            app.test_client_class = CustomClient
            client = app.test_client(authentication=\'Basic ....\')

        See :class:`~flask.testing.FlaskClient` for more information.

        .. versionchanged:: 0.4
           added support for ``with`` block usage for the client.

        .. versionadded:: 0.7
           The `use_cookies` parameter was added as well as the ability
           to override the client to be used by setting the
           :attr:`test_client_class` attribute.

        .. versionchanged:: 0.11
           Added `**kwargs` to support passing additional keyword arguments to
           the constructor of :attr:`test_client_class`.
        '''
    def test_cli_runner(self, **kwargs: t.Any) -> FlaskCliRunner:
        """Create a CLI runner for testing CLI commands.
        See :ref:`testing-cli`.

        Returns an instance of :attr:`test_cli_runner_class`, by default
        :class:`~flask.testing.FlaskCliRunner`. The Flask app object is
        passed as the first argument.

        .. versionadded:: 1.0
        """
    def handle_http_exception(self, e: HTTPException) -> HTTPException | ft.ResponseReturnValue:
        """Handles an HTTP exception.  By default this will invoke the
        registered error handlers and fall back to returning the
        exception as response.

        .. versionchanged:: 1.0.3
            ``RoutingException``, used internally for actions such as
             slash redirects during routing, is not passed to error
             handlers.

        .. versionchanged:: 1.0
            Exceptions are looked up by code *and* by MRO, so
            ``HTTPException`` subclasses can be handled with a catch-all
            handler for the base ``HTTPException``.

        .. versionadded:: 0.3
        """
    def handle_user_exception(self, e: Exception) -> HTTPException | ft.ResponseReturnValue:
        """This method is called whenever an exception occurs that
        should be handled. A special case is :class:`~werkzeug
        .exceptions.HTTPException` which is forwarded to the
        :meth:`handle_http_exception` method. This function will either
        return a response value or reraise the exception with the same
        traceback.

        .. versionchanged:: 1.0
            Key errors raised from request data like ``form`` show the
            bad key in debug mode rather than a generic bad request
            message.

        .. versionadded:: 0.7
        """
    def handle_exception(self, e: Exception) -> Response:
        """Handle an exception that did not have an error handler
        associated with it, or that was raised from an error handler.
        This always causes a 500 ``InternalServerError``.

        Always sends the :data:`got_request_exception` signal.

        If :data:`PROPAGATE_EXCEPTIONS` is ``True``, such as in debug
        mode, the error will be re-raised so that the debugger can
        display it. Otherwise, the original exception is logged, and
        an :exc:`~werkzeug.exceptions.InternalServerError` is returned.

        If an error handler is registered for ``InternalServerError`` or
        ``500``, it will be used. For consistency, the handler will
        always receive the ``InternalServerError``. The original
        unhandled exception is available as ``e.original_exception``.

        .. versionchanged:: 1.1.0
            Always passes the ``InternalServerError`` instance to the
            handler, setting ``original_exception`` to the unhandled
            error.

        .. versionchanged:: 1.1.0
            ``after_request`` functions and other finalization is done
            even for the default 500 response when there is no handler.

        .. versionadded:: 0.3
        """
    def log_exception(self, exc_info: tuple[type, BaseException, TracebackType] | tuple[None, None, None]) -> None:
        """Logs an exception.  This is called by :meth:`handle_exception`
        if debugging is disabled and right before the handler is called.
        The default implementation logs the exception as error on the
        :attr:`logger`.

        .. versionadded:: 0.8
        """
    def dispatch_request(self) -> ft.ResponseReturnValue:
        """Does the request dispatching.  Matches the URL and returns the
        return value of the view or error handler.  This does not have to
        be a response object.  In order to convert the return value to a
        proper response object, call :func:`make_response`.

        .. versionchanged:: 0.7
           This no longer does the exception handling, this code was
           moved to the new :meth:`full_dispatch_request`.
        """
    def full_dispatch_request(self) -> Response:
        """Dispatches the request and on top of that performs request
        pre and postprocessing as well as HTTP exception catching and
        error handling.

        .. versionadded:: 0.7
        """
    def finalize_request(self, rv: ft.ResponseReturnValue | HTTPException, from_error_handler: bool = False) -> Response:
        """Given the return value from a view function this finalizes
        the request by converting it into a response and invoking the
        postprocessing functions.  This is invoked for both normal
        request dispatching as well as error handlers.

        Because this means that it might be called as a result of a
        failure a special safe mode is available which can be enabled
        with the `from_error_handler` flag.  If enabled, failures in
        response processing will be logged and otherwise ignored.

        :internal:
        """
    def make_default_options_response(self) -> Response:
        """This method is called to create the default ``OPTIONS`` response.
        This can be changed through subclassing to change the default
        behavior of ``OPTIONS`` responses.

        .. versionadded:: 0.7
        """
    def ensure_sync(self, func: t.Callable) -> t.Callable:
        """Ensure that the function is synchronous for WSGI workers.
        Plain ``def`` functions are returned as-is. ``async def``
        functions are wrapped to run and wait for the response.

        Override this method to change how the app runs async views.

        .. versionadded:: 2.0
        """
    def async_to_sync(self, func: t.Callable[..., t.Coroutine]) -> t.Callable[..., t.Any]:
        """Return a sync function that will run the coroutine function.

        .. code-block:: python

            result = app.async_to_sync(func)(*args, **kwargs)

        Override this method to change how the app converts async code
        to be synchronously callable.

        .. versionadded:: 2.0
        """
    def url_for(self, endpoint: str, *, _anchor: str | None = None, _method: str | None = None, _scheme: str | None = None, _external: bool | None = None, **values: t.Any) -> str:
        """Generate a URL to the given endpoint with the given values.

        This is called by :func:`flask.url_for`, and can be called
        directly as well.

        An *endpoint* is the name of a URL rule, usually added with
        :meth:`@app.route() <route>`, and usually the same name as the
        view function. A route defined in a :class:`~flask.Blueprint`
        will prepend the blueprint's name separated by a ``.`` to the
        endpoint.

        In some cases, such as email messages, you want URLs to include
        the scheme and domain, like ``https://example.com/hello``. When
        not in an active request, URLs will be external by default, but
        this requires setting :data:`SERVER_NAME` so Flask knows what
        domain to use. :data:`APPLICATION_ROOT` and
        :data:`PREFERRED_URL_SCHEME` should also be configured as
        needed. This config is only used when not in an active request.

        Functions can be decorated with :meth:`url_defaults` to modify
        keyword arguments before the URL is built.

        If building fails for some reason, such as an unknown endpoint
        or incorrect values, the app's :meth:`handle_url_build_error`
        method is called. If that returns a string, that is returned,
        otherwise a :exc:`~werkzeug.routing.BuildError` is raised.

        :param endpoint: The endpoint name associated with the URL to
            generate. If this starts with a ``.``, the current blueprint
            name (if any) will be used.
        :param _anchor: If given, append this as ``#anchor`` to the URL.
        :param _method: If given, generate the URL associated with this
            method for the endpoint.
        :param _scheme: If given, the URL will have this scheme if it
            is external.
        :param _external: If given, prefer the URL to be internal
            (False) or require it to be external (True). External URLs
            include the scheme and domain. When not in an active
            request, URLs are external by default.
        :param values: Values to use for the variable parts of the URL
            rule. Unknown keys are appended as query string arguments,
            like ``?a=b&c=d``.

        .. versionadded:: 2.2
            Moved from ``flask.url_for``, which calls this method.
        """
    def make_response(self, rv: ft.ResponseReturnValue) -> Response:
        """Convert the return value from a view function to an instance of
        :attr:`response_class`.

        :param rv: the return value from the view function. The view function
            must return a response. Returning ``None``, or the view ending
            without returning, is not allowed. The following types are allowed
            for ``view_rv``:

            ``str``
                A response object is created with the string encoded to UTF-8
                as the body.

            ``bytes``
                A response object is created with the bytes as the body.

            ``dict``
                A dictionary that will be jsonify'd before being returned.

            ``list``
                A list that will be jsonify'd before being returned.

            ``generator`` or ``iterator``
                A generator that returns ``str`` or ``bytes`` to be
                streamed as the response.

            ``tuple``
                Either ``(body, status, headers)``, ``(body, status)``, or
                ``(body, headers)``, where ``body`` is any of the other types
                allowed here, ``status`` is a string or an integer, and
                ``headers`` is a dictionary or a list of ``(key, value)``
                tuples. If ``body`` is a :attr:`response_class` instance,
                ``status`` overwrites the exiting value and ``headers`` are
                extended.

            :attr:`response_class`
                The object is returned unchanged.

            other :class:`~werkzeug.wrappers.Response` class
                The object is coerced to :attr:`response_class`.

            :func:`callable`
                The function is called as a WSGI application. The result is
                used to create a response object.

        .. versionchanged:: 2.2
            A generator will be converted to a streaming response.
            A list will be converted to a JSON response.

        .. versionchanged:: 1.1
            A dict will be converted to a JSON response.

        .. versionchanged:: 0.9
           Previously a tuple was interpreted as the arguments for the
           response object.
        """
    def preprocess_request(self) -> ft.ResponseReturnValue | None:
        """Called before the request is dispatched. Calls
        :attr:`url_value_preprocessors` registered with the app and the
        current blueprint (if any). Then calls :attr:`before_request_funcs`
        registered with the app and the blueprint.

        If any :meth:`before_request` handler returns a non-None value, the
        value is handled as if it was the return value from the view, and
        further request handling is stopped.
        """
    def process_response(self, response: Response) -> Response:
        """Can be overridden in order to modify the response object
        before it's sent to the WSGI server.  By default this will
        call all the :meth:`after_request` decorated functions.

        .. versionchanged:: 0.5
           As of Flask 0.5 the functions registered for after request
           execution are called in reverse order of registration.

        :param response: a :attr:`response_class` object.
        :return: a new response object or the same, has to be an
                 instance of :attr:`response_class`.
        """
    def do_teardown_request(self, exc: BaseException | None = ...) -> None:
        """Called after the request is dispatched and the response is
        returned, right before the request context is popped.

        This calls all functions decorated with
        :meth:`teardown_request`, and :meth:`Blueprint.teardown_request`
        if a blueprint handled the request. Finally, the
        :data:`request_tearing_down` signal is sent.

        This is called by
        :meth:`RequestContext.pop() <flask.ctx.RequestContext.pop>`,
        which may be delayed during testing to maintain access to
        resources.

        :param exc: An unhandled exception raised while dispatching the
            request. Detected from the current exception information if
            not passed. Passed to each teardown function.

        .. versionchanged:: 0.9
            Added the ``exc`` argument.
        """
    def do_teardown_appcontext(self, exc: BaseException | None = ...) -> None:
        """Called right before the application context is popped.

        When handling a request, the application context is popped
        after the request context. See :meth:`do_teardown_request`.

        This calls all functions decorated with
        :meth:`teardown_appcontext`. Then the
        :data:`appcontext_tearing_down` signal is sent.

        This is called by
        :meth:`AppContext.pop() <flask.ctx.AppContext.pop>`.

        .. versionadded:: 0.9
        """
    def app_context(self) -> AppContext:
        """Create an :class:`~flask.ctx.AppContext`. Use as a ``with``
        block to push the context, which will make :data:`current_app`
        point at this application.

        An application context is automatically pushed by
        :meth:`RequestContext.push() <flask.ctx.RequestContext.push>`
        when handling a request, and when running a CLI command. Use
        this to manually create a context outside of these situations.

        ::

            with app.app_context():
                init_db()

        See :doc:`/appcontext`.

        .. versionadded:: 0.9
        """
    def request_context(self, environ: dict) -> RequestContext:
        """Create a :class:`~flask.ctx.RequestContext` representing a
        WSGI environment. Use a ``with`` block to push the context,
        which will make :data:`request` point at this request.

        See :doc:`/reqcontext`.

        Typically you should not call this from your own code. A request
        context is automatically pushed by the :meth:`wsgi_app` when
        handling a request. Use :meth:`test_request_context` to create
        an environment and context instead of this method.

        :param environ: a WSGI environment
        """
    def test_request_context(self, *args: t.Any, **kwargs: t.Any) -> RequestContext:
        """Create a :class:`~flask.ctx.RequestContext` for a WSGI
        environment created from the given values. This is mostly useful
        during testing, where you may want to run a function that uses
        request data without dispatching a full request.

        See :doc:`/reqcontext`.

        Use a ``with`` block to push the context, which will make
        :data:`request` point at the request for the created
        environment. ::

            with app.test_request_context(...):
                generate_report()

        When using the shell, it may be easier to push and pop the
        context manually to avoid indentation. ::

            ctx = app.test_request_context(...)
            ctx.push()
            ...
            ctx.pop()

        Takes the same arguments as Werkzeug's
        :class:`~werkzeug.test.EnvironBuilder`, with some defaults from
        the application. See the linked Werkzeug docs for most of the
        available arguments. Flask-specific behavior is listed here.

        :param path: URL path being requested.
        :param base_url: Base URL where the app is being served, which
            ``path`` is relative to. If not given, built from
            :data:`PREFERRED_URL_SCHEME`, ``subdomain``,
            :data:`SERVER_NAME`, and :data:`APPLICATION_ROOT`.
        :param subdomain: Subdomain name to append to
            :data:`SERVER_NAME`.
        :param url_scheme: Scheme to use instead of
            :data:`PREFERRED_URL_SCHEME`.
        :param data: The request body, either as a string or a dict of
            form keys and values.
        :param json: If given, this is serialized as JSON and passed as
            ``data``. Also defaults ``content_type`` to
            ``application/json``.
        :param args: other positional arguments passed to
            :class:`~werkzeug.test.EnvironBuilder`.
        :param kwargs: other keyword arguments passed to
            :class:`~werkzeug.test.EnvironBuilder`.
        """
    def wsgi_app(self, environ: dict, start_response: t.Callable) -> t.Any:
        """The actual WSGI application. This is not implemented in
        :meth:`__call__` so that middlewares can be applied without
        losing a reference to the app object. Instead of doing this::

            app = MyMiddleware(app)

        It's a better idea to do this instead::

            app.wsgi_app = MyMiddleware(app.wsgi_app)

        Then you still have the original application object around and
        can continue to call methods on it.

        .. versionchanged:: 0.7
            Teardown events for the request and app contexts are called
            even if an unhandled error occurs. Other events may not be
            called depending on when an error occurs during dispatch.
            See :ref:`callbacks-and-errors`.

        :param environ: A WSGI environment.
        :param start_response: A callable accepting a status code,
            a list of headers, and an optional exception context to
            start the response.
        """
    def __call__(self, environ: dict, start_response: t.Callable) -> t.Any:
        """The WSGI server calls the Flask application object as the
        WSGI application. This calls :meth:`wsgi_app`, which can be
        wrapped to apply middleware.
        """
