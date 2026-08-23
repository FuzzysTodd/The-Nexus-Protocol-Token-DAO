import _plotly_utils.basevalidators

class OverlayingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'overlaying', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
