from nltk.data import load as load
from nltk.tokenize.casual import TweetTokenizer as TweetTokenizer, casual_tokenize as casual_tokenize
from nltk.tokenize.destructive import NLTKWordTokenizer as NLTKWordTokenizer
from nltk.tokenize.legality_principle import LegalitySyllableTokenizer as LegalitySyllableTokenizer
from nltk.tokenize.mwe import MWETokenizer as MWETokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer as PunktSentenceTokenizer
from nltk.tokenize.regexp import BlanklineTokenizer as BlanklineTokenizer, RegexpTokenizer as RegexpTokenizer, WhitespaceTokenizer as WhitespaceTokenizer, WordPunctTokenizer as WordPunctTokenizer, blankline_tokenize as blankline_tokenize, regexp_tokenize as regexp_tokenize, wordpunct_tokenize as wordpunct_tokenize
from nltk.tokenize.repp import ReppTokenizer as ReppTokenizer
from nltk.tokenize.sexpr import SExprTokenizer as SExprTokenizer, sexpr_tokenize as sexpr_tokenize
from nltk.tokenize.simple import LineTokenizer as LineTokenizer, SpaceTokenizer as SpaceTokenizer, TabTokenizer as TabTokenizer, line_tokenize as line_tokenize
from nltk.tokenize.sonority_sequencing import SyllableTokenizer as SyllableTokenizer
from nltk.tokenize.stanford_segmenter import StanfordSegmenter as StanfordSegmenter
from nltk.tokenize.texttiling import TextTilingTokenizer as TextTilingTokenizer
from nltk.tokenize.toktok import ToktokTokenizer as ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer as TreebankWordDetokenizer, TreebankWordTokenizer as TreebankWordTokenizer
from nltk.tokenize.util import regexp_span_tokenize as regexp_span_tokenize, string_span_tokenize as string_span_tokenize

def sent_tokenize(text, language: str = 'english'):
    """
    Return a sentence-tokenized copy of *text*,
    using NLTK's recommended sentence tokenizer
    (currently :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into sentences
    :param language: the model name in the Punkt corpus
    """
def word_tokenize(text, language: str = 'english', preserve_line: bool = False):
    """
    Return a tokenized copy of *text*,
    using NLTK's recommended word tokenizer
    (currently an improved :class:`.TreebankWordTokenizer`
    along with :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into words
    :type text: str
    :param language: the model name in the Punkt corpus
    :type language: str
    :param preserve_line: A flag to decide whether to sentence tokenize the text or not.
    :type preserve_line: bool
    """
