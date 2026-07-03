import _plotly_utils.basevalidators

class AutoshiftValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'autoshift', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
