import _plotly_utils.basevalidators

class GridwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'gridwidth', parent_name: str = 'layout.geo.lonaxis', **kwargs) -> None: ...
