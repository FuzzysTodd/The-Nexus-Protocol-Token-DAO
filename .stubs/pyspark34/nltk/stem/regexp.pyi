from nltk.stem.api import StemmerI as StemmerI

class RegexpStemmer(StemmerI):
    """
    A stemmer that uses regular expressions to identify morphological
    affixes.  Any substrings that match the regular expressions will
    be removed.

        >>> from nltk.stem import RegexpStemmer
        >>> st = RegexpStemmer('ing$|s$|e$|able$', min=4)
        >>> st.stem('cars')
        'car'
        >>> st.stem('mass')
        'mas'
        >>> st.stem('was')
        'was'
        >>> st.stem('bee')
        'bee'
        >>> st.stem('compute')
        'comput'
        >>> st.stem('advisable')
        'advis'

    :type regexp: str or regexp
    :param regexp: The regular expression that should be used to
        identify morphological affixes.
    :type min: int
    :param min: The minimum length of string to stem
    """
    def __init__(self, regexp, min: int = 0) -> None: ...
    def stem(self, word): ...
