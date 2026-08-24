import enum
from _typeshed import Incomplete
from dataclasses import dataclass
from functools import cached_property
from traitlets.config.configurable import Configurable
from typing import Iterable, Iterator, List, Literal, Sequence, Set, Tuple, TypeVar, TypedDict
from typing_extensions import NotRequired, Protocol

__all__ = ['Completer', 'IPCompleter']

class ProvisionalCompleterWarning(FutureWarning):
    """
    Exception raise by an experimental feature in this module.

    Wrap code in :any:`provisionalcompleter` context manager if you
    are certain you want to use an unstable feature.
    """

class _FakeJediCompletion:
    """
    This is a workaround to communicate to the UI that Jedi has crashed and to
    report a bug. Will be used only id :any:`IPCompleter.debug` is set to true.

    Added in IPython 6.0 so should likely be removed for 7.0

    """
    name: Incomplete
    complete: Incomplete
    type: str
    name_with_symbols: Incomplete
    signature: str
    text: str
    def __init__(self, name) -> None: ...

class Completion:
    """
    Completion object used and returned by IPython completers.

    .. warning::

        Unstable

        This function is unstable, API may change without warning.
        It will also raise unless use in proper context manager.

    This act as a middle ground :any:`Completion` object between the
    :any:`jedi.api.classes.Completion` object and the Prompt Toolkit completion
    object. While Jedi need a lot of information about evaluator and how the
    code should be ran/inspected, PromptToolkit (and other frontend) mostly
    need user facing information.

    - Which range should be replaced replaced by what.
    - Some metadata (like completion type), or meta information to displayed to
      the use user.

    For debugging purpose we can also store the origin of the completion (``jedi``,
    ``IPython.python_matches``, ``IPython.magics_matches``...).
    """
    start: Incomplete
    end: Incomplete
    text: Incomplete
    type: Incomplete
    signature: Incomplete
    def __init__(self, start: int, end: int, text: str, *, type: str | None = None, _origin: str = '', signature: str = '') -> None: ...
    def __eq__(self, other) -> bool:
        """
        Equality and hash do not hash the type (as some completer may not be
        able to infer the type), but are use to (partially) de-duplicate
        completion.

        Completely de-duplicating completion is a bit tricker that just
        comparing as it depends on surrounding text, which Completions are not
        aware of.
        """
    def __hash__(self): ...

class SimpleCompletion:
    '''Completion item to be included in the dictionary returned by new-style Matcher (API v2).

    .. warning::

        Provisional

        This class is used to describe the currently supported attributes of
        simple completion items, and any additional implementation details
        should not be relied on. Additional attributes may be included in
        future versions, and meaning of text disambiguated from the current
        dual meaning of "text to insert" and "text to used as a label".
    '''
    text: Incomplete
    type: Incomplete
    def __init__(self, text: str, *, type: str | None = None) -> None: ...

class _MatcherResultBase(TypedDict):
    """Definition of dictionary to be returned by new-style Matcher (API v2)."""
    matched_fragment: NotRequired[str]
    suppress: NotRequired[bool | Set[str]]
    do_not_suppress: NotRequired[Set[str]]
    ordered: NotRequired[bool]

class SimpleMatcherResult(_MatcherResultBase, TypedDict):
    """Result of new-style completion matcher."""
    completions: Sequence[SimpleCompletion] | Iterator[SimpleCompletion]

class _JediMatcherResult(_MatcherResultBase):
    """Matching result returned by Jedi (will be processed differently)"""
    completions: Iterator[_JediCompletionLike]
AnyCompletion = TypeVar('AnyCompletion', AnyMatcherCompletion, Completion)

@dataclass
class CompletionContext:
    """Completion context provided as an argument to matchers in the Matcher API v2."""
    token: str
    full_text: str
    cursor_position: int
    cursor_line: int
    limit: int | None
    @cached_property
    def text_until_cursor(self) -> str: ...
    @cached_property
    def line_with_cursor(self) -> str: ...
    def __init__(self, token, full_text, cursor_position, cursor_line, limit) -> None: ...

