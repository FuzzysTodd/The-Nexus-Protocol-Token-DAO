from unicodedata2 import *
from unicodedata import *
from typing import TypeVar, overload

__all__ = ['lookup', 'name', 'decimal', 'digit', 'numeric', 'category', 'bidirectional', 'combining', 'east_asian_width', 'mirrored', 'decomposition', 'normalize', 'unidata_version', 'ucd_3_2_0', 'block', 'script', 'script_extension', 'script_name', 'script_code', 'script_horizontal_direction', 'ot_tags_from_script', 'ot_tag_to_script']

def script(char):
    '''Return the four-letter script code assigned to the Unicode character
    \'char\' as string.

    >>> script("a")
    \'Latn\'
    >>> script(",")
    \'Zyyy\'
    >>> script(chr(0x10FFFF))
    \'Zzzz\'
    '''
def script_extension(char):
    '''Return the script extension property assigned to the Unicode character
    \'char\' as a set of string.

    >>> script_extension("a") == {\'Latn\'}
    True
    >>> script_extension(chr(0x060C)) == {\'Rohg\', \'Syrc\', \'Yezi\', \'Arab\', \'Thaa\', \'Nkoo\'}
    True
    >>> script_extension(chr(0x10FFFF)) == {\'Zzzz\'}
    True
    '''
def script_name(code, default=...):
    """Return the long, human-readable script name given a four-letter
    Unicode script code.

    If no matching name is found, a KeyError is raised by default.

    You can use the 'default' argument to return a fallback value (e.g.
    'Unknown' or None) instead of throwing an error.
    """
def script_code(script_name, default=...):
    """Returns the four-letter Unicode script code from its long name

    If no matching script code is found, a KeyError is raised by default.

    You can use the 'default' argument to return a fallback string (e.g.
    'Zzzz' or None) instead of throwing an error.
    """
T = TypeVar('T')

@overload
def script_horizontal_direction(script_code: str, default: T) -> HorizDirection | T: ...
@overload
def script_horizontal_direction(script_code: str, default: type[KeyError] = ...) -> HorizDirection: ...
def block(char):
    '''Return the block property assigned to the Unicode character \'char\'
    as a string.

    >>> block("a")
    \'Basic Latin\'
    >>> block(chr(0x060C))
    \'Arabic\'
    >>> block(chr(0xEFFFF))
    \'No_Block\'
    '''
def ot_tags_from_script(script_code):
    """Return a list of OpenType script tags associated with a given
    Unicode script code.
    Return ['DFLT'] script tag for invalid/unknown script codes.
    """
def ot_tag_to_script(tag):
    '''Return the Unicode script code for the given OpenType script tag, or
    None for "DFLT" tag or if there is no Unicode script associated with it.
    Raises ValueError if the tag is invalid.
    '''

# Names in __all__ with no definition:
#   bidirectional
#   category
#   combining
#   decimal
#   decomposition
#   digit
#   east_asian_width
#   lookup
#   mirrored
#   name
#   normalize
#   numeric
#   ucd_3_2_0
#   unidata_version
