from _typeshed import Incomplete
from pygments.formatter import Formatter

__all__ = ['PangoMarkupFormatter']

class PangoMarkupFormatter(Formatter):
    """
    Format tokens as Pango Markup code. It can then be rendered to an SVG.

    .. versionadded:: 2.9
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    styles: Incomplete
    def __init__(self, **options) -> None: ...
    def format_unencoded(self, tokensource, outfile) -> None: ...
