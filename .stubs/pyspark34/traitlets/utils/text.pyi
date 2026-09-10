from typing import List

def indent(val: str) -> str: ...
def wrap_paragraphs(text: str, ncols: int = 80) -> List[str]:
    """Wrap multiple paragraphs to fit a specified width.

    This is equivalent to textwrap.wrap, but with support for multiple
    paragraphs, as separated by empty lines.

    Returns
    -------

    list of complete paragraphs, wrapped to fill `ncols` columns.
    """
