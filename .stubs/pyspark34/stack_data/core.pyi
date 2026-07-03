import ast
import executing
from _typeshed import Incomplete
from asttokens.util import Token as Token
from enum import Enum
from stack_data.utils import assert_ as assert_, cached_property as cached_property, collapse_repeated as collapse_repeated, frame_and_lineno as frame_and_lineno, group_by_key_func as group_by_key_func, is_frame as is_frame, iter_stack as iter_stack, line_range as line_range, truncate as truncate, unique_in_order as unique_in_order
from types import CodeType, FrameType, TracebackType
from typing import Any, Callable, Iterable, Iterator, List, Mapping, NamedTuple, Sequence, Tuple

class RangeInLine(NamedTuple):
    start: int
    end: int
    data: Any

class MarkerInLine(NamedTuple):
    position: int
    is_start: bool
    string: str

class BlankLines(Enum):
    """The values are intended to correspond to the following behaviour:
    HIDDEN: blank lines are not shown in the output
    VISIBLE: blank lines are visible in the output
    SINGLE: any consecutive blank lines are shown as a single blank line
            in the output. This option requires the line number to be shown.
            For a single blank line, the corresponding line number is shown.
            Two or more consecutive blank lines are shown as a single blank
            line in the output with a custom string shown instead of a
            specific line number.
    """
    HIDDEN: int
    VISIBLE: int
    SINGLE: int

class Variable(NamedTuple('_Variable', [('name', str), ('nodes', Sequence[ast.AST]), ('value', Any)])):
    """
    An expression that appears one or more times in source code and its associated value.
    This will usually be a variable but it can be any expression evaluated by pure_eval.
    - name is the source text of the expression.
    - nodes is a list of equivalent nodes representing the same expression.
    - value is the safely evaluated value of the expression.
    """
    __hash__: Incomplete
    __eq__: Incomplete

class Source(executing.Source):
    """
    The source code of a single file and associated metadata.

    In addition to the attributes from the base class executing.Source,
    if .tree is not None, meaning this is valid Python code, objects have:
        - pieces: a list of Piece objects
        - tokens_by_lineno: a defaultdict(list) mapping line numbers to lists of tokens.

    Don't construct this class. Get an instance from frame_info.source.
    """
    def pieces(self) -> List[range]: ...
    def tokens_by_lineno(self) -> Mapping[int, List[Token]]: ...
    def line_range(self, node: ast.AST) -> Tuple[int, int]: ...

class Options:
    """
    Configuration for FrameInfo, either in the constructor or the .stack_data classmethod.
    These all determine which Lines and gaps are produced by FrameInfo.lines. 

    before and after are the number of pieces of context to include in a frame
    in addition to the executing piece.

    include_signature is whether to include the function signature as a piece in a frame.

    If a piece (other than the executing piece) has more than max_lines_per_piece lines,
    it will be truncated with a gap in the middle. 
    """
    before: Incomplete
    after: Incomplete
    include_signature: Incomplete
    max_lines_per_piece: Incomplete
    pygments_formatter: Incomplete
    blank_lines: Incomplete
    def __init__(self, *, before: int = 3, after: int = 1, include_signature: bool = False, max_lines_per_piece: int = 6, pygments_formatter: Incomplete | None = None, blank_lines=...) -> None: ...

class LineGap:
    """
    A singleton representing one or more lines of source code that were skipped
    in FrameInfo.lines.

    LINE_GAP can be created in two ways:
    - by truncating a piece of context that's too long.
    - immediately after the signature piece if Options.include_signature is true
      and the following piece isn't already part of the included pieces. 
    """

LINE_GAP: Incomplete

class BlankLineRange:
    """
    Records the line number range for blank lines gaps between pieces.
    For a single blank line, begin_lineno == end_lineno.
    """
    begin_lineno: Incomplete
    end_lineno: Incomplete
    def __init__(self, begin_lineno: int, end_lineno: int) -> None: ...

