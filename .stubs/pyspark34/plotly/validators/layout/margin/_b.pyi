import _plotly_utils.basevalidators

class BValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'b', parent_name: str = 'layout.margin', **kwargs) -> None: ...
