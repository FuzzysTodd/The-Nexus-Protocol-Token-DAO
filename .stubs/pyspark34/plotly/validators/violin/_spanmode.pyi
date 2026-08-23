import _plotly_utils.basevalidators

class SpanmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'spanmode', parent_name: str = 'violin', **kwargs) -> None: ...
