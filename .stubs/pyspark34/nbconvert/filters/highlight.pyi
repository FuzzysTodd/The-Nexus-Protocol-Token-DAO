from _typeshed import Incomplete
from nbconvert.utils.base import NbConvertBase

__all__ = ['Highlight2HTML', 'Highlight2Latex']

class Highlight2HTML(NbConvertBase):
    """Convert highlighted code to html."""
    extra_formatter_options: Incomplete
    pygments_lexer: Incomplete
    def __init__(self, pygments_lexer: Incomplete | None = None, **kwargs) -> None:
        """Initialize the converter."""
    def __call__(self, source, language: Incomplete | None = None, metadata: Incomplete | None = None):
        """
        Return a syntax-highlighted version of the input source as html output.

        Parameters
        ----------
        source : str
            source of the cell to highlight
        language : str
            language to highlight the syntax of
        metadata : NotebookNode cell metadata
            metadata of the cell to highlight
        """

class Highlight2Latex(NbConvertBase):
    """Convert highlighted code to latex."""
    extra_formatter_options: Incomplete
    pygments_lexer: Incomplete
    def __init__(self, pygments_lexer: Incomplete | None = None, **kwargs) -> None:
        """Initialize the converter."""
    def __call__(self, source, language: Incomplete | None = None, metadata: Incomplete | None = None, strip_verbatim: bool = False):
        """
        Return a syntax-highlighted version of the input source as latex output.

        Parameters
        ----------
        source : str
            source of the cell to highlight
        language : str
            language to highlight the syntax of
        metadata : NotebookNode cell metadata
            metadata of the cell to highlight
        strip_verbatim : bool
            remove the Verbatim environment that pygments provides by default
        """
