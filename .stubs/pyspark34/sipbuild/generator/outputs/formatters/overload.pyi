from ...specification import PySlot as PySlot
from .scoped import ScopedFormatter as ScopedFormatter
from .utils import format_scoped_py_name as format_scoped_py_name

class OverloadFormatter(ScopedFormatter):
    """ This creates various string representations of an overload. """
    @property
    def fq_cpp_name(self):
        """ The fully qualified C++ name. """
    @property
    def fq_py_name(self):
        """ The fully qualified Python name. """
