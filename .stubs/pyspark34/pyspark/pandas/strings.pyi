import pyspark.pandas as ps
from _typeshed import Incomplete
from pyspark.sql.functions import pandas_udf as pandas_udf
from pyspark.sql.types import ArrayType as ArrayType, BinaryType as BinaryType, LongType as LongType, MapType as MapType, StringType as StringType
from typing import Any, Callable, Dict

class StringMethods:
    """String methods for pandas-on-Spark Series"""
    def __init__(self, series: ps.Series) -> None: ...
    def capitalize(self) -> ps.Series:
        """
        Convert Strings in the series to be capitalized.

        Examples
        --------
        >>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
        >>> s
        0                 lower
        1              CAPITALS
        2    this is a sentence
        3              SwApCaSe
        dtype: object

        >>> s.str.capitalize()
        0                 Lower
        1              Capitals
        2    This is a sentence
        3              Swapcase
        dtype: object
        """
    def title(self) -> ps.Series:
        """
        Convert Strings in the series to be title case.

        Examples
        --------
        >>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
        >>> s
        0                 lower
        1              CAPITALS
        2    this is a sentence
        3              SwApCaSe
        dtype: object

        >>> s.str.title()
        0                 Lower
        1              Capitals
        2    This Is A Sentence
        3              Swapcase
        dtype: object
        """
    def lower(self) -> ps.Series:
        """
        Convert strings in the Series/Index to all lowercase.

        Examples
        --------
        >>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
        >>> s
        0                 lower
        1              CAPITALS
        2    this is a sentence
        3              SwApCaSe
        dtype: object

        >>> s.str.lower()
        0                 lower
        1              capitals
        2    this is a sentence
        3              swapcase
        dtype: object
        """
    def upper(self) -> ps.Series:
        """
        Convert strings in the Series/Index to all uppercase.

        Examples
        --------
        >>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
        >>> s
        0                 lower
        1              CAPITALS
        2    this is a sentence
        3              SwApCaSe
        dtype: object

        >>> s.str.upper()
        0                 LOWER
        1              CAPITALS
        2    THIS IS A SENTENCE
        3              SWAPCASE
        dtype: object
        """
    def swapcase(self) -> ps.Series:
        """
        Convert strings in the Series/Index to be swap cased.

        Examples
        --------
        >>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
        >>> s
        0                 lower
        1              CAPITALS
        2    this is a sentence
        3              SwApCaSe
        dtype: object

        >>> s.str.swapcase()
        0                 LOWER
        1              capitals
        2    THIS IS A SENTENCE
        3              sWaPcAsE
        dtype: object
        """
    def startswith(self, pattern: str, na: Any | None = None) -> ps.Series:
        """
        Test if the start of each string element matches a pattern.

        Equivalent to :func:`str.startswith`.

        Parameters
        ----------
        pattern : str
            Character sequence. Regular expressions are not accepted.
        na : object, default None
            Object shown if element is not a string. NaN converted to None.

        Returns
        -------
        Series of bool or object
            pandas-on-Spark Series of booleans indicating whether the given pattern
            matches the start of each string element.

        Examples
        --------
        >>> s = ps.Series(['bat', 'Bear', 'cat', np.nan])
        >>> s
        0     bat
        1    Bear
        2     cat
        3    None
        dtype: object

        >>> s.str.startswith('b')
        0     True
        1    False
        2    False
        3     None
        dtype: object

        Specifying na to be False instead of None.

        >>> s.str.startswith('b', na=False)
        0     True
        1    False
        2    False
        3    False
        dtype: bool
        """
    def endswith(self, pattern: str, na: Any | None = None) -> ps.Series:
        """
        Test if the end of each string element matches a pattern.

        Equivalent to :func:`str.endswith`.

        Parameters
        ----------
        pattern : str
            Character sequence. Regular expressions are not accepted.
        na : object, default None
            Object shown if element is not a string. NaN converted to None.

        Returns
        -------
        Series of bool or object
            pandas-on-Spark Series of booleans indicating whether the given pattern
            matches the end of each string element.

        Examples
        --------
        >>> s = ps.Series(['bat', 'Bear', 'cat', np.nan])
        >>> s
        0     bat
        1    Bear
        2     cat
        3    None
        dtype: object

        >>> s.str.endswith('t')
        0     True
        1    False
        2     True
        3     None
        dtype: object

        Specifying na to be False instead of None.

        >>> s.str.endswith('t', na=False)
        0     True
        1    False
        2     True
        3    False
        dtype: bool
        """
    def strip(self, to_strip: str | None = None) -> ps.Series:
        """
        Remove leading and trailing characters.

        Strip whitespaces (including newlines) or a set of specified
        characters from each string in the Series/Index from left and
        right sides. Equivalent to :func:`str.strip`.

        Parameters
        ----------
        to_strip : str
            Specifying the set of characters to be removed. All combinations
            of this set of characters will be stripped. If None then
            whitespaces are removed.

        Returns
        -------
        Series of objects

        Examples
        --------
        >>> s = ps.Series(['1. Ant.', '2. Bee!\\t', None])
        >>> s
        0      1. Ant.
        1    2. Bee!\\t
        2         None
        dtype: object

        >>> s.str.strip()
        0    1. Ant.
        1    2. Bee!
        2       None
        dtype: object

        >>> s.str.strip('12.')
        0        Ant
        1     Bee!\\t
        2       None
        dtype: object

        >>> s.str.strip('.!\\t')
        0    1. Ant
        1    2. Bee
        2      None
        dtype: object
        """
    def lstrip(self, to_strip: str | None = None) -> ps.Series:
        """
        Remove leading characters.

        Strip whitespaces (including newlines) or a set of specified
        characters from each string in the Series/Index from left side.
        Equivalent to :func:`str.lstrip`.

        Parameters
        ----------
        to_strip : str
            Specifying the set of characters to be removed. All combinations
            of this set of characters will be stripped. If None then
            whitespaces are removed.

        Returns
        -------
        Series of object

        Examples
        --------
        >>> s = ps.Series(['1. Ant.', '2. Bee!\\t', None])
        >>> s
        0      1. Ant.
        1    2. Bee!\\t
        2         None
        dtype: object

        >>> s.str.lstrip('12.')
        0       Ant.
        1     Bee!\\t
        2       None
        dtype: object
        """
    def rstrip(self, to_strip: str | None = None) -> ps.Series:
        """
        Remove trailing characters.

        Strip whitespaces (including newlines) or a set of specified
        characters from each string in the Series/Index from right side.
        Equivalent to :func:`str.rstrip`.

        Parameters
        ----------
        to_strip : str
            Specifying the set of characters to be removed. All combinations
            of this set of characters will be stripped. If None then
            whitespaces are removed.

        Returns
        -------
        Series of object

        Examples
        --------
        >>> s = ps.Series(['1. Ant.', '2. Bee!\\t', None])
        >>> s
        0      1. Ant.
        1    2. Bee!\\t
        2         None
        dtype: object

        >>> s.str.rstrip('.!\\t')
        0    1. Ant
        1    2. Bee
        2      None
        dtype: object
        """
    def get(self, i: int) -> ps.Series:
        '''
        Extract element from each string or string list/tuple in the Series
        at the specified position.

        Parameters
        ----------
        i : int
            Position of element to extract.

        Returns
        -------
        Series of objects

        Examples
        --------
        >>> s1 = ps.Series(["String", "123"])
        >>> s1
        0    String
        1       123
        dtype: object

        >>> s1.str.get(1)
        0    t
        1    2
        dtype: object

        >>> s1.str.get(-1)
        0    g
        1    3
        dtype: object

        >>> s2 = ps.Series([["a", "b", "c"], ["x", "y"]])
        >>> s2
        0    [a, b, c]
        1       [x, y]
        dtype: object

        >>> s2.str.get(0)
        0    a
        1    x
        dtype: object

        >>> s2.str.get(2)
        0       c
        1    None
        dtype: object
        '''
    def isalnum(self) -> ps.Series:
        """
        Check whether all characters in each string are alphanumeric.

        This is equivalent to running the Python string method
        :func:`str.isalnum` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s1 = ps.Series(['one', 'one1', '1', ''])

        >>> s1.str.isalnum()
        0     True
        1     True
        2     True
        3    False
        dtype: bool

        Note that checks against characters mixed with any additional
        punctuation or whitespace will evaluate too false for an alphanumeric
        check.

        >>> s2 = ps.Series(['A B', '1.5', '3,000'])
        >>> s2.str.isalnum()
        0    False
        1    False
        2    False
        dtype: bool
        """
    def isalpha(self) -> ps.Series:
        """
        Check whether all characters in each string are alphabetic.

        This is equivalent to running the Python string method
        :func:`str.isalpha` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s1 = ps.Series(['one', 'one1', '1', ''])

        >>> s1.str.isalpha()
        0     True
        1    False
        2    False
        3    False
        dtype: bool
        """
    def isdigit(self) -> ps.Series:
        """
        Check whether all characters in each string are digits.

        This is equivalent to running the Python string method
        :func:`str.isdigit` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s = ps.Series(['23', '³', '⅕', ''])

        The s.str.isdecimal method checks for characters used to form numbers
        in base 10.

        >>> s.str.isdecimal()
        0     True
        1    False
        2    False
        3    False
        dtype: bool

        The s.str.isdigit method is the same as s.str.isdecimal but also
        includes special digits, like superscripted and subscripted digits in
        Unicode.

        >>> s.str.isdigit()
        0     True
        1     True
        2    False
        3    False
        dtype: bool

        The s.str.isnumeric method is the same as s.str.isdigit but also
        includes other characters that can represent quantities such as unicode
        fractions.

        >>> s.str.isnumeric()
        0     True
        1     True
        2     True
        3    False
        dtype: bool
        """
    def isspace(self) -> ps.Series:
        """
        Check whether all characters in each string are whitespaces.

        This is equivalent to running the Python string method
        :func:`str.isspace` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s = ps.Series([' ', '\\t\\r\\n ', ''])
        >>> s.str.isspace()
        0     True
        1     True
        2    False
        dtype: bool
        """
    def islower(self) -> ps.Series:
        """
        Check whether all characters in each string are lowercase.

        This is equivalent to running the Python string method
        :func:`str.islower` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s = ps.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])
        >>> s.str.islower()
        0     True
        1    False
        2    False
        3    False
        dtype: bool
        """
    def isupper(self) -> ps.Series:
        """
        Check whether all characters in each string are uppercase.

        This is equivalent to running the Python string method
        :func:`str.isupper` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s = ps.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])
        >>> s.str.isupper()
        0    False
        1    False
        2     True
        3    False
        dtype: bool
        """
    def istitle(self) -> ps.Series:
        """
        Check whether all characters in each string are title case.

        This is equivalent to running the Python string method
        :func:`str.istitle` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s = ps.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])

        The s.str.istitle method checks for whether all words are in title
        case (whether only the first letter of each word is capitalized).
        Words are assumed to be as any sequence of non-numeric characters
        separated by whitespace characters.

        >>> s.str.istitle()
        0    False
        1     True
        2    False
        3    False
        dtype: bool
        """
    def isnumeric(self) -> ps.Series:
        """
        Check whether all characters in each string are numeric.

        This is equivalent to running the Python string method
        :func:`str.isnumeric` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s1 = ps.Series(['one', 'one1', '1', ''])
        >>> s1.str.isnumeric()
        0    False
        1    False
        2     True
        3    False
        dtype: bool

        >>> s2 = ps.Series(['23', '³', '⅕', ''])

        The s2.str.isdecimal method checks for characters used to form numbers
        in base 10.

        >>> s2.str.isdecimal()
        0     True
        1    False
        2    False
        3    False
        dtype: bool

        The s2.str.isdigit method is the same as s2.str.isdecimal but also
        includes special digits, like superscripted and subscripted digits in
        Unicode.

        >>> s2.str.isdigit()
        0     True
        1     True
        2    False
        3    False
        dtype: bool

        The s2.str.isnumeric method is the same as s2.str.isdigit but also
        includes other characters that can represent quantities such as unicode
        fractions.

        >>> s2.str.isnumeric()
        0     True
        1     True
        2     True
        3    False
        dtype: bool
        """
    def isdecimal(self) -> ps.Series:
        """
        Check whether all characters in each string are decimals.

        This is equivalent to running the Python string method
        :func:`str.isdecimal` for each element of the Series/Index.
        If a string has zero characters, False is returned for that check.

        Examples
        --------
        >>> s = ps.Series(['23', '³', '⅕', ''])

        The s.str.isdecimal method checks for characters used to form numbers
        in base 10.

        >>> s.str.isdecimal()
        0     True
        1    False
        2    False
        3    False
        dtype: bool

        The s.str.isdigit method is the same as s.str.isdecimal but also
        includes special digits, like superscripted and subscripted digits in
        Unicode.

        >>> s.str.isdigit()
        0     True
        1     True
        2    False
        3    False
        dtype: bool

        The s.str.isnumeric method is the same as s.str.isdigit but also
        includes other characters that can represent quantities such as unicode
        fractions.

        >>> s.str.isnumeric()
        0     True
        1     True
        2     True
        3    False
        dtype: bool
        """
    def cat(self, others: Incomplete | None = None, sep: Incomplete | None = None, na_rep: Incomplete | None = None, join: Incomplete | None = None) -> None:
        """
        Not supported.
        """
    def center(self, width: int, fillchar: str = ' ') -> ps.Series:
        '''
        Filling left and right side of strings in the Series/Index with an
        additional character. Equivalent to :func:`str.center`.

        Parameters
        ----------
        width : int
            Minimum width of resulting string; additional characters will be
            filled with fillchar.
        fillchar : str
            Additional character for filling, default is whitespace.

        Returns
        -------
        Series of objects

        Examples
        --------
        >>> s = ps.Series(["caribou", "tiger"])
        >>> s
        0    caribou
        1      tiger
        dtype: object

        >>> s.str.center(width=10, fillchar=\'-\')
        0    -caribou--
        1    --tiger---
        dtype: object
        '''
    def contains(self, pat: str, case: bool = True, flags: int = 0, na: Any = None, regex: bool = True) -> ps.Series:
        """
        Test if pattern or regex is contained within a string of a Series.

        Return boolean Series based on whether a given pattern or regex is
        contained within a string of a Series.

        Analogous to :func:`match`, but less strict, relying on
        :func:`re.search` instead of :func:`re.match`.

        Parameters
        ----------
        pat : str
            Character sequence or regular expression.
        case : bool, default True
            If True, case sensitive.
        flags : int, default 0 (no flags)
            Flags to pass through to the re module, e.g. re.IGNORECASE.
        na : default None
            Fill value for missing values. NaN converted to None.
        regex : bool, default True
            If True, assumes the pat is a regular expression.
            If False, treats the pat as a literal string.


        Returns
        -------
        Series of boolean values or object
            A Series of boolean values indicating whether the given pattern is
            contained within the string of each element of the Series.

        Examples
        --------
        Returning a Series of booleans using only a literal pattern.

        >>> s1 = ps.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
        >>> s1.str.contains('og', regex=False)
        0    False
        1     True
        2    False
        3    False
        4     None
        dtype: object

        Specifying case sensitivity using case.

        >>> s1.str.contains('oG', case=True, regex=True)
        0    False
        1    False
        2    False
        3    False
        4     None
        dtype: object

        Specifying na to be False instead of NaN replaces NaN values with
        False. If Series does not contain NaN values the resultant dtype will
        be bool, otherwise, an object dtype.

        >>> s1.str.contains('og', na=False, regex=True)
        0    False
        1     True
        2    False
        3    False
        4    False
        dtype: bool

        Returning ‘house’ or ‘dog’ when either expression occurs in a string.

        >>> s1.str.contains('house|dog', regex=True)
        0    False
        1     True
        2     True
        3    False
        4     None
        dtype: object

        Ignoring case sensitivity using flags with regex.

        >>> import re
        >>> s1.str.contains('PARROT', flags=re.IGNORECASE, regex=True)
        0    False
        1    False
        2     True
        3    False
        4     None
        dtype: object

        Returning any digit using regular expression.

        >>> s1.str.contains('[0-9]', regex=True)
        0    False
        1    False
        2    False
        3     True
        4     None
        dtype: object

        Ensure pat is a not a literal pattern when regex is set to True.
        Note in the following example one might expect only s2[1] and s2[3]
        to return True. However, ‘.0’ as a regex matches any character followed
        by a 0.

        >>> s2 = ps.Series(['40','40.0','41','41.0','35'])
        >>> s2.str.contains('.0', regex=True)
        0     True
        1     True
        2    False
        3     True
        4    False
        dtype: bool
        """
    def count(self, pat: str, flags: int = 0) -> ps.Series:
        """
        Count occurrences of pattern in each string of the Series.

        This function is used to count the number of times a particular regex
        pattern is repeated in each of the string elements of the Series.

        Parameters
        ----------
        pat : str
            Valid regular expression.
        flags : int, default 0 (no flags)
            Flags for the re module.

        Returns
        -------
        Series of int
            A Series containing the integer counts of pattern matches.

        Examples
        --------
        >>> s = ps.Series(['A', 'B', 'Aaba', 'Baca', np.NaN, 'CABA', 'cat'])
        >>> s.str.count('a')
        0    0.0
        1    0.0
        2    2.0
        3    2.0
        4    NaN
        5    0.0
        6    1.0
        dtype: float64

        Escape '$' to find the literal dollar sign.

        >>> s = ps.Series(['$', 'B', 'Aab$', '$$ca', 'C$B$', 'cat'])
        >>> s.str.count('\\$')
        0    1
        1    0
        2    1
        3    2
        4    2
        5    0
        dtype: int64
        """
    def decode(self, encoding, errors: str = 'strict') -> None:
        """
        Not supported.
        """
    def encode(self, encoding, errors: str = 'strict') -> None:
        """
        Not supported.
        """
    def extract(self, pat, flags: int = 0, expand: bool = True) -> None:
        """
        Not supported.
        """
    def extractall(self, pat, flags: int = 0) -> None:
        """
        Not supported.
        """
    def find(self, sub: str, start: int = 0, end: int | None = None) -> ps.Series:
        """
        Return lowest indexes in each string in the Series where the
        substring is fully contained between [start:end].

        Return -1 on failure. Equivalent to standard :func:`str.find`.

        Parameters
        ----------
        sub : str
            Substring being searched.
        start : int
            Left edge index.
        end : int
            Right edge index.

        Returns
        -------
        Series of int
            Series of lowest matching indexes.

        Examples
        --------
        >>> s = ps.Series(['apple', 'oranges', 'bananas'])

        >>> s.str.find('a')
        0    0
        1    2
        2    1
        dtype: int64

        >>> s.str.find('a', start=2)
        0   -1
        1    2
        2    3
        dtype: int64

        >>> s.str.find('a', end=1)
        0    0
        1   -1
        2   -1
        dtype: int64

        >>> s.str.find('a', start=2, end=2)
        0   -1
        1   -1
        2   -1
        dtype: int64
        """
    def findall(self, pat: str, flags: int = 0) -> ps.Series:
        """
        Find all occurrences of pattern or regular expression in the Series.

        Equivalent to applying :func:`re.findall` to all the elements in
        the Series.

        Parameters
        ----------
        pat : str
            Pattern or regular expression.
        flags : int, default 0 (no flags)
            `re` module flags, e.g. `re.IGNORECASE`.

        Returns
        -------
        Series of object
            All non-overlapping matches of pattern or regular expression in
            each string of this Series.

        Examples
        --------
        >>> s = ps.Series(['Lion', 'Monkey', 'Rabbit'])

        The search for the pattern ‘Monkey’ returns one match:

        >>> s.str.findall('Monkey')
        0          []
        1    [Monkey]
        2          []
        dtype: object

        On the other hand, the search for the pattern ‘MONKEY’ doesn’t return
        any match:

        >>> s.str.findall('MONKEY')
        0    []
        1    []
        2    []
        dtype: object

        Flags can be added to the pattern or regular expression. For instance,
        to find the pattern ‘MONKEY’ ignoring the case:

        >>> import re
        >>> s.str.findall('MONKEY', flags=re.IGNORECASE)
        0          []
        1    [Monkey]
        2          []
        dtype: object

        When the pattern matches more than one string in the Series, all
        matches are returned:

        >>> s.str.findall('on')
        0    [on]
        1    [on]
        2      []
        dtype: object

        Regular expressions are supported too. For instance, the search for all
        the strings ending with the word ‘on’ is shown next:

        >>> s.str.findall('on$')
        0    [on]
        1      []
        2      []
        dtype: object

        If the pattern is found more than once in the same string, then a list
        of multiple strings is returned:

        >>> s.str.findall('b')
        0        []
        1        []
        2    [b, b]
        dtype: object
        """
    def index(self, sub: str, start: int = 0, end: int | None = None) -> ps.Series:
        """
        Return lowest indexes in each string where the substring is fully
        contained between [start:end].

        This is the same as :func:`str.find` except instead of returning -1,
        it raises a ValueError when the substring is not found. Equivalent to
        standard :func:`str.index`.

        Parameters
        ----------
        sub : str
            Substring being searched.
        start : int
            Left edge index.
        end : int
            Right edge index.

        Returns
        -------
        Series of int
            Series of lowest matching indexes.

        Examples
        --------
        >>> s = ps.Series(['apple', 'oranges', 'bananas'])

        >>> s.str.index('a')
        0    0
        1    2
        2    1
        dtype: int64

        The following expression throws an exception:

        >>> s.str.index('a', start=2) # doctest: +SKIP
        """
    def join(self, sep: str) -> ps.Series:
        """
        Join lists contained as elements in the Series with passed delimiter.

        If the elements of a Series are lists themselves, join the content of
        these lists using the delimiter passed to the function. This function
        is an equivalent to calling :func:`str.join` on the lists.

        Parameters
        ----------
        sep : str
            Delimiter to use between list entries.

        Returns
        -------
        Series of object
            Series with list entries concatenated by intervening occurrences of
            the delimiter.

        See Also
        --------
        str.split : Split strings around given separator/delimiter.
        str.rsplit : Splits string around given separator/delimiter,
            starting from the right.

        Examples
        --------
        Example with a list that contains a None element.

        >>> s = ps.Series([['lion', 'elephant', 'zebra'],
        ...                ['cat', None, 'dog']])
        >>> s
        0    [lion, elephant, zebra]
        1           [cat, None, dog]
        dtype: object

        Join all lists using a ‘-‘. The list containing None will produce None.

        >>> s.str.join('-')
        0    lion-elephant-zebra
        1                   None
        dtype: object
        """
    def len(self) -> ps.Series:
        '''
        Computes the length of each element in the Series.

        The element may be a sequence (such as a string, tuple or list).

        Returns
        -------
        Series of int
            A Series of integer values indicating the length of each element in
            the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for lists or tuples.

        >>> s1 = ps.Series([\'dog\', \'monkey\'])
        >>> s1.str.len()
        0    3
        1    6
        dtype: int64

        >>> s2 = ps.Series([["a", "b", "c"], []])
        >>> s2.str.len()
        0    3
        1    0
        dtype: int64
        '''
    def ljust(self, width: int, fillchar: str = ' ') -> ps.Series:
        '''
        Filling right side of strings in the Series with an additional
        character. Equivalent to :func:`str.ljust`.

        Parameters
        ----------
        width : int
            Minimum width of resulting string; additional characters will be
            filled with `fillchar`.
        fillchar : str
            Additional character for filling, default is whitespace.

        Returns
        -------
        Series of object

        Examples
        --------
        >>> s = ps.Series(["caribou", "tiger"])
        >>> s
        0    caribou
        1      tiger
        dtype: object

        >>> s.str.ljust(width=10, fillchar=\'-\')
        0    caribou---
        1    tiger-----
        dtype: object
        '''
    def match(self, pat: str, case: bool = True, flags: int = 0, na: Any = ...) -> ps.Series:
        """
        Determine if each string matches a regular expression.

        Analogous to :func:`contains`, but more strict, relying on
        :func:`re.match` instead of :func:`re.search`.

        Parameters
        ----------
        pat : str
            Character sequence or regular expression.
        case : bool, default True
            If True, case sensitive.
        flags : int, default 0 (no flags)
            Flags to pass through to the re module, e.g. re.IGNORECASE.
        na : default NaN
            Fill value for missing values.

        Returns
        -------
        Series of boolean values or object
            A Series of boolean values indicating whether the given pattern can
            be matched in the string of each element of the Series.

        Examples
        --------
        >>> s = ps.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
        >>> s.str.match('dog')
        0    False
        1     True
        2    False
        3    False
        4     None
        dtype: object

        >>> s.str.match('mouse|dog', case=False)
        0     True
        1     True
        2    False
        3    False
        4     None
        dtype: object

        >>> s.str.match('.+and.+', na=True)
        0    False
        1    False
        2     True
        3    False
        4     True
        dtype: bool

        >>> import re
        >>> s.str.match('MOUSE', flags=re.IGNORECASE)
        0     True
        1    False
        2    False
        3    False
        4     None
        dtype: object
        """
    def normalize(self, form: str) -> ps.Series:
        """
        Return the Unicode normal form for the strings in the Series.

        For more information on the forms, see the
        :func:`unicodedata.normalize`.

        Parameters
        ----------
        form : {‘NFC’, ‘NFKC’, ‘NFD’, ‘NFKD’}
            Unicode form.

        Returns
        -------
        Series of objects
            A Series of normalized strings.
        """
    def pad(self, width: int, side: str = 'left', fillchar: str = ' ') -> ps.Series:
        '''
        Pad strings in the Series up to width.

        Parameters
        ----------
        width : int
            Minimum width of resulting string; additional characters will be
            filled with character defined in `fillchar`.
        side : {‘left’, ‘right’, ‘both’}, default ‘left’
            Side from which to fill resulting string.
        fillchar : str, default \' \'
            Additional character for filling, default is whitespace.

        Returns
        -------
        Series of object
            Returns Series with minimum number of char in object.

        Examples
        --------
        >>> s = ps.Series(["caribou", "tiger"])
        >>> s
        0    caribou
        1      tiger
        dtype: object

        >>> s.str.pad(width=10)
        0       caribou
        1         tiger
        dtype: object

        >>> s.str.pad(width=10, side=\'right\', fillchar=\'-\')
        0    caribou---
        1    tiger-----
        dtype: object

        >>> s.str.pad(width=10, side=\'both\', fillchar=\'-\')
        0    -caribou--
        1    --tiger---
        dtype: object
        '''
    def partition(self, sep: str = ' ', expand: bool = True) -> ps.Series:
        """
        Not supported.
        """
    def repeat(self, repeats: int) -> ps.Series:
        """
        Duplicate each string in the Series.

        Parameters
        ----------
        repeats : int
            Repeat the string given number of times (int). Sequence of int
            is not supported.

        Returns
        -------
        Series of object
            Series or Index of repeated string objects specified by input
            parameter repeats.

        Examples
        --------
        >>> s = ps.Series(['a', 'b', 'c'])
        >>> s
        0    a
        1    b
        2    c
        dtype: object

        Single int repeats string in Series

        >>> s.str.repeat(repeats=2)
        0    aa
        1    bb
        2    cc
        dtype: object
        """
    def replace(self, pat: str, repl: str | Callable[[str], str], n: int = -1, case: bool | None = None, flags: int = 0, regex: bool = True) -> ps.Series:
        '''
        Replace occurrences of pattern/regex in the Series with some other
        string. Equivalent to :func:`str.replace` or :func:`re.sub`.

        Parameters
        ----------
        pat : str or compiled regex
            String can be a character sequence or regular expression.
        repl : str or callable
            Replacement string or a callable. The callable is passed the regex
            match object and must return a replacement string to be used. See
            :func:`re.sub`.
        n : int, default -1 (all)
            Number of replacements to make from start.
        case : boolean, default None
            If True, case sensitive (the default if pat is a string).
            Set to False for case insensitive.
            Cannot be set if pat is a compiled regex.
        flags: int, default 0 (no flags)
            re module flags, e.g. re.IGNORECASE.
            Cannot be set if pat is a compiled regex.
        regex : boolean, default True
            If True, assumes the passed-in pattern is a regular expression.
            If False, treats the pattern as a literal string.
            Cannot be set to False if pat is a compile regex or repl is a
            callable.

        Returns
        -------
        Series of object
            A copy of the string with all matching occurrences of pat replaced
            by repl.

        Examples
        --------
        When pat is a string and regex is True (the default), the given pat is
        compiled as a regex. When repl is a string, it replaces matching regex
        patterns as with :func:`re.sub`. NaN value(s) in the Series are changed
        to None:

        >>> ps.Series([\'foo\', \'fuz\', np.nan]).str.replace(\'f.\', \'ba\', regex=True)
        0     bao
        1     baz
        2    None
        dtype: object

        When pat is a string and regex is False, every pat is replaced with
        repl as with :func:`str.replace`:

        >>> ps.Series([\'f.o\', \'fuz\', np.nan]).str.replace(\'f.\', \'ba\', regex=False)
        0     bao
        1     fuz
        2    None
        dtype: object

        When repl is a callable, it is called on every pat using
        :func:`re.sub`. The callable should expect one positional argument (a
        regex object) and return a string.

        Reverse every lowercase alphabetic word:

        >>> repl = lambda m: m.group(0)[::-1]
        >>> ps.Series([\'foo 123\', \'bar baz\', np.nan]).str.replace(r\'[a-z]+\', repl)
        0    oof 123
        1    rab zab
        2       None
        dtype: object

        Using regex groups (extract second group and swap case):

        >>> pat = r"(?P<one>\\w+) (?P<two>\\w+) (?P<three>\\w+)"
        >>> repl = lambda m: m.group(\'two\').swapcase()
        >>> ps.Series([\'One Two Three\', \'Foo Bar Baz\']).str.replace(pat, repl)
        0    tWO
        1    bAR
        dtype: object

        Using a compiled regex with flags:

        >>> import re
        >>> regex_pat = re.compile(r\'FUZ\', flags=re.IGNORECASE)
        >>> ps.Series([\'foo\', \'fuz\', np.nan]).str.replace(regex_pat, \'bar\')
        0     foo
        1     bar
        2    None
        dtype: object
        '''
    def rfind(self, sub: str, start: int = 0, end: int | None = None) -> ps.Series:
        """
        Return highest indexes in each string in the Series where the
        substring is fully contained between [start:end].

        Return -1 on failure. Equivalent to standard :func:`str.rfind`.

        Parameters
        ----------
        sub : str
            Substring being searched.
        start : int
            Left edge index.
        end : int
            Right edge index.

        Returns
        -------
        Series of int
            Series of highest matching indexes.

        Examples
        --------
        >>> s = ps.Series(['apple', 'oranges', 'bananas'])

        >>> s.str.rfind('a')
        0    0
        1    2
        2    5
        dtype: int64

        >>> s.str.rfind('a', start=2)
        0   -1
        1    2
        2    5
        dtype: int64

        >>> s.str.rfind('a', end=1)
        0    0
        1   -1
        2   -1
        dtype: int64

        >>> s.str.rfind('a', start=2, end=2)
        0   -1
        1   -1
        2   -1
        dtype: int64
        """
    def rindex(self, sub: str, start: int = 0, end: int | None = None) -> ps.Series:
        """
        Return highest indexes in each string where the substring is fully
        contained between [start:end].

        This is the same as :func:`str.rfind` except instead of returning -1,
        it raises a ValueError when the substring is not found. Equivalent to
        standard :func:`str.rindex`.

        Parameters
        ----------
        sub : str
            Substring being searched.
        start : int
            Left edge index.
        end : int
            Right edge index.

        Returns
        -------
        Series of int
            Series of highest matching indexes.

        Examples
        --------
        >>> s = ps.Series(['apple', 'oranges', 'bananas'])

        >>> s.str.rindex('a')
        0    0
        1    2
        2    5
        dtype: int64

        The following expression throws an exception:

        >>> s.str.rindex('a', start=2) # doctest: +SKIP
        """
    def rjust(self, width: int, fillchar: str = ' ') -> ps.Series:
        '''
        Filling left side of strings in the Series with an additional
        character. Equivalent to :func:`str.rjust`.

        Parameters
        ----------
        width : int
            Minimum width of resulting string; additional characters will be
            filled with `fillchar`.
        fillchar : str
            Additional character for filling, default is whitespace.

        Returns
        -------
        Series of object

        Examples
        --------
        >>> s = ps.Series(["caribou", "tiger"])
        >>> s
        0    caribou
        1      tiger
        dtype: object

        >>> s.str.rjust(width=10)
        0       caribou
        1         tiger
        dtype: object

        >>> s.str.rjust(width=10, fillchar=\'-\')
        0    ---caribou
        1    -----tiger
        dtype: object
        '''
    def rpartition(self, sep: str = ' ', expand: bool = True) -> ps.Series:
        """
        Not supported.
        """
    def slice(self, start: int | None = None, stop: int | None = None, step: int | None = None) -> ps.Series:
        '''
        Slice substrings from each element in the Series.

        Parameters
        ----------
        start : int, optional
            Start position for slice operation.
        stop : int, optional
            Stop position for slice operation.
        step : int, optional
            Step size for slice operation.

        Returns
        -------
        Series of object
            Series from sliced substrings from original string objects.

        Examples
        --------
        >>> s = ps.Series(["koala", "fox", "chameleon"])
        >>> s
        0        koala
        1          fox
        2    chameleon
        dtype: object

        >>> s.str.slice(start=1)
        0        oala
        1          ox
        2    hameleon
        dtype: object

        >>> s.str.slice(stop=2)
        0    ko
        1    fo
        2    ch
        dtype: object

        >>> s.str.slice(step=2)
        0      kaa
        1       fx
        2    caeen
        dtype: object

        >>> s.str.slice(start=0, stop=5, step=3)
        0    kl
        1     f
        2    cm
        dtype: object
        '''
    def slice_replace(self, start: int | None = None, stop: int | None = None, repl: str | None = None) -> ps.Series:
        """
        Slice substrings from each element in the Series.

        Parameters
        ----------
        start : int, optional
            Start position for slice operation. If not specified (None), the
            slice is unbounded on the left, i.e. slice from the start of the
            string.
        stop : int, optional
            Stop position for slice operation. If not specified (None), the
            slice is unbounded on the right, i.e. slice until the end of the
            string.
        repl : str, optional
            String for replacement. If not specified (None), the sliced region
            is replaced with an empty string.

        Returns
        -------
        Series of object
            Series from sliced substrings from original string objects.

        Examples
        --------
        >>> s = ps.Series(['a', 'ab', 'abc', 'abdc', 'abcde'])
        >>> s
        0        a
        1       ab
        2      abc
        3     abdc
        4    abcde
        dtype: object

        Specify just start, meaning replace start until the end of the string
        with repl.

        >>> s.str.slice_replace(1, repl='X')
        0    aX
        1    aX
        2    aX
        3    aX
        4    aX
        dtype: object

        Specify just stop, meaning the start of the string to stop is replaced
        with repl, and the rest of the string is included.

        >>> s.str.slice_replace(stop=2, repl='X')
        0       X
        1       X
        2      Xc
        3     Xdc
        4    Xcde
        dtype: object

        Specify start and stop, meaning the slice from start to stop is
        replaced with repl. Everything before or after start and stop is
        included as is.

        >>> s.str.slice_replace(start=1, stop=3, repl='X')
        0      aX
        1      aX
        2      aX
        3     aXc
        4    aXde
        dtype: object
        """
    def split(self, pat: str | None = None, n: int = -1, expand: bool = False) -> ps.Series | ps.DataFrame:
        '''
        Split strings around given separator/delimiter.

        Splits the string in the Series from the beginning, at the specified
        delimiter string. Equivalent to :func:`str.split`.

        Parameters
        ----------
        pat : str, optional
            String or regular expression to split on. If not specified, split
            on whitespace.
        n : int, default -1 (all)
            Limit number of splits in output. None, 0 and -1 will be
            interpreted as return all splits.
        expand : bool, default False
            Expand the split strings into separate columns.

            * If ``True``, `n` must be a positive integer, and return DataFrame expanding
              dimensionality.
            * If ``False``, return Series, containing lists of strings.

        Returns
        -------
        Series, DataFrame
            Type matches caller unless `expand=True` (see Notes).

        See Also
        --------
        str.rsplit : Splits string around given separator/delimiter,
            starting from the right.
        str.join : Join lists contained as elements in the Series/Index
            with passed delimiter.

        Notes
        -----
        The handling of the `n` keyword depends on the number of found splits:

        - If found splits > `n`,  make first `n` splits only
        - If found splits <= `n`, make all splits
        - If for a certain row the number of found splits < `n`,
          append `None` for padding up to `n` if ``expand=True``

        If using ``expand=True``, Series callers return DataFrame objects with `n + 1` columns.

        .. note:: Even if `n` is much larger than found splits, the number of columns does NOT
            shrink unlike pandas.

        Examples
        --------
        >>> s = ps.Series(["this is a regular sentence",
        ...                "https://docs.python.org/3/tutorial/index.html",
        ...                np.nan])

        In the default setting, the string is split by whitespace.

        >>> s.str.split()
        0                   [this, is, a, regular, sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        Without the n parameter, the outputs of rsplit and split are identical.

        >>> s.str.rsplit()
        0                   [this, is, a, regular, sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        The n parameter can be used to limit the number of splits on the
        delimiter. The outputs of split and rsplit are different.

        >>> s.str.split(n=2)
        0                     [this, is, a regular sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        >>> s.str.rsplit(n=2)
        0                     [this is a, regular, sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        The pat parameter can be used to split by other characters.

        >>> s.str.split(pat = "/")
        0                         [this is a regular sentence]
        1    [https:, , docs.python.org, 3, tutorial, index...
        2                                                 None
        dtype: object

        When using ``expand=True``, the split elements will expand out into
        separate columns. If NaN is present, it is propagated throughout
        the columns during the split.

        >>> s.str.split(n=4, expand=True)
                                                       0     1     2        3         4
        0                                           this    is     a  regular  sentence
        1  https://docs.python.org/3/tutorial/index.html  None  None     None      None
        2                                           None  None  None     None      None

        For slightly more complex use cases like splitting the html document name
        from a url, a combination of parameter settings can be used.

        >>> s.str.rsplit("/", n=1, expand=True)
                                            0           1
        0          this is a regular sentence        None
        1  https://docs.python.org/3/tutorial  index.html
        2                                None        None

        Remember to escape special characters when explicitly using regular
        expressions.

        >>> s = ps.Series(["1+1=2"])
        >>> s.str.split(r"\\+|=", n=2, expand=True)
           0  1  2
        0  1  1  2
        '''
    def rsplit(self, pat: str | None = None, n: int = -1, expand: bool = False) -> ps.Series | ps.DataFrame:
        '''
        Split strings around given separator/delimiter.

        Splits the string in the Series from the end, at the specified
        delimiter string. Equivalent to :func:`str.rsplit`.

        Parameters
        ----------
        pat : str, optional
            String or regular expression to split on. If not specified, split
            on whitespace.
        n : int, default -1 (all)
            Limit number of splits in output. None, 0 and -1 will be
            interpreted as return all splits.
        expand : bool, default False
            Expand the split strings into separate columns.

            * If ``True``, `n` must be a positive integer, and return DataFrame expanding
              dimensionality.
            * If ``False``, return Series, containing lists of strings.

        Returns
        -------
        Series, DataFrame
            Type matches caller unless `expand=True` (see Notes).

        See Also
        --------
        str.split : Split strings around given separator/delimiter.
        str.join : Join lists contained as elements in the Series/Index
            with passed delimiter.

        Notes
        -----
        The handling of the `n` keyword depends on the number of found splits:

        - If found splits > `n`,  make first `n` splits only
        - If found splits <= `n`, make all splits
        - If for a certain row the number of found splits < `n`,
          append `None` for padding up to `n` if ``expand=True``

        If using ``expand=True``, Series callers return DataFrame objects with `n + 1` columns.

        .. note:: Even if `n` is much larger than found splits, the number of columns does NOT
            shrink unlike pandas.

        Examples
        --------
        >>> s = ps.Series(["this is a regular sentence",
        ...                "https://docs.python.org/3/tutorial/index.html",
        ...                np.nan])

        In the default setting, the string is split by whitespace.

        >>> s.str.split()
        0                   [this, is, a, regular, sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        Without the n parameter, the outputs of rsplit and split are identical.

        >>> s.str.rsplit()
        0                   [this, is, a, regular, sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        The n parameter can be used to limit the number of splits on the
        delimiter. The outputs of split and rsplit are different.

        >>> s.str.split(n=2)
        0                     [this, is, a regular sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        >>> s.str.rsplit(n=2)
        0                     [this is a, regular, sentence]
        1    [https://docs.python.org/3/tutorial/index.html]
        2                                               None
        dtype: object

        When using ``expand=True``, the split elements will expand out into
        separate columns. If NaN is present, it is propagated throughout
        the columns during the split.

        >>> s.str.split(n=4, expand=True)
                                                       0     1     2        3         4
        0                                           this    is     a  regular  sentence
        1  https://docs.python.org/3/tutorial/index.html  None  None     None      None
        2                                           None  None  None     None      None

        For slightly more complex use cases like splitting the html document name
        from a url, a combination of parameter settings can be used.

        >>> s.str.rsplit("/", n=1, expand=True)
                                            0           1
        0          this is a regular sentence        None
        1  https://docs.python.org/3/tutorial  index.html
        2                                None        None

        Remember to escape special characters when explicitly using regular
        expressions.

        >>> s = ps.Series(["1+1=2"])
        >>> s.str.split(r"\\+|=", n=2, expand=True)
           0  1  2
        0  1  1  2
        '''
    def translate(self, table: Dict) -> ps.Series:
        '''
        Map all characters in the string through the given mapping table.
        Equivalent to standard :func:`str.translate`.

        Parameters
        ----------
        table : dict
            Table is a mapping of Unicode ordinals to Unicode ordinals,
            strings, or None. Unmapped characters are left untouched.
            Characters mapped to None are deleted. :func:`str.maketrans` is a
            helper function for making translation tables.

        Returns
        -------
        Series of object
            Series with translated strings.

        Examples
        --------
        >>> s = ps.Series(["dog", "cat", "bird"])
        >>> m = str.maketrans({\'a\': \'X\', \'i\': \'Y\', \'o\': None})
        >>> s.str.translate(m)
        0      dg
        1     cXt
        2    bYrd
        dtype: object
        '''
    def wrap(self, width: int, **kwargs: bool) -> ps.Series:
        """
        Wrap long strings in the Series to be formatted in paragraphs with
        length less than a given width.

        This method has the same keyword parameters and defaults as
        :class:`textwrap.TextWrapper`.

        Parameters
        ----------
        width : int
            Maximum line-width. Lines separated with newline char.
        expand_tabs : bool, optional
            If true, tab characters will be expanded to spaces (default: True).
        replace_whitespace : bool, optional
            If true, each whitespace character remaining after tab expansion
            will be replaced by a single space (default: True).
        drop_whitespace : bool, optional
            If true, whitespace that, after wrapping, happens to end up at the
            beginning or end of a line is dropped (default: True).
        break_long_words : bool, optional
            If true, then words longer than width will be broken to
            ensure that no lines are longer than width. If it is false, long
            words will not be broken, and some lines may be longer than width
            (default: True).
        break_on_hyphens : bool, optional
            If true, wrapping will occur preferably on whitespace and right
            after hyphens in compound words, as it is customary in English.
            If false, only whitespaces will be considered as potentially good
            places for line breaks, but you need to set break_long_words to
            false if you want truly insecable words (default: True).

        Returns
        -------
        Series of object
            Series with wrapped strings.

        Examples
        --------
        >>> s = ps.Series(['line to be wrapped', 'another line to be wrapped'])
        >>> s.str.wrap(12)
        0             line to be\\nwrapped
        1    another line\\nto be\\nwrapped
        dtype: object
        """
    def zfill(self, width: int) -> ps.Series:
        """
        Pad strings in the Series by prepending ‘0’ characters.

        Strings in the Series are padded with ‘0’ characters on the left of the
        string to reach a total string length width. Strings in the Series with
        length greater or equal to width are unchanged.

        Differs from :func:`str.zfill` which has special handling for ‘+’/’-‘
        in the string.

        Parameters
        ----------
        width : int
            Minimum length of resulting string; strings with length less than
            width be prepended with ‘0’ characters.

        Returns
        -------
        Series of object
            Series with '0' left-padded strings.

        Examples
        --------
        >>> s = ps.Series(['-1', '1', '1000', np.nan])
        >>> s
        0      -1
        1       1
        2    1000
        3    None
        dtype: object

        Note that NaN is not a string, therefore it is converted to NaN. The
        minus sign in '-1' is treated as a regular character and the zero is
        added to the left of it (:func:`str.zfill` would have moved it to the
        left). 1000 remains unchanged as it is longer than width.

        >>> s.str.zfill(3)  # doctest: +SKIP
        0     -01
        1     001
        2    1000
        3    None
        dtype: object
        """
    def get_dummies(self, sep: str = '|') -> None:
        """
        Not supported.
        """
