import _plotly_utils.basevalidators

class RangesliderValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'rangeslider', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
