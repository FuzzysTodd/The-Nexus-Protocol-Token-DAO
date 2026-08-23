from _typeshed import Incomplete

NON_ALPHANUM_PATTERN: str
NON_ALPHANUM_RE: Incomplete
SPACES_PATTERN: str
SPACES_RE: Incomplete
VALID_TOKEN_PATTERN: str
VALID_TOKEN_RE: Incomplete

def tokenize(text, stemmer):
    """Tokenize input text into a list of tokens.

  This approach aims to replicate the approach taken by Chin-Yew Lin in
  the original ROUGE implementation.

  Args:
    text: A text blob to tokenize.
    stemmer: An optional stemmer.

  Returns:
    A list of string tokens extracted from input text.
  """
