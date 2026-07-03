import ast
import types
from _typeshed import Incomplete
from asttokens import ASTText, ASTTokens as ASTTokens
from asttokens.asttokens import ASTTextBase as ASTTextBase
from collections import namedtuple as namedtuple
from dis import Instruction as _Instruction
from itertools import zip_longest as zip_longest
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Iterator, List, Sequence, Set, Tuple, Type, TypeVar

function_node_types: Tuple[Type, ...]
cache: Incomplete
text_type = str

class EnhancedAST(ast.AST):
    parent: EnhancedAST

class Instruction(_Instruction):
    lineno: int

class EnhancedInstruction(Instruction): ...

def assert_(condition: Any, message: str = '') -> None:
    """
    Like an assert statement, but unaffected by -O
    :param condition: value that is expected to be truthy
    :type message: Any
    """
def get_instructions(co: types.CodeType) -> Iterator[EnhancedInstruction]: ...

TESTING: int

class NotOneValueFound(Exception):
    values: Incomplete
    def __init__(self, msg: str, values: Sequence = []) -> None: ...
T = TypeVar('T')

def only(it: Iterable[T]) -> T: ...

class Source:
    """
    The source code of a single file and associated metadata.

    The main method of interest is the classmethod `executing(frame)`.

    If you want an instance of this class, don't construct it.
    Ideally use the classmethod `for_frame(frame)`.
    If you don't have a frame, use `for_filename(filename [, module_globals])`.
    These methods cache instances by filename, so at most one instance exists per filename.

    Attributes:
        - filename
        - text
        - lines
        - tree: AST parsed from text, or None if text is not valid Python
            All nodes in the tree have an extra `parent` attribute

    Other methods of interest:
        - statements_at_line
        - asttokens
        - code_qualname
    """
    filename: Incomplete
    text: Incomplete
    lines: Incomplete
    tree: Incomplete
    def __init__(self, filename: str, lines: Sequence[str]) -> None:
        """
        Don't call this constructor, see the class docstring.
        """
    @classmethod
    def for_frame(cls, frame: types.FrameType, use_cache: bool = True) -> Source:
        """
        Returns the `Source` object corresponding to the file the frame is executing in.
        """
    @classmethod
    def for_filename(cls, filename: str | Path, module_globals: Dict[str, Any] | None = None, use_cache: bool = True) -> Source: ...
    @classmethod
    def lazycache(cls, frame: types.FrameType) -> None: ...
    @classmethod
    def executing(cls, frame_or_tb: types.TracebackType | types.FrameType) -> Executing:
        """
        Returns an `Executing` object representing the operation
        currently executing in the given frame or traceback object.
        """
    def statements_at_line(self, lineno: int) -> Set[EnhancedAST]:
        """
        Returns the statement nodes overlapping the given line.

        Returns at most one statement unless semicolons are present.

        If the `text` attribute is not valid python, meaning
        `tree` is None, returns an empty set.

        Otherwise, `Source.for_frame(frame).statements_at_line(frame.f_lineno)`
        should return at least one statement.
        """
    def asttext(self) -> ASTText:
        """
        Returns an ASTText object for getting the source of specific AST nodes.

        See http://asttokens.readthedocs.io/en/latest/api-index.html
        """
    def asttokens(self) -> ASTTokens:
        """
        Returns an ASTTokens object for getting the source of specific AST nodes.

        See http://asttokens.readthedocs.io/en/latest/api-index.html
        """
    @staticmethod
    def decode_source(source: str | bytes) -> text_type: ...
    @staticmethod
    def detect_encoding(source: bytes) -> str: ...
    def code_qualname(self, code: types.CodeType) -> str:
        """
        Imitates the __qualname__ attribute of functions for code objects.
        Given:

            - A function `func`
            - A frame `frame` for an execution of `func`, meaning:
                `frame.f_code is func.__code__`

        `Source.for_frame(frame).code_qualname(frame.f_code)`
        will be equal to `func.__qualname__`*. Works for Python 2 as well,
        where of course no `__qualname__` attribute exists.

        Falls back to `code.co_name` if there is no appropriate qualname.

        Based on https://github.com/wbolster/qualname

        (* unless `func` is a lambda
        nested inside another lambda on the same line, in which case
        the outer lambda's qualname will be returned for the codes
        of both lambdas)
        """

class Executing:
    """
    Information about the operation a frame is currently executing.

    Generally you will just want `node`, which is the AST node being executed,
    or None if it's unknown.

    If a decorator is currently being called, then:
        - `node` is a function or class definition
        - `decorator` is the expression in `node.decorator_list` being called
        - `statements == {node}`
    """
    frame: Incomplete
    source: Incomplete
    node: Incomplete
    statements: Incomplete
    decorator: Incomplete
    def __init__(self, frame: types.FrameType, source: Source, node: EnhancedAST, stmts: Set[ast.stmt], decorator: EnhancedAST | None) -> None: ...
    def code_qualname(self) -> str: ...
    def text(self) -> str: ...
    def text_range(self) -> Tuple[int, int]: ...