class _MatcherAPIv1Base(Protocol):
    def __call__(self, text: str) -> List[str]:
        """Call signature."""
    __qualname__: str

class _MatcherAPIv1Total(_MatcherAPIv1Base, Protocol):
    matcher_api_version: Literal[1] | None
    def __call__(self, text: str) -> List[str]:
        """Call signature."""

class MatcherAPIv2(Protocol):
    """Protocol describing Matcher API v2."""
    matcher_api_version: Literal[2]
    def __call__(self, context: CompletionContext) -> MatcherResult:
        """Call signature."""
    __qualname__: str

class CompletionSplitter:
    """An object to split an input line in a manner similar to readline.

    By having our own implementation, we can expose readline-like completion in
    a uniform manner to all frontends.  This object only needs to be given the
    line of text to be split and the cursor position on said line, and it
    returns the 'word' to be completed on at the cursor after splitting the
    entire line.

    What characters are used as splitting delimiters can be controlled by
    setting the ``delims`` attribute (this is a property that internally
    automatically builds the necessary regular expression)"""
    def __init__(self, delims: Incomplete | None = None) -> None: ...
    @property
    def delims(self):
        """Return the string of delimiter characters."""
    @delims.setter
    def delims(self, delims) -> None:
        """Set the delimiters for line splitting."""
    def split_line(self, line, cursor_pos: Incomplete | None = None):
        """Split a line of text with a cursor at the given position.
        """

class Completer(Configurable):
    greedy: Incomplete
    evaluation: Incomplete
    use_jedi: Incomplete
    jedi_compute_type_timeout: Incomplete
    debug: Incomplete
    backslash_combining_completions: Incomplete
    auto_close_dict_keys: Incomplete
    use_main_ns: bool
    namespace: Incomplete
    global_namespace: Incomplete
    custom_matchers: Incomplete
    def __init__(self, namespace: Incomplete | None = None, global_namespace: Incomplete | None = None, **kwargs) -> None:
        """Create a new completer for the command line.

        Completer(namespace=ns, global_namespace=ns2) -> completer instance.

        If unspecified, the default namespace where completions are performed
        is __main__ (technically, __main__.__dict__). Namespaces should be
        given as dictionaries.

        An optional second namespace can be given.  This allows the completer
        to handle cases where both the local and global scopes need to be
        distinguished.
        """
    matches: Incomplete
    def complete(self, text, state):
        """Return the next possible completion for 'text'.

        This is called successively with state == 0, 1, 2, ... until it
        returns None.  The completion should begin with 'text'.

        """
    def global_matches(self, text):
        """Compute matches when text is a simple name.

        Return a list of all keywords, built-in functions and names currently
        defined in self.namespace or self.global_namespace that match.

        """
    def attr_matches(self, text):
        """Compute matches when text contains a dot.

        Assuming the text is of the form NAME.NAME....[NAME], and is
        evaluatable in self.namespace or self.global_namespace, it will be
        evaluated and its attributes (as revealed by dir()) are used as
        possible completions.  (For class instances, class members are
        also considered.)

        WARNING: this can still invoke arbitrary C code, if an object
        with a __getattr__ hook is evaluated.

        """

class _DictKeyState(enum.Flag):
    """Represent state of the key match in context of other possible matches.

    - given `d1 = {'a': 1}` completion on `d1['<tab>` will yield `{'a': END_OF_ITEM}` as there is no tuple.
    - given `d2 = {('a', 'b'): 1}`: `d2['a', '<tab>` will yield `{'b': END_OF_TUPLE}` as there is no tuple members to add beyond `'b'`.
    - given `d3 = {('a', 'b'): 1}`: `d3['<tab>` will yield `{'a': IN_TUPLE}` as `'a'` can be added.
    - given `d4 = {'a': 1, ('a', 'b'): 2}`: `d4['<tab>` will yield `{'a': END_OF_ITEM & END_OF_TUPLE}`
    """
    BASELINE: int
    END_OF_ITEM: Incomplete
    END_OF_TUPLE: Incomplete
    IN_TUPLE: Incomplete

