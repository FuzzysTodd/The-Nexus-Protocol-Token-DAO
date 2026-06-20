from _typeshed import Incomplete
from nltk.data import find as find, load as load
from nltk.tag.api import TaggerI as TaggerI
from nltk.tag.brill import BrillTagger as BrillTagger
from nltk.tag.brill_trainer import BrillTaggerTrainer as BrillTaggerTrainer
from nltk.tag.crf import CRFTagger as CRFTagger
from nltk.tag.hmm import HiddenMarkovModelTagger as HiddenMarkovModelTagger, HiddenMarkovModelTrainer as HiddenMarkovModelTrainer
from nltk.tag.hunpos import HunposTagger as HunposTagger
from nltk.tag.mapping import map_tag as map_tag, tagset_mapping as tagset_mapping
from nltk.tag.perceptron import PerceptronTagger as PerceptronTagger
from nltk.tag.senna import SennaChunkTagger as SennaChunkTagger, SennaNERTagger as SennaNERTagger, SennaTagger as SennaTagger
from nltk.tag.sequential import AffixTagger as AffixTagger, BigramTagger as BigramTagger, ClassifierBasedPOSTagger as ClassifierBasedPOSTagger, ClassifierBasedTagger as ClassifierBasedTagger, ContextTagger as ContextTagger, DefaultTagger as DefaultTagger, NgramTagger as NgramTagger, RegexpTagger as RegexpTagger, SequentialBackoffTagger as SequentialBackoffTagger, TrigramTagger as TrigramTagger, UnigramTagger as UnigramTagger
from nltk.tag.stanford import StanfordNERTagger as StanfordNERTagger, StanfordPOSTagger as StanfordPOSTagger, StanfordTagger as StanfordTagger
from nltk.tag.tnt import TnT as TnT
from nltk.tag.util import str2tuple as str2tuple, tuple2str as tuple2str, untag as untag

RUS_PICKLE: str

def pos_tag(tokens, tagset: Incomplete | None = None, lang: str = 'eng'):
    '''
    Use NLTK\'s currently recommended part of speech tagger to
    tag the given list of tokens.

        >>> from nltk.tag import pos_tag
        >>> from nltk.tokenize import word_tokenize
        >>> pos_tag(word_tokenize("John\'s big idea isn\'t all that bad.")) # doctest: +NORMALIZE_WHITESPACE
        [(\'John\', \'NNP\'), ("\'s", \'POS\'), (\'big\', \'JJ\'), (\'idea\', \'NN\'), (\'is\', \'VBZ\'),
        ("n\'t", \'RB\'), (\'all\', \'PDT\'), (\'that\', \'DT\'), (\'bad\', \'JJ\'), (\'.\', \'.\')]
        >>> pos_tag(word_tokenize("John\'s big idea isn\'t all that bad."), tagset=\'universal\') # doctest: +NORMALIZE_WHITESPACE
        [(\'John\', \'NOUN\'), ("\'s", \'PRT\'), (\'big\', \'ADJ\'), (\'idea\', \'NOUN\'), (\'is\', \'VERB\'),
        ("n\'t", \'ADV\'), (\'all\', \'DET\'), (\'that\', \'DET\'), (\'bad\', \'ADJ\'), (\'.\', \'.\')]

    NB. Use `pos_tag_sents()` for efficient tagging of more than one sentence.

    :param tokens: Sequence of tokens to be tagged
    :type tokens: list(str)
    :param tagset: the tagset to be used, e.g. universal, wsj, brown
    :type tagset: str
    :param lang: the ISO 639 code of the language, e.g. \'eng\' for English, \'rus\' for Russian
    :type lang: str
    :return: The tagged tokens
    :rtype: list(tuple(str, str))
    '''
def pos_tag_sents(sentences, tagset: Incomplete | None = None, lang: str = 'eng'):
    """
    Use NLTK's currently recommended part of speech tagger to tag the
    given list of sentences, each consisting of a list of tokens.

    :param sentences: List of sentences to be tagged
    :type sentences: list(list(str))
    :param tagset: the tagset to be used, e.g. universal, wsj, brown
    :type tagset: str
    :param lang: the ISO 639 code of the language, e.g. 'eng' for English, 'rus' for Russian
    :type lang: str
    :return: The list of tagged sentences
    :rtype: list(list(tuple(str, str)))
    """
