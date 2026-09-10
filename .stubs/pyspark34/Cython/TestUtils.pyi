import unittest
from .CodeWriter import CodeWriter as CodeWriter
from .Compiler import Errors as Errors, TreePath as TreePath
from .Compiler.TreeFragment import TreeFragment as TreeFragment, strip_common_indent as strip_common_indent
from .Compiler.Visitor import TreeVisitor as TreeVisitor, VisitorTransform as VisitorTransform
from _typeshed import Incomplete

class NodeTypeWriter(TreeVisitor):
    result: Incomplete
    def __init__(self) -> None: ...
    def visit_Node(self, node) -> None: ...

def treetypes(root):
    """Returns a string representing the tree by class names.
    There's a leading and trailing whitespace so that it can be
    compared by simple string comparison while still making test
    cases look ok."""

class CythonTest(unittest.TestCase):
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def assertLines(self, expected, result) -> None:
        """Checks that the given strings or lists of strings are equal line by line"""
    def codeToLines(self, tree): ...
    def codeToString(self, tree): ...
    def assertCode(self, expected, result_tree) -> None: ...
    def assertNodeExists(self, path, result_tree) -> None: ...
    def fragment(self, code, pxds: Incomplete | None = None, pipeline: Incomplete | None = None):
        """Simply create a tree fragment using the name of the test-case in parse errors."""
    def treetypes(self, root): ...
    def should_fail(self, func, exc_type=...):
        '''Calls "func" and fails if it doesn\'t raise the right exception
        (any exception by default). Also returns the exception in question.
        '''
    def should_not_fail(self, func):
        """Calls func and succeeds if and only if no exception is raised
        (i.e. converts exception raising into a failed testcase). Returns
        the return value of func."""

class TransformTest(CythonTest):
    """
    Utility base class for transform unit tests. It is based around constructing
    test trees (either explicitly or by parsing a Cython code string); running
    the transform, serialize it using a customized Cython serializer (with
    special markup for nodes that cannot be represented in Cython),
    and do a string-comparison line-by-line of the result.

    To create a test case:
     - Call run_pipeline. The pipeline should at least contain the transform you
       are testing; pyx should be either a string (passed to the parser to
       create a post-parse tree) or a node representing input to pipeline.
       The result will be a transformed result.

     - Check that the tree is correct. If wanted, assertCode can be used, which
       takes a code string as expected, and a ModuleNode in result_tree
       (it serializes the ModuleNode to a string and compares line-by-line).

    All code strings are first stripped for whitespace lines and then common
    indentation.

    Plans: One could have a pxd dictionary parameter to run_pipeline.
    """
    def run_pipeline(self, pipeline, pyx, pxds: Incomplete | None = None): ...

class TreeAssertVisitor(VisitorTransform):
    def __init__(self) -> None: ...
    def create_c_file_validator(self): ...
    def visit_ModuleNode(self, node): ...
    def visit_CompilerDirectivesNode(self, node): ...
    visit_Node: Incomplete

def unpack_source_tree(tree_file, workdir, cython_root): ...
def write_file(file_path, content, dedent: bool = False, encoding: Incomplete | None = None) -> None:
    """Write some content (text or bytes) to the file
    at `file_path` without translating `'\\n'` into `os.linesep`.

    The default encoding is `'utf-8'`.
    """
def write_newer_file(file_path, newer_than, content, dedent: bool = False, encoding: Incomplete | None = None) -> None:
    """
    Write `content` to the file `file_path` without translating `'\\n'`
    into `os.linesep` and make sure it is newer than the file `newer_than`.

    The default encoding is `'utf-8'` (same as for `write_file`).
    """
