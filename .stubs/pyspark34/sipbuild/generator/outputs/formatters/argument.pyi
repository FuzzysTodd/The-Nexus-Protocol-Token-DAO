from ...scoped_name import STRIP_NONE as STRIP_NONE
from ...specification import ArgumentType as ArgumentType, ArrayArgument as ArrayArgument, ClassKey as ClassKey, ValueType as ValueType
from ..type_hints import TypeHintManager as TypeHintManager, format_voidptr as format_voidptr
from .base_formatter import BaseFormatter as BaseFormatter
from .utils import format_scoped_py_name as format_scoped_py_name
from _typeshed import Incomplete

class ArgumentFormatter(BaseFormatter):
    """ This creates various string representations of an argument. """
    def cpp_type(self, *, name: Incomplete | None = None, scope: Incomplete | None = None, strip=..., make_public: bool = False, use_typename: bool = True, as_xml: bool = False):
        """ Return the argument as a C++ type. """
    def py_default_value(self, type_name, embedded: bool = False, as_xml: bool = False):
        """ Return the Python representation of the argument's default value.
        """
    def as_py_type(self, pep484: bool = False, default_value: bool = False, as_xml: bool = False):
        """ Return the argument as a Python type. """
    def as_rest_ref(self, out, as_xml: bool = False):
        """ Return the argument as a reST reference. """
    def as_type_hint(self, module, out, defined):
        """ Return the argument as a type hint. """
