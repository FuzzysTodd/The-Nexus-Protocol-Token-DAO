import _plotly_utils.basevalidators

class AutorangeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'autorange', parent_name: str = 'layout.xaxis.rangeslider', **kwargs) -> None: ...
