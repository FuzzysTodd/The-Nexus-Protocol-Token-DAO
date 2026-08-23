import abc
from _typeshed import Incomplete
from typing import Dict, NamedTuple

class Score(NamedTuple('Score', [('precision', Incomplete), ('recall', Incomplete), ('fmeasure', Incomplete)])):
    """Tuple containing precision, recall, and f-measure values."""

class BaseScorer(metaclass=abc.ABCMeta):
    """Base class for Scorer objects."""
    @abc.abstractmethod
    def score(self, target: str, prediction: str) -> Dict[str, Score]:
        """Calculates score between the target and prediction.

    Args:
      target: Text containing the target (ground truth) text.
      prediction: Text containing the predicted text.

    Returns:
      A dict mapping each score_type (string) to Score object.
    """

class AggregateScore(NamedTuple('AggregateScore', [('low', Incomplete), ('mid', Incomplete), ('high', Incomplete)])):
    """Tuple containing confidence intervals for scores."""

class BootstrapAggregator:
    '''Aggregates scores to provide confidence intervals.

  Sample usage:
    scorer = rouge_scorer.RougeScorer([\'rouge1\', \'rougeL\'])
    aggregator = Aggregator()
    aggregator.add_scores(scorer.score("one two three", "one two"))
    aggregator.add_scores(scorer.score("one two five six", "seven eight"))
    result = aggregator.aggregate()
    print result
    {\'rougeL\': AggregateScore(
         low=Score(precision=0.0, recall=0.0, fmeasure=0.0),
         mid=Score(precision=0.5, recall=0.33, fmeasure=0.40),
         high=Score(precision=1.0, recall=0.66, fmeasure=0.80)),
     \'rouge1\': AggregateScore(
         low=Score(precision=0.0, recall=0.0, fmeasure=0.0),
         mid=Score(precision=0.5, recall=0.33, fmeasure=0.40),
         high=Score(precision=1.0, recall=0.66, fmeasure=0.80))}
  '''
    def __init__(self, confidence_interval: float = 0.95, n_samples: int = 1000) -> None:
        """Initializes a BootstrapAggregator object.

    Args:
      confidence_interval: Confidence interval to compute on the mean as a
        decimal.
      n_samples: Number of samples to use for bootstrap resampling.

    Raises:
      ValueError: If invalid argument is given.
    """
    def add_scores(self, scores) -> None:
        """Adds a sample for future aggregation.

    Args:
      scores: Dict mapping score_type strings to a namedtuple object/class
        representing a score.
    """
    def aggregate(self):
        """Aggregates scores previously added using add_scores.

    Returns:
      A dict mapping score_type to AggregateScore objects.
    """

def fmeasure(precision, recall):
    """Computes f-measure given precision and recall values."""
