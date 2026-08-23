import _plotly_utils.basevalidators

class BorderwidthValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'borderwidth', parent_name: str = 'layout.xaxis.rangeslider', **kwargs) -> None: ...
