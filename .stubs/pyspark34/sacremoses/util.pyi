from _typeshed import Incomplete

class CJKChars:
    """
    An object that enumerates the code points of the CJK characters as listed on
    http://en.wikipedia.org/wiki/Basic_Multilingual_Plane#Basic_Multilingual_Plane
    """
    Hangul_Jamo: Incomplete
    CJK_Radicals: Incomplete
    Phags_Pa: Incomplete
    Hangul_Syllables: Incomplete
    CJK_Compatibility_Ideographs: Incomplete
    CJK_Compatibility_Forms: Incomplete
    Katakana_Hangul_Halfwidth: Incomplete
    Ideographic_Symbols_And_Punctuation: Incomplete
    Tangut: Incomplete
    Kana_Supplement: Incomplete
    Nushu: Incomplete
    Supplementary_Ideographic_Plane: Incomplete
    ranges: Incomplete

def is_cjk(character):
    """
    This checks for CJK character.

        >>> CJKChars().ranges
        [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215), (63744, 64255), (65072, 65103), (65381, 65500), (94208, 101119), (110592, 110895), (110960, 111359), (131072, 196607)]
        >>> is_cjk(u'㏾')
        True
        >>> is_cjk(u'﹟')
        False

    :param character: The character that needs to be checked.
    :type character: char
    :return: bool
    """
def xml_escape(text):
    '''
    This function transforms the input text into an "escaped" version suitable
    for well-formed XML formatting.
    Note that the default xml.sax.saxutils.escape() function don\'t escape
    some characters that Moses does so we have to manually add them to the
    entities dictionary.

        >>> input_str = \'\'\')| & < > \' " ] [\'\'\'
        >>> expected_output =  \'\'\')| &amp; &lt; &gt; \' " ] [\'\'\'
        >>> escape(input_str) == expected_output
        True
        >>> xml_escape(input_str)
        \')&#124; &amp; &lt; &gt; &apos; &quot; &#93; &#91;\'

    :param text: The text that needs to be escaped.
    :type text: str
    :rtype: str
    '''
def xml_unescape(text):
    '''
    This function transforms the "escaped" version suitable
    for well-formed XML formatting into humanly-readable string.
    Note that the default xml.sax.saxutils.unescape() function don\'t unescape
    some characters that Moses does so we have to manually add them to the
    entities dictionary.

        >>> from xml.sax.saxutils import unescape
        >>> s = \')&#124; &amp; &lt; &gt; &apos; &quot; &#93; &#91;\'
        >>> expected = \'\'\')| & < > \' " ] [\'\'\'
        >>> xml_unescape(s) == expected
        True

    :param text: The text that needs to be unescaped.
    :type text: str
    :rtype: str
    '''
def pairwise(iterable):
    """
    From https://docs.python.org/3/library/itertools.html#recipes
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
def grouper(iterable, n, fillvalue: Incomplete | None = None):
    """Collect data into fixed-length chunks or blocks
    from https://stackoverflow.com/a/16789869/610569
    """
def parallelize_preprocess(func, iterator, processes, progress_bar: bool = False): ...
