import _plotly_utils.basevalidators

class TicklabelmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'ticklabelmode', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
