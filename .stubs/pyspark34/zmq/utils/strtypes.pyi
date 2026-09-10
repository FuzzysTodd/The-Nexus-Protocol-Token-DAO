from _typeshed import Incomplete

__all__ = ['asbytes', 'bytes', 'unicode', 'basestring', 'b', 'u', 'cast_bytes', 'cast_unicode']

bytes = bytes
unicode = str
basestring: Incomplete

def cast_bytes(s, encoding: str = 'utf8', errors: str = 'strict'):
    """cast unicode or bytes to bytes"""
def cast_unicode(s, encoding: str = 'utf8', errors: str = 'strict'):
    """cast bytes or unicode to unicode"""
b = cast_bytes
asbytes = cast_bytes
u = cast_unicode
