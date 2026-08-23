import _plotly_utils.basevalidators

class SymbolValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'symbol', parent_name: str = 'scattermapbox.marker', **kwargs) -> None: ...
