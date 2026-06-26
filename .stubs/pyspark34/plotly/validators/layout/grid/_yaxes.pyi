import _plotly_utils.basevalidators

class YaxesValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name: str = 'yaxes', parent_name: str = 'layout.grid', **kwargs) -> None: ...
