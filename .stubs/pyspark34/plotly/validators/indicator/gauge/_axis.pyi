import _plotly_utils.basevalidators

class AxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'axis', parent_name: str = 'indicator.gauge', **kwargs) -> None: ...
