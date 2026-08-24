from .exceptions import *
from .actions import *
import abc
import re
import typing
from .results import ParseResults as ParseResults
from .unicode import pyparsing_unicode as pyparsing_unicode
from .util import __config_flags
from _typeshed import Incomplete
from abc import ABC
from enum import Enum
from functools import cached_property as cached_property
from pathlib import Path
from typing import Any, Callable, Generator, List, NamedTuple, Sequence, Set, TextIO, Tuple

str_type: Tuple[type, ...]

class __compat__(__config_flags):
    """
    A cross-version compatibility configuration for pyparsing features that will be
    released in a future version. By setting values in this configuration to True,
    those features can be enabled in prior versions for compatibility development
    and testing.

    - ``collect_all_And_tokens`` - flag to enable fix for Issue #63 that fixes erroneous grouping
      of results names when an :class:`And` expression is nested within an :class:`Or` or :class:`MatchFirst`;
      maintained for compatibility, but setting to ``False`` no longer restores pre-2.3.1
      behavior
    """
    collect_all_And_tokens: bool

class __diag__(__config_flags):
    warn_multiple_tokens_in_named_alternation: bool
    warn_ungrouped_named_tokens_in_collection: bool
    warn_name_set_on_empty_Forward: bool
    warn_on_parse_using_empty_Forward: bool
    warn_on_assignment_to_Forward: bool
    warn_on_multiple_string_args_to_oneof: bool
    warn_on_match_first_with_lshift_operator: bool
    enable_debug_on_named_expressions: bool
    @classmethod
    def enable_all_warnings(cls) -> None: ...

class Diagnostics(Enum):
    """
    Diagnostic configuration (all default to disabled)
    - ``warn_multiple_tokens_in_named_alternation`` - flag to enable warnings when a results
      name is defined on a :class:`MatchFirst` or :class:`Or` expression with one or more :class:`And` subexpressions
    - ``warn_ungrouped_named_tokens_in_collection`` - flag to enable warnings when a results
      name is defined on a containing expression with ungrouped subexpressions that also
      have results names
    - ``warn_name_set_on_empty_Forward`` - flag to enable warnings when a :class:`Forward` is defined
      with a results name, but has no contents defined
    - ``warn_on_parse_using_empty_Forward`` - flag to enable warnings when a :class:`Forward` is
      defined in a grammar but has never had an expression attached to it
    - ``warn_on_assignment_to_Forward`` - flag to enable warnings when a :class:`Forward` is defined
      but is overwritten by assigning using ``'='`` instead of ``'<<='`` or ``'<<'``
    - ``warn_on_multiple_string_args_to_oneof`` - flag to enable warnings when :class:`one_of` is
      incorrectly called with multiple str arguments
    - ``enable_debug_on_named_expressions`` - flag to auto-enable debug on all subsequent
      calls to :class:`ParserElement.set_name`

    Diagnostics are enabled/disabled by calling :class:`enable_diag` and :class:`disable_diag`.
    All warnings can be enabled by calling :class:`enable_all_warnings`.
    """
    warn_multiple_tokens_in_named_alternation: int
    warn_ungrouped_named_tokens_in_collection: int
    warn_name_set_on_empty_Forward: int
    warn_on_parse_using_empty_Forward: int
    warn_on_assignment_to_Forward: int
    warn_on_multiple_string_args_to_oneof: int
    warn_on_match_first_with_lshift_operator: int
    enable_debug_on_named_expressions: int

def enable_diag(diag_enum: Diagnostics) -> None:
    """
    Enable a global pyparsing diagnostic flag (see :class:`Diagnostics`).
    """
def disable_diag(diag_enum: Diagnostics) -> None:
    """
    Disable a global pyparsing diagnostic flag (see :class:`Diagnostics`).
    """
def enable_all_warnings() -> None:
    """
    Enable all global pyparsing diagnostic warnings (see :class:`Diagnostics`).
    """
ParseAction = Callable[[], Any] | Callable[[ParseResults], Any] | Callable[[int, ParseResults], Any] | Callable[[str, int, ParseResults], Any]
ParseCondition = Callable[[], bool] | Callable[[ParseResults], bool] | Callable[[int, ParseResults], bool] | Callable[[str, int, ParseResults], bool]
ParseFailAction: Incomplete
DebugStartAction: Incomplete
DebugSuccessAction: Incomplete
DebugExceptionAction: Incomplete
alphas: Incomplete
identchars: Incomplete
identbodychars: Incomplete
nums: str
hexnums: Incomplete
alphanums: Incomplete
printables: Incomplete

def condition_as_parse_action(fn: ParseCondition, message: str = None, fatal: bool = False) -> ParseAction:
    """
    Function to convert a simple predicate function that returns ``True`` or ``False``
    into a parse action. Can be used in places when a parse action is required
    and :class:`ParserElement.add_condition` cannot be used (such as when adding a condition
    to an operator level in :class:`infix_notation`).

    Optional keyword arguments:

    - ``message`` - define a custom message to be used in the raised exception
    - ``fatal`` - if True, will raise :class:`ParseFatalException` to stop parsing immediately;
      otherwise will raise :class:`ParseException`

    """
def null_debug_action(*args) -> None:
    """'Do-nothing' debug action, to suppress debugging output during parsing."""

