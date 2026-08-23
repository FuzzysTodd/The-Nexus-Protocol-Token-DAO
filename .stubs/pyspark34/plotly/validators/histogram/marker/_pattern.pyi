import _plotly_utils.basevalidators

class PatternValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'pattern', parent_name: str = 'histogram.marker', **kwargs) -> None: ...
