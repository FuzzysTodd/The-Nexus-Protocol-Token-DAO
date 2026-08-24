from .core import Keyword as Keyword, ParseException as ParseException, ParserElement as ParserElement, __compat__ as __compat__, __diag__ as __diag__
from _typeshed import Incomplete
from collections.abc import Generator

class pyparsing_test:
    """
    namespace class for classes useful in writing unit tests
    """
    class reset_pyparsing_context:
        '''
        Context manager to be used when writing unit tests that modify pyparsing config values:
        - packrat parsing
        - bounded recursion parsing
        - default whitespace characters.
        - default keyword characters
        - literal string auto-conversion class
        - __diag__ settings

        Example::

            with reset_pyparsing_context():
                # test that literals used to construct a grammar are automatically suppressed
                ParserElement.inlineLiteralsUsing(Suppress)

                term = Word(alphas) | Word(nums)
                group = Group(\'(\' + term[...] + \')\')

                # assert that the \'()\' characters are not included in the parsed tokens
                self.assertParseAndCheckList(group, "(abc 123 def)", [\'abc\', \'123\', \'def\'])

            # after exiting context manager, literals are converted to Literal expressions again
        '''
        def __init__(self) -> None: ...
        def save(self): ...
        def restore(self): ...
        def copy(self): ...
        def __enter__(self): ...
        def __exit__(self, *args) -> None: ...
    class TestParseResultsAsserts:
        """
        A mixin class to add parse results assertion methods to normal unittest.TestCase classes.
        """
        def assertParseResultsEquals(self, result, expected_list: Incomplete | None = None, expected_dict: Incomplete | None = None, msg: Incomplete | None = None) -> None:
            """
            Unit test assertion to compare a :class:`ParseResults` object with an optional ``expected_list``,
            and compare any defined results names with an optional ``expected_dict``.
            """
        def assertParseAndCheckList(self, expr, test_string, expected_list, msg: Incomplete | None = None, verbose: bool = True) -> None:
            """
            Convenience wrapper assert to test a parser element and input string, and assert that
            the resulting ``ParseResults.asList()`` is equal to the ``expected_list``.
            """
        def assertParseAndCheckDict(self, expr, test_string, expected_dict, msg: Incomplete | None = None, verbose: bool = True) -> None:
            """
            Convenience wrapper assert to test a parser element and input string, and assert that
            the resulting ``ParseResults.asDict()`` is equal to the ``expected_dict``.
            """
        def assertRunTestResults(self, run_tests_report, expected_parse_results: Incomplete | None = None, msg: Incomplete | None = None) -> None:
            """
            Unit test assertion to evaluate output of ``ParserElement.runTests()``. If a list of
            list-dict tuples is given as the ``expected_parse_results`` argument, then these are zipped
            with the report tuples returned by ``runTests`` and evaluated using ``assertParseResultsEquals``.
            Finally, asserts that the overall ``runTests()`` success value is ``True``.

            :param run_tests_report: tuple(bool, [tuple(str, ParseResults or Exception)]) returned from runTests
            :param expected_parse_results (optional): [tuple(str, list, dict, Exception)]
            """
        def assertRaisesParseException(self, exc_type=..., msg: Incomplete | None = None) -> Generator[None, None, None]: ...
    @staticmethod
    def with_line_numbers(s: str, start_line: int | None = None, end_line: int | None = None, expand_tabs: bool = True, eol_mark: str = '|', mark_spaces: str | None = None, mark_control: str | None = None) -> str:
        '''
        Helpful method for debugging a parser - prints a string with line and column numbers.
        (Line and column numbers are 1-based.)

        :param s: tuple(bool, str - string to be printed with line and column numbers
        :param start_line: int - (optional) starting line number in s to print (default=1)
        :param end_line: int - (optional) ending line number in s to print (default=len(s))
        :param expand_tabs: bool - (optional) expand tabs to spaces, to match the pyparsing default
        :param eol_mark: str - (optional) string to mark the end of lines, helps visualize trailing spaces (default="|")
        :param mark_spaces: str - (optional) special character to display in place of spaces
        :param mark_control: str - (optional) convert non-printing control characters to a placeholding
                                 character; valid values:
                                 - "unicode" - replaces control chars with Unicode symbols, such as "␍" and "␊"
                                 - any single character string - replace control characters with given string
                                 - None (default) - string is displayed as-is

        :return: str - input string with leading line numbers and column number headers
        '''
