from ...scoped_name import STRIP_NONE as STRIP_NONE
from ...specification import ArgumentType as ArgumentType, ArrayArgument as ArrayArgument
from .argument import ArgumentFormatter as ArgumentFormatter
from .base_formatter import BaseFormatter as BaseFormatter
from _typeshed import Incomplete

class SignatureFormatter(BaseFormatter):
    """ This creates various string representations of a signature. """
    def cpp_arguments(self, *, scope: Incomplete | None = None, strip=..., make_public: bool = False, as_xml: bool = False):
        """ Return the C++ representation of the signature arguments. """
    @property
    def py_arguments(self):
        """ The Python representation of the signature arguments. """
    @property
    def py_results(self):
        """ The Python representation of the signature results. """
