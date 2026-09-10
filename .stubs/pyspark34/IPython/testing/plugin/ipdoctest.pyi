import doctest
from _typeshed import Incomplete

log: Incomplete

class DocTestFinder(doctest.DocTestFinder): ...

class IPDoctestOutputChecker(doctest.OutputChecker):
    """Second-chance checker with support for random tests.

    If the default comparison doesn't pass, this checker looks in the expected
    output string for flags that tell us to ignore the output.
    """
    random_re: Incomplete
    def check_output(self, want, got, optionflags):
        """Check output, accepting special markers embedded in the output.

        If the output didn't pass the default validation but the special string
        '#random' is included, we accept it."""

class IPExample(doctest.Example): ...

class IPDocTestParser(doctest.DocTestParser):
    """
    A class used to parse strings containing doctest examples.

    Note: This is a version modified to properly recognize IPython input and
    convert any IPython examples into valid Python ones.
    """
    def ip2py(self, source):
        """Convert input IPython source into valid Python."""
    def parse(self, string, name: str = '<string>'):
        """
        Divide the given string into examples and intervening text,
        and return them as a list of alternating Examples and strings.
        Line numbers for the Examples are 0-based.  The optional
        argument `name` is a name identifying this string, and is only
        used for error messages.
        """

SKIP: Incomplete

class IPDocTestRunner(doctest.DocTestRunner):
    """Test runner that synchronizes the IPython namespace with test globals.
    """
    def run(self, test, compileflags: Incomplete | None = None, out: Incomplete | None = None, clear_globs: bool = True): ...
