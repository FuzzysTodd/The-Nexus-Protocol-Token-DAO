from _typeshed import Incomplete
from mako import compat as compat, util as util

class MakoException(Exception): ...
class RuntimeException(MakoException): ...

class CompileException(MakoException):
    lineno: Incomplete
    pos: Incomplete
    filename: Incomplete
    source: Incomplete
    def __init__(self, message, source, lineno, pos, filename) -> None: ...

class SyntaxException(MakoException):
    lineno: Incomplete
    pos: Incomplete
    filename: Incomplete
    source: Incomplete
    def __init__(self, message, source, lineno, pos, filename) -> None: ...

class UnsupportedError(MakoException):
    """raised when a retired feature is used."""
class NameConflictError(MakoException):
    """raised when a reserved word is used inappropriately"""
class TemplateLookupException(MakoException): ...
class TopLevelLookupException(TemplateLookupException): ...

class RichTraceback:
    """Pull the current exception from the ``sys`` traceback and extracts
    Mako-specific template information.

    See the usage examples in :ref:`handling_exceptions`.

    """
    error: Incomplete
    records: Incomplete
    source: Incomplete
    lineno: Incomplete
    def __init__(self, error: Incomplete | None = None, traceback: Incomplete | None = None) -> None: ...
    @property
    def errorname(self): ...
    @property
    def traceback(self):
        """Return a list of 4-tuple traceback records (i.e. normal python
        format) with template-corresponding lines remapped to the originating
        template.

        """
    @property
    def reverse_records(self): ...
    @property
    def reverse_traceback(self):
        """Return the same data as traceback, except in reverse order."""

def text_error_template(lookup: Incomplete | None = None):
    """Provides a template that renders a stack trace in a similar format to
    the Python interpreter, substituting source template filenames, line
    numbers and code for that of the originating source template, as
    applicable.

    """
def html_error_template():
    """Provides a template that renders a stack trace in an HTML format,
    providing an excerpt of code as well as substituting source template
    filenames, line numbers and code for that of the originating source
    template, as applicable.

    The template's default ``encoding_errors`` value is
    ``'htmlentityreplace'``. The template has two options. With the
    ``full`` option disabled, only a section of an HTML document is
    returned. With the ``css`` option disabled, the default stylesheet
    won't be included.

    """
