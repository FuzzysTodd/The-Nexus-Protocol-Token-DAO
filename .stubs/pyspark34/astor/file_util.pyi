from _typeshed import Incomplete
from collections.abc import Generator

fopen = open

class CodeToAst:
    """Given a module, or a function that was compiled as part
    of a module, re-compile the module into an AST and extract
    the sub-AST for the function.  Allow caching to reduce
    number of compiles.

    Also contains static helper utility functions to
    look for python files, to parse python files, and to extract
    the file/line information from a code object.
    """
    @staticmethod
    def find_py_files(srctree, ignore: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Return all the python files in a source tree

        Ignores any path that contains the ignore string

        This is not used by other class methods, but is
        designed to be used in code that uses this class.
        """
    @staticmethod
    def parse_file(fname):
        """Parse a python file into an AST.

        This is a very thin wrapper around ast.parse

            TODO: Handle encodings other than the default for Python 2
                        (issue #26)
        """
    @staticmethod
    def get_file_info(codeobj):
        """Returns the file and line number of a code object.

            If the code object has a __file__ attribute (e.g. if
            it is a module), then the returned line number will
            be 0
        """
    cache: Incomplete
    def __init__(self, cache: Incomplete | None = None) -> None: ...
    def __call__(self, codeobj): ...

code_to_ast: Incomplete
