__all__ = ['asReStructuredText', 'asStructuredText']

def asStructuredText(I, munge: int = 0, rst: bool = False):
    """ Output structured text format.  Note, this will whack any existing
    'structured' format of the text.

    If `rst=True`, then the output will quote all code as inline literals in
    accordance with 'reStructuredText' markup principles.
    """
def asReStructuredText(I, munge: int = 0):
    """ Output reStructuredText format.  Note, this will whack any existing
    'structured' format of the text."""
