from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Perluniprops', 'NonbreakingPrefixes']

class Perluniprops:
    """
    This class is used to read lists of characters from the Perl Unicode
    Properties (see http://perldoc.perl.org/perluniprops.html).
    The files in the perluniprop.zip are extracted using the Unicode::Tussle
    module from http://search.cpan.org/~bdfoy/Unicode-Tussle-1.11/lib/Unicode/Tussle.pm
    """
    datadir: Incomplete
    available_categories: Incomplete
    def __init__(self) -> None: ...
    def chars(self, category: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        This module returns a list of characters from  the Perl Unicode Properties.
        They are very useful when porting Perl tokenizers to Python.

            >>> from sacremoses.corpus import Perluniprops
            >>> pup = Perluniprops()
            >>> list(pup.chars('Open_Punctuation'))[:5] == [u'(', u'[', u'{', u'༺', u'༼']
            True
            >>> list(pup.chars('Currency_Symbol'))[:5] == [u'$', u'¢', u'£', u'¤', u'¥']
            True
            >>> pup.available_categories[:5]
            ['Close_Punctuation', 'Currency_Symbol', 'IsAlnum', 'IsAlpha', 'IsLower']

        :return: a generator of characters given the specific unicode character category
        """

class NonbreakingPrefixes:
    """
    This is a class to read the nonbreaking prefixes textfiles from the
    Moses Machine Translation toolkit. These lists are used in the Python port
    of the Moses' word tokenizer.
    """
    datadir: Incomplete
    available_langs: Incomplete
    def __init__(self) -> None: ...
    def words(self, lang: Incomplete | None = None, ignore_lines_startswith: str = '#') -> Generator[Incomplete, None, None]:
        """
        This module returns a list of nonbreaking prefixes for the specified
        language(s).

            >>> from sacremoses.corpus import NonbreakingPrefixes
            >>> nbp = NonbreakingPrefixes()
            >>> list(nbp.words('en'))[:10] == [u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'I', u'J']
            True
            >>> list(nbp.words('ta'))[:5] == ['ர', 'ூ', 'திரு', 'ஏ', 'பீ']
            True

        :return: a generator words for the specified language(s).
        """
