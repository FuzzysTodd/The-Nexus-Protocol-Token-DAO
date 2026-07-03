import _plotly_utils.basevalidators

class RangemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'rangemode', parent_name: str = 'layout.xaxis.rangeslider.yaxis', **kwargs) -> None: ...
