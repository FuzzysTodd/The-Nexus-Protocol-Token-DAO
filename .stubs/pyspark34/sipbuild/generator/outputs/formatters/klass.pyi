from ...scoped_name import STRIP_NONE as STRIP_NONE
from .scoped import EmbeddedScopeFormatter as EmbeddedScopeFormatter
from .template import TemplateFormatter as TemplateFormatter
from .utils import format_scoped_py_name as format_scoped_py_name, iface_is_defined as iface_is_defined
from _typeshed import Incomplete

class ClassFormatter(EmbeddedScopeFormatter):
    """ This creates various string representations of a class. """
    def as_rest_ref(self):
        """ Return the fully qualified Python name as a reST reference. """
    def scoped_name(self, *, scope: Incomplete | None = None, strip=..., make_public: bool = False, as_xml: bool = False):
        """ Return an appropriately scoped class name. """
    def as_type_hint(self, module, defined):
        """ Return the type hint. """
