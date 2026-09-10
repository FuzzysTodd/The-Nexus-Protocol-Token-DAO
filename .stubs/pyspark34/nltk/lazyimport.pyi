from _typeshed import Incomplete

class LazyModule:
    """Lazy module class.

    Lazy modules are imported into the given namespaces whenever a
    non-special attribute (there are some attributes like __doc__
    that class instances handle without calling __getattr__) is
    requested. The module is then registered under the given name
    in locals usually replacing the import wrapper instance. The
    import itself is done using globals as global namespace.

    Example of creating a lazy load module:

    ISO = LazyModule('ISO',locals(),globals())

    Later, requesting an attribute from ISO will load the module
    automatically into the locals() namespace, overriding the
    LazyModule instance:

    t = ISO.Week(1998,1,1)

    """
    def __init__(self, name, locals, globals: Incomplete | None = None) -> None:
        """Create a LazyModule instance wrapping module name.

        The module will later on be registered in locals under the
        given module name.

        globals is optional and defaults to locals.

        """
    def __getattr__(self, name):
        """Import the module on demand and get the attribute."""
    def __setattr__(self, name, value) -> None:
        """Import the module on demand and set the attribute."""
