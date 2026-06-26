import _plotly_utils.basevalidators

class RValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'r', parent_name: str = 'layout.title.pad', **kwargs) -> None: ...
