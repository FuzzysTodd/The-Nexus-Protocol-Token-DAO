import _plotly_utils.basevalidators

class RangebreaksValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'rangebreaks', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