class QualnameVisitor(ast.NodeVisitor):
    stack: Incomplete
    qualnames: Incomplete
    def __init__(self) -> None: ...
    def add_qualname(self, node: ast.AST, name: str | None = None) -> None: ...
    def visit_FunctionDef(self, node: ast.AST, name: str | None = None) -> None: ...
    visit_AsyncFunctionDef = visit_FunctionDef
    def visit_Lambda(self, node: ast.AST) -> None: ...
    def visit_ClassDef(self, node: ast.AST) -> None: ...

future_flags: Incomplete

def compile_similar_to(source: ast.Module, matching_code: types.CodeType) -> Any: ...

sentinel: str

def is_rewritten_by_pytest(code: types.CodeType) -> bool: ...

class SentinelNodeFinder:
    result: EnhancedAST
    frame: Incomplete
    tree: Incomplete
    code: Incomplete
    is_pytest: Incomplete
    ignore_linenos: Incomplete
    decorator: Incomplete
    instruction: Incomplete
    def __init__(self, frame: types.FrameType, stmts: Set[EnhancedAST], tree: ast.Module, lasti: int, source: Source) -> None: ...
    def find_decorator(self, stmts: List[EnhancedAST] | Set[EnhancedAST]) -> None: ...
    def clean_instructions(self, code: types.CodeType) -> List[EnhancedInstruction]: ...
    def get_original_clean_instructions(self) -> List[EnhancedInstruction]: ...
    def matching_nodes(self, exprs: Set[EnhancedAST]) -> Iterator[EnhancedAST]: ...
    def compile_instructions(self) -> List[EnhancedInstruction]: ...
    def find_codes(self, root_code: types.CodeType) -> list: ...
    def get_actual_current_instruction(self, lasti: int) -> EnhancedInstruction:
        """
        Get the instruction corresponding to the current
        frame offset, skipping EXTENDED_ARG instructions
        """

def non_sentinel_instructions(instructions: List[EnhancedInstruction], start: int) -> Iterator[Tuple[int, EnhancedInstruction]]:
    """
    Yields (index, instruction) pairs excluding the basic
    instructions introduced by the sentinel transformation
    """
def walk_both_instructions(original_instructions: List[EnhancedInstruction], original_start: int, instructions: List[EnhancedInstruction], start: int) -> Iterator[Tuple[int, EnhancedInstruction, int, EnhancedInstruction]]:
    """
    Yields matching indices and instructions from the new and original instructions,
    leaving out changes made by the sentinel transformation.
    """
def handle_jumps(instructions: List[EnhancedInstruction], original_instructions: List[EnhancedInstruction]) -> None:
    """
    Transforms instructions in place until it looks more like original_instructions.
    This is only needed in 3.10+ where optimisations lead to more drastic changes
    after the sentinel transformation.
    Replaces JUMP instructions that aren't also present in original_instructions
    with the sections that they jump to until a raise or return.
    In some other cases duplication found in `original_instructions`
    is replicated in `instructions`.
    """
def find_new_matching(orig_section: List[EnhancedInstruction], instructions: List[EnhancedInstruction]) -> Iterator[List[EnhancedInstruction]]:
    """
    Yields sections of `instructions` which match `orig_section`.
    The yielded sections include sentinel instructions, but these
    are ignored when checking for matches.
    """
def handle_jump(original_instructions: List[EnhancedInstruction], original_start: int, instructions: List[EnhancedInstruction], start: int) -> List[EnhancedInstruction] | None:
    """
    Returns the section of instructions starting at `start` and ending
    with a RETURN_VALUE or RAISE_VARARGS instruction.
    There should be a matching section in original_instructions starting at original_start.
    If that section doesn't appear elsewhere in original_instructions,
    then also delete the returned section of instructions.
    """
def check_duplicates(original_i: int, orig_section: List[EnhancedInstruction], original_instructions: List[EnhancedInstruction]) -> bool:
    """
    Returns True if a section of original_instructions starting somewhere other
    than original_i and matching orig_section is found, i.e. orig_section is duplicated.
    """
def sections_match(orig_section: List[EnhancedInstruction], dup_section: List[EnhancedInstruction]) -> bool:
    """
    Returns True if the given lists of instructions have matching linenos and opnames.
    """
def opnames_match(inst1: Instruction, inst2: Instruction) -> bool: ...
def get_setter(node: EnhancedAST) -> Callable[[ast.AST], None] | None: ...

lock: Incomplete

def statement_containing_node(node: ast.AST) -> EnhancedAST: ...
def assert_linenos(tree: ast.AST) -> Iterator[int]: ...
def is_ipython_cell_code_name(code_name: str) -> bool: ...
def is_ipython_cell_filename(filename: str) -> bool: ...
def is_ipython_cell_code(code_obj: types.CodeType) -> bool: ...
def find_node_ipython(frame: types.FrameType, lasti: int, stmts: Set[EnhancedAST], source: Source) -> Tuple[Any | None, Any | None]: ...
def attr_names_match(attr: str, argval: str) -> bool:
    """
    Checks that the user-visible attr (from ast) can correspond to
    the argval in the bytecode, i.e. the real attribute fetched internally,
    which may be mangled for private attributes.
    """
def node_linenos(node: ast.AST) -> Iterator[int]: ...
NodeFinder = SentinelNodeFinder
