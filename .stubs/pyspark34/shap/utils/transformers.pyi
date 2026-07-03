from ._general import safe_isinstance as safe_isinstance
from _typeshed import Incomplete

MODELS_FOR_SEQ_TO_SEQ_CAUSAL_LM: Incomplete
MODELS_FOR_CAUSAL_LM: Incomplete
MODELS_FOR_MASKED_LM: Incomplete
SENTENCEPIECE_TOKENIZERS: Incomplete

def is_transformers_lm(model):
    """ Check if the given model object is a huggingface transformers language model.
    """
def parse_prefix_suffix_for_tokenizer(tokenizer):
    """ Set prefix and suffix tokens based on null tokens.

    Example for distillgpt2: null_tokens=[], for BART: null_tokens = [0,2] and for MarianMT: null_tokens=[0]
    used to slice tokens belonging to sentence after passing through tokenizer.encode().
    """
def getattr_silent(obj, attr):
    """ This turns of verbose logging of missing attributes for huggingface transformers.

    This is motivated by huggingface transformers objects that print error warnings
    when we access unset properties.
    """
