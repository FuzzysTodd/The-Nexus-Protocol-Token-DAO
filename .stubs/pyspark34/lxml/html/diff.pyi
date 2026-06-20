import difflib
from _typeshed import Incomplete

__all__ = ['html_annotate', 'htmldiff']

basestring = str

def html_annotate(doclist, markup=...):
    '''
    doclist should be ordered from oldest to newest, like::

        >>> version1 = \'Hello World\'
        >>> version2 = \'Goodbye World\'
        >>> print(html_annotate([(version1, \'version 1\'),
        ...                      (version2, \'version 2\')]))
        <span title="version 2">Goodbye</span> <span title="version 1">World</span>

    The documents must be *fragments* (str/UTF8 or unicode), not
    complete documents

    The markup argument is a function to markup the spans of words.
    This function is called like markup(\'Hello\', \'version 2\'), and
    returns HTML.  The first argument is text and never includes any
    markup.  The default uses a span with a title:

        >>> print(default_markup(\'Some Text\', \'by Joe\'))
        <span title="by Joe">Some Text</span>
    '''
def htmldiff(old_html, new_html):
    """ Do a diff of the old and new document.  The documents are HTML
    *fragments* (str/UTF8 or unicode), they are not complete documents
    (i.e., no <html> tag).

    Returns HTML with <ins> and <del> tags added around the
    appropriate text.  

    Markup is generally ignored, with the markup from new_html
    preserved, and possibly some markup from old_html (though it is
    considered acceptable to lose some of the old markup).  Only the
    words in the HTML are diffed.  The exception is <img> tags, which
    are treated like words, and the href attribute of <a> tags, which
    are noted inside the tag itself when there are changes.
    """

class DEL_START: ...
class DEL_END: ...
class NoDeletes(Exception):
    """ Raised when the document no longer contains any pending deletes
    (DEL_START/DEL_END) """

class token(_unicode):
    """ Represents a diffable token, generally a word that is displayed to
    the user.  Opening tags are attached to this token when they are
    adjacent (pre_tags) and closing tags that follow the word
    (post_tags).  Some exceptions occur when there are empty tags
    adjacent to a word, so there may be close tags in pre_tags, or
    open tags in post_tags.

    We also keep track of whether the word was originally followed by
    whitespace, even though we do not want to treat the word as
    equivalent to a similar word that does not have a trailing
    space."""
    hide_when_equal: bool
    def __new__(cls, text, pre_tags: Incomplete | None = None, post_tags: Incomplete | None = None, trailing_whitespace: str = ''): ...
    def html(self): ...

class tag_token(token):
    """ Represents a token that is actually a tag.  Currently this is just
    the <img> tag, which takes up visible space just like a word but
    is only represented in a document by a tag.  """
    def __new__(cls, tag, data, html_repr, pre_tags: Incomplete | None = None, post_tags: Incomplete | None = None, trailing_whitespace: str = ''): ...
    def html(self): ...

class href_token(token):
    """ Represents the href in an anchor tag.  Unlike other words, we only
    show the href when it changes.  """
    hide_when_equal: bool
    def html(self): ...

class InsensitiveSequenceMatcher(difflib.SequenceMatcher):
    """
    Acts like SequenceMatcher, but tries not to find very small equal
    blocks amidst large spans of changes
    """
    threshold: int
    def get_matching_blocks(self): ...
