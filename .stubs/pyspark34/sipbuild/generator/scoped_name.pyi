from _typeshed import Incomplete

STRIP_NONE: int
STRIP_GLOBAL: int

class ScopedName:
    """ Encapsulate a scoped name. """
    def __init__(self, name) -> None:
        """ Initialise the scoped name. """
    def __eq__(self, other):
        """ Compare with another scoped name for equality. """
    def __delitem__(self, index) -> None:
        """ Remove the requested name. """
    def __getitem__(self, index):
        """ Get the requested name. """
    def __len__(self) -> int:
        """ Return the length of the name, ie. the number of indivual names.
        """
    def __lt__(self, other):
        """ Compare with another scoped name to allow lists to be sorted. """
    def __setitem__(self, index, name) -> None:
        """ Set the requested name. """
    @property
    def absolute(self):
        """ The absolute version of the name. """
    def append(self, name) -> None:
        """ Append a simple name. """
    @property
    def as_cpp(self):
        """ The C++ representation of the name. """
    @property
    def as_py(self):
        """ The Python representation of the name. """
    @property
    def as_word(self):
        """ The word representation of the name. """
    @property
    def base_name(self):
        """ The base name of the scoped name. """
    def cpp_stripped(self, strip):
        """ Return the C++ representation of the name with leading scopes
        stripped.
        """
    @property
    def is_absolute(self):
        """ True if the scoped name is absolute. """
    @property
    def is_simple(self):
        """ Return True if the name is simple, ie. relative and unscoped. """
    def make_absolute(self) -> None:
        """ Make sure the scoped name is absolute. """
    def matches(self, scoped_name, scope: Incomplete | None = None):
        """ Return True if a scoped name matches this taking account of an
        optional scope if the scoped name is relative.
        """
    @classmethod
    def parse(cls, raw):
        """ Return a ScopedName object by parsing a raw string. """
    def prepend(self, scoped_name) -> None:
        """ Prepend a scoped name. """
    @property
    def scope(self):
        """ The scoped name that is the enclosing scope of this one.  It will
        be None if there isn't one.
        """
