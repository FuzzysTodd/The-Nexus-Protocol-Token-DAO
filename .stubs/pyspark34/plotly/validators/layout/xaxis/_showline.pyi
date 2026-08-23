import _plotly_utils.basevalidators

class ShowlineValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showline', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
