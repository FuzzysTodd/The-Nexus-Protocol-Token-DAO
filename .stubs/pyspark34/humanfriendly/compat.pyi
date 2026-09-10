from html.entities import name2codepoint as name2codepoint
from html.parser import HTMLParser as HTMLParser
from io import StringIO as StringIO
from shutil import which as which
from time import time as monotonic

__all__ = ['HTMLParser', 'StringIO', 'basestring', 'coerce_string', 'interactive_prompt', 'is_string', 'is_unicode', 'monotonic', 'name2codepoint', 'on_macos', 'on_windows', 'unichr', 'unicode', 'which']

unicode = unicode
unichr = unichr
basestring = basestring
interactive_prompt = raw_input
unicode = str
unichr = chr
basestring = str
interactive_prompt = input

def coerce_string(value):
    """
    Coerce any value to a Unicode string (:func:`python2:unicode` in Python 2 and :class:`python3:str` in Python 3).

    :param value: The value to coerce.
    :returns: The value coerced to a Unicode string.
    """
def is_string(value):
    """
    Check if a value is a :func:`python2:basestring` (in Python 2) or :class:`python3:str` (in Python 3) object.

    :param value: The value to check.
    :returns: :data:`True` if the value is a string, :data:`False` otherwise.
    """
def is_unicode(value):
    """
    Check if a value is a :func:`python2:unicode` (in Python 2) or :class:`python2:str` (in Python 3) object.

    :param value: The value to check.
    :returns: :data:`True` if the value is a Unicode string, :data:`False` otherwise.
    """
def on_macos():
    """
    Check if we're running on Apple MacOS.

    :returns: :data:`True` if running MacOS, :data:`False` otherwise.
    """
def on_windows():
    """
    Check if we're running on the Microsoft Windows OS.

    :returns: :data:`True` if running Windows, :data:`False` otherwise.
    """
