import _plotly_utils.basevalidators

class BelowValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'below', parent_name: str = 'scattermapbox', **kwargs) -> None: ...