class Line:
    """
    A single line of source code for a particular stack frame.

    Typically this is obtained from FrameInfo.lines.
    Since that list may also contain LINE_GAP, you should first check
    that this is really a Line before using it.

    Attributes:
        - frame_info
        - lineno: the 1-based line number within the file
        - text: the raw source of this line. For displaying text, see .render() instead.
        - leading_indent: the number of leading spaces that should probably be stripped.
            This attribute is set within FrameInfo.lines. If you construct this class
            directly you should probably set it manually (at least to 0).
        - is_current: whether this is the line currently being executed by the interpreter
            within this frame.
        - tokens: a list of source tokens in this line

    There are several helpers for constructing RangeInLines which can be converted to markers
    using markers_from_ranges which can be passed to .render():
        - token_ranges
        - variable_ranges
        - executing_node_ranges
        - range_from_node
    """
    frame_info: Incomplete
    lineno: Incomplete
    text: Incomplete
    leading_indent: Incomplete
    def __init__(self, frame_info: FrameInfo, lineno: int) -> None: ...
    @property
    def is_current(self) -> bool:
        """
        Whether this is the line currently being executed by the interpreter
        within this frame.
        """
    @property
    def tokens(self) -> List[Token]:
        """
        A list of source tokens in this line.
        The tokens are Token objects from asttokens:
        https://asttokens.readthedocs.io/en/latest/api-index.html#asttokens.util.Token
        """
    def token_ranges(self) -> List[RangeInLine]:
        """
        A list of RangeInLines for each token in .tokens,
        where range.data is a Token object from asttokens:
        https://asttokens.readthedocs.io/en/latest/api-index.html#asttokens.util.Token
        """
    def variable_ranges(self) -> List[RangeInLine]:
        """
        A list of RangeInLines for each Variable that appears at least partially in this line.
        The data attribute of the range is a pair (variable, node) where node is the particular
        AST node from the list variable.nodes that corresponds to this range.
        """
    def executing_node_ranges(self) -> List[RangeInLine]:
        """
        A list of one or zero RangeInLines for the executing node of this frame.
        The list will have one element if the node can be found and it overlaps this line.
        """
    def range_from_node(self, node: ast.AST, data: Any, common_indent: int = 0) -> RangeInLine | None:
        """
        If the given node overlaps with this line, return a RangeInLine
        with the correct start and end and the given data.
        Otherwise, return None.
        """
    def render(self, markers: Iterable[MarkerInLine] = (), *, strip_leading_indent: bool = True, pygmented: bool = False, escape_html: bool = False) -> str:
        """
        Produces a string for display consisting of .text
        with the .strings of each marker inserted at the correct positions.
        If strip_leading_indent is true (the default) then leading spaces
        common to all lines in this frame will be excluded.
        """

def markers_from_ranges(ranges: Iterable[RangeInLine], converter: Callable[[RangeInLine], Tuple[str, str] | None]) -> List[MarkerInLine]:
    """
    Helper to create MarkerInLines given some RangeInLines.
    converter should be a function accepting a RangeInLine returning
    either None (which is ignored) or a pair of strings which
    are used to create two markers included in the returned list.
    """
def style_with_executing_node(style, modifier): ...

class RepeatedFrames:
    """
    A sequence of consecutive stack frames which shouldn't be displayed because
    the same code and line number were repeated many times in the stack, e.g.
    because of deep recursion.

    Attributes:
        - frames: list of raw frame or traceback objects
        - frame_keys: list of tuples (frame.f_code, lineno) extracted from the frame objects.
                        It's this information from the frames that is used to determine
                        whether two frames should be considered similar (i.e. repeating).
        - description: A string briefly describing frame_keys
    """
    frames: Incomplete
    frame_keys: Incomplete
    def __init__(self, frames: List[FrameType | TracebackType], frame_keys: List[Tuple[CodeType, int]]) -> None: ...
    def description(self) -> str:
        """
        A string briefly describing the repeated frames, e.g.
            my_function at line 10 (100 times)
        """