class ParserElement(ABC, metaclass=abc.ABCMeta):
    """Abstract base level parser element class."""
    DEFAULT_WHITE_CHARS: str
    verbose_stacktrace: bool
    @staticmethod
    def set_default_whitespace_chars(chars: str) -> None:
        '''
        Overrides the default whitespace chars

        Example::

            # default whitespace chars are space, <TAB> and newline
            Word(alphas)[1, ...].parse_string("abc def\\nghi jkl")  # -> [\'abc\', \'def\', \'ghi\', \'jkl\']

            # change to just treat newline as significant
            ParserElement.set_default_whitespace_chars(" \\t")
            Word(alphas)[1, ...].parse_string("abc def\\nghi jkl")  # -> [\'abc\', \'def\']
        '''
    @staticmethod
    def inline_literals_using(cls) -> None:
        '''
        Set class to be used for inclusion of string literals into a parser.

        Example::

            # default literal class used is Literal
            integer = Word(nums)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            date_str.parse_string("1999/12/31")  # -> [\'1999\', \'/\', \'12\', \'/\', \'31\']


            # change to Suppress
            ParserElement.inline_literals_using(Suppress)
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")

            date_str.parse_string("1999/12/31")  # -> [\'1999\', \'12\', \'31\']
        '''
    class DebugActions(NamedTuple):
        debug_try: DebugStartAction | None
        debug_match: DebugSuccessAction | None
        debug_fail: DebugExceptionAction | None
    parseAction: Incomplete
    failAction: Incomplete
    customName: Incomplete
    resultsName: Incomplete
    saveAsList: Incomplete
    skipWhitespace: bool
    whiteChars: Incomplete
    copyDefaultWhiteChars: bool
    mayReturnEmpty: bool
    keepTabs: bool
    ignoreExprs: Incomplete
    debug: bool
    streamlined: bool
    mayIndexError: bool
    errmsg: str
    modalResults: bool
    debugActions: Incomplete
    callPreparse: bool
    callDuringTry: bool
    suppress_warnings_: Incomplete
    def __init__(self, savelist: bool = False) -> None: ...
    def suppress_warning(self, warning_type: Diagnostics) -> ParserElement:
        '''
        Suppress warnings emitted for a particular diagnostic on this expression.

        Example::

            base = pp.Forward()
            base.suppress_warning(Diagnostics.warn_on_parse_using_empty_Forward)

            # statement would normally raise a warning, but is now suppressed
            print(base.parseString("x"))

        '''
    def copy(self) -> ParserElement:
        '''
        Make a copy of this :class:`ParserElement`.  Useful for defining
        different parse actions for the same parsing pattern, using copies of
        the original parse element.

        Example::

            integer = Word(nums).set_parse_action(lambda toks: int(toks[0]))
            integerK = integer.copy().add_parse_action(lambda toks: toks[0] * 1024) + Suppress("K")
            integerM = integer.copy().add_parse_action(lambda toks: toks[0] * 1024 * 1024) + Suppress("M")

            print((integerK | integerM | integer)[1, ...].parse_string("5K 100 640K 256M"))

        prints::

            [5120, 100, 655360, 268435456]

        Equivalent form of ``expr.copy()`` is just ``expr()``::

            integerM = integer().add_parse_action(lambda toks: toks[0] * 1024 * 1024) + Suppress("M")
        '''
    def set_results_name(self, name: str, list_all_matches: bool = False, *, listAllMatches: bool = False) -> ParserElement:
        '''
        Define name for referencing matching tokens as a nested attribute
        of the returned parse results.

        Normally, results names are assigned as you would assign keys in a dict:
        any existing value is overwritten by later values. If it is necessary to
        keep all values captured for a particular results name, call ``set_results_name``
        with ``list_all_matches`` = True.

        NOTE: ``set_results_name`` returns a *copy* of the original :class:`ParserElement` object;
        this is so that the client can define a basic element, such as an
        integer, and reference it in multiple places with different names.

        You can also set results names using the abbreviated syntax,
        ``expr("name")`` in place of ``expr.set_results_name("name")``
        - see :class:`__call__`. If ``list_all_matches`` is required, use
        ``expr("name*")``.

        Example::

            date_str = (integer.set_results_name("year") + \'/\'
                        + integer.set_results_name("month") + \'/\'
                        + integer.set_results_name("day"))

            # equivalent form:
            date_str = integer("year") + \'/\' + integer("month") + \'/\' + integer("day")
        '''
    def set_break(self, break_flag: bool = True) -> ParserElement:
        """
        Method to invoke the Python pdb debugger when this element is
        about to be parsed. Set ``break_flag`` to ``True`` to enable, ``False`` to
        disable.
        """
    def set_parse_action(self, *fns: ParseAction, **kwargs) -> ParserElement:
        '''
        Define one or more actions to perform when successfully matching parse element definition.

        Parse actions can be called to perform data conversions, do extra validation,
        update external data structures, or enhance or replace the parsed tokens.
        Each parse action ``fn`` is a callable method with 0-3 arguments, called as
        ``fn(s, loc, toks)`` , ``fn(loc, toks)`` , ``fn(toks)`` , or just ``fn()`` , where:

        - s   = the original string being parsed (see note below)
        - loc = the location of the matching substring
        - toks = a list of the matched tokens, packaged as a :class:`ParseResults` object

        The parsed tokens are passed to the parse action as ParseResults. They can be
        modified in place using list-style append, extend, and pop operations to update
        the parsed list elements; and with dictionary-style item set and del operations
        to add, update, or remove any named results. If the tokens are modified in place,
        it is not necessary to return them with a return statement.

        Parse actions can also completely replace the given tokens, with another ``ParseResults``
        object, or with some entirely different object (common for parse actions that perform data
        conversions). A convenient way to build a new parse result is to define the values
        using a dict, and then create the return value using :class:`ParseResults.from_dict`.

        If None is passed as the ``fn`` parse action, all previously added parse actions for this
        expression are cleared.

        Optional keyword arguments:

        - call_during_try = (default= ``False``) indicate if parse action should be run during
          lookaheads and alternate testing. For parse actions that have side effects, it is
          important to only call the parse action once it is determined that it is being
          called as part of a successful parse. For parse actions that perform additional
          validation, then call_during_try should be passed as True, so that the validation
          code is included in the preliminary "try" parses.

        Note: the default parsing behavior is to expand tabs in the input string
        before starting the parsing process.  See :class:`parse_string` for more
        information on parsing strings containing ``<TAB>`` s, and suggested
        methods to maintain a consistent view of the parsed string, the parse
        location, and line and column positions within the parsed string.

        Example::

            # parse dates in the form YYYY/MM/DD

            # use parse action to convert toks from str to int at parse time
            def convert_to_int(toks):
                return int(toks[0])

            # use a parse action to verify that the date is a valid date
            def is_valid_date(instring, loc, toks):
                from datetime import date
                year, month, day = toks[::2]
                try:
                    date(year, month, day)
                except ValueError:
                    raise ParseException(instring, loc, "invalid date given")

            integer = Word(nums)
            date_str = integer + \'/\' + integer + \'/\' + integer

            # add parse actions
            integer.set_parse_action(convert_to_int)
            date_str.set_parse_action(is_valid_date)

            # note that integer fields are now ints, not strings
            date_str.run_tests(\'\'\'
                # successful parse - note that integer fields were converted to ints
                1999/12/31

                # fail - invalid date
                1999/13/31
                \'\'\')
        '''
    def add_parse_action(self, *fns: ParseAction, **kwargs) -> ParserElement:
        """
        Add one or more parse actions to expression's list of parse actions. See :class:`set_parse_action`.

        See examples in :class:`copy`.
        """
    def add_condition(self, *fns: ParseCondition, **kwargs) -> ParserElement:
        '''Add a boolean predicate function to expression\'s list of parse actions. See
        :class:`set_parse_action` for function call signatures. Unlike ``set_parse_action``,
        functions passed to ``add_condition`` need to return boolean success/fail of the condition.

        Optional keyword arguments:

        - message = define a custom message to be used in the raised exception
        - fatal = if True, will raise ParseFatalException to stop parsing immediately; otherwise will raise
          ParseException
        - call_during_try = boolean to indicate if this method should be called during internal tryParse calls,
          default=False

        Example::

            integer = Word(nums).set_parse_action(lambda toks: int(toks[0]))
            year_int = integer.copy()
            year_int.add_condition(lambda toks: toks[0] >= 2000, message="Only support years 2000 and later")
            date_str = year_int + \'/\' + integer + \'/\' + integer

            result = date_str.parse_string("1999/12/31")  # -> Exception: Only support years 2000 and later (at char 0),
                                                                         (line:1, col:1)
        '''
    def set_fail_action(self, fn: ParseFailAction) -> ParserElement:
        """
        Define action to perform if parsing fails at this expression.
        Fail acton fn is a callable function that takes the arguments
        ``fn(s, loc, expr, err)`` where:

        - s = string being parsed
        - loc = location where expression match was attempted and failed
        - expr = the parse expression that failed
        - err = the exception thrown

        The function returns no value.  It may throw :class:`ParseFatalException`
        if it is desired to stop parsing immediately."""
    def preParse(self, instring, loc): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def postParse(self, instring, loc, tokenlist): ...
    def try_parse(self, instring: str, loc: int, raise_fatal: bool = False) -> int: ...
    def can_parse_next(self, instring: str, loc: int) -> bool: ...
    recursion_lock: Incomplete
    recursion_memos: typing.Dict[Tuple[int, 'Forward', bool], Tuple[int, ParseResults | Exception]]
    packrat_cache: Incomplete
    packrat_cache_lock: Incomplete
    packrat_cache_stats: Incomplete
    @staticmethod
    def reset_cache() -> None: ...
    @staticmethod
    def disable_memoization() -> None:
        """
        Disables active Packrat or Left Recursion parsing and their memoization

        This method also works if neither Packrat nor Left Recursion are enabled.
        This makes it safe to call before activating Packrat nor Left Recursion
        to clear any previous settings.
        """
    @staticmethod
    def enable_left_recursion(cache_size_limit: int | None = None, *, force: bool = False) -> None:
        '''
        Enables "bounded recursion" parsing, which allows for both direct and indirect
        left-recursion. During parsing, left-recursive :class:`Forward` elements are
        repeatedly matched with a fixed recursion depth that is gradually increased
        until finding the longest match.

        Example::

            import pyparsing as pp
            pp.ParserElement.enable_left_recursion()

            E = pp.Forward("E")
            num = pp.Word(pp.nums)
            # match `num`, or `num \'+\' num`, or `num \'+\' num \'+\' num`, ...
            E <<= E + \'+\' - num | num

            print(E.parse_string("1+2+3"))

        Recursion search naturally memoizes matches of ``Forward`` elements and may
        thus skip reevaluation of parse actions during backtracking. This may break
        programs with parse actions which rely on strict ordering of side-effects.

        Parameters:

        - cache_size_limit - (default=``None``) - memoize at most this many
          ``Forward`` elements during matching; if ``None`` (the default),
          memoize all ``Forward`` elements.

        Bounded Recursion parsing works similar but not identical to Packrat parsing,
        thus the two cannot be used together. Use ``force=True`` to disable any
        previous, conflicting settings.
        '''
    @staticmethod
    def enable_packrat(cache_size_limit: int = 128, *, force: bool = False) -> None:
        '''
        Enables "packrat" parsing, which adds memoizing to the parsing logic.
        Repeated parse attempts at the same string location (which happens
        often in many complex grammars) can immediately return a cached value,
        instead of re-executing parsing/validating code.  Memoizing is done of
        both valid results and parsing exceptions.

        Parameters:

        - cache_size_limit - (default= ``128``) - if an integer value is provided
          will limit the size of the packrat cache; if None is passed, then
          the cache size will be unbounded; if 0 is passed, the cache will
          be effectively disabled.

        This speedup may break existing programs that use parse actions that
        have side-effects.  For this reason, packrat parsing is disabled when
        you first import pyparsing.  To activate the packrat feature, your
        program must call the class method :class:`ParserElement.enable_packrat`.
        For best results, call ``enable_packrat()`` immediately after
        importing pyparsing.

        Example::

            import pyparsing
            pyparsing.ParserElement.enable_packrat()

        Packrat parsing works similar but not identical to Bounded Recursion parsing,
        thus the two cannot be used together. Use ``force=True`` to disable any
        previous, conflicting settings.
        '''
    def parse_string(self, instring: str, parse_all: bool = False, *, parseAll: bool = False) -> ParseResults:
        """
        Parse a string with respect to the parser definition. This function is intended as the primary interface to the
        client code.

        :param instring: The input string to be parsed.
        :param parse_all: If set, the entire input string must match the grammar.
        :param parseAll: retained for pre-PEP8 compatibility, will be removed in a future release.
        :raises ParseException: Raised if ``parse_all`` is set and the input string does not match the whole grammar.
        :returns: the parsed data as a :class:`ParseResults` object, which may be accessed as a `list`, a `dict`, or
          an object with attributes if the given parser includes results names.

        If the input string is required to match the entire grammar, ``parse_all`` flag must be set to ``True``. This
        is also equivalent to ending the grammar with :class:`StringEnd`().

        To report proper column numbers, ``parse_string`` operates on a copy of the input string where all tabs are
        converted to spaces (8 spaces per tab, as per the default in ``string.expandtabs``). If the input string
        contains tabs and the grammar uses parse actions that use the ``loc`` argument to index into the string
        being parsed, one can ensure a consistent view of the input string by doing one of the following:

        - calling ``parse_with_tabs`` on your grammar before calling ``parse_string`` (see :class:`parse_with_tabs`),
        - define your parse action using the full ``(s,loc,toks)`` signature, and reference the input string using the
          parse action's ``s`` argument, or
        - explicitly expand the tabs in your input string before calling ``parse_string``.

        Examples:

        By default, partial matches are OK.

        >>> res = Word('a').parse_string('aaaaabaaa')
        >>> print(res)
        ['aaaaa']

        The parsing behavior varies by the inheriting class of this abstract class. Please refer to the children
        directly to see more examples.

        It raises an exception if parse_all flag is set and instring does not match the whole grammar.

        >>> res = Word('a').parse_string('aaaaabaaa', parse_all=True)
        Traceback (most recent call last):
        ...
        pyparsing.ParseException: Expected end of text, found 'b'  (at char 5), (line:1, col:6)
        """
    def scan_string(self, instring: str, max_matches: int = ..., overlap: bool = False, *, debug: bool = False, maxMatches: int = ...) -> Generator[Tuple[ParseResults, int, int], None, None]:
        '''
        Scan the input string for expression matches.  Each match will return the
        matching tokens, start location, and end location.  May be called with optional
        ``max_matches`` argument, to clip scanning after \'n\' matches are found.  If
        ``overlap`` is specified, then overlapping matches will be reported.

        Note that the start and end locations are reported relative to the string
        being parsed.  See :class:`parse_string` for more information on parsing
        strings with embedded tabs.

        Example::

            source = "sldjf123lsdjjkf345sldkjf879lkjsfd987"
            print(source)
            for tokens, start, end in Word(alphas).scan_string(source):
                print(\' \'*start + \'^\'*(end-start))
                print(\' \'*start + tokens[0])

        prints::

            sldjf123lsdjjkf345sldkjf879lkjsfd987
            ^^^^^
            sldjf
                    ^^^^^^^
                    lsdjjkf
                              ^^^^^^
                              sldkjf
                                       ^^^^^^
                                       lkjsfd
        '''
    def transform_string(self, instring: str, *, debug: bool = False) -> str:
        '''
        Extension to :class:`scan_string`, to modify matching text with modified tokens that may
        be returned from a parse action.  To use ``transform_string``, define a grammar and
        attach a parse action to it that modifies the returned token list.
        Invoking ``transform_string()`` on a target string will then scan for matches,
        and replace the matched text patterns according to the logic in the parse
        action.  ``transform_string()`` returns the resulting transformed string.

        Example::

            wd = Word(alphas)
            wd.set_parse_action(lambda toks: toks[0].title())

            print(wd.transform_string("now is the winter of our discontent made glorious summer by this sun of york."))

        prints::

            Now Is The Winter Of Our Discontent Made Glorious Summer By This Sun Of York.
        '''
    def search_string(self, instring: str, max_matches: int = ..., *, debug: bool = False, maxMatches: int = ...) -> ParseResults:
        '''
        Another extension to :class:`scan_string`, simplifying the access to the tokens found
        to match the given parse expression.  May be called with optional
        ``max_matches`` argument, to clip searching after \'n\' matches are found.

        Example::

            # a capitalized word starts with an uppercase letter, followed by zero or more lowercase letters
            cap_word = Word(alphas.upper(), alphas.lower())

            print(cap_word.search_string("More than Iron, more than Lead, more than Gold I need Electricity"))

            # the sum() builtin can be used to merge results into a single ParseResults object
            print(sum(cap_word.search_string("More than Iron, more than Lead, more than Gold I need Electricity")))

        prints::

            [[\'More\'], [\'Iron\'], [\'Lead\'], [\'Gold\'], [\'I\'], [\'Electricity\']]
            [\'More\', \'Iron\', \'Lead\', \'Gold\', \'I\', \'Electricity\']
        '''
    def split(self, instring: str, maxsplit: int = ..., include_separators: bool = False, *, includeSeparators: bool = False) -> Generator[str, None, None]:
        '''
        Generator method to split a string using the given expression as a separator.
        May be called with optional ``maxsplit`` argument, to limit the number of splits;
        and the optional ``include_separators`` argument (default= ``False``), if the separating
        matching text should be included in the split results.

        Example::

            punc = one_of(list(".,;:/-!?"))
            print(list(punc.split("This, this?, this sentence, is badly punctuated!")))

        prints::

            [\'This\', \' this\', \'\', \' this sentence\', \' is badly punctuated\', \'\']
        '''
    def __add__(self, other) -> ParserElement:
        '''
        Implementation of ``+`` operator - returns :class:`And`. Adding strings to a :class:`ParserElement`
        converts them to :class:`Literal`s by default.

        Example::

            greet = Word(alphas) + "," + Word(alphas) + "!"
            hello = "Hello, World!"
            print(hello, "->", greet.parse_string(hello))

        prints::

            Hello, World! -> [\'Hello\', \',\', \'World\', \'!\']

        ``...`` may be used as a parse expression as a short form of :class:`SkipTo`.

            Literal(\'start\') + ... + Literal(\'end\')

        is equivalent to:

            Literal(\'start\') + SkipTo(\'end\')("_skipped*") + Literal(\'end\')

        Note that the skipped text is returned with \'_skipped\' as a results name,
        and to support having multiple skips in the same parser, the value returned is
        a list of all skipped text.
        '''
    def __radd__(self, other) -> ParserElement:
        """
        Implementation of ``+`` operator when left operand is not a :class:`ParserElement`
        """
    def __sub__(self, other) -> ParserElement:
        """
        Implementation of ``-`` operator, returns :class:`And` with error stop
        """
    def __rsub__(self, other) -> ParserElement:
        """
        Implementation of ``-`` operator when left operand is not a :class:`ParserElement`
        """
    def __mul__(self, other) -> ParserElement:
        '''
        Implementation of ``*`` operator, allows use of ``expr * 3`` in place of
        ``expr + expr + expr``.  Expressions may also be multiplied by a 2-integer
        tuple, similar to ``{min, max}`` multipliers in regular expressions.  Tuples
        may also include ``None`` as in:
        - ``expr*(n, None)`` or ``expr*(n, )`` is equivalent
             to ``expr*n + ZeroOrMore(expr)``
             (read as "at least n instances of ``expr``")
        - ``expr*(None, n)`` is equivalent to ``expr*(0, n)``
             (read as "0 to n instances of ``expr``")
        - ``expr*(None, None)`` is equivalent to ``ZeroOrMore(expr)``
        - ``expr*(1, None)`` is equivalent to ``OneOrMore(expr)``

        Note that ``expr*(None, n)`` does not raise an exception if
        more than n exprs exist in the input stream; that is,
        ``expr*(None, n)`` does not enforce a maximum number of expr
        occurrences.  If this behavior is desired, then write
        ``expr*(None, n) + ~expr``
        '''
    def __rmul__(self, other) -> ParserElement: ...
    def __or__(self, other) -> ParserElement:
        """
        Implementation of ``|`` operator - returns :class:`MatchFirst`
        """
    def __ror__(self, other) -> ParserElement:
        """
        Implementation of ``|`` operator when left operand is not a :class:`ParserElement`
        """
    def __xor__(self, other) -> ParserElement:
        """
        Implementation of ``^`` operator - returns :class:`Or`
        """
    def __rxor__(self, other) -> ParserElement:
        """
        Implementation of ``^`` operator when left operand is not a :class:`ParserElement`
        """
    def __and__(self, other) -> ParserElement:
        """
        Implementation of ``&`` operator - returns :class:`Each`
        """
    def __rand__(self, other) -> ParserElement:
        """
        Implementation of ``&`` operator when left operand is not a :class:`ParserElement`
        """
    def __invert__(self) -> ParserElement:
        """
        Implementation of ``~`` operator - returns :class:`NotAny`
        """
    __iter__: Incomplete
    def __getitem__(self, key):
        '''
        use ``[]`` indexing notation as a short form for expression repetition:

        - ``expr[n]`` is equivalent to ``expr*n``
        - ``expr[m, n]`` is equivalent to ``expr*(m, n)``
        - ``expr[n, ...]`` or ``expr[n,]`` is equivalent
             to ``expr*n + ZeroOrMore(expr)``
             (read as "at least n instances of ``expr``")
        - ``expr[..., n]`` is equivalent to ``expr*(0, n)``
             (read as "0 to n instances of ``expr``")
        - ``expr[...]`` and ``expr[0, ...]`` are equivalent to ``ZeroOrMore(expr)``
        - ``expr[1, ...]`` is equivalent to ``OneOrMore(expr)``

        ``None`` may be used in place of ``...``.

        Note that ``expr[..., n]`` and ``expr[m, n]``do not raise an exception
        if more than ``n`` ``expr``s exist in the input stream.  If this behavior is
        desired, then write ``expr[..., n] + ~expr``.
        '''
    def __call__(self, name: str = None) -> ParserElement:
        '''
        Shortcut for :class:`set_results_name`, with ``list_all_matches=False``.

        If ``name`` is given with a trailing ``\'*\'`` character, then ``list_all_matches`` will be
        passed as ``True``.

        If ``name` is omitted, same as calling :class:`copy`.

        Example::

            # these are equivalent
            userdata = Word(alphas).set_results_name("name") + Word(nums + "-").set_results_name("socsecno")
            userdata = Word(alphas)("name") + Word(nums + "-")("socsecno")
        '''
    def suppress(self) -> ParserElement:
        """
        Suppresses the output of this :class:`ParserElement`; useful to keep punctuation from
        cluttering up returned output.
        """
    def ignore_whitespace(self, recursive: bool = True) -> ParserElement:
        """
        Enables the skipping of whitespace before matching the characters in the
        :class:`ParserElement`'s defined pattern.

        :param recursive: If ``True`` (the default), also enable whitespace skipping in child elements (if any)
        """
    def leave_whitespace(self, recursive: bool = True) -> ParserElement:
        """
        Disables the skipping of whitespace before matching the characters in the
        :class:`ParserElement`'s defined pattern.  This is normally only used internally by
        the pyparsing module, but may be needed in some whitespace-sensitive grammars.

        :param recursive: If true (the default), also disable whitespace skipping in child elements (if any)
        """
    def set_whitespace_chars(self, chars: Set[str] | str, copy_defaults: bool = False) -> ParserElement:
        """
        Overrides the default whitespace chars
        """
    def parse_with_tabs(self) -> ParserElement:
        """
        Overrides default behavior to expand ``<TAB>`` s to spaces before parsing the input string.
        Must be called before ``parse_string`` when the input grammar contains elements that
        match ``<TAB>`` characters.
        """
    def ignore(self, other: ParserElement) -> ParserElement:
        """
        Define expression to be ignored (e.g., comments) while doing pattern
        matching; may be called repeatedly, to define multiple comment or other
        ignorable patterns.

        Example::

            patt = Word(alphas)[1, ...]
            patt.parse_string('ablaj /* comment */ lskjd')
            # -> ['ablaj']

            patt.ignore(c_style_comment)
            patt.parse_string('ablaj /* comment */ lskjd')
            # -> ['ablaj', 'lskjd']
        """
    def set_debug_actions(self, start_action: DebugStartAction, success_action: DebugSuccessAction, exception_action: DebugExceptionAction) -> ParserElement:
        """
        Customize display of debugging messages while doing pattern matching:

        - ``start_action`` - method to be called when an expression is about to be parsed;
          should have the signature ``fn(input_string: str, location: int, expression: ParserElement, cache_hit: bool)``

        - ``success_action`` - method to be called when an expression has successfully parsed;
          should have the signature ``fn(input_string: str, start_location: int, end_location: int, expression: ParserELement, parsed_tokens: ParseResults, cache_hit: bool)``

        - ``exception_action`` - method to be called when expression fails to parse;
          should have the signature ``fn(input_string: str, location: int, expression: ParserElement, exception: Exception, cache_hit: bool)``
        """
    def set_debug(self, flag: bool = True) -> ParserElement:
        '''
        Enable display of debugging messages while doing pattern matching.
        Set ``flag`` to ``True`` to enable, ``False`` to disable.

        Example::

            wd = Word(alphas).set_name("alphaword")
            integer = Word(nums).set_name("numword")
            term = wd | integer

            # turn on debugging for wd
            wd.set_debug()

            term[1, ...].parse_string("abc 123 xyz 890")

        prints::

            Match alphaword at loc 0(1,1)
            Matched alphaword -> [\'abc\']
            Match alphaword at loc 3(1,4)
            Exception raised:Expected alphaword (at char 4), (line:1, col:5)
            Match alphaword at loc 7(1,8)
            Matched alphaword -> [\'xyz\']
            Match alphaword at loc 11(1,12)
            Exception raised:Expected alphaword (at char 12), (line:1, col:13)
            Match alphaword at loc 15(1,16)
            Exception raised:Expected alphaword (at char 15), (line:1, col:16)

        The output shown is that produced by the default debug actions - custom debug actions can be
        specified using :class:`set_debug_actions`. Prior to attempting
        to match the ``wd`` expression, the debugging message ``"Match <exprname> at loc <n>(<line>,<col>)"``
        is shown. Then if the parse succeeds, a ``"Matched"`` message is shown, or an ``"Exception raised"``
        message is shown. Also note the use of :class:`set_name` to assign a human-readable name to the expression,
        which makes debugging and exception messages easier to understand - for instance, the default
        name created for the :class:`Word` expression without calling ``set_name`` is ``"W:(A-Za-z)"``.
        '''
    @property
    def default_name(self) -> str: ...
    def set_name(self, name: str) -> ParserElement:
        '''
        Define name for this expression, makes debugging and exception messages clearer.
        Example::
            Word(nums).parse_string("ABC")  # -> Exception: Expected W:(0-9) (at char 0), (line:1, col:1)
            Word(nums).set_name("integer").parse_string("ABC")  # -> Exception: Expected integer (at char 0), (line:1, col:1)
        '''
    @property
    def name(self) -> str: ...
    def streamline(self) -> ParserElement: ...
    def recurse(self) -> Sequence['ParserElement']: ...
    def validate(self, validateTrace: Incomplete | None = None) -> None:
        """
        Check defined expressions for valid structure, check for infinite recursive definitions.
        """
    def parse_file(self, file_or_filename: str | Path | TextIO, encoding: str = 'utf-8', parse_all: bool = False, *, parseAll: bool = False) -> ParseResults:
        """
        Execute the parse expression on the given file or filename.
        If a filename is specified (instead of a file object),
        the entire file is opened, read, and closed before parsing.
        """
    def __eq__(self, other): ...
    def __hash__(self): ...
    def matches(self, test_string: str, parse_all: bool = True, *, parseAll: bool = True) -> bool:
        '''
        Method for quick testing of a parser against a test string. Good for simple
        inline microtests of sub expressions while building up larger parser.

        Parameters:
        - ``test_string`` - to test against this expression for a match
        - ``parse_all`` - (default= ``True``) - flag to pass to :class:`parse_string` when running tests

        Example::

            expr = Word(nums)
            assert expr.matches("100")
        '''
    def run_tests(self, tests: str | List[str], parse_all: bool = True, comment: ParserElement | str | None = '#', full_dump: bool = True, print_results: bool = True, failure_tests: bool = False, post_parse: Callable[[str, ParseResults], str] = None, file: TextIO | None = None, with_line_numbers: bool = False, *, parseAll: bool = True, fullDump: bool = True, printResults: bool = True, failureTests: bool = False, postParse: Callable[[str, ParseResults], str] = None) -> Tuple[bool, List[Tuple[str, ParseResults | Exception]]]:
        '''
        Execute the parse expression on a series of test strings, showing each
        test, the parsed results or where the parse failed. Quick and easy way to
        run a parse expression against a list of sample strings.

        Parameters:
        - ``tests`` - a list of separate test strings, or a multiline string of test strings
        - ``parse_all`` - (default= ``True``) - flag to pass to :class:`parse_string` when running tests
        - ``comment`` - (default= ``\'#\'``) - expression for indicating embedded comments in the test
          string; pass None to disable comment filtering
        - ``full_dump`` - (default= ``True``) - dump results as list followed by results names in nested outline;
          if False, only dump nested list
        - ``print_results`` - (default= ``True``) prints test output to stdout
        - ``failure_tests`` - (default= ``False``) indicates if these tests are expected to fail parsing
        - ``post_parse`` - (default= ``None``) optional callback for successful parse results; called as
          `fn(test_string, parse_results)` and returns a string to be added to the test output
        - ``file`` - (default= ``None``) optional file-like object to which test output will be written;
          if None, will default to ``sys.stdout``
        - ``with_line_numbers`` - default= ``False``) show test strings with line and column numbers

        Returns: a (success, results) tuple, where success indicates that all tests succeeded
        (or failed if ``failure_tests`` is True), and the results contain a list of lines of each
        test\'s output

        Example::

            number_expr = pyparsing_common.number.copy()

            result = number_expr.run_tests(\'\'\'
                # unsigned integer
                100
                # negative integer
                -100
                # float with scientific notation
                6.02e23
                # integer with scientific notation
                1e-12
                \'\'\')
            print("Success" if result[0] else "Failed!")

            result = number_expr.run_tests(\'\'\'
                # stray character
                100Z
                # missing leading digit before \'.\'
                -.100
                # too many \'.\'
                3.14.159
                \'\'\', failure_tests=True)
            print("Success" if result[0] else "Failed!")

        prints::

            # unsigned integer
            100
            [100]

            # negative integer
            -100
            [-100]

            # float with scientific notation
            6.02e23
            [6.02e+23]

            # integer with scientific notation
            1e-12
            [1e-12]

            Success

            # stray character
            100Z
               ^
            FAIL: Expected end of text (at char 3), (line:1, col:4)

            # missing leading digit before \'.\'
            -.100
            ^
            FAIL: Expected {real number with scientific notation | real number | signed integer} (at char 0), (line:1, col:1)

            # too many \'.\'
            3.14.159
                ^
            FAIL: Expected end of text (at char 4), (line:1, col:5)

            Success

        Each test string must be on a single line. If you want to test a string that spans multiple
        lines, create a test like this::

            expr.run_tests(r"this is a test\\n of strings that spans \\n 3 lines")

        (Note that this is a raw string literal, you must include the leading ``\'r\'``.)
        '''
    def create_diagram(self, output_html: TextIO | Path | str, vertical: int = 3, show_results_names: bool = False, show_groups: bool = False, **kwargs) -> None:
        """
        Create a railroad diagram for the parser.

        Parameters:
        - output_html (str or file-like object) - output target for generated
          diagram HTML
        - vertical (int) - threshold for formatting multiple alternatives vertically
          instead of horizontally (default=3)
        - show_results_names - bool flag whether diagram should show annotations for
          defined results names
        - show_groups - bool flag whether groups should be highlighted with an unlabeled surrounding box
        Additional diagram-formatting keyword arguments can also be included;
        see railroad.Diagram class.
        """
    setDefaultWhitespaceChars = set_default_whitespace_chars
    inlineLiteralsUsing = inline_literals_using
    setResultsName = set_results_name
    setBreak = set_break
    setParseAction = set_parse_action
    addParseAction = add_parse_action
    addCondition = add_condition
    setFailAction = set_fail_action
    tryParse = try_parse
    canParseNext = can_parse_next
    resetCache = reset_cache
    enableLeftRecursion = enable_left_recursion
    enablePackrat = enable_packrat
    parseString = parse_string
    scanString = scan_string
    searchString = search_string
    transformString = transform_string
    setWhitespaceChars = set_whitespace_chars
    parseWithTabs = parse_with_tabs
    setDebugActions = set_debug_actions
    setDebug = set_debug
    defaultName = default_name
    setName = set_name
    parseFile = parse_file
    runTests = run_tests
    ignoreWhitespace = ignore_whitespace
    leaveWhitespace = leave_whitespace

