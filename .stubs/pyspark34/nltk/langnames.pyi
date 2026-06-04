from _typeshed import Incomplete
from nltk.corpus import bcp47 as bcp47

codepattern: Incomplete

def langname(tag, typ: str = 'full'):
    '''
    Convert a composite BCP-47 tag to a language name

    >>> from nltk.langnames import langname
    >>> langname(\'ca-Latn-ES-valencia\')
    \'Catalan: Latin: Spain: Valencian\'

    >>> langname(\'ca-Latn-ES-valencia\', typ="short")
    \'Catalan\'
    '''
def langcode(name, typ: int = 2):
    """
    Convert language name to iso639-3 language code. Returns the short 2-letter
    code by default, if one is available, and the 3-letter code otherwise:

    >>> from nltk.langnames import langcode
    >>> langcode('Modern Greek (1453-)')
    'el'

    Specify 'typ=3' to get the 3-letter code:

    >>> langcode('Modern Greek (1453-)', typ=3)
    'ell'
    """
def tag2q(tag):
    """
    Convert BCP-47 tag to Wikidata Q-code

    >>> tag2q('nds-u-sd-demv')
    'Q4289225'
    """
def q2tag(qcode):
    """
    Convert Wikidata Q-code to BCP-47 tag

    >>> q2tag('Q4289225')
    'nds-u-sd-demv'
    """
def q2name(qcode, typ: str = 'full'):
    '''
    Convert Wikidata Q-code to BCP-47 (full or short) language name

    >>> q2name(\'Q4289225\')
    \'Low German: Mecklenburg-Vorpommern\'

    >>> q2name(\'Q4289225\', "short")
    \'Low German\'
    '''
def lang2q(name):
    """
    Convert simple language name to Wikidata Q-code

    >>> lang2q('Low German')
    'Q25433'
    """
def inverse_dict(dic):
    """Return inverse mapping, but only if it is bijective"""

wiki_bcp47: Incomplete
iso639short: Incomplete
iso639retired: Incomplete
iso639long: Incomplete
iso639code_retired: Incomplete
