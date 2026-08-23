import _plotly_utils.basevalidators

class GaugeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'gauge', parent_name: str = 'indicator', **kwargs) -> None: ...
