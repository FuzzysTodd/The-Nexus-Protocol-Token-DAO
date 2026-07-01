import _plotly_utils.basevalidators

class SymbolValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'symbol', parent_name: str = 'scattergeo.marker', **kwargs) -> None: ...
