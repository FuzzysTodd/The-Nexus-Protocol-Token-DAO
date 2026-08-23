from ...specification import ValueType as ValueType
from .argument import ArgumentFormatter as ArgumentFormatter
from .base_formatter import BaseFormatter as BaseFormatter
from .enum import EnumFormatter as EnumFormatter
from .variable import VariableFormatter as VariableFormatter

class ValueListFormatter(BaseFormatter):
    """ This creates various string representations of a list of values. """
    @property
    def cpp_expression(self):
        """ The C++ representation of the value list as an expression. """
    def py_expression(self, embedded: bool = False, as_xml: bool = False):
        """ The Python representation of the value list as an expression. """
    def as_rest_ref(self, as_xml: bool = False):
        """ Return the Python representation of the value list as a reST
        reference.
        """
