from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ..utils import safe_isinstance as safe_isinstance
from ..utils.transformers import SENTENCEPIECE_TOKENIZERS as SENTENCEPIECE_TOKENIZERS, getattr_silent as getattr_silent, parse_prefix_suffix_for_tokenizer as parse_prefix_suffix_for_tokenizer
from ._masker import Masker as Masker
from _typeshed import Incomplete

class Text(Masker):
    ''' This masks out tokens according to the given tokenizer.

    The masked variables are

    output_type : "string" (default) or "token_ids"

    '''
    tokenizer: Incomplete
    output_type: Incomplete
    collapse_mask_token: Incomplete
    input_mask_token: Incomplete
    mask_token: Incomplete
    mask_token_id: Incomplete
    keep_prefix: Incomplete
    keep_suffix: Incomplete
    text_data: bool
    fixed_background: Incomplete
    default_batch_size: int
    immutable_outputs: bool
    def __init__(self, tokenizer: Incomplete | None = None, mask_token: Incomplete | None = None, collapse_mask_token: str = 'auto', output_type: str = 'string') -> None:
        ''' Build a new Text masker given an optional passed tokenizer.

        Parameters
        ----------
        tokenizer : callable or None
            The tokenizer used to break apart strings during masking. The passed tokenizer must support a minimal
            subset of the HuggingFace Transformers PreTrainedTokenizerBase API. This minimal subset means the
            tokenizer must return a dictionary with \'input_ids\' and then either include
            an \'offset_mapping\' entry in the same dictionary or provide a .convert_ids_to_tokens or .decode method.

        mask_token : string, int, or None
            The sub-string or integer token id used to mask out portions of a string. If None it will use the
            tokenizer\'s .mask_token attribute, if defined, or "..." if the tokenizer does not have a .mask_token
            attribute.

        collapse_mask_token : True, False, or "auto"
            If True, when several consecutive tokens are masked only one mask token is used to replace the entire
            series of original tokens.
        '''
    def __call__(self, mask, s): ...
    def data_transform(self, s):
        """ Called by explainers to allow us to convert data to better match masking (here this means tokenizing).
        """
    def token_segments(self, s):
        """ Returns the substrings associated with each token in the given string.
        """
    def clustering(self, s):
        """ Compute the clustering of tokens for the given string.
        """
    def shape(self, s):
        """ The shape of what we return as a masker.

        Note we only return a single sample, so there is no expectation averaging.
        """
    def mask_shapes(self, s):
        """ The shape of the masks we expect.
        """
    def invariants(self, s):
        """ The names of the features for each mask position for the given input string.
        """
    def feature_names(self, s):
        """ The names of the features for each mask position for the given input string.
        """
    def save(self, out_file) -> None:
        """ Save a Text masker to a file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True):
        """ Load a Text masker from a file stream.
        """

class SimpleTokenizer:
    """ A basic model agnostic tokenizer.
    """
    split_pattern: Incomplete
    def __init__(self, split_pattern: str = '\\W+') -> None:
        """ Create a tokenizer based on a simple splitting pattern.
        """
    def __call__(self, s, return_offsets_mapping: bool = True):
        """ Tokenize the passed string, optionally returning the offsets of each token in the original string.
        """

def post_process_sentencepiece_tokenizer_output(s):
    """ replaces whitespace encoded as '_' with ' ' for sentencepiece tokenizers.
    """

openers: Incomplete
closers: Incomplete
enders: Incomplete
connectors: Incomplete

class Token:
    """ A token representation used for token clustering.
    """
    s: Incomplete
    balanced: bool
    def __init__(self, value) -> None: ...

class TokenGroup:
    """ A token group (substring) representation used for token clustering.
    """
    g: Incomplete
    index: Incomplete
    def __init__(self, group, index: Incomplete | None = None) -> None: ...
    def __getitem__(self, index): ...
    def __add__(self, o): ...
    def __len__(self) -> int: ...

def merge_score(group1, group2, special_tokens):
    """ Compute the score of merging two token groups.

    special_tokens: tokens (such as separator tokens) that should be grouped last
    """
def merge_closest_groups(groups, special_tokens) -> None:
    """ Finds the two token groups with the best merge score and merges them.
    """
def partition_tree(decoded_tokens, special_tokens):
    """ Build a heriarchial clustering of tokens that align with sentence structure.

    Note that this is fast and heuristic right now.
    TODO: Build this using a real constituency parser.
    """
