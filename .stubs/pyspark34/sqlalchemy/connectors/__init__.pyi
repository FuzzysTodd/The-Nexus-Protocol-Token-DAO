from ..engine.interfaces import Dialect

class Connector(Dialect):
    """Base class for dialect mixins, for DBAPIs that work
    across entirely different database backends.

    Currently the only such mixin is pyodbc.

    """
