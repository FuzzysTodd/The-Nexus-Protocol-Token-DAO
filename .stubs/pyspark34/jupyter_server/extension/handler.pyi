from _typeshed import Incomplete
from jupyter_server.base.handlers import FileFindHandler as FileFindHandler

class ExtensionHandlerJinjaMixin:
    """Mixin class for ExtensionApp handlers that use jinja templating for
    template rendering.
    """
    def get_template(self, name):
        """Return the jinja template object for a given name"""

class ExtensionHandlerMixin:
    '''Base class for Jupyter server extension handlers.

    Subclasses can serve static files behind a namespaced
    endpoint: "<base_url>/static/<name>/"

    This allows multiple extensions to serve static files under
    their own namespace and avoid intercepting requests for
    other extensions.
    '''
    name: Incomplete
    def initialize(self, name, *args, **kwargs) -> None: ...
    @property
    def extensionapp(self): ...
    @property
    def serverapp(self): ...
    @property
    def log(self): ...
    @property
    def config(self): ...
    @property
    def server_config(self): ...
    @property
    def base_url(self) -> str: ...
    @property
    def static_url_prefix(self): ...
    @property
    def static_path(self): ...
    def static_url(self, path, include_host: Incomplete | None = None, **kwargs):
        """Returns a static URL for the given relative static file path.
        This method requires you set the ``{name}_static_path``
        setting in your extension (which specifies the root directory
        of your static files).
        This method returns a versioned url (by default appending
        ``?v=<signature>``), which allows the static files to be
        cached indefinitely.  This can be disabled by passing
        ``include_version=False`` (in the default implementation;
        other static file implementations are not required to support
        this, but they may support other options).
        By default this method returns URLs relative to the current
        host, but if ``include_host`` is true the URL returned will be
        absolute.  If this handler has an ``include_host`` attribute,
        that value will be used as the default for all `static_url`
        calls that do not pass ``include_host`` as a keyword argument.
        """
