from .exception import NoMatches as NoMatches
from _typeshed import Incomplete

LOG: Incomplete

class Extension:
    """Book-keeping object for tracking extensions.

    The arguments passed to the constructor are saved as attributes of
    the instance using the same names, and can be accessed by the
    callables passed to :meth:`map` or when iterating over an
    :class:`ExtensionManager` directly.

    :param name: The entry point name.
    :type name: str
    :param entry_point: The EntryPoint instance returned by
        :mod:`entrypoints`.
    :type entry_point: EntryPoint
    :param plugin: The value returned by entry_point.load()
    :param obj: The object returned by ``plugin(*args, **kwds)`` if the
                manager invoked the extension on load.

    """
    name: Incomplete
    entry_point: Incomplete
    plugin: Incomplete
    obj: Incomplete
    def __init__(self, name, entry_point, plugin, obj) -> None: ...
    @property
    def module_name(self):
        """The name of the module from which the entry point is loaded.

        :return: A string in 'dotted.module' format.
        """
    @property
    def attr(self):
        """The attribute of the module to be loaded."""
    @property
    def entry_point_target(self):
        """The module and attribute referenced by this extension's entry_point.

        :return: A string representation of the target of the entry point in
            'dotted.module:object' format.
        """

class ExtensionManager:
    """Base class for all of the other managers.

    :param namespace: The namespace for the entry points.
    :type namespace: str
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
    :param propagate_map_exceptions: Boolean controlling whether exceptions
        are propagated up through the map call or whether they are logged and
        then ignored
    :type propagate_map_exceptions: bool
    :param on_load_failure_callback: Callback function that will be called when
        an entrypoint can not be loaded. The arguments that will be provided
        when this is called (when an entrypoint fails to load) are
        (manager, entrypoint, exception)
    :type on_load_failure_callback: function
    :param verify_requirements: Use setuptools to enforce the
        dependencies of the plugin(s) being loaded. Defaults to False.
    :type verify_requirements: bool
    """
    def __init__(self, namespace, invoke_on_load: bool = False, invoke_args=(), invoke_kwds={}, propagate_map_exceptions: bool = False, on_load_failure_callback: Incomplete | None = None, verify_requirements: bool = False) -> None: ...
    @classmethod
    def make_test_instance(cls, extensions, namespace: str = 'TESTING', propagate_map_exceptions: bool = False, on_load_failure_callback: Incomplete | None = None, verify_requirements: bool = False):
        """Construct a test ExtensionManager

        Test instances are passed a list of extensions to work from rather
        than loading them from entry points.

        :param extensions: Pre-configured Extension instances to use
        :type extensions: list of :class:`~stevedore.extension.Extension`
        :param namespace: The namespace for the manager; used only for
            identification since the extensions are passed in.
        :type namespace: str
        :param propagate_map_exceptions: When calling map, controls whether
            exceptions are propagated up through the map call or whether they
            are logged and then ignored
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
    ENTRY_POINT_CACHE: Incomplete
    def list_entry_points(self):
        """Return the list of entry points for this namespace.

        The entry points are not actually loaded, their list is just read and
        returned.

        """
    def entry_points_names(self):
        """Return the list of entry points names for this namespace."""
    def names(self):
        """Returns the names of the discovered extensions"""
    def map(self, func, *args, **kwds):
        """Iterate over the extensions invoking func() for each.

        The signature for func() should be::

            def func(ext, *args, **kwds):
                pass

        The first argument to func(), 'ext', is the
        :class:`~stevedore.extension.Extension` instance.

        Exceptions raised from within func() are propagated up and
        processing stopped if self.propagate_map_exceptions is True,
        otherwise they are logged and ignored.

        :param func: Callable to invoke for each extension.
        :param args: Variable arguments to pass to func()
        :param kwds: Keyword arguments to pass to func()
        :returns: List of values returned from func()
        """
    def map_method(self, method_name, *args, **kwds):
        """Iterate over the extensions invoking a method by name.

        This is equivalent of using :meth:`map` with func set to
        `lambda x: x.obj.method_name()`
        while being more convenient.

        Exceptions raised from within the called method are propagated up
        and processing stopped if self.propagate_map_exceptions is True,
        otherwise they are logged and ignored.

        .. versionadded:: 0.12

        :param method_name: The extension method name
                            to call for each extension.
        :param args: Variable arguments to pass to method
        :param kwds: Keyword arguments to pass to method
        :returns: List of values returned from methods
        """
    def items(self):
        """Return an iterator of tuples of the form (name, extension).

        This is analogous to the Mapping.items() method.
        """
    def __iter__(self):
        """Produce iterator for the manager.

        Iterating over an ExtensionManager produces the :class:`Extension`
        instances in the order they would be invoked.
        """
    def __getitem__(self, name):
        """Return the named extension.

        Accessing an ExtensionManager as a dictionary (``em['name']``)
        produces the :class:`Extension` instance with the
        specified name.
        """
    def __contains__(self, name) -> bool:
        """Return true if name is in list of enabled extensions."""
