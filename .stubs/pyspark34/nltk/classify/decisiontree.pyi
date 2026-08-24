from _typeshed import Incomplete
from nltk.classify.api import ClassifierI as ClassifierI
from nltk.probability import FreqDist as FreqDist, MLEProbDist as MLEProbDist, entropy as entropy

class DecisionTreeClassifier(ClassifierI):
    def __init__(self, label, feature_name: Incomplete | None = None, decisions: Incomplete | None = None, default: Incomplete | None = None) -> None:
        """
        :param label: The most likely label for tokens that reach
            this node in the decision tree.  If this decision tree
            has no children, then this label will be assigned to
            any token that reaches this decision tree.
        :param feature_name: The name of the feature that this
            decision tree selects for.
        :param decisions: A dictionary mapping from feature values
            for the feature identified by ``feature_name`` to
            child decision trees.
        :param default: The child that will be used if the value of
            feature ``feature_name`` does not match any of the keys in
            ``decisions``.  This is used when constructing binary
            decision trees.
        """
    def labels(self): ...
    def classify(self, featureset): ...
    def error(self, labeled_featuresets): ...
    def pretty_format(self, width: int = 70, prefix: str = '', depth: int = 4):
        """
        Return a string containing a pretty-printed version of this
        decision tree.  Each line in this string corresponds to a
        single decision tree node or leaf, and indentation is used to
        display the structure of the decision tree.
        """
    def pseudocode(self, prefix: str = '', depth: int = 4):
        """
        Return a string representation of this decision tree that
        expresses the decisions it makes as a nested set of pseudocode
        if statements.
        """
    @staticmethod
    def train(labeled_featuresets, entropy_cutoff: float = 0.05, depth_cutoff: int = 100, support_cutoff: int = 10, binary: bool = False, feature_values: Incomplete | None = None, verbose: bool = False):
        """
        :param binary: If true, then treat all feature/value pairs as
            individual binary features, rather than using a single n-way
            branch for each feature.
        """
    @staticmethod
    def leaf(labeled_featuresets): ...
    @staticmethod
    def stump(feature_name, labeled_featuresets): ...
    def refine(self, labeled_featuresets, entropy_cutoff, depth_cutoff, support_cutoff, binary: bool = False, feature_values: Incomplete | None = None, verbose: bool = False) -> None: ...
    @staticmethod
    def best_stump(feature_names, labeled_featuresets, verbose: bool = False): ...
    @staticmethod
    def binary_stump(feature_name, feature_value, labeled_featuresets): ...
    @staticmethod
    def best_binary_stump(feature_names, labeled_featuresets, feature_values, verbose: bool = False): ...

def f(x): ...
def demo() -> None: ...