class IPCompleter(Completer):
    """Extension of the completer class with IPython-specific features"""
    dict_keys_only: Incomplete
    suppress_competing_matchers: Incomplete
    merge_completions: Incomplete
    disable_matchers: Incomplete
    omit__names: Incomplete
    limit_to__all__: Incomplete
    profile_completions: Incomplete
    profiler_output_dir: Incomplete
    magic_escape: Incomplete
    splitter: Incomplete
    matches: Incomplete
    shell: Incomplete
    space_name_re: Incomplete
    glob: Incomplete
    dumb_terminal: Incomplete
    clean_glob: Incomplete
    docstring_sig_re: Incomplete
    docstring_kwd_re: Incomplete
    magic_arg_matchers: Incomplete
    custom_completers: Incomplete
    def __init__(self, shell: Incomplete | None = None, namespace: Incomplete | None = None, global_namespace: Incomplete | None = None, config: Incomplete | None = None, **kwargs) -> None:
        """IPCompleter() -> completer

        Return a completer object.

        Parameters
        ----------
        shell
            a pointer to the ipython shell itself.  This is needed
            because this completer knows about magic functions, and those can
            only be accessed via the ipython instance.
        namespace : dict, optional
            an optional dict where completions are performed.
        global_namespace : dict, optional
            secondary optional dict for completions, to
            handle cases (such as IPython embedded inside functions) where
            both Python scopes are visible.
        config : Config
            traitlet's config object
        **kwargs
            passed to super class unmodified.
        """
    @property
    def matchers(self) -> List[Matcher]:
        """All active matcher routines for completion"""
    def all_completions(self, text: str) -> List[str]:
        """
        Wrapper around the completion methods for the benefit of emacs.
        """
    def file_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Same as :any:`file_matches`, but adopted to new Matcher API."""
    def file_matches(self, text: str) -> List[str]:
        """Match filenames, expanding ~USER type strings.

        Most of the seemingly convoluted logic in this completer is an
        attempt to handle filenames with spaces in them.  And yet it's not
        quite perfect, because Python's readline doesn't expose all of the
        GNU readline details needed for this to be done correctly.

        For a filename with a space in it, the printed completions will be
        only the parts after what's already been typed (instead of the
        full completions, as is normally done).  I don't think with the
        current (as of Python 2.3) Python readline it's possible to do
        better.

        .. deprecated:: 8.6
            You can use :meth:`file_matcher` instead.
        """
    def magic_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match magics."""
    def magic_matches(self, text: str):
        """Match magics.

        .. deprecated:: 8.6
            You can use :meth:`magic_matcher` instead.
        """
    def magic_config_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match class names and attributes for %config magic."""
    def magic_config_matches(self, text: str) -> List[str]:
        """Match class names and attributes for %config magic.

        .. deprecated:: 8.6
            You can use :meth:`magic_config_matcher` instead.
        """
    def magic_color_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match color schemes for %colors magic."""
    def magic_color_matches(self, text: str) -> List[str]:
        """Match color schemes for %colors magic.

        .. deprecated:: 8.6
            You can use :meth:`magic_color_matcher` instead.
        """
    def python_matches(self, text: str) -> Iterable[str]:
        """Match attributes or global python names"""
    def python_func_kw_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match named parameters (kwargs) of the last open function."""
    def python_func_kw_matches(self, text):
        """Match named parameters (kwargs) of the last open function.

        .. deprecated:: 8.6
            You can use :meth:`python_func_kw_matcher` instead.
        """
    def dict_key_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match string keys in a dictionary, after e.g. ``foo[``."""
    def dict_key_matches(self, text: str) -> List[str]:
        """Match string keys in a dictionary, after e.g. ``foo[``.

        .. deprecated:: 8.6
            You can use :meth:`dict_key_matcher` instead.
        """
    def unicode_name_matcher(self, context: CompletionContext):
        """Same as :any:`unicode_name_matches`, but adopted to new Matcher API."""
    @staticmethod
    def unicode_name_matches(text: str) -> Tuple[str, List[str]]:
        """Match Latex-like syntax for unicode characters base
        on the name of the character.

        This does  ``\\GREEK SMALL LETTER ETA`` -> ``η``

        Works only on valid python 3 identifier, or on combining characters that
        will combine to form a valid identifier.
        """
    def latex_name_matcher(self, context: CompletionContext):
        """Match Latex syntax for unicode characters.

        This does both ``\\alp`` -> ``\\alpha`` and ``\\alpha`` -> ``α``
        """
    def latex_matches(self, text: str) -> Tuple[str, Sequence[str]]:
        """Match Latex syntax for unicode characters.

        This does both ``\\alp`` -> ``\\alpha`` and ``\\alpha`` -> ``α``

        .. deprecated:: 8.6
            You can use :meth:`latex_name_matcher` instead.
        """
    def custom_completer_matcher(self, context):
        """Dispatch custom completer.

        If a match is found, suppresses all other matchers except for Jedi.
        """
    def dispatch_custom_completer(self, text):
        """
        .. deprecated:: 8.6
            You can use :meth:`custom_completer_matcher` instead.
        """
    def completions(self, text: str, offset: int) -> Iterator[Completion]:
        '''
        Returns an iterator over the possible completions

        .. warning::

            Unstable

            This function is unstable, API may change without warning.
            It will also raise unless use in proper context manager.

        Parameters
        ----------
        text : str
            Full text of the current input, multi line string.
        offset : int
            Integer representing the position of the cursor in ``text``. Offset
            is 0-based indexed.

        Yields
        ------
        Completion

        Notes
        -----
        The cursor on a text can either be seen as being "in between"
        characters or "On" a character depending on the interface visible to
        the user. For consistency the cursor being on "in between" characters X
        and Y is equivalent to the cursor being "on" character Y, that is to say
        the character the cursor is on is considered as being after the cursor.

        Combining characters may span more that one position in the
        text.

        .. note::

            If ``IPCompleter.debug`` is :any:`True` will yield a ``--jedi/ipython--``
            fake Completion token to distinguish completion returned by Jedi
            and usual IPython completion.

        .. note::

            Completions are not completely deduplicated yet. If identical
            completions are coming from different sources this function does not
            ensure that each completion object will only be present once.
        '''
    def complete(self, text: Incomplete | None = None, line_buffer: Incomplete | None = None, cursor_pos: Incomplete | None = None) -> Tuple[str, Sequence[str]]:
        """Find completions for the given text and line context.

        Note that both the text and the line_buffer are optional, but at least
        one of them must be given.

        Parameters
        ----------
        text : string, optional
            Text to perform the completion on.  If not given, the line buffer
            is split using the instance's CompletionSplitter object.
        line_buffer : string, optional
            If not given, the completer attempts to obtain the current line
            buffer via readline.  This keyword allows clients which are
            requesting for text completions in non-readline contexts to inform
            the completer of the entire text.
        cursor_pos : int, optional
            Index of the cursor in the full line buffer.  Should be provided by
            remote frontends where kernel has no access to frontend state.

        Returns
        -------
        Tuple of two items:
        text : str
            Text that was actually used in the completion.
        matches : list
            A list of completion matches.

        Notes
        -----
            This API is likely to be deprecated and replaced by
            :any:`IPCompleter.completions` in the future.

        """
    def fwd_unicode_matcher(self, context: CompletionContext):
        """Same as :any:`fwd_unicode_match`, but adopted to new Matcher API."""
    def fwd_unicode_match(self, text: str) -> Tuple[str, Sequence[str]]:
        """
        Forward match a string starting with a backslash with a list of
        potential Unicode completions.

        Will compute list of Unicode character names on first call and cache it.

        .. deprecated:: 8.6
            You can use :meth:`fwd_unicode_matcher` instead.

        Returns
        -------
        At tuple with:
            - matched text (empty if no matches)
            - list of potential completions, empty tuple  otherwise)
        """
    @property
    def unicode_names(self) -> List[str]:
        """List of names of unicode code points that can be completed.

        The list is lazily initialized on first access.
        """
