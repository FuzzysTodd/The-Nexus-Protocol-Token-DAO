import _plotly_utils.basevalidators

class XcalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'xcalendar', parent_name: str = 'candlestick', **kwargs) -> None: ...
