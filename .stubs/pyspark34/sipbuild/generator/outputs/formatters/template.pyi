from ...scoped_name import STRIP_GLOBAL as STRIP_GLOBAL, STRIP_NONE as STRIP_NONE
from .scoped import ScopedFormatter as ScopedFormatter
from .signature import SignatureFormatter as SignatureFormatter

class TemplateFormatter(ScopedFormatter):
    """ This creates various string representations of a template. """
    def cpp_type(self, *, strip=..., as_xml: bool = False):
        """ Return the C++ representation of the template type. """
