import _plotly_utils.basevalidators

class LegendValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'legend', parent_name: str = 'layout', **kwargs) -> None: ...
