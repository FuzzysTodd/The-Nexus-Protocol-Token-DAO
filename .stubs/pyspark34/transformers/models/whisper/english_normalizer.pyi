from ...utils import is_more_itertools_available as is_more_itertools_available
from _typeshed import Incomplete
from typing import Iterator, List

ADDITIONAL_DIACRITICS: Incomplete

def remove_symbols_and_diacritics(s: str, keep: str = ''):
    """
    Replace any other markers, symbols, and punctuations with a space, and drop any diacritics (category 'Mn' and some
    manual mappings)
    """
def remove_symbols(s: str):
    """
    Replace any other markers, symbols, punctuations with a space, keeping diacritics
    """

class BasicTextNormalizer:
    clean: Incomplete
    split_letters: Incomplete
    def __init__(self, remove_diacritics: bool = False, split_letters: bool = False) -> None: ...
    def __call__(self, s: str): ...

class EnglishNumberNormalizer:
    """
    Convert any spelled-out numbers into arabic numbers, while handling:

    - remove any commas
    - keep the suffixes such as: `1960s`, `274th`, `32nd`, etc.
    - spell out currency symbols after the number. e.g. `$20 million` -> `20000000 dollars`
    - spell out `one` and `ones`
    - interpret successive single-digit numbers as nominal: `one oh one` -> `101`
    """
    zeros: Incomplete
    ones: Incomplete
    ones_plural: Incomplete
    ones_ordinal: Incomplete
    ones_suffixed: Incomplete
    tens: Incomplete
    tens_plural: Incomplete
    tens_ordinal: Incomplete
    tens_suffixed: Incomplete
    multipliers: Incomplete
    multipliers_plural: Incomplete
    multipliers_ordinal: Incomplete
    multipliers_suffixed: Incomplete
    decimals: Incomplete
    preceding_prefixers: Incomplete
    following_prefixers: Incomplete
    prefixes: Incomplete
    suffixers: Incomplete
    specials: Incomplete
    words: Incomplete
    literal_words: Incomplete
    def __init__(self) -> None: ...
    def process_words(self, words: List[str]) -> Iterator[str]: ...
    def preprocess(self, s: str): ...
    def postprocess(self, s: str): ...
    def __call__(self, s: str): ...

class EnglishSpellingNormalizer:
    """
    Applies British-American spelling mappings as listed in [1].

    [1] https://www.tysto.com/uk-us-spelling-list.html
    """
    mapping: Incomplete
    def __init__(self, english_spelling_mapping) -> None: ...
    def __call__(self, s: str): ...

class EnglishTextNormalizer:
    ignore_patterns: str
    replacers: Incomplete
    standardize_numbers: Incomplete
    standardize_spellings: Incomplete
    def __init__(self, english_spelling_mapping) -> None: ...
    def __call__(self, s: str): ...
