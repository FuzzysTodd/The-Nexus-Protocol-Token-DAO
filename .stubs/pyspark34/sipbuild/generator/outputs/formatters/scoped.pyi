from .base_formatter import BaseFormatter as BaseFormatter
from .utils import format_scoped_py_name as format_scoped_py_name
from _typeshed import Incomplete

class ScopedFormatter(BaseFormatter):
    """ A base class for formatters of objects that can be contained by a
    scope.
    """
    scope: Incomplete
    def __init__(self, spec, object, scope) -> None:
        """ Initialise the object. """
    @property
    def cpp_scope(self):
        """ The C++ scope as a string. """
    @property
    def fq_cpp_name(self):
        """ The fully qualified C++ name. """
    @property
    def fq_py_name(self):
        """ The fully qualified Python name. """

class EmbeddedScopeFormatter(ScopedFormatter):
    """ A base class for formatters of objects that have a reference to their
    scope.
    """
    def __init__(self, spec, object) -> None:
        """ Initialise the object. """
