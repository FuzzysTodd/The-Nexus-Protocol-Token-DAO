from _typeshed import Incomplete
from absl.testing import absltest
from rouge_score import rouge_scorer as rouge_scorer, scoring as scoring, test_util as test_util

class BootstrapAggregatorTest(absltest.TestCase):
    targets: Incomplete
    predictions: Incomplete
    def setUp(self) -> None: ...
    def assertSimilarAggregates(self, precision, recall, fmeasure, aggregate, delta=...) -> None:
        """Helper method for asserting matching aggregate scores.

    Args:
      precision: Tuple of (low, mid, high) precision scores.
      recall: Tuple of (low, mid, high) recall scores.
      fmeasure: Tuple of (low, mid, high) fmeasure scores.
      aggregate: An AggregateScore object.
      delta: Tolerance delta for matching values.
    """
    def testConsistentPercentiles(self) -> None: ...
    def testLargeConfidence(self) -> None: ...
    def testMultipleRougeTypes(self) -> None: ...
    def testConfidenceIntervalsAgainstRouge155(self) -> None: ...
    def testConfidenceIntervalsAgainstRouge155WithStemming(self) -> None: ...
    def testConfidenceIntervalsAgainstRouge155WithStemmingMultiLine(self) -> None: ...
