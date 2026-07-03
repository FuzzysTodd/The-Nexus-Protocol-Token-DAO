from _typeshed import Incomplete
from nltk.probability import FreqDist as FreqDist
from nltk.tokenize.api import TokenizerI as TokenizerI
from typing import Any, Dict, Iterator, List, Tuple

REASON_DEFAULT_DECISION: str
REASON_KNOWN_COLLOCATION: str
REASON_ABBR_WITH_ORTHOGRAPHIC_HEURISTIC: str
REASON_ABBR_WITH_SENTENCE_STARTER: str
REASON_INITIAL_WITH_ORTHOGRAPHIC_HEURISTIC: str
REASON_NUMBER_WITH_ORTHOGRAPHIC_HEURISTIC: str
REASON_INITIAL_WITH_SPECIAL_ORTHOGRAPHIC_HEURISTIC: str

class PunktLanguageVars:
    """
    Stores variables, mostly regular expressions, which may be
    language-dependent for correct application of the algorithm.
    An extension of this class may modify its properties to suit
    a language other than English; an instance can then be passed
    as an argument to PunktSentenceTokenizer and PunktTrainer
    constructors.
    """
    sent_end_chars: Incomplete
    internal_punctuation: str
    re_boundary_realignment: Incomplete
    def word_tokenize(self, s):
        """Tokenize a string to split off punctuation other than periods"""
    def period_context_re(self):
        """Compiles and returns a regular expression to find contexts
        including possible sentence boundaries."""

class PunktParameters:
    """Stores data used to perform sentence boundary detection with Punkt."""
    abbrev_types: Incomplete
    collocations: Incomplete
    sent_starters: Incomplete
    ortho_context: Incomplete
    def __init__(self) -> None: ...
    def clear_abbrevs(self) -> None: ...
    def clear_collocations(self) -> None: ...
    def clear_sent_starters(self) -> None: ...
    def clear_ortho_context(self) -> None: ...
    def add_ortho_context(self, typ, flag) -> None: ...

class PunktToken:
    """Stores a token of text with annotations produced during
    sentence boundary detection."""
    tok: Incomplete
    type: Incomplete
    period_final: Incomplete
    def __init__(self, tok, **params) -> None: ...
    @property
    def type_no_period(self):
        """
        The type with its final period removed if it has one.
        """
    @property
    def type_no_sentperiod(self):
        """
        The type with its final period removed if it is marked as a
        sentence break.
        """
    @property
    def first_upper(self):
        """True if the token's first character is uppercase."""
    @property
    def first_lower(self):
        """True if the token's first character is lowercase."""
    @property
    def first_case(self): ...
    @property
    def is_ellipsis(self):
        """True if the token text is that of an ellipsis."""
    @property
    def is_number(self):
        """True if the token text is that of a number."""
    @property
    def is_initial(self):
        """True if the token text is that of an initial."""
    @property
    def is_alpha(self):
        """True if the token text is all alphabetic."""
    @property
    def is_non_punct(self):
        """True if the token is either a number or is alphabetic."""

class PunktBaseClass:
    """
    Includes common components of PunktTrainer and PunktSentenceTokenizer.
    """
    def __init__(self, lang_vars: Incomplete | None = None, token_cls=..., params: Incomplete | None = None) -> None: ...

