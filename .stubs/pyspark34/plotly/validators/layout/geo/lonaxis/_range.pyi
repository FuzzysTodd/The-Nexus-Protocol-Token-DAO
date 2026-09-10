import _plotly_utils.basevalidators

class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'range', parent_name: str = 'layout.geo.lonaxis', **kwargs) -> None: ...
