from _typeshed import Incomplete

special_unicode = unicode

class special_unicode: ...
basestring = basestring
basestring = str
mysplit: Incomplete
replacements: Incomplete

def string_triplequote_repr(s):
    """Return string's python representation in triple quotes.
    """
def pretty_string(s, embedded, current_line, uni_lit: bool = False, min_trip_str: int = 20, max_line: int = 100):
    """There are a lot of reasons why we might not want to or
       be able to return a triple-quoted string.  We can always
       punt back to the default normal string.
    """
