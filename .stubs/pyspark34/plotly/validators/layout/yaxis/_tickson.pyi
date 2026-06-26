import _plotly_utils.basevalidators

class TicksonValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'tickson', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
