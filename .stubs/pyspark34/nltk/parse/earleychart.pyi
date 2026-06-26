from _typeshed import Incomplete
from collections.abc import Generator
from nltk.parse.chart import BottomUpPredictCombineRule as BottomUpPredictCombineRule, BottomUpPredictRule as BottomUpPredictRule, CachedTopDownPredictRule as CachedTopDownPredictRule, Chart as Chart, ChartParser as ChartParser, EdgeI as EdgeI, EmptyPredictRule as EmptyPredictRule, FilteredBottomUpPredictCombineRule as FilteredBottomUpPredictCombineRule, FilteredSingleEdgeFundamentalRule as FilteredSingleEdgeFundamentalRule, LeafEdge as LeafEdge, LeafInitRule as LeafInitRule, SingleEdgeFundamentalRule as SingleEdgeFundamentalRule, TopDownInitRule as TopDownInitRule
from nltk.parse.featurechart import FeatureBottomUpPredictCombineRule as FeatureBottomUpPredictCombineRule, FeatureBottomUpPredictRule as FeatureBottomUpPredictRule, FeatureChart as FeatureChart, FeatureChartParser as FeatureChartParser, FeatureEmptyPredictRule as FeatureEmptyPredictRule, FeatureSingleEdgeFundamentalRule as FeatureSingleEdgeFundamentalRule, FeatureTopDownInitRule as FeatureTopDownInitRule, FeatureTopDownPredictRule as FeatureTopDownPredictRule

class IncrementalChart(Chart):
    def initialize(self) -> None: ...
    def edges(self): ...
    def iteredges(self): ...
    def select(self, end, **restrictions): ...

class FeatureIncrementalChart(IncrementalChart, FeatureChart):
    def select(self, end, **restrictions): ...

class CompleteFundamentalRule(SingleEdgeFundamentalRule): ...

class CompleterRule(CompleteFundamentalRule):
    def apply(self, chart, grammar, edge) -> Generator[Incomplete, Incomplete, None]: ...

class ScannerRule(CompleteFundamentalRule):
    def apply(self, chart, grammar, edge) -> Generator[Incomplete, Incomplete, None]: ...

class PredictorRule(CachedTopDownPredictRule): ...

class FilteredCompleteFundamentalRule(FilteredSingleEdgeFundamentalRule):
    def apply(self, chart, grammar, edge) -> Generator[Incomplete, Incomplete, None]: ...

class FeatureCompleteFundamentalRule(FeatureSingleEdgeFundamentalRule): ...
class FeatureCompleterRule(CompleterRule): ...
class FeatureScannerRule(ScannerRule): ...
class FeaturePredictorRule(FeatureTopDownPredictRule): ...

EARLEY_STRATEGY: Incomplete
TD_INCREMENTAL_STRATEGY: Incomplete
BU_INCREMENTAL_STRATEGY: Incomplete
BU_LC_INCREMENTAL_STRATEGY: Incomplete
LC_INCREMENTAL_STRATEGY: Incomplete

class IncrementalChartParser(ChartParser):
    """
    An *incremental* chart parser implementing Jay Earley's
    parsing algorithm:

    | For each index end in [0, 1, ..., N]:
    |   For each edge such that edge.end = end:
    |     If edge is incomplete and edge.next is not a part of speech:
    |       Apply PredictorRule to edge
    |     If edge is incomplete and edge.next is a part of speech:
    |       Apply ScannerRule to edge
    |     If edge is complete:
    |       Apply CompleterRule to edge
    | Return any complete parses in the chart
    """
    def __init__(self, grammar, strategy=..., trace: int = 0, trace_chart_width: int = 50, chart_class=...) -> None:
        """
        Create a new Earley chart parser, that uses ``grammar`` to
        parse texts.

        :type grammar: CFG
        :param grammar: The grammar used to parse texts.
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            and higher numbers will produce more verbose tracing
            output.
        :type trace_chart_width: int
        :param trace_chart_width: The default total width reserved for
            the chart in trace output.  The remainder of each line will
            be used to display edges.
        :param chart_class: The class that should be used to create
            the charts used by this parser.
        """
    def chart_parse(self, tokens, trace: Incomplete | None = None): ...

class EarleyChartParser(IncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class IncrementalTopDownChartParser(IncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class IncrementalBottomUpChartParser(IncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class IncrementalBottomUpLeftCornerChartParser(IncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class IncrementalLeftCornerChartParser(IncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

EARLEY_FEATURE_STRATEGY: Incomplete
TD_INCREMENTAL_FEATURE_STRATEGY: Incomplete
BU_INCREMENTAL_FEATURE_STRATEGY: Incomplete
BU_LC_INCREMENTAL_FEATURE_STRATEGY: Incomplete

class FeatureIncrementalChartParser(IncrementalChartParser, FeatureChartParser):
    def __init__(self, grammar, strategy=..., trace_chart_width: int = 20, chart_class=..., **parser_args) -> None: ...

class FeatureEarleyChartParser(FeatureIncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class FeatureIncrementalTopDownChartParser(FeatureIncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class FeatureIncrementalBottomUpChartParser(FeatureIncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

class FeatureIncrementalBottomUpLeftCornerChartParser(FeatureIncrementalChartParser):
    def __init__(self, grammar, **parser_args) -> None: ...

def demo(print_times: bool = True, print_grammar: bool = False, print_trees: bool = True, trace: int = 2, sent: str = 'I saw John with a dog with my cookie', numparses: int = 5) -> None:
    """
    A demonstration of the Earley parsers.
    """
