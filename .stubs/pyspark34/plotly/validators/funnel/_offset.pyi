import _plotly_utils.basevalidators

class OffsetValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'offset', parent_name: str = 'funnel', **kwargs) -> None: ...
