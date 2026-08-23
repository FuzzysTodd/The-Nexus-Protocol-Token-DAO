from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import auth_context_middleware as auth_context_middleware, client_feature_flags as client_feature_flags, empty_path_redirect as empty_path_redirect, experiment_id as experiment_id, experimental_plugin as experimental_plugin, http_util as http_util, path_prefix as path_prefix, security_validator as security_validator
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.core import core_plugin as core_plugin
from tensorboard.util import tb_logging as tb_logging

DATA_PREFIX: str
PLUGIN_PREFIX: str
PLUGINS_LISTING_ROUTE: str
PLUGIN_ENTRY_ROUTE: str
EXPERIMENTAL_PLUGINS_QUERY_PARAM: str
logger: Incomplete

def TensorBoardWSGIApp(flags, plugins, data_provider: Incomplete | None = None, assets_zip_provider: Incomplete | None = None, deprecated_multiplexer: Incomplete | None = None, auth_providers: Incomplete | None = None, experimental_middlewares: Incomplete | None = None):
    '''Constructs a TensorBoard WSGI app from plugins and data providers.

    Args:
      flags: An argparse.Namespace containing TensorBoard CLI flags.
      plugins: A list of plugins, which can be provided as TBPlugin subclasses
          or TBLoader instances or subclasses.
      data_provider: Instance of `tensorboard.data.provider.DataProvider`. May
          be `None` if `flags.generic_data` is set to `"false"` in which case
          `deprecated_multiplexer` must be passed instead.
      assets_zip_provider: See TBContext documentation for more information. If
          `None` a placeholder assets zipfile will be used containing only a
          default `index.html` file, and the actual frontend assets must be
          supplied by middleware wrapping this WSGI app.
      deprecated_multiplexer: Optional `plugin_event_multiplexer.EventMultiplexer`
          to use for any plugins not yet enabled for the DataProvider API.
          Required if the data_provider argument is not passed.
      auth_providers: Optional mapping whose values are `AuthProvider` values
        and whose keys are used by (e.g.) data providers to specify
        `AuthProvider`s via the `AuthContext.get` interface. Defaults to `{}`.
      experimental_middlewares: Optional list of WSGI middlewares (i.e.,
        callables that take a WSGI application and return a WSGI application)
        to apply directly around the core TensorBoard app itself, "inside" the
        request redirection machinery for `--path_prefix`, experiment IDs, etc.
        You can use this to add handlers for additional routes. Middlewares are
        applied in listed order, so the first element of this list is the
        innermost application. Defaults to `[]`. This parameter is experimental
        and may be reworked or removed.

    Returns:
      A WSGI application that implements the TensorBoard backend.

    :type plugins: list[base_plugin.TBLoader]
    '''
def make_plugin_loader(plugin_spec):
    """Returns a plugin loader for the given plugin.

    Args:
      plugin_spec: A TBPlugin subclass, or a TBLoader instance or subclass.

    Returns:
      A TBLoader for the given plugin.

    :type plugin_spec:
      Type[base_plugin.TBPlugin] | Type[base_plugin.TBLoader] |
      base_plugin.TBLoader
    :rtype: base_plugin.TBLoader
    """

class TensorBoardWSGI:
    """The TensorBoard WSGI app that delegates to a set of TBPlugin."""
    exact_routes: Incomplete
    prefix_routes: Incomplete
    def __init__(self, plugins, path_prefix: str = '', data_provider: Incomplete | None = None, experimental_plugins: Incomplete | None = None, auth_providers: Incomplete | None = None, experimental_middlewares: Incomplete | None = None) -> None:
        '''Constructs TensorBoardWSGI instance.

        Args:
          plugins: A list of base_plugin.TBPlugin subclass instances.
          path_prefix: A prefix of the path when app isn\'t served from root.
          data_provider: `tensorboard.data.provider.DataProvider` or
            `None`; if present, will inform the "active" state of
            `/plugins_listing`.
          experimental_plugins: A list of plugin names that are only provided
              experimentally. The corresponding plugins will only be activated for
              a user if the user has specified the plugin with the experimentalPlugin
              query parameter in the URL.
          auth_providers: Optional mapping whose values are `AuthProvider`
            values and whose keys are used by (e.g.) data providers to specify
            `AuthProvider`s via the `AuthContext.get` interface.
            Defaults to `{}`.
          experimental_middlewares: Optional list of WSGI middlewares to apply
            directly around the core TensorBoard app itself. Defaults to `[]`.
            This parameter is experimental and may be reworked or removed.

        Returns:
          A WSGI application for the set of all TBPlugin instances.

        Raises:
          ValueError: If some plugin has no plugin_name
          ValueError: If some plugin has an invalid plugin_name (plugin
              names must only contain [A-Za-z0-9_.-])
          ValueError: If two plugins have the same plugin_name
          ValueError: If some plugin handles a route that does not start
              with a slash

        :type plugins: list[base_plugin.TBPlugin]
        '''
    def __call__(self, environ, start_response):
        """Central entry point for the TensorBoard application.

        This __call__ method conforms to the WSGI spec, so that instances of this
        class are WSGI applications.

        Args:
          environ: See WSGI spec (PEP 3333).
          start_response: See WSGI spec (PEP 3333).
        """