class _PendingSkip(ParserElement):
    anchor: Incomplete
    must_skip: Incomplete
    def __init__(self, expr: ParserElement, must_skip: bool = False) -> None: ...
    def __add__(self, other) -> ParserElement: ...
    def parseImpl(self, *args) -> None: ...

class Token(ParserElement):
    """Abstract :class:`ParserElement` subclass, for defining atomic
    matching patterns.
    """
    def __init__(self) -> None: ...

class Empty(Token):
    """
    An empty token, will always match.
    """
    mayReturnEmpty: bool
    mayIndexError: bool
    def __init__(self) -> None: ...

class NoMatch(Token):
    """
    A token that will never match.
    """
    mayReturnEmpty: bool
    mayIndexError: bool
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True) -> None: ...

class Literal(Token):
    '''
    Token to exactly match a specified string.

    Example::

        Literal(\'blah\').parse_string(\'blah\')  # -> [\'blah\']
        Literal(\'blah\').parse_string(\'blahfooblah\')  # -> [\'blah\']
        Literal(\'blah\').parse_string(\'bla\')  # -> Exception: Expected "blah"

    For case-insensitive matching, use :class:`CaselessLiteral`.

    For keyword matching (force word break before and after the matched string),
    use :class:`Keyword` or :class:`CaselessKeyword`.
    '''
    match: Incomplete
    matchLen: Incomplete
    firstMatchChar: Incomplete
    errmsg: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    __class__: Incomplete
    def __init__(self, match_string: str = '', *, matchString: str = '') -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class _SingleCharLiteral(Literal):
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Keyword(Token):
    '''
    Token to exactly match a specified string as a keyword, that is,
    it must be immediately followed by a non-keyword character.  Compare
    with :class:`Literal`:

    - ``Literal("if")`` will match the leading ``\'if\'`` in
      ``\'ifAndOnlyIf\'``.
    - ``Keyword("if")`` will not; it will only match the leading
      ``\'if\'`` in ``\'if x=1\'``, or ``\'if(y==2)\'``

    Accepts two optional constructor arguments in addition to the
    keyword string:

    - ``identChars`` is a string of characters that would be valid
      identifier characters, defaulting to all alphanumerics + "_" and
      "$"
    - ``caseless`` allows case-insensitive matching, default is ``False``.

    Example::

        Keyword("start").parse_string("start")  # -> [\'start\']
        Keyword("start").parse_string("starting")  # -> Exception

    For case-insensitive matching, use :class:`CaselessKeyword`.
    '''
    DEFAULT_KEYWORD_CHARS: Incomplete
    match: Incomplete
    matchLen: Incomplete
    firstMatchChar: Incomplete
    errmsg: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    caseless: Incomplete
    caselessmatch: Incomplete
    identChars: Incomplete
    def __init__(self, match_string: str = '', ident_chars: str | None = None, caseless: bool = False, *, matchString: str = '', identChars: str | None = None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    @staticmethod
    def set_default_keyword_chars(chars) -> None:
        """
        Overrides the default characters used by :class:`Keyword` expressions.
        """
    setDefaultKeywordChars = set_default_keyword_chars

class CaselessLiteral(Literal):
    '''
    Token to match a specified string, ignoring case of letters.
    Note: the matched results will always be in the case of the given
    match string, NOT the case of the input text.

    Example::

        CaselessLiteral("CMD")[1, ...].parse_string("cmd CMD Cmd10")
        # -> [\'CMD\', \'CMD\', \'CMD\']

    (Contrast with example for :class:`CaselessKeyword`.)
    '''
    returnString: Incomplete
    errmsg: Incomplete
    def __init__(self, match_string: str = '', *, matchString: str = '') -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class CaselessKeyword(Keyword):
    '''
    Caseless version of :class:`Keyword`.

    Example::

        CaselessKeyword("CMD")[1, ...].parse_string("cmd CMD Cmd10")
        # -> [\'CMD\', \'CMD\']

    (Contrast with example for :class:`CaselessLiteral`.)
    '''
    def __init__(self, match_string: str = '', ident_chars: str | None = None, *, matchString: str = '', identChars: str | None = None) -> None: ...

class CloseMatch(Token):
    '''A variation on :class:`Literal` which matches "close" matches,
    that is, strings with at most \'n\' mismatching characters.
    :class:`CloseMatch` takes parameters:

    - ``match_string`` - string to be matched
    - ``caseless`` - a boolean indicating whether to ignore casing when comparing characters
    - ``max_mismatches`` - (``default=1``) maximum number of
      mismatches allowed to count as a match

    The results from a successful parse will contain the matched text
    from the input string and the following named results:

    - ``mismatches`` - a list of the positions within the
      match_string where mismatches were found
    - ``original`` - the original match_string used to compare
      against the input string

    If ``mismatches`` is an empty list, then the match was an exact
    match.

    Example::

        patt = CloseMatch("ATCATCGAATGGA")
        patt.parse_string("ATCATCGAAXGGA") # -> ([\'ATCATCGAAXGGA\'], {\'mismatches\': [[9]], \'original\': [\'ATCATCGAATGGA\']})
        patt.parse_string("ATCAXCGAAXGGA") # -> Exception: Expected \'ATCATCGAATGGA\' (with up to 1 mismatches) (at char 0), (line:1, col:1)

        # exact match
        patt.parse_string("ATCATCGAATGGA") # -> ([\'ATCATCGAATGGA\'], {\'mismatches\': [[]], \'original\': [\'ATCATCGAATGGA\']})

        # close match allowing up to 2 mismatches
        patt = CloseMatch("ATCATCGAATGGA", max_mismatches=2)
        patt.parse_string("ATCAXCGAAXGGA") # -> ([\'ATCAXCGAAXGGA\'], {\'mismatches\': [[4, 9]], \'original\': [\'ATCATCGAATGGA\']})
    '''
    match_string: Incomplete
    maxMismatches: Incomplete
    errmsg: Incomplete
    caseless: Incomplete
    mayIndexError: bool
    mayReturnEmpty: bool
    def __init__(self, match_string: str, max_mismatches: int = None, *, maxMismatches: int = 1, caseless: bool = False) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Word(Token):
    '''Token for matching words composed of allowed character sets.
    Parameters:
    - ``init_chars`` - string of all characters that should be used to
      match as a word; "ABC" will match "AAA", "ABAB", "CBAC", etc.;
      if ``body_chars`` is also specified, then this is the string of
      initial characters
    - ``body_chars`` - string of characters that
      can be used for matching after a matched initial character as
      given in ``init_chars``; if omitted, same as the initial characters
      (default=``None``)
    - ``min`` - minimum number of characters to match (default=1)
    - ``max`` - maximum number of characters to match (default=0)
    - ``exact`` - exact number of characters to match (default=0)
    - ``as_keyword`` - match as a keyword (default=``False``)
    - ``exclude_chars`` - characters that might be
      found in the input ``body_chars`` string but which should not be
      accepted for matching ;useful to define a word of all
      printables except for one or two characters, for instance
      (default=``None``)

    :class:`srange` is useful for defining custom character set strings
    for defining :class:`Word` expressions, using range notation from
    regular expression character sets.

    A common mistake is to use :class:`Word` to match a specific literal
    string, as in ``Word("Address")``. Remember that :class:`Word`
    uses the string argument to define *sets* of matchable characters.
    This expression would match "Add", "AAA", "dAred", or any other word
    made up of the characters \'A\', \'d\', \'r\', \'e\', and \'s\'. To match an
    exact literal string, use :class:`Literal` or :class:`Keyword`.

    pyparsing includes helper strings for building Words:

    - :class:`alphas`
    - :class:`nums`
    - :class:`alphanums`
    - :class:`hexnums`
    - :class:`alphas8bit` (alphabetic characters in ASCII range 128-255
      - accented, tilded, umlauted, etc.)
    - :class:`punc8bit` (non-alphabetic characters in ASCII range
      128-255 - currency, symbols, superscripts, diacriticals, etc.)
    - :class:`printables` (any non-whitespace character)

    ``alphas``, ``nums``, and ``printables`` are also defined in several
    Unicode sets - see :class:`pyparsing_unicode``.

    Example::

        # a word composed of digits
        integer = Word(nums) # equivalent to Word("0123456789") or Word(srange("0-9"))

        # a word with a leading capital, and zero or more lowercase
        capital_word = Word(alphas.upper(), alphas.lower())

        # hostnames are alphanumeric, with leading alpha, and \'-\'
        hostname = Word(alphas, alphanums + \'-\')

        # roman numeral (not a strict parser, accepts invalid mix of characters)
        roman = Word("IVXLCDM")

        # any string of non-whitespace characters, except for \',\'
        csv_value = Word(printables, exclude_chars=",")
    '''
    initChars: Incomplete
    initCharsOrig: Incomplete
    bodyCharsOrig: Incomplete
    bodyChars: Incomplete
    maxSpecified: Incomplete
    minLen: Incomplete
    maxLen: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    asKeyword: Incomplete
    reString: Incomplete
    re: Incomplete
    re_match: Incomplete
    __class__: Incomplete
    def __init__(self, init_chars: str = '', body_chars: str | None = None, min: int = 1, max: int = 0, exact: int = 0, as_keyword: bool = False, exclude_chars: str | None = None, *, initChars: str | None = None, bodyChars: str | None = None, asKeyword: bool = False, excludeChars: str | None = None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class _WordRegex(Word):
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Char(_WordRegex):
    """A short-cut class for defining :class:`Word` ``(characters, exact=1)``,
    when defining a match of any single character in a string of
    characters.
    """
    reString: Incomplete
    re: Incomplete
    re_match: Incomplete
    def __init__(self, charset: str, as_keyword: bool = False, exclude_chars: str | None = None, *, asKeyword: bool = False, excludeChars: str | None = None) -> None: ...

class Regex(Token):
    '''Token for matching strings that match a given regular
    expression. Defined with string specifying the regular expression in
    a form recognized by the stdlib Python  `re module <https://docs.python.org/3/library/re.html>`_.
    If the given regex contains named groups (defined using ``(?P<name>...)``),
    these will be preserved as named :class:`ParseResults`.

    If instead of the Python stdlib ``re`` module you wish to use a different RE module
    (such as the ``regex`` module), you can do so by building your ``Regex`` object with
    a compiled RE that was compiled using ``regex``.

    Example::

        realnum = Regex(r"[+-]?\\d+\\.\\d*")
        # ref: https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
        roman = Regex(r"M{0,4}(CM|CD|D?{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

        # named fields in a regex will be returned as named results
        date = Regex(r\'(?P<year>\\d{4})-(?P<month>\\d\\d?)-(?P<day>\\d\\d?)\')

        # the Regex class will accept re\'s compiled using the regex module
        import regex
        parser = pp.Regex(regex.compile(r\'[0-9]\'))
    '''
    reString: Incomplete
    flags: Incomplete
    pattern: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    asGroupList: Incomplete
    asMatch: Incomplete
    def __init__(self, pattern: Any, flags: re.RegexFlag | int = 0, as_group_list: bool = False, as_match: bool = False, *, asGroupList: bool = False, asMatch: bool = False) -> None:
        """The parameters ``pattern`` and ``flags`` are passed
        to the ``re.compile()`` function as-is. See the Python
        `re module <https://docs.python.org/3/library/re.html>`_ module for an
        explanation of the acceptable patterns and flags.
        """
    @cached_property
    def re(self): ...
    @cached_property
    def re_match(self): ...
    @cached_property
    def mayReturnEmpty(self): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def parseImplAsGroupList(self, instring, loc, doActions: bool = True): ...
    def parseImplAsMatch(self, instring, loc, doActions: bool = True): ...
    def sub(self, repl: str) -> ParserElement:
        '''
        Return :class:`Regex` with an attached parse action to transform the parsed
        result as if called using `re.sub(expr, repl, string) <https://docs.python.org/3/library/re.html#re.sub>`_.

        Example::

            make_html = Regex(r"(\\w+):(.*?):").sub(r"<\\1>\\2</\\1>")
            print(make_html.transform_string("h1:main title:"))
            # prints "<h1>main title</h1>"
        '''

class QuotedString(Token):
    '''
    Token for matching strings that are delimited by quoting characters.

    Defined with the following parameters:

    - ``quote_char`` - string of one or more characters defining the
      quote delimiting string
    - ``esc_char`` - character to re_escape quotes, typically backslash
      (default= ``None``)
    - ``esc_quote`` - special quote sequence to re_escape an embedded quote
      string (such as SQL\'s ``""`` to re_escape an embedded ``"``)
      (default= ``None``)
    - ``multiline`` - boolean indicating whether quotes can span
      multiple lines (default= ``False``)
    - ``unquote_results`` - boolean indicating whether the matched text
      should be unquoted (default= ``True``)
    - ``end_quote_char`` - string of one or more characters defining the
      end of the quote delimited string (default= ``None``  => same as
      quote_char)
    - ``convert_whitespace_escapes`` - convert escaped whitespace
      (``\'\\t\'``, ``\'\\n\'``, etc.) to actual whitespace
      (default= ``True``)

    Example::

        qs = QuotedString(\'"\')
        print(qs.search_string(\'lsjdf "This is the quote" sldjf\'))
        complex_qs = QuotedString(\'{{\', end_quote_char=\'}}\')
        print(complex_qs.search_string(\'lsjdf {{This is the "quote"}} sldjf\'))
        sql_qs = QuotedString(\'"\', esc_quote=\'""\')
        print(sql_qs.search_string(\'lsjdf "This is the quote with ""embedded"" quotes" sldjf\'))

    prints::

        [[\'This is the quote\']]
        [[\'This is the "quote"\']]
        [[\'This is the quote with "embedded" quotes\']]
    '''
    ws_map: Incomplete
    quoteChar: Incomplete
    quoteCharLen: Incomplete
    firstQuoteChar: Incomplete
    endQuoteChar: Incomplete
    endQuoteCharLen: Incomplete
    escChar: Incomplete
    escQuote: Incomplete
    unquoteResults: Incomplete
    convertWhitespaceEscapes: Incomplete
    escCharReplacePattern: Incomplete
    flags: Incomplete
    pattern: Incomplete
    re: Incomplete
    reString: Incomplete
    re_match: Incomplete
    errmsg: Incomplete
    mayIndexError: bool
    mayReturnEmpty: bool
    def __init__(self, quote_char: str = '', esc_char: str | None = None, esc_quote: str | None = None, multiline: bool = False, unquote_results: bool = True, end_quote_char: str | None = None, convert_whitespace_escapes: bool = True, *, quoteChar: str = '', escChar: str | None = None, escQuote: str | None = None, unquoteResults: bool = True, endQuoteChar: str | None = None, convertWhitespaceEscapes: bool = True) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class CharsNotIn(Token):
    '''Token for matching words composed of characters *not* in a given
    set (will include whitespace in matched characters if not listed in
    the provided exclusion set - see example). Defined with string
    containing all disallowed characters, and an optional minimum,
    maximum, and/or exact length.  The default value for ``min`` is
    1 (a minimum value < 1 is not valid); the default values for
    ``max`` and ``exact`` are 0, meaning no maximum or exact
    length restriction.

    Example::

        # define a comma-separated-value as anything that is not a \',\'
        csv_value = CharsNotIn(\',\')
        print(delimited_list(csv_value).parse_string("dkls,lsdkjf,s12 34,@!#,213"))

    prints::

        [\'dkls\', \'lsdkjf\', \'s12 34\', \'@!#\', \'213\']
    '''
    skipWhitespace: bool
    notChars: Incomplete
    notCharsSet: Incomplete
    minLen: Incomplete
    maxLen: Incomplete
    errmsg: Incomplete
    mayReturnEmpty: Incomplete
    mayIndexError: bool
    def __init__(self, not_chars: str = '', min: int = 1, max: int = 0, exact: int = 0, *, notChars: str = '') -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class White(Token):
    '''Special matching class for matching whitespace.  Normally,
    whitespace is ignored by pyparsing grammars.  This class is included
    when some whitespace structures are significant.  Define with
    a string containing the whitespace characters to be matched; default
    is ``" \\t\\r\\n"``.  Also takes optional ``min``,
    ``max``, and ``exact`` arguments, as defined for the
    :class:`Word` class.
    '''
    whiteStrs: Incomplete
    matchWhite: Incomplete
    mayReturnEmpty: bool
    errmsg: Incomplete
    minLen: Incomplete
    maxLen: Incomplete
    def __init__(self, ws: str = ' \t\r\n', min: int = 1, max: int = 0, exact: int = 0) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class PositionToken(Token):
    mayReturnEmpty: bool
    mayIndexError: bool
    def __init__(self) -> None: ...

class GoToColumn(PositionToken):
    """Token to advance to a specific column of input text; useful for
    tabular report scraping.
    """
    col: Incomplete
    def __init__(self, colno: int) -> None: ...
    def preParse(self, instring, loc): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class LineStart(PositionToken):
    """Matches if current position is at the beginning of a line within
    the parse string

    Example::

        test = '''\\\n        AAA this line
        AAA and this line
          AAA but not this one
        B AAA and definitely not this one
        '''

        for t in (LineStart() + 'AAA' + restOfLine).search_string(test):
            print(t)

    prints::

        ['AAA', ' this line']
        ['AAA', ' and this line']

    """
    orig_whiteChars: Incomplete
    skipper: Incomplete
    errmsg: str
    def __init__(self) -> None: ...
    def preParse(self, instring, loc): ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class LineEnd(PositionToken):
    """Matches if current position is at the end of a line within the
    parse string
    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class StringStart(PositionToken):
    """Matches if current position is at the beginning of the parse
    string
    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class StringEnd(PositionToken):
    """
    Matches if current position is at the end of the parse string
    """
    errmsg: str
    def __init__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class WordStart(PositionToken):
    """Matches if the current position is at the beginning of a
    :class:`Word`, and is not preceded by any character in a given
    set of ``word_chars`` (default= ``printables``). To emulate the
    ``\x08`` behavior of regular expressions, use
    ``WordStart(alphanums)``. ``WordStart`` will also match at
    the beginning of the string being parsed, or at the beginning of
    a line.
    """
    wordChars: Incomplete
    errmsg: str
    def __init__(self, word_chars: str = ..., *, wordChars: str = ...) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class WordEnd(PositionToken):
    """Matches if the current position is at the end of a :class:`Word`,
    and is not followed by any character in a given set of ``word_chars``
    (default= ``printables``). To emulate the ``\x08`` behavior of
    regular expressions, use ``WordEnd(alphanums)``. ``WordEnd``
    will also match at the end of the string being parsed, or at the end
    of a line.
    """
    wordChars: Incomplete
    skipWhitespace: bool
    errmsg: str
    def __init__(self, word_chars: str = ..., *, wordChars: str = ...) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class ParseExpression(ParserElement):
    """Abstract subclass of ParserElement, for combining and
    post-processing parsed tokens.
    """
    exprs: Incomplete
    callPreparse: bool
    def __init__(self, exprs: typing.Iterable[ParserElement], savelist: bool = False) -> None: ...
    def recurse(self) -> Sequence[ParserElement]: ...
    def append(self, other) -> ParserElement: ...
    def leave_whitespace(self, recursive: bool = True) -> ParserElement:
        """
        Extends ``leave_whitespace`` defined in base class, and also invokes ``leave_whitespace`` on
           all contained expressions.
        """
    def ignore_whitespace(self, recursive: bool = True) -> ParserElement:
        """
        Extends ``ignore_whitespace`` defined in base class, and also invokes ``leave_whitespace`` on
           all contained expressions.
        """
    def ignore(self, other) -> ParserElement: ...
    errmsg: Incomplete
    def streamline(self) -> ParserElement: ...
    def validate(self, validateTrace: Incomplete | None = None) -> None: ...
    def copy(self) -> ParserElement: ...
    ignoreWhitespace = ignore_whitespace
    leaveWhitespace = leave_whitespace

class And(ParseExpression):
    '''
    Requires all given :class:`ParseExpression` s to be found in the given order.
    Expressions may be separated by whitespace.
    May be constructed using the ``\'+\'`` operator.
    May also be constructed using the ``\'-\'`` operator, which will
    suppress backtracking.

    Example::

        integer = Word(nums)
        name_expr = Word(alphas)[1, ...]

        expr = And([integer("id"), name_expr("name"), integer("age")])
        # more easily written as:
        expr = integer("id") + name_expr("name") + integer("age")
    '''
    class _ErrorStop(Empty):
        def __init__(self, *args, **kwargs) -> None: ...
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    callPreparse: bool
    def __init__(self, exprs_arg: typing.Iterable[ParserElement], savelist: bool = True) -> None: ...
    exprs: Incomplete
    def streamline(self) -> ParserElement: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def __iadd__(self, other): ...

class Or(ParseExpression):
    '''Requires that at least one :class:`ParseExpression` is found. If
    two expressions match, the expression that matches the longest
    string will be used. May be constructed using the ``\'^\'``
    operator.

    Example::

        # construct Or using \'^\' operator

        number = Word(nums) ^ Combine(Word(nums) + \'.\' + Word(nums))
        print(number.search_string("123 3.1416 789"))

    prints::

        [[\'123\'], [\'3.1416\'], [\'789\']]
    '''
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    def __init__(self, exprs: typing.Iterable[ParserElement], savelist: bool = False) -> None: ...
    saveAsList: Incomplete
    def streamline(self) -> ParserElement: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def __ixor__(self, other): ...

class MatchFirst(ParseExpression):
    '''Requires that at least one :class:`ParseExpression` is found. If
    more than one expression matches, the first one listed is the one that will
    match. May be constructed using the ``\'|\'`` operator.

    Example::

        # construct MatchFirst using \'|\' operator

        # watch the order of expressions to match
        number = Word(nums) | Combine(Word(nums) + \'.\' + Word(nums))
        print(number.search_string("123 3.1416 789")) #  Fail! -> [[\'123\'], [\'3\'], [\'1416\'], [\'789\']]

        # put more selective expression first
        number = Combine(Word(nums) + \'.\' + Word(nums)) | Word(nums)
        print(number.search_string("123 3.1416 789")) #  Better -> [[\'123\'], [\'3.1416\'], [\'789\']]
    '''
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    def __init__(self, exprs: typing.Iterable[ParserElement], savelist: bool = False) -> None: ...
    saveAsList: Incomplete
    def streamline(self) -> ParserElement: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def __ior__(self, other): ...

class Each(ParseExpression):
    '''Requires all given :class:`ParseExpression` s to be found, but in
    any order. Expressions may be separated by whitespace.

    May be constructed using the ``\'&\'`` operator.

    Example::

        color = one_of("RED ORANGE YELLOW GREEN BLUE PURPLE BLACK WHITE BROWN")
        shape_type = one_of("SQUARE CIRCLE TRIANGLE STAR HEXAGON OCTAGON")
        integer = Word(nums)
        shape_attr = "shape:" + shape_type("shape")
        posn_attr = "posn:" + Group(integer("x") + \',\' + integer("y"))("posn")
        color_attr = "color:" + color("color")
        size_attr = "size:" + integer("size")

        # use Each (using operator \'&\') to accept attributes in any order
        # (shape and posn are required, color and size are optional)
        shape_spec = shape_attr & posn_attr & Opt(color_attr) & Opt(size_attr)

        shape_spec.run_tests(\'\'\'
            shape: SQUARE color: BLACK posn: 100, 120
            shape: CIRCLE size: 50 color: BLUE posn: 50,80
            color:GREEN size:20 shape:TRIANGLE posn:20,40
            \'\'\'
            )

    prints::

        shape: SQUARE color: BLACK posn: 100, 120
        [\'shape:\', \'SQUARE\', \'color:\', \'BLACK\', \'posn:\', [\'100\', \',\', \'120\']]
        - color: BLACK
        - posn: [\'100\', \',\', \'120\']
          - x: 100
          - y: 120
        - shape: SQUARE


        shape: CIRCLE size: 50 color: BLUE posn: 50,80
        [\'shape:\', \'CIRCLE\', \'size:\', \'50\', \'color:\', \'BLUE\', \'posn:\', [\'50\', \',\', \'80\']]
        - color: BLUE
        - posn: [\'50\', \',\', \'80\']
          - x: 50
          - y: 80
        - shape: CIRCLE
        - size: 50


        color: GREEN size: 20 shape: TRIANGLE posn: 20,40
        [\'color:\', \'GREEN\', \'size:\', \'20\', \'shape:\', \'TRIANGLE\', \'posn:\', [\'20\', \',\', \'40\']]
        - color: GREEN
        - posn: [\'20\', \',\', \'40\']
          - x: 20
          - y: 40
        - shape: TRIANGLE
        - size: 20
    '''
    mayReturnEmpty: Incomplete
    skipWhitespace: bool
    initExprGroups: bool
    saveAsList: bool
    def __init__(self, exprs: typing.Iterable[ParserElement], savelist: bool = True) -> None: ...
    def streamline(self) -> ParserElement: ...
    opt1map: Incomplete
    optionals: Incomplete
    multioptionals: Incomplete
    multirequired: Incomplete
    required: Incomplete
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class ParseElementEnhance(ParserElement):
    """Abstract subclass of :class:`ParserElement`, for combining and
    post-processing parsed tokens.
    """
    expr: Incomplete
    mayIndexError: Incomplete
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    saveAsList: Incomplete
    callPreparse: Incomplete
    def __init__(self, expr: ParserElement | str, savelist: bool = False) -> None: ...
    def recurse(self) -> Sequence[ParserElement]: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def leave_whitespace(self, recursive: bool = True) -> ParserElement: ...
    def ignore_whitespace(self, recursive: bool = True) -> ParserElement: ...
    def ignore(self, other) -> ParserElement: ...
    def streamline(self) -> ParserElement: ...
    def validate(self, validateTrace: Incomplete | None = None) -> None: ...
    ignoreWhitespace = ignore_whitespace
    leaveWhitespace = leave_whitespace

class IndentedBlock(ParseElementEnhance):
    """
    Expression to match one or more expressions at a given indentation level.
    Useful for parsing text where structure is implied by indentation (like Python source code).
    """
    class _Indent(Empty):
        errmsg: Incomplete
        def __init__(self, ref_col: int) -> None: ...
    class _IndentGreater(Empty):
        errmsg: Incomplete
        def __init__(self, ref_col: int) -> None: ...
    parent_anchor: int
    def __init__(self, expr: ParserElement, *, recursive: bool = False, grouped: bool = True) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class AtStringStart(ParseElementEnhance):
    '''Matches if expression matches at the beginning of the parse
    string::

        AtStringStart(Word(nums)).parse_string("123")
        # prints ["123"]

        AtStringStart(Word(nums)).parse_string("    123")
        # raises ParseException
    '''
    callPreparse: bool
    def __init__(self, expr: ParserElement | str) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class AtLineStart(ParseElementEnhance):
    """Matches if an expression matches at the beginning of a line within
    the parse string

    Example::

        test = '''\\\n        AAA this line
        AAA and this line
          AAA but not this one
        B AAA and definitely not this one
        '''

        for t in (AtLineStart('AAA') + restOfLine).search_string(test):
            print(t)

    prints::

        ['AAA', ' this line']
        ['AAA', ' and this line']

    """
    callPreparse: bool
    def __init__(self, expr: ParserElement | str) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class FollowedBy(ParseElementEnhance):
    '''Lookahead matching of the given parse expression.
    ``FollowedBy`` does *not* advance the parsing position within
    the input string, it only verifies that the specified parse
    expression matches at the current position.  ``FollowedBy``
    always returns a null token list. If any results names are defined
    in the lookahead expression, those *will* be returned for access by
    name.

    Example::

        # use FollowedBy to match a label only if it is followed by a \':\'
        data_word = Word(alphas)
        label = data_word + FollowedBy(\':\')
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word, stop_on=label).set_parse_action(\' \'.join))

        attr_expr[1, ...].parse_string("shape: SQUARE color: BLACK posn: upper left").pprint()

    prints::

        [[\'shape\', \'SQUARE\'], [\'color\', \'BLACK\'], [\'posn\', \'upper left\']]
    '''
    mayReturnEmpty: bool
    def __init__(self, expr: ParserElement | str) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class PrecededBy(ParseElementEnhance):
    '''Lookbehind matching of the given parse expression.
    ``PrecededBy`` does not advance the parsing position within the
    input string, it only verifies that the specified parse expression
    matches prior to the current position.  ``PrecededBy`` always
    returns a null token list, but if a results name is defined on the
    given expression, it is returned.

    Parameters:

    - expr - expression that must match prior to the current parse
      location
    - retreat - (default= ``None``) - (int) maximum number of characters
      to lookbehind prior to the current parse location

    If the lookbehind expression is a string, :class:`Literal`,
    :class:`Keyword`, or a :class:`Word` or :class:`CharsNotIn`
    with a specified exact or maximum length, then the retreat
    parameter is not required. Otherwise, retreat must be specified to
    give a maximum number of characters to look back from
    the current parse position for a lookbehind match.

    Example::

        # VB-style variable names with type prefixes
        int_var = PrecededBy("#") + pyparsing_common.identifier
        str_var = PrecededBy("$") + pyparsing_common.identifier

    '''
    expr: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    exact: bool
    retreat: Incomplete
    errmsg: Incomplete
    skipWhitespace: bool
    def __init__(self, expr: ParserElement | str, retreat: int | None = None) -> None: ...
    def parseImpl(self, instring, loc: int = 0, doActions: bool = True): ...

class Located(ParseElementEnhance):
    '''
    Decorates a returned token with its starting and ending
    locations in the input string.

    This helper adds the following results names:

    - ``locn_start`` - location where matched expression begins
    - ``locn_end`` - location where matched expression ends
    - ``value`` - the actual parsed results

    Be careful if the input text contains ``<TAB>`` characters, you
    may want to call :class:`ParserElement.parse_with_tabs`

    Example::

        wd = Word(alphas)
        for match in Located(wd).search_string("ljsdf123lksdjjf123lkkjj1222"):
            print(match)

    prints::

        [0, [\'ljsdf\'], 5]
        [8, [\'lksdjjf\'], 15]
        [18, [\'lkkjj\'], 23]

    '''
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class NotAny(ParseElementEnhance):
    '''
    Lookahead to disallow matching with the given parse expression.
    ``NotAny`` does *not* advance the parsing position within the
    input string, it only verifies that the specified parse expression
    does *not* match at the current position.  Also, ``NotAny`` does
    *not* skip over leading whitespace. ``NotAny`` always returns
    a null token list.  May be constructed using the ``\'~\'`` operator.

    Example::

        AND, OR, NOT = map(CaselessKeyword, "AND OR NOT".split())

        # take care not to mistake keywords for identifiers
        ident = ~(AND | OR | NOT) + Word(alphas)
        boolean_term = Opt(NOT) + ident

        # very crude boolean expression - to support parenthesis groups and
        # operation hierarchy, use infix_notation
        boolean_expr = boolean_term + ((AND | OR) + boolean_term)[...]

        # integers that are followed by "." are actually floats
        integer = Word(nums) + ~Char(".")
    '''
    skipWhitespace: bool
    mayReturnEmpty: bool
    errmsg: Incomplete
    def __init__(self, expr: ParserElement | str) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class _MultipleMatch(ParseElementEnhance):
    saveAsList: bool
    def __init__(self, expr: ParserElement, stop_on: ParserElement | str | None = None, *, stopOn: ParserElement | str | None = None) -> None: ...
    not_ender: Incomplete
    def stopOn(self, ender) -> ParserElement: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class OneOrMore(_MultipleMatch):
    '''
    Repetition of one or more of the given expression.

    Parameters:
    - expr - expression that must match one or more times
    - stop_on - (default= ``None``) - expression for a terminating sentinel
         (only required if the sentinel would ordinarily match the repetition
         expression)

    Example::

        data_word = Word(alphas)
        label = data_word + FollowedBy(\':\')
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word).set_parse_action(\' \'.join))

        text = "shape: SQUARE posn: upper left color: BLACK"
        attr_expr[1, ...].parse_string(text).pprint()  # Fail! read \'color\' as data instead of next label -> [[\'shape\', \'SQUARE color\']]

        # use stop_on attribute for OneOrMore to avoid reading label string as part of the data
        attr_expr = Group(label + Suppress(\':\') + OneOrMore(data_word, stop_on=label).set_parse_action(\' \'.join))
        OneOrMore(attr_expr).parse_string(text).pprint() # Better -> [[\'shape\', \'SQUARE\'], [\'posn\', \'upper left\'], [\'color\', \'BLACK\']]

        # could also be written as
        (attr_expr * (1,)).parse_string(text).pprint()
    '''

class ZeroOrMore(_MultipleMatch):
    """
    Optional repetition of zero or more of the given expression.

    Parameters:
    - ``expr`` - expression that must match zero or more times
    - ``stop_on`` - expression for a terminating sentinel
      (only required if the sentinel would ordinarily match the repetition
      expression) - (default= ``None``)

    Example: similar to :class:`OneOrMore`
    """
    mayReturnEmpty: bool
    def __init__(self, expr: ParserElement, stop_on: ParserElement | str | None = None, *, stopOn: ParserElement | str | None = None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class _NullToken:
    def __bool__(self) -> bool: ...

class Opt(ParseElementEnhance):
    """
    Optional matching of the given expression.

    Parameters:
    - ``expr`` - expression that must match zero or more times
    - ``default`` (optional) - value to be returned if the optional expression is not found.

    Example::

        # US postal code can be a 5-digit zip, plus optional 4-digit qualifier
        zip = Combine(Word(nums, exact=5) + Opt('-' + Word(nums, exact=4)))
        zip.run_tests('''
            # traditional ZIP code
            12345

            # ZIP+4 form
            12101-0001

            # invalid ZIP
            98765-
            ''')

    prints::

        # traditional ZIP code
        12345
        ['12345']

        # ZIP+4 form
        12101-0001
        ['12101-0001']

        # invalid ZIP
        98765-
             ^
        FAIL: Expected end of text (at char 5), (line:1, col:6)
    """
    saveAsList: Incomplete
    defaultValue: Incomplete
    mayReturnEmpty: bool
    def __init__(self, expr: ParserElement | str, default: Any = ...) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
Optional = Opt

class SkipTo(ParseElementEnhance):
    '''
    Token for skipping over all undefined text until the matched
    expression is found.

    Parameters:
    - ``expr`` - target expression marking the end of the data to be skipped
    - ``include`` - if ``True``, the target expression is also parsed
      (the skipped text and target expression are returned as a 2-element
      list) (default= ``False``).
    - ``ignore`` - (default= ``None``) used to define grammars (typically quoted strings and
      comments) that might contain false matches to the target expression
    - ``fail_on`` - (default= ``None``) define expressions that are not allowed to be
      included in the skipped test; if found before the target expression is found,
      the :class:`SkipTo` is not a match

    Example::

        report = \'\'\'
            Outstanding Issues Report - 1 Jan 2000

               # | Severity | Description                               |  Days Open
            -----+----------+-------------------------------------------+-----------
             101 | Critical | Intermittent system crash                 |          6
              94 | Cosmetic | Spelling error on Login (\'log|n\')         |         14
              79 | Minor    | System slow when running too many reports |         47
            \'\'\'
        integer = Word(nums)
        SEP = Suppress(\'|\')
        # use SkipTo to simply match everything up until the next SEP
        # - ignore quoted strings, so that a \'|\' character inside a quoted string does not match
        # - parse action will call token.strip() for each matched token, i.e., the description body
        string_data = SkipTo(SEP, ignore=quoted_string)
        string_data.set_parse_action(token_map(str.strip))
        ticket_expr = (integer("issue_num") + SEP
                      + string_data("sev") + SEP
                      + string_data("desc") + SEP
                      + integer("days_open"))

        for tkt in ticket_expr.search_string(report):
            print tkt.dump()

    prints::

        [\'101\', \'Critical\', \'Intermittent system crash\', \'6\']
        - days_open: \'6\'
        - desc: \'Intermittent system crash\'
        - issue_num: \'101\'
        - sev: \'Critical\'
        [\'94\', \'Cosmetic\', "Spelling error on Login (\'log|n\')", \'14\']
        - days_open: \'14\'
        - desc: "Spelling error on Login (\'log|n\')"
        - issue_num: \'94\'
        - sev: \'Cosmetic\'
        [\'79\', \'Minor\', \'System slow when running too many reports\', \'47\']
        - days_open: \'47\'
        - desc: \'System slow when running too many reports\'
        - issue_num: \'79\'
        - sev: \'Minor\'
    '''
    ignoreExpr: Incomplete
    mayReturnEmpty: bool
    mayIndexError: bool
    includeMatch: Incomplete
    saveAsList: bool
    failOn: Incomplete
    errmsg: Incomplete
    def __init__(self, other: ParserElement | str, include: bool = False, ignore: bool = None, fail_on: ParserElement | str | None = None, *, failOn: ParserElement | str = None) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...

class Forward(ParseElementEnhance):
    """
    Forward declaration of an expression to be defined later -
    used for recursive grammars, such as algebraic infix notation.
    When the expression is known, it is assigned to the ``Forward``
    variable using the ``'<<'`` operator.

    Note: take care when assigning to ``Forward`` not to overlook
    precedence of operators.

    Specifically, ``'|'`` has a lower precedence than ``'<<'``, so that::

        fwd_expr << a | b | c

    will actually be evaluated as::

        (fwd_expr << a) | b | c

    thereby leaving b and c out as parseable alternatives.  It is recommended that you
    explicitly group the values inserted into the ``Forward``::

        fwd_expr << (a | b | c)

    Converting to use the ``'<<='`` operator instead will avoid this problem.

    See :class:`ParseResults.pprint` for an example of a recursive
    parser created using ``Forward``.
    """
    caller_frame: Incomplete
    lshift_line: Incomplete
    def __init__(self, other: ParserElement | str | None = None) -> None: ...
    expr: Incomplete
    mayIndexError: Incomplete
    mayReturnEmpty: Incomplete
    skipWhitespace: Incomplete
    saveAsList: Incomplete
    def __lshift__(self, other): ...
    def __ilshift__(self, other): ...
    def __or__(self, other): ...
    def __del__(self) -> None: ...
    def parseImpl(self, instring, loc, doActions: bool = True): ...
    def leave_whitespace(self, recursive: bool = True) -> ParserElement: ...
    def ignore_whitespace(self, recursive: bool = True) -> ParserElement: ...
    streamlined: bool
    def streamline(self) -> ParserElement: ...
    def validate(self, validateTrace: Incomplete | None = None) -> None: ...
    def copy(self) -> ParserElement: ...
    ignoreWhitespace = ignore_whitespace
    leaveWhitespace = leave_whitespace

class TokenConverter(ParseElementEnhance):
    """
    Abstract subclass of :class:`ParseExpression`, for converting parsed results.
    """
    saveAsList: bool
    def __init__(self, expr: ParserElement | str, savelist: bool = False) -> None: ...

class Combine(TokenConverter):
    """Converter to concatenate all matching tokens to a single string.
    By default, the matching patterns must also be contiguous in the
    input string; this can be disabled by specifying
    ``'adjacent=False'`` in the constructor.

    Example::

        real = Word(nums) + '.' + Word(nums)
        print(real.parse_string('3.1416')) # -> ['3', '.', '1416']
        # will also erroneously match the following
        print(real.parse_string('3. 1416')) # -> ['3', '.', '1416']

        real = Combine(Word(nums) + '.' + Word(nums))
        print(real.parse_string('3.1416')) # -> ['3.1416']
        # no match when there are internal spaces
        print(real.parse_string('3. 1416')) # -> Exception: Expected W:(0123...)
    """
    adjacent: Incomplete
    skipWhitespace: bool
    joinString: Incomplete
    callPreparse: bool
    def __init__(self, expr: ParserElement, join_string: str = '', adjacent: bool = True, *, joinString: str | None = None) -> None: ...
    def ignore(self, other) -> ParserElement: ...
    def postParse(self, instring, loc, tokenlist): ...

class Group(TokenConverter):
    '''Converter to return the matched tokens as a list - useful for
    returning tokens of :class:`ZeroOrMore` and :class:`OneOrMore` expressions.

    The optional ``aslist`` argument when set to True will return the
    parsed tokens as a Python list instead of a pyparsing ParseResults.

    Example::

        ident = Word(alphas)
        num = Word(nums)
        term = ident | num
        func = ident + Opt(delimited_list(term))
        print(func.parse_string("fn a, b, 100"))
        # -> [\'fn\', \'a\', \'b\', \'100\']

        func = ident + Group(Opt(delimited_list(term)))
        print(func.parse_string("fn a, b, 100"))
        # -> [\'fn\', [\'a\', \'b\', \'100\']]
    '''
    saveAsList: bool
    def __init__(self, expr: ParserElement, aslist: bool = False) -> None: ...
    def postParse(self, instring, loc, tokenlist): ...

class Dict(TokenConverter):
    '''Converter to return a repetitive expression as a list, but also
    as a dictionary. Each element can also be referenced using the first
    token in the expression as its key. Useful for tabular report
    scraping when the first column can be used as a item key.

    The optional ``asdict`` argument when set to True will return the
    parsed tokens as a Python dict instead of a pyparsing ParseResults.

    Example::

        data_word = Word(alphas)
        label = data_word + FollowedBy(\':\')

        text = "shape: SQUARE posn: upper left color: light blue texture: burlap"
        attr_expr = (label + Suppress(\':\') + OneOrMore(data_word, stop_on=label).set_parse_action(\' \'.join))

        # print attributes as plain groups
        print(attr_expr[1, ...].parse_string(text).dump())

        # instead of OneOrMore(expr), parse using Dict(Group(expr)[1, ...]) - Dict will auto-assign names
        result = Dict(Group(attr_expr)[1, ...]).parse_string(text)
        print(result.dump())

        # access named fields as dict entries, or output as dict
        print(result[\'shape\'])
        print(result.as_dict())

    prints::

        [\'shape\', \'SQUARE\', \'posn\', \'upper left\', \'color\', \'light blue\', \'texture\', \'burlap\']
        [[\'shape\', \'SQUARE\'], [\'posn\', \'upper left\'], [\'color\', \'light blue\'], [\'texture\', \'burlap\']]
        - color: \'light blue\'
        - posn: \'upper left\'
        - shape: \'SQUARE\'
        - texture: \'burlap\'
        SQUARE
        {\'color\': \'light blue\', \'posn\': \'upper left\', \'texture\': \'burlap\', \'shape\': \'SQUARE\'}

    See more examples at :class:`ParseResults` of accessing fields by results name.
    '''
    saveAsList: bool
    def __init__(self, expr: ParserElement, asdict: bool = False) -> None: ...
    def postParse(self, instring, loc, tokenlist): ...

class Suppress(TokenConverter):
    '''Converter for ignoring the results of a parsed expression.

    Example::

        source = "a, b, c,d"
        wd = Word(alphas)
        wd_list1 = wd + (\',\' + wd)[...]
        print(wd_list1.parse_string(source))

        # often, delimiters that are useful during parsing are just in the
        # way afterward - use Suppress to keep them out of the parsed output
        wd_list2 = wd + (Suppress(\',\') + wd)[...]
        print(wd_list2.parse_string(source))

        # Skipped text (using \'...\') can be suppressed as well
        source = "lead in START relevant text END trailing text"
        start_marker = Keyword("START")
        end_marker = Keyword("END")
        find_body = Suppress(...) + start_marker + ... + end_marker
        print(find_body.parse_string(source)

    prints::

        [\'a\', \',\', \'b\', \',\', \'c\', \',\', \'d\']
        [\'a\', \'b\', \'c\', \'d\']
        [\'START\', \'relevant text \', \'END\']

    (See also :class:`delimited_list`.)
    '''
    def __init__(self, expr: ParserElement | str, savelist: bool = False) -> None: ...
    def __add__(self, other) -> ParserElement: ...
    def __sub__(self, other) -> ParserElement: ...
    def postParse(self, instring, loc, tokenlist): ...
    def suppress(self) -> ParserElement: ...

def trace_parse_action(f: ParseAction) -> ParseAction:
    '''Decorator for debugging parse actions.

    When the parse action is called, this decorator will print
    ``">> entering method-name(line:<current_source_line>, <parse_location>, <matched_tokens>)"``.
    When the parse action completes, the decorator will print
    ``"<<"`` followed by the returned value, or any exception that the parse action raised.

    Example::

        wd = Word(alphas)

        @trace_parse_action
        def remove_duplicate_chars(tokens):
            return \'\'.join(sorted(set(\'\'.join(tokens))))

        wds = wd[1, ...].set_parse_action(remove_duplicate_chars)
        print(wds.parse_string("slkdjs sld sldd sdlf sdljf"))

    prints::

        >>entering remove_duplicate_chars(line: \'slkdjs sld sldd sdlf sdljf\', 0, ([\'slkdjs\', \'sld\', \'sldd\', \'sdlf\', \'sdljf\'], {}))
        <<leaving remove_duplicate_chars (ret: \'dfjkls\')
        [\'dfjkls\']
    '''

empty: Incomplete
line_start: Incomplete
line_end: Incomplete
string_start: Incomplete
string_end: Incomplete

def srange(s: str) -> str:
    '''Helper to easily define string ranges for use in :class:`Word`
    construction. Borrows syntax from regexp ``\'[]\'`` string range
    definitions::

        srange("[0-9]")   -> "0123456789"
        srange("[a-z]")   -> "abcdefghijklmnopqrstuvwxyz"
        srange("[a-z$_]") -> "abcdefghijklmnopqrstuvwxyz$_"

    The input string must be enclosed in []\'s, and the returned string
    is the expanded character set joined into a single string. The
    values enclosed in the []\'s may be:

    - a single character
    - an escaped character with a leading backslash (such as ``\\-``
      or ``\\]``)
    - an escaped hex character with a leading ``\'\\x\'``
      (``\\x21``, which is a ``\'!\'`` character) (``\\0x##``
      is also supported for backwards compatibility)
    - an escaped octal character with a leading ``\'\\0\'``
      (``\\041``, which is a ``\'!\'`` character)
    - a range of any of the above, separated by a dash (``\'a-z\'``,
      etc.)
    - any combination of the above (``\'aeiouy\'``,
      ``\'a-zA-Z0-9_$\'``, etc.)
    '''
def token_map(func, *args) -> ParseAction:
    """Helper to define a parse action by mapping a function to all
    elements of a :class:`ParseResults` list. If any additional args are passed,
    they are forwarded to the given function as additional arguments
    after the token, as in
    ``hex_integer = Word(hexnums).set_parse_action(token_map(int, 16))``,
    which will convert the parsed data to an integer using base 16.

    Example (compare the last to example in :class:`ParserElement.transform_string`::

        hex_ints = Word(hexnums)[1, ...].set_parse_action(token_map(int, 16))
        hex_ints.run_tests('''
            00 11 22 aa FF 0a 0d 1a
            ''')

        upperword = Word(alphas).set_parse_action(token_map(str.upper))
        upperword[1, ...].run_tests('''
            my kingdom for a horse
            ''')

        wd = Word(alphas).set_parse_action(token_map(str.title))
        wd[1, ...].set_parse_action(' '.join).run_tests('''
            now is the winter of our discontent made glorious summer by this sun of york
            ''')

    prints::

        00 11 22 aa FF 0a 0d 1a
        [0, 17, 34, 170, 255, 10, 13, 26]

        my kingdom for a horse
        ['MY', 'KINGDOM', 'FOR', 'A', 'HORSE']

        now is the winter of our discontent made glorious summer by this sun of york
        ['Now Is The Winter Of Our Discontent Made Glorious Summer By This Sun Of York']
    """
def autoname_elements() -> None:
    """
    Utility to simplify mass-naming of parser elements, for
    generating railroad diagram with named subdiagrams.
    """

dbl_quoted_string: Incomplete
sgl_quoted_string: Incomplete
quoted_string: Incomplete
unicode_string: Incomplete
alphas8bit: Incomplete
punc8bit: Incomplete
tokenMap = token_map
conditionAsParseAction = condition_as_parse_action
nullDebugAction = null_debug_action
sglQuotedString = sgl_quoted_string
dblQuotedString = dbl_quoted_string
quotedString = quoted_string
unicodeString = unicode_string
lineStart = line_start
lineEnd = line_end
stringStart = string_start
stringEnd = string_end
traceParseAction = trace_parse_action
