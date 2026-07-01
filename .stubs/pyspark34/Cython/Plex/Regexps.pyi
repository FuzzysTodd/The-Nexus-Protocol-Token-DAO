from . import Errors as Errors
from _typeshed import Incomplete

maxint: Incomplete
BOL: str
EOL: str
EOF: str
nl_code: Incomplete

def chars_to_ranges(s):
    """
    Return a list of character codes consisting of pairs
    [code1a, code1b, code2a, code2b,...] which cover all
    the characters in |s|.
    """
def uppercase_range(code1, code2):
    """
    If the range of characters from code1 to code2-1 includes any
    lower case letters, return the corresponding upper case range.
    """
def lowercase_range(code1, code2):
    """
    If the range of characters from code1 to code2-1 includes any
    upper case letters, return the corresponding lower case range.
    """
def CodeRanges(code_list):
    """
    Given a list of codes as returned by chars_to_ranges, return
    an RE which will match a character in any of the ranges.
    """
def CodeRange(code1, code2):
    """
    CodeRange(code1, code2) is an RE which matches any character
    with a code |c| in the range |code1| <= |c| < |code2|.
    """

class RE:
    """RE is the base class for regular expression constructors.
    The following operators are defined on REs:

         re1 + re2         is an RE which matches |re1| followed by |re2|
         re1 | re2         is an RE which matches either |re1| or |re2|
    """
    nullable: int
    match_nl: int
    str: Incomplete
    def build_machine(self, machine, initial_state, final_state, match_bol, nocase) -> None:
        """
        This method should add states to |machine| to implement this
        RE, starting at |initial_state| and ending at |final_state|.
        If |match_bol| is true, the RE must be able to match at the
        beginning of a line. If nocase is true, upper and lower case
        letters should be treated as equivalent.
        """
    def build_opt(self, m, initial_state, c):
        """
        Given a state |s| of machine |m|, return a new state
        reachable from |s| on character |c| or epsilon.
        """
    def __add__(self, other): ...
    def __or__(self, other): ...
    def check_re(self, num, value) -> None: ...
    def check_string(self, num, value) -> None: ...
    def check_char(self, num, value) -> None: ...
    def wrong_type(self, num, value, expected) -> None: ...

def Char(c):
    """
    Char(c) is an RE which matches the character |c|.
    """

class RawCodeRange(RE):
    """
    RawCodeRange(code1, code2) is a low-level RE which matches any character
    with a code |c| in the range |code1| <= |c| < |code2|, where the range
    does not include newline. For internal use only.
    """
    nullable: int
    match_nl: int
    range: Incomplete
    uppercase_range: Incomplete
    lowercase_range: Incomplete
    def __init__(self, code1, code2) -> None: ...
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...
    def calc_str(self): ...

class _RawNewline(RE):
    """
    RawNewline is a low-level RE which matches a newline character.
    For internal use only.
    """
    nullable: int
    match_nl: int
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...

RawNewline: Incomplete

class SpecialSymbol(RE):
    """
    SpecialSymbol(sym) is an RE which matches the special input
    symbol |sym|, which is one of BOL, EOL or EOF.
    """
    nullable: int
    match_nl: int
    sym: Incomplete
    def __init__(self, sym) -> None: ...
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...

class Seq(RE):
    """Seq(re1, re2, re3...) is an RE which matches |re1| followed by
    |re2| followed by |re3|..."""
    re_list: Incomplete
    nullable: Incomplete
    match_nl: Incomplete
    def __init__(self, *re_list) -> None: ...
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...
    def calc_str(self): ...

class Alt(RE):
    """Alt(re1, re2, re3...) is an RE which matches either |re1| or
    |re2| or |re3|..."""
    re_list: Incomplete
    nullable_res: Incomplete
    non_nullable_res: Incomplete
    nullable: Incomplete
    match_nl: Incomplete
    def __init__(self, *re_list) -> None: ...
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...
    def calc_str(self): ...

class Rep1(RE):
    """Rep1(re) is an RE which matches one or more repetitions of |re|."""
    re: Incomplete
    nullable: Incomplete
    match_nl: Incomplete
    def __init__(self, re) -> None: ...
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...
    def calc_str(self): ...

class SwitchCase(RE):
    """
    SwitchCase(re, nocase) is an RE which matches the same strings as RE,
    but treating upper and lower case letters according to |nocase|. If
    |nocase| is true, case is ignored, otherwise it is not.
    """
    re: Incomplete
    nocase: Incomplete
    nullable: Incomplete
    match_nl: Incomplete
    def __init__(self, re, nocase) -> None: ...
    def build_machine(self, m, initial_state, final_state, match_bol, nocase) -> None: ...
    def calc_str(self): ...

Empty: Incomplete

def Str1(s):
    """
    Str1(s) is an RE which matches the literal string |s|.
    """
def Str(*strs):
    """
    Str(s) is an RE which matches the literal string |s|.
    Str(s1, s2, s3, ...) is an RE which matches any of |s1| or |s2| or |s3|...
    """
def Any(s):
    """
    Any(s) is an RE which matches any character in the string |s|.
    """
def AnyBut(s):
    """
    AnyBut(s) is an RE which matches any character (including
    newline) which is not in the string |s|.
    """

AnyChar: Incomplete

def Range(s1, s2: Incomplete | None = None):
    """
    Range(c1, c2) is an RE which matches any single character in the range
    |c1| to |c2| inclusive.
    Range(s) where |s| is a string of even length is an RE which matches
    any single character in the ranges |s[0]| to |s[1]|, |s[2]| to |s[3]|,...
    """
def Opt(re):
    """
    Opt(re) is an RE which matches either |re| or the empty string.
    """
def Rep(re):
    """
    Rep(re) is an RE which matches zero or more repetitions of |re|.
    """
def NoCase(re):
    """
    NoCase(re) is an RE which matches the same strings as RE, but treating
    upper and lower case letters as equivalent.
    """
def Case(re):
    """
    Case(re) is an RE which matches the same strings as RE, but treating
    upper and lower case letters as distinct, i.e. it cancels the effect
    of any enclosing NoCase().
    """

Bol: Incomplete
Eol: Incomplete
Eof: Incomplete
