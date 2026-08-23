from .exception import MultipleMatches as MultipleMatches, NoMatches as NoMatches
from .named import NamedExtensionManager as NamedExtensionManager
from _typeshed import Incomplete

class DriverManager(NamedExtensionManager):
    """Load a single plugin with a given name from the namespace.

    :param namespace: The namespace for the entry points.
    :type namespace: str
    :param name: The name of the driver to load.
    :type name: str
    :param invoke_on_load: Boolean controlling whether to invoke the
        object returned by the entry point after the driver is loaded.
    :type invoke_on_load: bool
    :param invoke_args: Positional arguments to pass when invoking
        the object returned by the entry point. Only used if invoke_on_load
        is True.
    :type invoke_args: tuple
    :param invoke_kwds: Named arguments to pass when invoking
        the object returned by the entry point. Only used if invoke_on_load
        is True.
    :type invoke_kwds: dict
    :param on_load_failure_callback: Callback function that will be called when
        an entrypoint can not be loaded. The arguments that will be provided
        when this is called (when an entrypoint fails to load) are
        (manager, entrypoint, exception)
    :type on_load_failure_callback: function
    :param verify_requirements: Use setuptools to enforce the
        dependencies of the plugin(s) being loaded. Defaults to False.
    :type verify_requirements: bool
    :type warn_on_missing_entrypoint: bool
    """
    def __init__(self, namespace, name, invoke_on_load: bool = False, invoke_args=(), invoke_kwds={}, on_load_failure_callback: Incomplete | None = None, verify_requirements: bool = False, warn_on_missing_entrypoint: bool = True) -> None: ...
    @classmethod
    def make_test_instance(cls, extension, namespace: str = 'TESTING', propagate_map_exceptions: bool = False, on_load_failure_callback: Incomplete | None = None, verify_requirements: bool = False):
        """Construct a test DriverManager

        Test instances are passed a list of extensions to work from rather
        than loading them from entry points.

        :param extension: Pre-configured Extension instance
        :type extension: :class:`~stevedore.extension.Extension`
        :param namespace: The namespace for the manager; used only for
            identification since the extensions are passed in.
        :type namespace: str
        :param propagate_map_exceptions: Boolean controlling whether exceptions
            are propagated up through the map call or whether they are logged
            and then ignored
        :type propagate_map_exceptions: bool
        :param on_load_failure_callback: Callback function that will
            be called when an entrypoint can not be loaded. The
            arguments that will be provided when this is called (when
            an entrypoint fails to load) are (manager, entrypoint,
            exception)
        :type on_load_failure_callback: function
        :param verify_requirements: Use setuptools to enforce the
            dependencies of the plugin(s) being loaded. Defaults to False.
        :type verify_requirements: bool
        :return: The manager instance, initialized for testing

        """
    def __call__(self, func, *args, **kwds):
        """Invokes func() for the single loaded extension.

        The signature for func() should be::

            def func(ext, *args, **kwds):
                pass

        The first argument to func(), 'ext', is the
        :class:`~stevedore.extension.Extension` instance.

        Exceptions raised from within func() are logged and ignored.

        :param func: Callable to invoke for each extension.
        :param args: Variable arguments to pass to func()
        :param kwds: Keyword arguments to pass to func()
        :returns: List of values returned from func()
        """
    @property
    def driver(self):
        """Returns the driver being used by this manager."""
