from _typeshed import Incomplete
from sacremoses.corpus import NonbreakingPrefixes as NonbreakingPrefixes, Perluniprops as Perluniprops
from six import text_type as text_type

perluniprops: Incomplete
nonbreaking_prefixes: Incomplete

class MosesSentTokenizer:
    """
    This is a Python port of the Moses Tokenizer from
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/ems/support/split-sentences.perl
    """
