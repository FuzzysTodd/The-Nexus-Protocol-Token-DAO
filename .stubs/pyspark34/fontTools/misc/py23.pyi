import math as _math
from .textTools import Tag as Tag, bytechr as bytechr, byteord as byteord, bytesjoin as bytesjoin, strjoin as strjoin, tobytes as tobytes, tostr as tostr
from io import BytesIO as BytesIO, StringIO as UnicodeIO
from types import SimpleNamespace as SimpleNamespace

__all__ = ['basestring', 'bytechr', 'byteord', 'BytesIO', 'bytesjoin', 'open', 'Py23Error', 'range', 'RecursionError', 'round', 'SimpleNamespace', 'StringIO', 'strjoin', 'Tag', 'tobytes', 'tostr', 'tounicode', 'unichr', 'unicode', 'UnicodeIO', 'xrange', 'zip']

class Py23Error(NotImplementedError): ...
RecursionError = RecursionError
StringIO = UnicodeIO
basestring = str
isclose = _math.isclose
isfinite = _math.isfinite
open = open
range = range
round = round
round3 = round
unichr = chr
unicode = str
zip = zip
tounicode = tostr

def xrange(*args, **kwargs) -> None: ...
