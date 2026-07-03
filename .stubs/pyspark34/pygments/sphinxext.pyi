from _typeshed import Incomplete
from docutils.parsers.rst import Directive

MODULEDOC: str
LEXERDOC: str
FMTERDOC: str
FILTERDOC: str

class PygmentsDoc(Directive):
    """
    A directive to collect all lexers/formatters/filters and generate
    autoclass directives for them.
    """
    has_content: bool
    required_arguments: int
    optional_arguments: int
    final_argument_whitespace: bool
    option_spec: Incomplete
    filenames: Incomplete
    def run(self): ...
    def document_lexers_overview(self):
        '''Generate a tabular overview of all lexers.

        The columns are the lexer name, the extensions handled by this lexer
        (or "None"), the aliases and a link to the lexer class.'''
    def document_lexers(self): ...
    def document_formatters(self): ...
    def document_filters(self): ...

def setup(app) -> None: ...
