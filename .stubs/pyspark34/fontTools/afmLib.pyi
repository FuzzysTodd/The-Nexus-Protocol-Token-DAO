from _typeshed import Incomplete

identifierRE: Incomplete
charRE: Incomplete
kernRE: Incomplete
compositeRE: Incomplete
componentRE: Incomplete
preferredAttributeOrder: Incomplete

class error(Exception): ...

class AFM:
    def __init__(self, path: Incomplete | None = None) -> None:
        """AFM file reader.

        Instantiating an object with a path name will cause the file to be opened,
        read, and parsed. Alternatively the path can be left unspecified, and a
        file can be parsed later with the :meth:`read` method."""
    def read(self, path) -> None:
        """Opens, reads and parses a file."""
    def parsechar(self, rest) -> None: ...
    def parsekernpair(self, rest) -> None: ...
    def parseattr(self, word, rest) -> None: ...
    def parsecomposite(self, rest) -> None: ...
    def write(self, path, sep: str = '\r'):
        """Writes out an AFM font to the given path."""
    def has_kernpair(self, pair):
        """Returns `True` if the given glyph pair (specified as a tuple) exists
        in the kerning dictionary."""
    def kernpairs(self):
        """Returns a list of all kern pairs in the kerning dictionary."""
    def has_char(self, char):
        """Returns `True` if the given glyph exists in the font."""
    def chars(self):
        """Returns a list of all glyph names in the font."""
    def comments(self):
        """Returns all comments from the file."""
    def addComment(self, comment) -> None:
        """Adds a new comment to the file."""
    def addComposite(self, glyphName, components) -> None:
        """Specifies that the glyph `glyphName` is made up of the given components.
        The components list should be of the following form::

                [
                        (glyphname, xOffset, yOffset),
                        ...
                ]

        """
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value) -> None: ...
    def __delattr__(self, attr) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...

def readlines(path): ...
def writelines(path, lines, sep: str = '\r') -> None: ...
