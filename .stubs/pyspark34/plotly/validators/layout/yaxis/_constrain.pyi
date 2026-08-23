import _plotly_utils.basevalidators

class ConstrainValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'constrain', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
