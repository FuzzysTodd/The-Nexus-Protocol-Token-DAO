from _typeshed import Incomplete
from rouge_score import scoring as scoring, tokenizers as tokenizers

class RougeScorer(scoring.BaseScorer):
    """Calculate rouges scores between two blobs of text.

  Sample usage:
    scorer = RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score('The quick brown fox jumps over the lazy dog',
                          'The quick brown dog jumps on the log.')
  """
    rouge_types: Incomplete
    def __init__(self, rouge_types, use_stemmer: bool = False, split_summaries: bool = False, tokenizer: Incomplete | None = None) -> None:
        """Initializes a new RougeScorer.

    Valid rouge types that can be computed are:
      rougen (e.g. rouge1, rouge2): n-gram based scoring.
      rougeL: Longest common subsequence based scoring.

    Args:
      rouge_types: A list of rouge types to calculate.
      use_stemmer: Bool indicating whether Porter stemmer should be used to
        strip word suffixes to improve matching. This arg is used in the
        DefaultTokenizer, but other tokenizers might or might not choose to
        use this.
      split_summaries: whether to add newlines between sentences for rougeLsum
      tokenizer: Tokenizer object which has a tokenize() method.
    Returns:
      A dict mapping rouge types to Score tuples.
    """
    def score_multi(self, targets, prediction):
        """Calculates rouge scores between targets and prediction.

    The target with the maximum f-measure is used for the final score for
    each score type..

    Args:
      targets: list of texts containing the targets
      prediction: Text containing the predicted text.
    Returns:
      A dict mapping each rouge type to a Score object.
    Raises:
      ValueError: If an invalid rouge type is encountered.
    """
    def score(self, target, prediction):
        """Calculates rouge scores between the target and prediction.

    Args:
      target: Text containing the target (ground truth) text,
      or if a list
      prediction: Text containing the predicted text.
    Returns:
      A dict mapping each rouge type to a Score object.
    Raises:
      ValueError: If an invalid rouge type is encountered.
    """

def lcs_ind(ref, can):
    """Returns one of the longest lcs."""
