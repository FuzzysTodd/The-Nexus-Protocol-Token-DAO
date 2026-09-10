import _plotly_utils.basevalidators

class DvalueValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'dvalue', parent_name: str = 'layout.xaxis.rangebreak', **kwargs) -> None: ...
