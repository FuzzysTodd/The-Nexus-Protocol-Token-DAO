from _typeshed import Incomplete

__all__ = ['wrap_text', 'html2text', 'clean_html', 'add_anchor', 'strip_dollars', 'strip_files_prefix', 'comment_lines', 'get_lines', 'ipython2python', 'posix_path', 'path2url', 'add_prompts', 'ascii_only', 'prevent_list_blocks', 'strip_trailing_newline', 'text_base64']

def wrap_text(text, width: int = 100):
    """
    Intelligently wrap text.
    Wrap text without breaking words if possible.

    Parameters
    ----------
    text : str
        Text to wrap.
    width : int, optional
        Number of characters to wrap to, default 100.
    """
def html2text(element):
    """extract inner text from html

    Analog of jQuery's $(element).text()
    """
def clean_html(element):
    """Clean an html element."""
def add_anchor(html, anchor_link_text: str = '¶'):
    """Add an id and an anchor-link to an html header

    For use on markdown headings
    """
def add_prompts(code, first: str = '>>> ', cont: str = '... '):
    """Add prompts to code snippets"""
def strip_dollars(text):
    """
    Remove all dollar symbols from text

    Parameters
    ----------
    text : str
        Text to remove dollars from
    """
def strip_files_prefix(text):
    '''
    Fix all fake URLs that start with ``files/``, stripping out the ``files/`` prefix.
    Applies to both urls (for html) and relative paths (for markdown paths).

    Parameters
    ----------
    text : str
        Text in which to replace \'src="files/real...\' with \'src="real...\'
    '''
def comment_lines(text, prefix: str = '# '):
    """
    Build a Python comment line from input text.

    Parameters
    ----------
    text : str
        Text to comment out.
    prefix : str
        Character to append to the start of each line.
    """
def get_lines(text, start: Incomplete | None = None, end: Incomplete | None = None):
    """
    Split the input text into separate lines and then return the
    lines that the caller is interested in.

    Parameters
    ----------
    text : str
        Text to parse lines from.
    start : int, optional
        First line to grab from.
    end : int, optional
        Last line to grab from.
    """
def ipython2python(code):
    """Transform IPython syntax to pure Python syntax

    Parameters
    ----------
    code : str
        IPython code, to be transformed to pure Python
    """
def posix_path(path):
    """Turn a path into posix-style path/to/etc

    Mainly for use in latex on Windows,
    where native Windows paths are not allowed.
    """
def path2url(path):
    """Turn a file path into a URL"""
def ascii_only(s):
    """ensure a string is ascii"""
def prevent_list_blocks(s):
    """
    Prevent presence of enumerate or itemize blocks in latex headings cells
    """
def strip_trailing_newline(text):
    """
    Strips a newline from the end of text.
    """
def text_base64(text):
    """
    Encode base64 text
    """
