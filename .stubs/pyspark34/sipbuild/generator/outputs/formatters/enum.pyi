from ...specification import IfaceFileType as IfaceFileType
from .scoped import EmbeddedScopeFormatter as EmbeddedScopeFormatter
from .utils import format_scoped_py_name as format_scoped_py_name, iface_is_defined as iface_is_defined
from _typeshed import Incomplete
from collections.abc import Generator

class EnumFormatter(EmbeddedScopeFormatter):
    """ This creates various string representations of an enum. """
    @property
    def fq_py_member_names(self) -> Generator[Incomplete, None, None]:
        """ An iterator over the fully qualified Python names of the members of
        the enum.
        """
    def member_as_rest_ref(self, member):
        """ Return the fully qualified Python name of a member as a reST
        reference.
        """
    def as_rest_ref(self):
        """ Return the fully qualified Python name as a reST reference. """
    def as_type_hint(self, module, defined):
        """ Return the type hint. """
