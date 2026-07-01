import _plotly_utils.basevalidators

class EndValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'end', parent_name: str = 'histogram.xbins', **kwargs) -> None: ...
