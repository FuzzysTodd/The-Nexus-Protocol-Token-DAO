from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

class TBPlugin(metaclass=ABCMeta):
    """TensorBoard plugin interface.

    Every plugin must extend from this class.

    Subclasses should have a trivial constructor that takes a TBContext
    argument. Any operation that might throw an exception should either be
    done lazily or made safe with a TBLoader subclass, so the plugin won't
    negatively impact the rest of TensorBoard.

    Fields:
      plugin_name: The plugin_name will also be a prefix in the http
        handlers, e.g. `data/plugins/$PLUGIN_NAME/$HANDLER` The plugin
        name must be unique for each registered plugin, or a ValueError
        will be thrown when the application is constructed. The plugin
        name must only contain characters among [A-Za-z0-9_.-], and must
        be nonempty, or a ValueError will similarly be thrown.
    """
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Initializes this plugin.

        The default implementation does nothing. Subclasses are encouraged
        to override this and save any necessary fields from the `context`.

        Args:
          context: A `base_plugin.TBContext` object.
        """
    @abstractmethod
    def get_plugin_apps(self):
        """Returns a set of WSGI applications that the plugin implements.

        Each application gets registered with the tensorboard app and is served
        under a prefix path that includes the name of the plugin.

        Returns:
          A dict mapping route paths to WSGI applications. Each route path
          should include a leading slash.
        """
    @abstractmethod
    def is_active(self):
        """Determines whether this plugin is active.

        A plugin may not be active for instance if it lacks relevant data. If a
        plugin is inactive, the frontend may avoid issuing requests to its routes.

        Returns:
          A boolean value. Whether this plugin is active.
        """
    def frontend_metadata(self):
        """Defines how the plugin will be displayed on the frontend.

        The base implementation returns a default value. Subclasses
        should override this and specify either an `es_module_path` or
        (for legacy plugins) an `element_name`, and are encouraged to
        set any other relevant attributes.
        """
    def data_plugin_names(self):
        """Experimental. Lists plugins whose summary data this plugin reads.

        Returns:
          A collection of strings representing plugin names (as read
          from `SummaryMetadata.plugin_data.plugin_name`) from which
          this plugin may read data. Defaults to `(self.plugin_name,)`.
        """

class FrontendMetadata:
    """Metadata required to render a plugin on the frontend.

    Each argument to the constructor is publicly accessible under a
    field of the same name. See constructor docs for further details.
    """
    def __init__(self, *, disable_reload: Incomplete | None = None, element_name: Incomplete | None = None, es_module_path: Incomplete | None = None, remove_dom: Incomplete | None = None, tab_name: Incomplete | None = None, is_ng_component: Incomplete | None = None) -> None:
        '''Creates a `FrontendMetadata` value.

        The argument list is sorted and may be extended in the future;
        therefore, callers must pass only named arguments to this
        constructor.

        Args:
          disable_reload: Whether to disable the reload button and
              auto-reload timer. A `bool`; defaults to `False`.
          element_name: For legacy plugins, name of the custom element
              defining the plugin frontend: e.g., `"tf-scalar-dashboard"`.
              A `str` or `None` (for iframed plugins). Mutually exclusive
              with `es_module_path`.
          es_module_path: ES module to use as an entry point to this plugin.
              A `str` that is a key in the result of `get_plugin_apps()`, or
              `None` for legacy plugins bundled with TensorBoard as part of
              `webfiles.zip`. Mutually exclusive with legacy `element_name`
          remove_dom: Whether to remove the plugin DOM when switching to a
              different plugin, to trigger the Polymer \'detached\' event.
              A `bool`; defaults to `False`.
          tab_name: Name to show in the menu item for this dashboard within
              the navigation bar. May differ from the plugin name: for
              instance, the tab name should not use underscores to separate
              words. Should be a `str` or `None` (the default; indicates to
              use the plugin name as the tab name).
          is_ng_component: Set to `True` only for built-in Angular plugins.
              In this case, the `plugin_name` property of the Plugin, which is
              mapped to the `id` property in JavaScript\'s `UiPluginMetadata` type,
              is used to select the Angular component. A `True` value is mutually
              exclusive with `element_name` and `es_module_path`.
        '''
    @property
    def disable_reload(self): ...
    @property
    def element_name(self): ...
    @property
    def is_ng_component(self): ...
    @property
    def es_module_path(self): ...
    @property
    def remove_dom(self): ...
    @property
    def tab_name(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class TBContext:
    """Magic container of information passed from TensorBoard core to plugins.

    A TBContext instance is passed to the constructor of a TBPlugin class. Plugins
    are strongly encouraged to assume that any of these fields can be None. In
    cases when a field is considered mandatory by a plugin, it can either crash
    with ValueError, or silently choose to disable itself by returning False from
    its is_active method.

    All fields in this object are thread safe.
    """
    assets_zip_provider: Incomplete
    data_provider: Incomplete
    flags: Incomplete
    logdir: Incomplete
    multiplexer: Incomplete
    plugin_name_to_instance: Incomplete
    sampling_hints: Incomplete
    window_title: Incomplete
    def __init__(self, *, assets_zip_provider: Incomplete | None = None, data_provider: Incomplete | None = None, flags: Incomplete | None = None, logdir: Incomplete | None = None, multiplexer: Incomplete | None = None, plugin_name_to_instance: Incomplete | None = None, sampling_hints: Incomplete | None = None, window_title: Incomplete | None = None) -> None:
        '''Instantiates magic container.

        The argument list is sorted and may be extended in the future; therefore,
        callers must pass only named arguments to this constructor.

        Args:
          assets_zip_provider: A function that returns a newly opened file handle
              for a zip file containing all static assets. The file names inside the
              zip file are considered absolute paths on the web server. The file
              handle this function returns must be closed. It is assumed that you
              will pass this file handle to zipfile.ZipFile. This zip file should
              also have been created by the tensorboard_zip_file build rule.
          data_provider: Instance of `tensorboard.data.provider.DataProvider`. May
            be `None` if `flags.generic_data` is set to `"false"`.
          flags: An object of the runtime flags provided to TensorBoard to their
              values.
          logdir: The string logging directory TensorBoard was started with.
          multiplexer: An EventMultiplexer with underlying TB data. Plugins should
              copy this data over to the database when the db fields are set.
          plugin_name_to_instance: A mapping between plugin name to instance.
              Plugins may use this property to access other plugins. The context
              object is passed to plugins during their construction, so a given
              plugin may be absent from this mapping until it is registered. Plugin
              logic should handle cases in which a plugin is absent from this
              mapping, lest a KeyError is raised.
          sampling_hints: Map from plugin name to `int` or `NoneType`, where
              the value represents the user-specified downsampling limit as
              given to the `--samples_per_plugin` flag, or `None` if none was
              explicitly given for this plugin.
          window_title: A string specifying the window title.
        '''

class TBLoader:
    """TBPlugin factory base class.

    Plugins can override this class to customize how a plugin is loaded at
    startup. This might entail adding command-line arguments, checking if
    optional dependencies are installed, and potentially also specializing
    the plugin class at runtime.

    When plugins use optional dependencies, the loader needs to be
    specified in its own module. That way it's guaranteed to be
    importable, even if the `TBPlugin` itself can't be imported.

    Subclasses must have trivial constructors.
    """
    def define_flags(self, parser) -> None:
        """Adds plugin-specific CLI flags to parser.

        The default behavior is to do nothing.

        When overriding this method, it's recommended that plugins call the
        `parser.add_argument_group(plugin_name)` method for readability. No
        flags should be specified that would cause `parse_args([])` to fail.

        Args:
          parser: The argument parsing object, which may be mutated.
        """
    def fix_flags(self, flags) -> None:
        """Allows flag values to be corrected or validated after parsing.

        Args:
          flags: The parsed argparse.Namespace object.

        Raises:
          base_plugin.FlagsError: If a flag is invalid or a required
              flag is not passed.
        """
    def load(self, context) -> None:
        """Loads a TBPlugin instance during the setup phase.

        Args:
          context: The TBContext instance.

        Returns:
          A plugin instance or None if it could not be loaded. Loaders that return
          None are skipped.

        :type context: TBContext
        :rtype: TBPlugin | None
        """

class BasicLoader(TBLoader):
    """Simple TBLoader that's sufficient for most plugins."""
    plugin_class: Incomplete
    def __init__(self, plugin_class) -> None:
        """Creates simple plugin instance maker.

        :param plugin_class: :class:`TBPlugin`
        """
    def load(self, context): ...

class FlagsError(ValueError):
    """Raised when a command line flag is not specified or is invalid."""
