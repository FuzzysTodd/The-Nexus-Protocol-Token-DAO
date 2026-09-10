from IPython.utils.encoding import DEFAULT_ENCODING as DEFAULT_ENCODING
from _typeshed import Incomplete

coding_declaration: Incomplete

class Macro:
    """Simple class to store the value of macros as strings.

    Macro is just a callable that executes a string of IPython
    input when called.
    """
    value: Incomplete
    def __init__(self, code) -> None:
        """store the macro value, as a single string which can be executed"""
    def __add__(self, other): ...
