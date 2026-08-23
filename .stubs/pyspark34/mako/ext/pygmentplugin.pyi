from _typeshed import Incomplete
from pygments.lexer import DelegatingLexer, RegexLexer

class MakoLexer(RegexLexer):
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class MakoHtmlLexer(DelegatingLexer):
    name: str
    aliases: Incomplete
    def __init__(self, **options) -> None: ...

class MakoXmlLexer(DelegatingLexer):
    name: str
    aliases: Incomplete
    def __init__(self, **options) -> None: ...

class MakoJavascriptLexer(DelegatingLexer):
    name: str
    aliases: Incomplete
    def __init__(self, **options) -> None: ...

class MakoCssLexer(DelegatingLexer):
    name: str
    aliases: Incomplete
    def __init__(self, **options) -> None: ...

pygments_html_formatter: Incomplete

def syntax_highlight(filename: str = '', language: Incomplete | None = None): ...
