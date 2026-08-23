import _plotly_utils.basevalidators

class ValuesValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'values', parent_name: str = 'layout.xaxis.rangebreak', **kwargs) -> None: ...
