from _typeshed import Incomplete

INFSTR: Incomplete

def interleave(inter, f, seq) -> None:
    """Call f on each item in seq, calling inter() in between.
    """

class Unparser:
    """Methods in this class recursively traverse an AST and
    output source code for the abstract syntax; original formatting
    is disregarded. """
    f: Incomplete
    future_imports: Incomplete
    def __init__(self, tree, file=...) -> None:
        """Unparser(tree, file=sys.stdout) -> None.
         Print the source for tree to file."""
    def fill(self, text: str = '') -> None:
        """Indent a piece of text, according to the current indentation level"""
    def write(self, text) -> None:
        """Append a piece of text to the current line."""
    def enter(self) -> None:
        """Print ':', and increase the indentation."""
    def leave(self) -> None:
        """Decrease the indentation level."""
    def dispatch(self, tree) -> None:
        """Dispatcher function, dispatching tree type T to method _T."""
    unop: Incomplete
    binop: Incomplete
    cmpops: Incomplete
    boolops: Incomplete

def roundtrip(filename, output=...) -> None: ...
def testdir(a) -> None: ...
def main(args) -> None: ...
