from _typeshed import Incomplete
from typing import Callable

dialects: Incomplete
engine_cursor: Incomplete
engine_default: Incomplete
engine_reflection: Incomplete
engine_result: Incomplete
engine_url: Incomplete
orm_clsregistry: Incomplete
orm_base: Incomplete
orm: Incomplete
orm_attributes: Incomplete
orm_decl_api: Incomplete
orm_decl_base: Incomplete
orm_descriptor_props: Incomplete
orm_dependency: Incomplete
orm_mapper: Incomplete
orm_properties: Incomplete
orm_relationships: Incomplete
orm_session: Incomplete
orm_strategies: Incomplete
orm_strategy_options: Incomplete
orm_state: Incomplete
orm_util: Incomplete
sql_default_comparator: Incomplete
sql_dml: Incomplete
sql_elements: Incomplete
sql_functions: Incomplete
sql_naming: Incomplete
sql_selectable: Incomplete
sql_traversals: Incomplete
sql_schema: Incomplete
sql_sqltypes: Incomplete
sql_util: Incomplete

class _ModuleRegistry:
    """Registry of modules to load in a package init file.

    To avoid potential thread safety issues for imports that are deferred
    in a function, like https://bugs.python.org/issue38884, these modules
    are added to the system module cache by importing them after the packages
    has finished initialization.

    A global instance is provided under the name :attr:`.preloaded`. Use
    the function :func:`.preload_module` to register modules to load and
    :meth:`.import_prefix` to load all the modules that start with the
    given path.

    While the modules are loaded in the global module cache, it's advisable
    to access them using :attr:`.preloaded` to ensure that it was actually
    registered. Each registered module is added to the instance ``__dict__``
    in the form `<package>_<module>`, omitting ``sqlalchemy`` from the package
    name. Example: ``sqlalchemy.sql.util`` becomes ``preloaded.sql_util``.
    """
    module_registry: Incomplete
    prefix: Incomplete
    def __init__(self, prefix: str = 'sqlalchemy.') -> None: ...
    def preload_module(self, *deps: str) -> Callable[[_FN], _FN]:
        """Adds the specified modules to the list to load.

        This method can be used both as a normal function and as a decorator.
        No change is performed to the decorated object.
        """
    def import_prefix(self, path: str) -> None:
        """Resolve all the modules in the registry that start with the
        specified path.
        """

preload_module: Incomplete
import_prefix: Incomplete
