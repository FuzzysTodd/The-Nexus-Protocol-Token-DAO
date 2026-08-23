import _plotly_utils.basevalidators

class LegendwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'legendwidth', parent_name: str = 'candlestick', **kwargs) -> None: ...
