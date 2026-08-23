import _plotly_utils.basevalidators

class OutlierwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'outlierwidth', parent_name: str = 'violin.marker.line', **kwargs) -> None: ...
