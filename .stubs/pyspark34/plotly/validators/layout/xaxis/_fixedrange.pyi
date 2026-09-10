import _plotly_utils.basevalidators

class FixedrangeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'fixedrange', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
