from .constant import FREQUENCIES as FREQUENCIES, KO_NAMES as KO_NAMES, LANGUAGE_SUPPORTED_COUNT as LANGUAGE_SUPPORTED_COUNT, TOO_SMALL_SEQUENCE as TOO_SMALL_SEQUENCE, ZH_NAMES as ZH_NAMES
from .md import is_suspiciously_successive_range as is_suspiciously_successive_range
from .models import CoherenceMatches as CoherenceMatches
from .utils import is_accentuated as is_accentuated, is_latin as is_latin, is_multi_byte_encoding as is_multi_byte_encoding, is_unicode_range_secondary as is_unicode_range_secondary, unicode_range as unicode_range
from typing import List, Tuple

def encoding_unicode_range(iana_name: str) -> List[str]:
    """
    Return associated unicode ranges in a single byte code page.
    """
def unicode_range_languages(primary_range: str) -> List[str]:
    """
    Return inferred languages used with a unicode range.
    """
def encoding_languages(iana_name: str) -> List[str]:
    """
    Single-byte encoding language association. Some code page are heavily linked to particular language(s).
    This function does the correspondence.
    """
def mb_encoding_languages(iana_name: str) -> List[str]:
    """
    Multi-byte encoding language association. Some code page are heavily linked to particular language(s).
    This function does the correspondence.
    """
def get_target_features(language: str) -> Tuple[bool, bool]:
    """
    Determine main aspects from a supported language if it contains accents and if is pure Latin.
    """
def alphabet_languages(characters: List[str], ignore_non_latin: bool = False) -> List[str]:
    """
    Return associated languages associated to given characters.
    """
def characters_popularity_compare(language: str, ordered_characters: List[str]) -> float:
    """
    Determine if a ordered characters list (by occurrence from most appearance to rarest) match a particular language.
    The result is a ratio between 0. (absolutely no correspondence) and 1. (near perfect fit).
    Beware that is function is not strict on the match in order to ease the detection. (Meaning close match is 1.)
    """
def alpha_unicode_split(decoded_sequence: str) -> List[str]:
    """
    Given a decoded text sequence, return a list of str. Unicode range / alphabet separation.
    Ex. a text containing English/Latin with a bit a Hebrew will return two items in the resulting list;
    One containing the latin letters and the other hebrew.
    """
def merge_coherence_ratios(results: List[CoherenceMatches]) -> CoherenceMatches:
    """
    This function merge results previously given by the function coherence_ratio.
    The return type is the same as coherence_ratio.
    """
def filter_alt_coherence_matches(results: CoherenceMatches) -> CoherenceMatches:
    '''
    We shall NOT return "English—" in CoherenceMatches because it is an alternative
    of "English". This function only keeps the best match and remove the em-dash in it.
    '''
def coherence_ratio(decoded_sequence: str, threshold: float = 0.1, lg_inclusion: str | None = None) -> CoherenceMatches:
    """
    Detect ANY language that can be identified in given sequence. The sequence will be analysed by layers.
    A layer = Character extraction by alphabets/ranges.
    """
