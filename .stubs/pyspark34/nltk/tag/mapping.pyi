from nltk.data import load as load

def tagset_mapping(source, target):
    """
    Retrieve the mapping dictionary between tagsets.

    >>> tagset_mapping('ru-rnc', 'universal') == {'!': '.', 'A': 'ADJ', 'C': 'CONJ', 'AD': 'ADV',            'NN': 'NOUN', 'VG': 'VERB', 'COMP': 'CONJ', 'NC': 'NUM', 'VP': 'VERB', 'P': 'ADP',            'IJ': 'X', 'V': 'VERB', 'Z': 'X', 'VI': 'VERB', 'YES_NO_SENT': 'X', 'PTCL': 'PRT'}
    True
    """
def map_tag(source, target, source_tag):
    """
    Maps the tag from the source tagset to the target tagset.

    >>> map_tag('en-ptb', 'universal', 'VBZ')
    'VERB'
    >>> map_tag('en-ptb', 'universal', 'VBP')
    'VERB'
    >>> map_tag('en-ptb', 'universal', '``')
    '.'
    """
