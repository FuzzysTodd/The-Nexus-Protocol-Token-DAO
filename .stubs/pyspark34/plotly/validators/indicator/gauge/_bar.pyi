import _plotly_utils.basevalidators

class BarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'bar', parent_name: str = 'indicator.gauge', **kwargs) -> None: ...