class PunktTrainer(PunktBaseClass):
    """Learns parameters used in Punkt sentence boundary detection."""
    def __init__(self, train_text: Incomplete | None = None, verbose: bool = False, lang_vars: Incomplete | None = None, token_cls=...) -> None: ...
    def get_params(self):
        """
        Calculates and returns parameters for sentence boundary detection as
        derived from training."""
    ABBREV: float
    IGNORE_ABBREV_PENALTY: bool
    ABBREV_BACKOFF: int
    COLLOCATION: float
    SENT_STARTER: int
    INCLUDE_ALL_COLLOCS: bool
    INCLUDE_ABBREV_COLLOCS: bool
    MIN_COLLOC_FREQ: int
    def train(self, text, verbose: bool = False, finalize: bool = True) -> None:
        """
        Collects training data from a given text. If finalize is True, it
        will determine all the parameters for sentence boundary detection. If
        not, this will be delayed until get_params() or finalize_training() is
        called. If verbose is True, abbreviations found will be listed.
        """
    def train_tokens(self, tokens, verbose: bool = False, finalize: bool = True) -> None:
        """
        Collects training data from a given list of tokens.
        """
    def finalize_training(self, verbose: bool = False) -> None:
        """
        Uses data that has been gathered in training to determine likely
        collocations and sentence starters.
        """
    def freq_threshold(self, ortho_thresh: int = 2, type_thresh: int = 2, colloc_thres: int = 2, sentstart_thresh: int = 2) -> None:
        """
        Allows memory use to be reduced after much training by removing data
        about rare tokens that are unlikely to have a statistical effect with
        further training. Entries occurring above the given thresholds will be
        retained.
        """
    def find_abbrev_types(self) -> None:
        '''
        Recalculates abbreviations given type frequencies, despite no prior
        determination of abbreviations.
        This fails to include abbreviations otherwise found as "rare".
        '''

class PunktSentenceTokenizer(PunktBaseClass, TokenizerI):
    """
    A sentence tokenizer which uses an unsupervised algorithm to build
    a model for abbreviation words, collocations, and words that start
    sentences; and then uses that model to find sentence boundaries.
    This approach has been shown to work well for many European
    languages.
    """
    def __init__(self, train_text: Incomplete | None = None, verbose: bool = False, lang_vars: Incomplete | None = None, token_cls=...) -> None:
        """
        train_text can either be the sole training text for this sentence
        boundary detector, or can be a PunktParameters object.
        """
    def train(self, train_text, verbose: bool = False):
        """
        Derives parameters from a given training text, or uses the parameters
        given. Repeated calls to this method destroy previous parameters. For
        incremental training, instantiate a separate PunktTrainer instance.
        """
    def tokenize(self, text: str, realign_boundaries: bool = True) -> List[str]:
        """
        Given a text, returns a list of the sentences in that text.
        """
    def debug_decisions(self, text: str) -> Iterator[Dict[str, Any]]:
        """
        Classifies candidate periods as sentence breaks, yielding a dict for
        each that may be used to understand why the decision was made.

        See format_debug_decision() to help make this output readable.
        """
    def span_tokenize(self, text: str, realign_boundaries: bool = True) -> Iterator[Tuple[int, int]]:
        """
        Given a text, generates (start, end) spans of sentences
        in the text.
        """
    def sentences_from_text(self, text: str, realign_boundaries: bool = True) -> List[str]:
        """
        Given a text, generates the sentences in that text by only
        testing candidate sentence breaks. If realign_boundaries is
        True, includes in the sentence closing punctuation that
        follows the period.
        """
    def text_contains_sentbreak(self, text: str) -> bool:
        """
        Returns True if the given text includes a sentence break.
        """
    def sentences_from_text_legacy(self, text: str) -> Iterator[str]:
        """
        Given a text, generates the sentences in that text. Annotates all
        tokens, rather than just those with possible sentence breaks. Should
        produce the same results as ``sentences_from_text``.
        """
    def sentences_from_tokens(self, tokens: Iterator[PunktToken]) -> Iterator[PunktToken]:
        """
        Given a sequence of tokens, generates lists of tokens, each list
        corresponding to a sentence.
        """
    def dump(self, tokens: Iterator[PunktToken]) -> None: ...
    PUNCTUATION: Incomplete

DEBUG_DECISION_FMT: str

def format_debug_decision(d): ...
def demo(text, tok_cls=..., train_cls=...):
    """Builds a punkt model and applies it to the same text"""