class FrameInfo:
    """
    Information about a frame!
    Pass either a frame object or a traceback object,
    and optionally an Options object to configure.

    Or use the classmethod FrameInfo.stack_data() for an iterator of FrameInfo and
    RepeatedFrames objects. 

    Attributes:
        - frame: an actual stack frame object, either frame_or_tb or frame_or_tb.tb_frame
        - options
        - code: frame.f_code
        - source: a Source object
        - filename: a hopefully absolute file path derived from code.co_filename
        - scope: the AST node of the innermost function, class or module being executed
        - lines: a list of Line/LineGap objects to display, determined by options
        - executing: an Executing object from the `executing` library, which has:
            - .node: the AST node being executed in this frame, or None if it's unknown
            - .statements: a set of one or more candidate statements (AST nodes, probably just one)
                currently being executed in this frame.
            - .code_qualname(): the __qualname__ of the function or class being executed,
                or just the code name.

    Properties returning one or more pieces of source code (ranges of lines):
        - scope_pieces: all the pieces in the scope
        - included_pieces: a subset of scope_pieces determined by options
        - executing_piece: the piece currently being executed in this frame

    Properties returning lists of Variable objects:
        - variables: all variables in the scope
        - variables_by_lineno: variables organised into lines
        - variables_in_lines: variables contained within FrameInfo.lines
        - variables_in_executing_piece: variables contained within FrameInfo.executing_piece
    """
    executing: Incomplete
    frame: Incomplete
    code: Incomplete
    options: Incomplete
    source: Incomplete
    def __init__(self, frame_or_tb: FrameType | TracebackType, options: Options | None = None) -> None: ...
    @classmethod
    def stack_data(cls, frame_or_tb: FrameType | TracebackType, options: Options | None = None, *, collapse_repeated_frames: bool = True) -> Iterator[FrameInfo | RepeatedFrames]:
        """
        An iterator of FrameInfo and RepeatedFrames objects representing
        a full traceback or stack. Similar consecutive frames are collapsed into RepeatedFrames
        objects, so always check what type of object has been yielded.

        Pass either a frame object or a traceback object,
        and optionally an Options object to configure.
        """
    def scope_pieces(self) -> List[range]:
        """
        All the pieces (ranges of lines) contained in this object's .scope,
        unless there is no .scope (because the source isn't valid Python syntax)
        in which case it returns all the pieces in the source file, each containing one line.
        """
    def filename(self) -> str:
        """
        A hopefully absolute file path derived from .code.co_filename,
        the current working directory, and sys.path.
        Code based on ipython.
        """
    def executing_piece(self) -> range:
        """
        The piece (range of lines) containing the line currently being executed
        by the interpreter in this frame.
        """
    def included_pieces(self) -> List[range]:
        """
        The list of pieces (ranges of lines) to display for this frame.
        Consists of .executing_piece, surrounding context pieces
        determined by .options.before and .options.after,
        and the function signature if a function is being executed and
        .options.include_signature is True (in which case this might not
        be a contiguous range of pieces).
        Always a subset of .scope_pieces.
        """
    def lines(self) -> List[Line | LineGap | BlankLineRange]:
        """
        A list of lines to display, determined by options.
        The objects yielded either have type Line, BlankLineRange
        or are the singleton LINE_GAP.
        Always check the type that you're dealing with when iterating.

        LINE_GAP can be created in two ways:
            - by truncating a piece of context that's too long, determined by
                .options.max_lines_per_piece
            - immediately after the signature piece if Options.include_signature is true
              and the following piece isn't already part of the included pieces.

        The Line objects are all within the ranges from .included_pieces.
        """
    def scope(self) -> ast.AST | None:
        """
        The AST node of the innermost function, class or module being executed.
        """
    def variables(self) -> List[Variable]:
        """
        All Variable objects whose nodes are contained within .scope
        and whose values could be safely evaluated by pure_eval.
        """
    def variables_by_lineno(self) -> Mapping[int, List[Tuple[Variable, ast.AST]]]:
        """
        A mapping from 1-based line numbers to lists of pairs:
            - A Variable object
            - A specific AST node from the variable's .nodes list that's
                in the line at that line number.
        """
    def variables_in_lines(self) -> List[Variable]:
        """
        A list of Variable objects contained within the lines returned by .lines.
        """
    def variables_in_executing_piece(self) -> List[Variable]:
        """
        A list of Variable objects contained within the lines
        in the range returned by .executing_piece.
        """
