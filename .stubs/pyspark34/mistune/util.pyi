def expand_leading_tab(text: str, width: int = 4): ...
def expand_tab(text: str, space: str = '    '): ...
def escape(s: str, quote: bool = True):
    '''Escape characters of ``&<>``. If quote=True, ``"`` will be
    converted to ``&quote;``.'''
def escape_url(link: str):
    """Escape URL for safety."""
def safe_entity(s: str):
    """Escape characters for safety."""
def unikey(s: str):
    """Generate a unique key for links and footnotes."""
def unescape(s: str):
    """
    Copy from `html.unescape`, but `_charref` is different. CommonMark
    does not accept entity references without a trailing semicolon
    """
def striptags(s: str): ...
def strip_end(src: str): ...
