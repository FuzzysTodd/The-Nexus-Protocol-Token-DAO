import _plotly_utils.basevalidators

class HistnormValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'histnorm', parent_name: str = 'histogram', **kwargs) -> None: ...
