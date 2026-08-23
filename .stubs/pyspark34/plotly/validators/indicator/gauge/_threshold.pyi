import _plotly_utils.basevalidators

class ThresholdValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'threshold', parent_name: str = 'indicator.gauge', **kwargs) -> None: ...
