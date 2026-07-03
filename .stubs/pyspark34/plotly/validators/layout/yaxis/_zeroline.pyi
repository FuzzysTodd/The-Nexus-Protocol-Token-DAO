import _plotly_utils.basevalidators

class ZerolineValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'zeroline', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
